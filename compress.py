from PIL import Image # type: ignore
import os

def batch_compress(input_folder, output_folder, quality=85):
    os.makedirs(output_folder, exist_ok=True)
    for file_name in os.listdir(input_folder):
        if file_name.endswith((".jpg", ".jpeg", ".png")):
            img = Image.open(os.path.join(input_folder, file_name))
            img.save(os.path.join(output_folder, file_name), optimize=True, quality=quality)
    print(f"Compressed images saved to {output_folder}.")
from PIL import Image # type: ignore
import os

def batch_export(input_folder, output_folder, new_format="JPEG"):
    os.makedirs(output_folder, exist_ok=True)
    for file_name in os.listdir(input_folder):
        if file_name.endswith((".jpg", ".jpeg", ".png")):
            img = Image.open(os.path.join(input_folder, file_name))
            file_name_without_ext = os.path.splitext(file_name)[0]
            output_file = os.path.join(output_folder, f"{file_name_without_ext}.{new_format.lower()}")
            img.save(output_file, format=new_format)
    print(f"Exported images to {new_format} format.")
