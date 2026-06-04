from pypdf import PdfReader
import ollama

reader = PdfReader("sample.pdf")

text = ""
for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text + "\n"

response = ollama.chat(
    model="gemma3:1b",
    messages=[
        {
            "role": "user",
            "content": f"Summarize this PDF in 5 bullet points:\n\n{text[:5000]}"
        }
    ]
)

summary = response["message"]["content"]

print(summary)

with open("summary.txt", "w", encoding="utf-8") as f:
    f.write(summary)

print("Summary saved to summary.txt")