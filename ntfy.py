import requests
from datetime import datetime
from image_utils import resize_for_ntfy
from dotenv import load_dotenv
import os

load_dotenv()

NTFY_TOPIC = os.getenv("NTFY_TOPIC")
NTFY_URL = f"https://ntfy.sh/{NTFY_TOPIC}"


def send_ntfy_alert(image_path, confianca=None):
    data = datetime.now().strftime("%d/%m/%y ")
    hora = datetime.now().strftime("%H:%M")

    mensagem = f"O Jhoe fez cocô na sala em {data} às {hora}."
    if confianca is not None:
        mensagem += f" (confiança {confianca}%)"

    # 🔥 reduz imagem antes de enviar
    reduced_image = resize_for_ntfy(image_path)

    headers = {
        "Title": "Alerta de Coco",
        "Tags": "warning,poop,house",
        "Priority": "5",
        "Content-Type": "image/jpeg"
    }

    with open(reduced_image, "rb") as img:
        response = requests.post(
            NTFY_URL,
            headers=headers,
            data=img,
            params={"message": mensagem},
            timeout=30
        )

    if response.status_code not in (200, 201):
        print("❌ Erro ao enviar ntfy:", response.text)
    else:
        print("🔔 Alerta ntfy enviado com sucesso")
