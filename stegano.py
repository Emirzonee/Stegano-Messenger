import sys
import os
from PIL import Image

def text_to_bin(message):
    return ''.join(format(ord(i), '08b') for i in message)

def bin_to_text(binary_data):
    all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data.endswith("#####"):
            return decoded_data[:-5]
    return decoded_data

def encode_image(image_path, secret_message, output_path):
    try:
        if not os.path.exists(image_path):
            print(f"Error: Source file '{image_path}' not found.")
            return

        print(f"Encoding message into '{image_path}'...")
        image = Image.open(image_path).convert('RGB')
        pixels = image.load()
        
        secret_message += "#####"
        binary_message = text_to_bin(secret_message)
        data_len = len(binary_message)
        width, height = image.size
        
        if data_len > width * height * 3:
            print("Error: Message too large for image capacity.")
            return

        idx = 0
        for y in range(height):
            for x in range(width):
                if idx < data_len:
                    r, g, b = pixels[x, y]
                    r = (r & ~1) | int(binary_message[idx]); idx += 1
                    if idx < data_len:
                        g = (g & ~1) | int(binary_message[idx]); idx += 1
                    if idx < data_len:
                        b = (b & ~1) | int(binary_message[idx]); idx += 1
                    pixels[x, y] = (r, g, b)
                else:
                    break
            if idx >= data_len: break
        
        image.save(output_path, "PNG")
        print(f"Success: Output saved to '{output_path}'")
        
    except Exception as e:
        print(f"Error: {e}")

def decode_image(image_path):
    try:
        if not os.path.exists(image_path):
            print(f"Error: File '{image_path}' not found.")
            return

        print(f"Decoding data from '{image_path}'...")
        image = Image.open(image_path).convert('RGB')
        pixels = image.load()
        
        binary_data = []
        width, height = image.size
        
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                binary_data.extend([str(r & 1), str(g & 1), str(b & 1)])

        message = bin_to_text("".join(binary_data))
        print("-" * 30)
        print("Decoded Message:")
        print(message)
        print("-" * 30)

    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Encode: python stegano.py encode <image> <message>")
        print("  Decode: python stegano.py decode <image>")
        return

    command = sys.argv[1].lower()

    if command == "encode":
        if len(sys.argv) < 4:
            print("Error: Missing arguments for encoding.")
            return
        img = sys.argv[2]
        msg = " ".join(sys.argv[3:])
        encode_image(img, msg, "secret_output.png")
    
    elif command == "decode":
        if len(sys.argv) < 3:
            print("Error: Missing image path.")
            return
        img = sys.argv[2]
        decode_image(img)
    
    else:
        print(f"Error: Unknown command '{command}'")

if __name__ == "__main__":
    main()