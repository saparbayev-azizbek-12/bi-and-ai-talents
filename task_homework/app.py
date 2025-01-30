import os
import time
import requests
from environs import Env
from first_page_pdf import get_image_of_pdf

env = Env()
env.read_env()

TOKEN = env("TOKEN")
CHANNEL_USERNAME = env("CHANNEL_USERNAME")

def mark_change(path):
    return str(path).replace('\\', "/")

def size_checker(file_path):
    file_size = os.path.getsize(file_path) / (1024 * 1024)
    return True if file_size < 50 else False

# Local variables
count1, count2 = 0, 0
valid_files = []
invalid_files = []

# Input your PDF files directory path here
PDF_DIR_PATH = input("Enter your PDF directory path: ")

if os.listdir(PDF_DIR_PATH):
    for pdf_path in os.listdir(PDF_DIR_PATH):
        if pdf_path.endswith(".pdf"):
            PDF_PATH = f"{PDF_DIR_PATH}\{pdf_path}"
            if size_checker(PDF_PATH):
                IMAGE_PATH = mark_change(get_image_of_pdf(PDF_PATH))

                count2 += 1
                valid_files.append(pdf_path)

                send_photo_url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
                photo_files = {"photo": open(IMAGE_PATH, "rb")}
                photo_params = {"chat_id": CHANNEL_USERNAME}

                photo_response = requests.post(send_photo_url, files=photo_files, data=photo_params)
                photo_data = photo_response.json()

                if photo_data.get("ok"):
                    message_id = photo_data["result"]["message_id"]
                    print(f"Image sent successfully! Message ID: {message_id}")
                    
                    time.sleep(2)

                    send_document_url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
                    document_files = {"document": open(mark_change(PDF_PATH), "rb")}
                    document_params = {
                        "chat_id": CHANNEL_USERNAME,
                        "reply_to_message_id": message_id
                    }

                    document_response = requests.post(send_document_url, files=document_files, data=document_params)
                    document_data = document_response.json()

                    if document_data.get("ok"):
                        print("PDF sent successfully as a reply to the image.")
                    else:
                        print("Failed to send PDF:", document_data)
                else:
                    print("Failed to send the image:", photo_data)
            else:
                invalid_files.append(pdf_path)
        else:
            count1 += 1
else:
    print("\nThe directory is empty!")
if count1 != 0 and count2 == 0:
    print("\nNo PDF file found in the directory.")


# Print valid and invalid files
if valid_files:
    print("\nThe following files were sent successfully:")
    for i, valid in enumerate(valid_files):
        print(f"{i+1}. {valid}")

if invalid_files:
    print("\nThe following files were not sent due to their size exceeding the limit:")
    for i, invalid in enumerate(invalid_files):
        print(f"{i+1}. {invalid}")
        