from PIL import Image
import os

def resize_image(input_path, output_path, width, height):
    try:
        with Image.open(input_path) as img:
            resized_img = img.resize((width, height))
            resized_img.save(output_path)
            print(f"Image saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("=== Image Resizer ===")
    input_path = input("Enter path to image file: ")
    output_path = input("Enter path to save resized image: ")
    width = int(input("Enter new width: "))
    height = int(input("Enter new height: "))
    
    resize_image(input_path, output_path, width, height)
