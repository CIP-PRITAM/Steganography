import cv2  
import os 
import string

def encrypt_message(image_path, message, password, output_image="encryptedImage.png"):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not open the image.")
        return

    rows, cols, _ = img.shape
    max_chars = rows * cols  

    if len(message) > max_chars:
        print("Error: Message is too long for this image.")
        return

    # Embed password with message
    message = f"{password}::{message}"
    
    n, m, z = 0, 0, 0
    for char in message:
        img[n, m, z] = ord(char)  # Store ASCII value
        n = (n + 1) % rows  
        m = (m + 1) % cols  
        z = (z + 1) % 3  

    cv2.imwrite(output_image, img)
    print(f"Message encrypted successfully into {output_image}")
    os.system(f"start {output_image}")  

# Run encryption
if __name__ == "__main__":
    img_path = input("Enter image path: ")
    secret_msg = input("Enter secret message: ")
    passcode = input("Enter passcode: ")
    encrypt_message(img_path, secret_msg, passcode)