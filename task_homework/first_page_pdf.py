import os
import re
import fitz #PyMuPDF

def get_image_of_pdf(path):
    with fitz.open(path) as pdf_document:

        directory = r"C:\Users\ADMIN\Desktop\bi-and-ai-talents\task_homework\media"
        
        exiting_numbers = [int(re.findall(r'\d+', f)[0]) for f in os.listdir(directory) if f.startswith("first_page_") and f.endswith(".png")]
        if exiting_numbers:
            number = max(exiting_numbers) + 1
        else:
            number = 1

        first_page = pdf_document[0]
        pix = first_page.get_pixmap()
        image_path = fr"{directory}\first_page_{number}.png"
        pix.save(image_path)
        print(f"\nFirst page saved as 'first_page_{number}.png")
    return image_path
