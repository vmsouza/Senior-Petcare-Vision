import cv2
import time

def capture_frame(
    rtsp_url,
    output_path="frame.jpg",
    warmup_frames=20,
    timeout_sec=5
):
    cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)

    if not cap.isOpened():
        raise Exception("Não foi possível conectar ao stream RTSP")

    # reduz buffer (menos atraso)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    start = time.time()
    frame = None

    # descarta frames até pegar um válido
    for _ in range(warmup_frames):
        ret, frame = cap.read()
        if not ret:
            if time.time() - start > timeout_sec:
                cap.release()
                raise Exception("Timeout ao capturar frame RTSP")
            continue

    cap.release()

    if frame is None:
        raise Exception("Frame inválido")

    cv2.imwrite(output_path, frame)
    return output_path
