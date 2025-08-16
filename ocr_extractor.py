# run_ocr.py

import pytesseract
from PIL import Image, UnidentifiedImageError

def extract_text_from_image(image_path: str) -> str:
    """
    Extracts text from an image file using Tesseract OCR.

    Args:
        image_path (str): The full path to the image file.

    Returns:
        str: The extracted text, or an error message if something goes wrong.
    """
    try:
        print(f"Attempting to open image at: {image_path}")
        img = Image.open(image_path)
        
        print("Image opened successfully. Extracting text...")
        text = pytesseract.image_to_string(img)
        
        return text

    except FileNotFoundError:
        return f"Error: The file was not found at '{image_path}'."
        
    except UnidentifiedImageError:
        return f"Error: The file at '{image_path}' is not a valid image."

    except pytesseract.TesseractNotFoundError:
        return (
            "Error: Tesseract is not installed or it's not in your PATH.\n"
            "Please ensure Tesseract is installed correctly."
        )
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# --- Main execution block ---
if __name__ == "__main__":
    
    # <-- THIS IS THE LINE WITH YOUR PATH
    # The 'r' before the string is important for Windows paths.
    IMAGE_PATH = r"C:\Users\saten\Downloads\PROJECTS\Other Projects\OCR Extractor\test_img.jpg"

    print("--- Starting OCR Program ---")
    
    # Call the function with the pre-defined path
    extracted_text = extract_text_from_image(IMAGE_PATH)

    # Display the result
    print("\n--- Extracted Text ---")
    if "Error:" in extracted_text:
        print(extracted_text)
    elif not extracted_text.strip():
        print("[No text was detected in the image.]")
    else:
        print(extracted_text)
    print("----------------------")