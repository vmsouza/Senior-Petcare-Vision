import cv2
import time

def capture_frame(rtsp_url, output_path="frame.jpg", warmup=2):
    cap = cv2.VideoCapture(rtsp_url)

    if not cap.isOpened():
        raise Exception("Não foi possível conectar ao stream RTSP")

    # dá um tempo para o buffer estabilizar
    time.sleep(warmup)

    ret, frame = cap.read()
    cap.release()

    if not ret:
        raise Exception("Falha ao capturar frame")

    cv2.imwrite(output_path, frame)
    return output_path
