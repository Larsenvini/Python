import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input.jpg output.jpg")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    if not valid_extension(input_path) or not valid_extension(output_path):
        sys.exit("Input and output must be .jpg, .jpeg or .png")

    if not same_extension(input_path, output_path):
        sys.exit("Input and output must have the same extension")

    if not os.path.isfile(input_path):
        sys.exit(f"Input file does not exist: {input_path}")

    try:
        process_image(input_path, output_path)
    except Exception as e:
        sys.exit(f"Error processing image: {e}")

def valid_extension(filename):
    valid_extensions ={".jpg", ".jpeg", ".png"}
    ext = os.path.splitext(filename)[1].lower()
    return ext in valid_extensions

def same_extension(file1,file2):
    return os.path.splitext(file1)[1].lower() == os.path.splitext(file2)[1].lower()

def process_image(input_path, output_path):
    try:
        shirt = Image.open("shirt.png")
        size = shirt.size
        print(f"Shirt size: {size}")

        with Image.open(input_path) as im:
            im = ImageOps.fit(im, size, method=Image.LANCZOS, bleed=0.0, centering=(0.5, 0.5))
            print(f"Resized image size: {im.size}")

            im.paste(shirt, (0, 0), shirt)
            im.save(output_path)
            print(f"Image saved as {output_path}")

    except FileNotFoundError as fnf_error:
        sys.exit(f"Error: {fnf_error}")
    except Exception as e:
        sys.exit(f"Error processing image: {e}")


if __name__ == "__main__":
    main()
