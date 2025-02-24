import cv2
import os
import string

def decrypt_message(image_path, password):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not open the image.")
        return

    n, m, z = 0, 0, 0
    extracted_message = ""

    while True:
        char = chr(img[n, m, z])  
        if char == "\x00":  
            break  
        extracted_message += char
        n = (n + 1) % img.shape[0]  
        m = (m + 1) % img.shape[1]  
        z = (z + 1) % 3  

    # Validate password
    if "::" in extracted_message:
        stored_password, secret_message = extracted_message.split("::", 1)
        if stored_password == password:
            print("Decryption successful! Secret message:", secret_message)
        else:
            print("Error: Incorrect password!")
    else:
        print("Error: No valid encrypted message found.")

# Run decryption
if __name__ == "__main__":
    img_path = input("Enter encrypted image path: ")
    passcode = input("Enter passcode for decryption: ")
    decrypt_message(img_path, passcode)