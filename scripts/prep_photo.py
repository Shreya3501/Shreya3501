from rembg import remove
from PIL import Image
import cv2
import numpy as np
import sys

if len(sys.argv) != 2:
    print("Usage: python prep_photo.py images/source-photo.jpg")
    exit()

input_path = sys.argv[1]

img = Image.open(input_path)

img = remove(img)

img = img.convert("RGBA")

white = Image.new("RGBA", img.size, (255, 255, 255, 255))
white.paste(img, mask=img.split()[3])

white = white.convert("L")

arr = np.array(white)

clahe = cv2.createCLAHE(
    clipLimit=2.0,
    tileGridSize=(8, 8)
)

result = clahe.apply(arr)

cv2.imwrite("source-prepped.png", result)

print("Done!")