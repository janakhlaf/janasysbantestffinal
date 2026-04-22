from openai import OpenAI
from prompts import CHATBOT_PROMPT


def normal_chat(client: OpenAI, message: str) -> str:
    response = client.responses.create(
        model="gpt-5.4",
        input=[
            {"role": "system", "content": CHATBOT_PROMPT},
            {"role": "user", "content": message}
        ]
    )
    return response.output_text.strip()