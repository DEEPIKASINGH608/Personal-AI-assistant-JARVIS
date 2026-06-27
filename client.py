from openai import OpenAI
import os

client = OpenAI(
        api_key="OPENAI_API_KEY"
    )

completion = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a virtual assistant that named Jarvis skilled in tasks like Alexa and Google Cloud"},
            {"role": "user", "content": "What is coding?"}
        ]

    )

print(completion.choices[0].message.content)