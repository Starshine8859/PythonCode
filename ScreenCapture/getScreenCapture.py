import pytesseract
from PIL import Image, ImageDraw, ImageFont
import mss
import os
from datetime import datetime

# Set Tesseract path if needed (Windows example)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def capture_all_screens():
    with mss.mss() as sct:
        screenshots = []
        for index, monitor in enumerate(sct.monitors[1:], start=1):  # skip monitor[0], it’s all monitors
            screenshot = sct.grab(monitor)
            img = Image.frombytes('RGB', screenshot.size, screenshot.rgb)
            screenshots.append((index, img))
        return screenshots

def extract_text(image):
    return pytesseract.image_to_string(image)

def save_image_with_text_border(index, image, text):
    width, height = image.size
    font = ImageFont.load_default()
    padding = 20
    text_lines = text.strip().split('\n')
    text_height = (font.getsize("A")[1] + 2) * len(text_lines) + padding

    new_img = Image.new('RGB', (width, height + text_height), (255, 255, 255))
    new_img.paste(image, (0, 0))

    draw = ImageDraw.Draw(new_img)
    y = height + 10
    for line in text_lines:
        draw.text((10, y), line, fill=(0, 0, 0), font=font)
        y += font.getsize(line)[1] + 2

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    base_path = "screenshots"
    os.makedirs(base_path, exist_ok=True)

    orig_path = os.path.join(base_path, f"screen_{index}_{timestamp}.png")
    final_path = os.path.join(base_path, f"screen_{index}_{timestamp}_annotated.png")

    image.save(orig_path)
    new_img.save(final_path)
    print(f"Saved original: {orig_path}")
    print(f"Saved with text: {final_path}")

def main():
    screenshots = capture_all_screens()
    for index, image in screenshots:
        text = extract_text(image)
        save_image_with_text_border(index, image, text)

if __name__ == "__main__":
    main()
