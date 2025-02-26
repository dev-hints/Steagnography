from tkinter import filedialog, messagebox, Tk, Button, Label, Entry
from PIL import Image
import cv2
import numpy as np

def encode_message():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return

    img = cv2.imread(file_path)
    message = entry.get()
    
    if not message:
        messagebox.showerror("Error", "Enter a message to encode")
        return
    
    # Convert message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'  # Delimiter to detect end of message
    
    data_index = 0
    binary_len = len(binary_message)
    
    for row in img:
        for pixel in row:
            for i in range(3):  # Loop over RGB channels
                if data_index < binary_len:
                    pixel[i] = int(bin(pixel[i])[2:-1] + binary_message[data_index], 2)
                    data_index += 1
                else:
                    break
            if data_index >= binary_len:
                break
        if data_index >= binary_len:
            break
    
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG file", "*.png")])
    if save_path:
        cv2.imwrite(save_path, img)
        messagebox.showinfo("Success", "Message encoded and saved successfully!")

# GUI Setup
root = Tk()
root.title("Steganography - Encode Text in Image")

Label(root, text="Enter message:").pack()
entry = Entry(root, width=50)
entry.pack()

Button(root, text="Select Image & Encode", command=encode_message).pack()
root.mainloop()
