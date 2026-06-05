from pypdf import PdfReader
import ollama

reader = PdfReader("sample.pdf")

text = ""

for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text + "\n"

# Clean text
text = " ".join(text.split())

response = ollama.chat(
    model="gemma3:4b",
    messages=[
        {
            "role": "user",
            "content": f"""
You are an expert document analyst.

Analyze this document and provide:

1. Document Type
2. Main Purpose
3. Key Parties Involved
4. Important Dates
5. Financial Terms
6. Major Obligations and Risks

Use clear bullet points.

Document:

{text[:15000]}
"""
        }
    ]
)

summary = response["message"]["content"]

with open("summary.txt", "w", encoding="utf-8") as f:
    f.write(summary)

print(summary)