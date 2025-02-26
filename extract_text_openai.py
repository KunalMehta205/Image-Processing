import os
import base64
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = <OPENAI_API_KEY >

client = OpenAI()

# Better way is to upload the image and send the link of the image.
# Encoding large files takes time.


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


image_path = "./transactionImages/payTM.jpg"

base64_image = encode_image(image_path)
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Given the image, extract the text from the image."},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
                },
            ],
        }
    ],
    max_tokens=500,
)

print(response.choices[0].message.content)
