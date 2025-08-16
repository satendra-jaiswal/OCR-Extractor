# 🖼️ OCR Extractor  

A simple Python-based **Optical Character Recognition (OCR)** tool that extracts text from images using **Tesseract OCR** and **Pillow (PIL)**.  

---

## 📌 Features  
- 📄 Extracts text from multiple image formats (JPG, PNG, etc.)  
- ⚠️ Handles errors gracefully (invalid images, missing files, Tesseract not installed)  
- 🖥️ Easy-to-run script with customizable image path  
- 🔍 Detects when no text is present in the image  

---

## 🛠️ Tech Stack  
- **Python 3.x**  
- **pytesseract** (Python wrapper for Tesseract OCR)  
- **Pillow (PIL)**  

---

## 📂 Project Structure  
```bash
OCR-Extractor/
│── run_ocr.py          # Main Python script
│── test_img.jpg        # Sample image 1
│── test_img2.jpg       # Sample image 2
│── test_img3.jpg       # Sample image 3
│── output_example.png  # Screenshot of OCR result
└── README.md           # Documentation

