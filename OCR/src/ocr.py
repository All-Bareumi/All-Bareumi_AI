import pytesseract
import cv2 
import matplotlib.pyplot as plt

path = '../data/ocr_test.png'
image = cv2.imread(path)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# use Tesseract to OCR the image 
text = pytesseract.image_to_string(rgb_image, lang='kor')
print(text)

