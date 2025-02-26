from PIL import Image as image
from pytesseract import pytesseract
import cv2

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
preprocess_dir = './preProcessedImages'


def preprocess_image(image_path):
    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    thresh = cv2.threshold(
        gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    denoised = cv2.fastNlMeansDenoising(thresh, h=30)
    print(f"Preprocessing Path: {preprocess_dir}/{image_path.split('/')[2]}")
    cv2.imwrite(f"{preprocess_dir}/{image_path.split('/')[2]}", denoised)

    return denoised


def extract_text_from_image(img_path, allow_preprocessing=False):
    try:
        if allow_preprocessing:
            print("Preprocessing...")
            processed_image = preprocess_image(img_path)
            pil_img = image.fromarray(processed_image)
            pytesseract.tesseract_cmd = path_to_tesseract
            text_data = pytesseract.image_to_string(pil_img, lang="eng")
            return text_data
        else:
            img = image.open(img_path)
            text_data = pytesseract.image_to_string(img)
            return text_data

    except Exception as e:
        print(e)


if __name__ == "__main__":
    path = './transactionImages/gPay.jpg'
    image_preprocessing_allowed = True
    data = extract_text_from_image(path, image_preprocessing_allowed)
    print(data)
