import ollama

text = """
Artificial Intelligence is transforming industries by automating repetitive tasks,
improving decision-making, increasing productivity, and enabling innovation.
"""

response = ollama.chat(
    model='gemma3:1b',
    messages=[
        {
            'role': 'user',
            'content': f'Summarize this in 5 bullet points:\n{text}'
        }
    ]
)

print(response['message']['content'])