from openai import OpenAI
from config import OPENAI_TOKEN

client = OpenAI(api_key=OPENAI_TOKEN)

def generate_chatgpt_response(prompt):
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[     {
            "role": "user",
            "content": prompt,
        }])

    return response.choices[0].message.content
