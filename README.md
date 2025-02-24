need to run python 3

encrypt py and decrypt py need cv2 library

solution

pip install opencv-python


1. Encrypting a Message

To hide a secret message in an image:

python encrypt.py

Steps:

1. The script will ask for the image file (mypic.png).

2. Enter the secret message you want to hide.

3. Provide a password for security.

4. The encrypted image is saved as encryptedImage.png



2. Decrypting a Message

To retrieve the hidden message from the encrypted image:

python decrypt.py

Steps:

1. The script reads encryptedImage.png

2. You must enter the correct password.

3. If the password matches, the hidden message is displayed.
