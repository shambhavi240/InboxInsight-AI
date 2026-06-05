import base64
import os
import subprocess
import tempfile
import re
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import gspread
from pypdf import PdfReader

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/spreadsheets"
]

OLLAMA_EXE = r"C:\Users\shamb\AppData\Local\Programs\Ollama\ollama.exe"


def summarize_with_ollama(text):
    prompt = f"""
    Summarize the following document in 5 concise bullet points:

    {text[:4000]}
    """

    command = [OLLAMA_EXE, "run", "llama3.2:3b"] if os.path.exists(OLLAMA_EXE) else ["ollama", "run", "gemma3:1b"]
    print("\n===== TEXT SENT TO OLLAMA =====")
    print(text[:1000])
    print("================================\n")
    result = subprocess.run(
    command,
    input=prompt,
    text=True,
    encoding="utf-8",
    errors="replace",
    capture_output=True,
    timeout=600,
)

    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "Ollama failed to generate a summary.")

    import re

    output = result.stdout

    output = re.sub(r'\x1b\[[0-9;]*[A-Za-z]', '', output)
    return output.strip()


def extract_pdf_text(gmail_service, message, part):
    attachment_id = part.get("body", {}).get("attachmentId")
    if not attachment_id:
        return ""

    attachment = gmail_service.users().messages().attachments().get(
        userId="me",
        messageId=message["id"],
        id=attachment_id,
    ).execute()

    file_data = base64.urlsafe_b64decode(attachment["data"].encode("utf-8"))

    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_file:
        temp_file.write(file_data)
        temp_path = temp_file.name

    try:
        reader = PdfReader(temp_path)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        print("\n===== PDF EXTRACTED =====")
        print(text[:1000])
        print("=========================\n")

        return text
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)


def process_emails():
    flow = InstalledAppFlow.from_client_secrets_file(
    "credentials.json",
    SCOPES
)
    creds = flow.run_local_server(port=0)

    # Gmail
    gmail_service = build("gmail", "v1", credentials=creds)

    # Google Sheet
    gc = gspread.authorize(creds)

    sheet = gc.open_by_key(
        "1DnDzJlIe-uaeaMkT0e8m-YNXW7yPmWUQtXA_h0XpMng"
    )

    worksheet = sheet.sheet1

    # Clear old data except header
    worksheet.clear()

    worksheet.update(
    "A1:G1",
    [[
        "S.No",
        "Sender",
        "Date",
        "Subject",
        "Email Preview",
        "Attachment Name",
        "AI Summary"
    ]]
)

    results = gmail_service.users().messages().list(
        userId="me",
        maxResults=100
    ).execute()

    messages = results.get("messages", [])

    row = 2
    sno = 1

    for msg in messages:

        message = gmail_service.users().messages().get(
            userId="me",
            id=msg["id"]
        ).execute()

        headers = message["payload"]["headers"]

        sender = ""
        subject = ""
        date = ""

        for header in headers:
            if header["name"] == "From":
                sender = header["value"]

            elif header["name"] == "Subject":
                subject = header["value"]

            elif header["name"] == "Date":
                date = header["value"]

        preview = message.get("snippet", "")

        attachment_name = "No Attachment"
        ai_summary = ""

        parts = message.get("payload", {}).get("parts", [])

        for part in parts:
            filename = part.get("filename", "")

            if filename.lower().endswith(".pdf"):
                print(f"PDF Found: {filename}")
                attachment_name = filename
                pdf_text = extract_pdf_text(gmail_service, message, part)

                if pdf_text.strip():
                    try:
                        print(f"Subject: {subject}")
                        print(f"Attachment: {attachment_name}")
                        ai_summary = summarize_with_ollama(pdf_text)
                    except Exception as e:
                        ai_summary = f"Summary Error: {str(e)}"
                else:
                    ai_summary = "No readable text found in PDF"

                break

        worksheet.update(
            f"A{row}:G{row}",
            [[
                sno,
                sender,
                date,
                subject,
                preview,
                attachment_name,
                ai_summary
            ]]
        )

        row += 1
        sno += 1

    return "✅ Sheet updated successfully"


if __name__ == "__main__":
    print(process_emails())