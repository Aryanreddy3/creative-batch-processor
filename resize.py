from PIL import Image # type: ignore
import os

def batch_resize(input_folder, output_folder, size=(800, 800)):
    os.makedirs(output_folder, exist_ok=True)
    for file_name in os.listdir(input_folder):
        if file_name.endswith((".jpg", ".png", ".jpeg")):
            img = Image.open(os.path.join(input_folder, file_name))
            img = img.resize(size)
            img.save(os.path.join(output_folder, file_name))
    print(f"Resized images saved to {output_folder}.")
