from openai import OpenAI
from prompts import SIMILARITY_PROMPT


def similar_chat(client: OpenAI, message: str) -> str:
    response = client.responses.create(
        model="gpt-5.4",
        input=[
            {"role": "system", "content": SIMILARITY_PROMPT},
            {"role": "user", "content": message}
        ]
    )
    return response.output_text.strip()