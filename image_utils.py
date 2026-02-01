import cv2
import os


def resize_for_ntfy(
    input_path,
    output_path=None,
    max_width=960,
    jpeg_quality=70
):
    if output_path is None:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_ntfy.jpg"

    img = cv2.imread(input_path)
    if img is None:
        raise Exception("Não foi possível abrir a imagem")

    h, w = img.shape[:2]

    if w > max_width:
        scale = max_width / w
        new_w = int(w * scale)
        new_h = int(h * scale)
        img = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)

    cv2.imwrite(
        output_path,
        img,
        [cv2.IMWRITE_JPEG_QUALITY, jpeg_quality]
    )

    return output_path
