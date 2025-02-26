from tkinter import filedialog, messagebox, Tk, Button, Label
import cv2

def decode_message():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return

    img = cv2.imread(file_path)
    binary_data = ""
    
    for row in img:
        for pixel in row:
            for i in range(3):  # Loop over RGB channels
                binary_data += bin(pixel[i])[-1]  # Extract LSB

    # Convert binary to text
    text = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if byte == "1111111111111110":  # End delimiter
            break
        text += chr(int(byte, 2))
    
    messagebox.showinfo("Decoded Message", f"Hidden Message: {text}")

# GUI Setup
root = Tk()
root.title("Steganography - Decode Message from Image")

Label(root, text="Select Image to Decode Message").pack()
Button(root, text="Select Image & Decode", command=decode_message).pack()
root.mainloop()
