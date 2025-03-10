# PRODIGY_CS_01_Encrypting and Decrypting text script
# Caesar Cipher GUI

This is a simple GUI application that implements the **Caesar Cipher** algorithm for encrypting and decrypting text. The application allows users to input a message and a shift value, then perform encryption or decryption. It also includes convenient "Paste" and "Copy" buttons for easier text handling.

## Features
- **Encrypt and Decrypt Messages** using the Caesar Cipher
- **User-friendly Interface** with labeled input fields and buttons
- **Paste & Copy Support** for easier text handling
- **Automatic Placeholder Handling** in the text entry field

## Requirements
Make sure you have the following installed:
- Python 3.x
- Tkinter (included in standard Python installation)
- `pyperclip` module (for clipboard functionality)

To install `pyperclip`, run:
```sh
pip install pyperclip
```

## How to Use
1. **Enter the text** in the input field.
2. **Enter the shift value** (default is 3).
3. Click **Encrypt** to encode the message.
4. Click **Decrypt** to decode the message.
5. Use the **Paste** button to paste copied text into the input field.
6. Use the **Copy** button to copy the result to the clipboard.

## Screenshot
![App Screenshot](https://github.com/Abr-ahamis/PRODIGY_CS_01/blob/main/Screenshot%202025-03-03%20165030.png)

## Code Structure
- **`caesar_cipher(text, shift, decrypt=False)`**: Implements the Caesar cipher logic.
- **`encrypt()`**: Handles encryption using the shift value.
- **`decrypt()`**: Handles decryption using the shift value.
- **`paste_text()`**: Pastes text from the clipboard into the input field.
- **`copy_result()`**: Copies the result to the clipboard.
- **GUI elements**: Tkinter widgets for input, output, and buttons.

## License
This project is open-source and free to use. Feel free to modify and improve it!

---
Happy coding! 🚀

