import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image
import numpy as np
import Encryption
import Decryption
# Encryption Function
def encrypt_image(image_path, secret_message, passcode):
    if len(passcode) != 4:
        messagebox.showerror("Error", "Invalid passcode size! Passcode must be 4 digits.")
        return

    try:
        # Open the image
        img = Image.open(image_path)
        img = img.convert("RGB")  # Convert to RGB mode
        pixels = np.array(img)

        # Add delimiter to mark the end of the message
        secret_message += str(passcode)+"#####"
        pixels = Encryption.encryption(secret_message, pixels)

        # Save the encrypted image
        encrypted_img = Image.fromarray(pixels)
        output_path = image_path.replace(".", "_encrypted.")
        encrypted_img.save(output_path)
        messagebox.showinfo("Success", f"Message encrypted successfully!\nSaved as: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Decryption Function
def decrypt_image(image_path, passcode):
    if len(passcode) != 4:
        messagebox.showerror("Error", "Invalid passcode size! Passcode must be 4 digits.")
        return
    try:
        # Open the image
        img = Image.open(image_path)
        img = img.convert("RGB")  # Convert to RGB mode
        pixels = np.array(img)

        message = Decryption.decryption(pixels)
        # Verify if the message was found
        cpasscode = message[-9:-5]
        if message[-5:]=="#####":
            # Verify passcode (for demonstration, we assume passcode is part of the message)
            if passcode == cpasscode:  # Replace with your passcode validation logic
                messagebox.showinfo("Success", f"Decrypted Message: {message[:-9]}")
            else:
                messagebox.showerror("Error", "Incorrect passcode!")
        else:
            messagebox.showerror("Error", "No hidden message found!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI Setup
def create_gui():
    root = tk.Tk()
    root.title("Secure Data Hiding in Images")
    root.geometry("400x300")
    root.configure(bg="#f0f0f0")

    # Encryption Section
    def encrypt():
        image_path = filedialog.askopenfilename(title="Select Image to Encrypt", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if not image_path:
            return

        secret_message = entry_message.get("1.0", tk.END).strip()
        passcode = entry_passcode.get().strip()

        if secret_message and passcode:
            encrypt_image(image_path, secret_message, passcode)

    # Decryption Section
    def decrypt():
        image_path = filedialog.askopenfilename(title="Select Image to Decrypt", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if not image_path:
            return

        # Ask for passcode in a new dialog
        passcode = simpledialog.askstring("Passcode", "Enter 4-Digit Passcode:", show='*')
        if passcode:
            decrypt_image(image_path, passcode)

    # GUI Elements
    label_title = tk.Label(root, text="Secure Data Hiding in Images", font=("Arial", 14), bg="#f0f0f0")
    label_title.pack(pady=10)

    label_message = tk.Label(root, text="Enter Secret Message:", bg="#f0f0f0")
    label_message.pack()
    entry_message = tk.Text(root, height=4, width=40)
    entry_message.pack(pady=5)

    label_passcode = tk.Label(root, text="Enter 4-Digit Passcode:", bg="#f0f0f0")
    label_passcode.pack()
    entry_passcode = tk.Entry(root, width=22)
    entry_passcode.pack(pady=10)

    button_encrypt = tk.Button(root, text="Encrypt", command=encrypt, bg="#389bd9", fg="black", padx=10, pady=5)
    button_encrypt.pack(pady=6)

    button_decrypt = tk.Button(root, text="Decrypt", command=decrypt, bg="#ff4040", fg="white", padx=10, pady=5)
    button_decrypt.pack(pady=6)

    root.mainloop()

# Run the GUI
if __name__ == "__main__":
    create_gui()