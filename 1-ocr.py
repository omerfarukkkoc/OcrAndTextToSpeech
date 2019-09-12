from PIL import Image
import pytesseract

im = Image.open("text4.jpg")

text = pytesseract.image_to_string(im, lang='tur')

print(text)
