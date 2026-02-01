import base64
import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_URL = "https://api.openai.com/v1/responses"


def b64_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def analyze_image(
    image_to_check,
    exemplo_no_coco="sem_coco.jpg",
    exemplo_with_coco="com_coco.jpg"
):
    img_check_b64 = b64_image(image_to_check)
    img_no_coco_b64 = b64_image(exemplo_no_coco)
    img_with_coco_b64 = b64_image(exemplo_with_coco)

    payload = {
        "model": "gpt-5-mini",
        "input": [
            {
                "role": "system",
                "content": (
                    "Você é um classificador visual especializado em identificar "
                    "fezes de cachorro no piso de uma sala. "
                    "Ignore pessoas, cachorro, sombras, reflexos e iluminação. "
                    "Considere apenas o piso."
                )
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "Exemplo de ambiente LIMPO (sem cocô):"
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{img_no_coco_b64}"
                    },
                    {
                        "type": "input_text",
                        "text": "Exemplo de ambiente COM cocô:"
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{img_with_coco_b64}"
                    },
                    {
                        "type": "input_text",
                        "text": (
                            "Agora analise a PRÓXIMA imagem e responda APENAS em JSON:\n"
                            "{ \"fez_coco\": true|false, \"confianca\": 0-100 }\n"
                            "A posição do cocô NÃO importa."
                        )
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{img_check_b64}"
                    }
                ]
            }
        ]
    }

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        OPENAI_URL,
        json=payload,
        headers=headers,
        timeout=60
    )

    if response.status_code != 200:
        print("ERRO GPT:", response.text)

    response.raise_for_status()
    data = response.json()

    output_text = None

    for item in data.get("output", []):
        if item.get("type") == "message":
            for content in item.get("content", []):
                if content.get("type") == "output_text":
                    output_text = content.get("text")
                    break

    if not output_text:
        raise Exception(f"Resposta inesperada da API: {data}")

    return output_text
