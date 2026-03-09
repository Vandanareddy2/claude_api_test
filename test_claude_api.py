import anthropic

client = anthropic.Anthropic(
    api_key="YOUR_API_KEY"
)

response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=200,
    messages=[
        {"role": "user", "content": "Say hello and confirm the Claude API is working."}
    ]
)

print(response.content[0].text)