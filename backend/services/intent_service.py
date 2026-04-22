from openai import OpenAI
from prompts import INTENT_PROMPT


def classify_intent(client: OpenAI, message: str) -> str:
    response = client.responses.create(
        model="gpt-5.4",
        input=[
            {"role": "system", "content": INTENT_PROMPT},
            {"role": "user", "content": message}
        ]
    )
    return response.output_text.strip()