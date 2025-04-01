
# This script demonstrates how to use the OpenAI API with a custom base URL.
# Visit https://platform.openai.com    
from openai import OpenAI

client = OpenAI(
    api_key="<API_KEY>",
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of Japan?"},
    ],
    stream=False
)

print(response.choices[0].message.content)
