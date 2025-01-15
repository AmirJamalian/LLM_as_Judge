
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},  # System message
        {"role": "user", "content": "What is AI?"}  # User's query
    ],
    max_tokens=100,
)

print(response.choices[0].message['content'].strip())
