import requests
import os
from datetime import datetime

WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
WHATSAPP_PHONE_ID = os.getenv("WHATSAPP_PHONE_ID")

WHATSAPP_URL = f"https://graph.facebook.com/v18.0/{WHATSAPP_PHONE_ID}/messages"


def send_whatsapp_template(phone_number):
    data_hora = datetime.now().strftime("%d/%m/%y %H:%M")

    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "template",
        "template": {
            "name": "utilidade_aviso_coco",
            "language": {
                "code": "en"
            },
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": data_hora
                        }
                    ]
                }
            ]
        }
    }

    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        WHATSAPP_URL,
        json=payload,
        headers=headers,
        timeout=30
    )

    if response.status_code not in (200, 201):
        print(f"Erro WhatsApp ({phone_number}):", response.text)
    else:
        print(f"WhatsApp enviado para {phone_number} em {data_hora}")
