import os
import json
from dotenv import load_dotenv

from rtsp import capture_frame
from gpt import analyze_image
from ntfy import send_ntfy_alert

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

load_dotenv(os.path.join(BASE_DIR, ".env"))

RTSP_URL = os.getenv("RTSP_URL")

def main():
    try:
        print("📸 Capturando imagem da câmera...")
        image_path = capture_frame(RTSP_URL)

        print("🧠 Analisando imagem...")
        result_text = analyze_image(image_path)

        result = json.loads(result_text)

        fez_coco = result.get("fez_coco", False)
        confianca = result.get("confianca", 0)

        print(f"🔎 Classificação: fez_coco={fez_coco} | confiança={confianca}")

        if fez_coco is True:
            print("🚨 Cocô detectado! Enviando alerta via ntfy...")
            send_ntfy_alert(image_path, confianca)
        else:
            print("✅ Ambiente limpo. Nenhuma ação necessária.")

    except Exception as e:
        print("❌ Erro no fluxo principal:", e)


if __name__ == "__main__":
    main()
