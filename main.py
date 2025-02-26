import os
from extract_text import extract_text_from_image

if __name__ == "__main__":
    transaction_dir = './transactionImages/'  # Directory path
    transactionImages = os.listdir(transaction_dir)
    allow_preprocessing = True

    for img_name in transactionImages:
        img_path = os.path.join(transaction_dir, img_name)
        print(f"Image Path: {img_path}")
        data = extract_text_from_image(img_path, allow_preprocessing)
        print(f"{data}\n")
