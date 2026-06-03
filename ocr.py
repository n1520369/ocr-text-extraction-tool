from PIL import Image
import pytesseract

image_path = input("Enter image path: ")

try:
    image = Image.open(image_path)

    extracted_text = pytesseract.image_to_string(image)

    print("\nExtracted Text:\n")
    print(extracted_text)

except Exception as e:
    print(f"Error: {e}")
