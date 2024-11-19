import os
from PIL import Image # type: ignore


image_path = "assets/forest01.jpg"
output_path = "output/forest01_resized.jpg"

image_path = "assets/mountree.jpg"
output_path = "output/mountree_resized.jpg"

image_path = "assets/azgp.jpg"
output_path = "output/azgp_resized.jpg"
image_path = "assets/aroad.jpg"
output_path = "output/aroad_resized.jpg"



img = Image.open(image_path)
img.save(output_path)
print("Image saved successfully!")
from resize import batch_resize

input_folder = "assets/"
output_folder = "output/"
size = (800, 800)  # Width x Height


batch_resize(input_folder, output_folder, size)
from rename import batch_rename

batch_rename(input_folder, new_name="processed_image")
from compress import batch_compress

batch_compress(input_folder, output_folder, quality=70)
from resize import batch_resize
from rename import batch_rename
from compress import batch_compress

input_folder = "assets/"
output_folder = "output/"

# Resize
batch_resize(input_folder, output_folder, size=(800, 800))

# Rename
batch_rename(output_folder, new_name="final_image")

# Compress
batch_compress(output_folder, output_folder, quality=80)
from resize import batch_resize
from rename import batch_rename
from compress import batch_compress
from filters import apply_filter
from PIL import Image # type: ignore

input_folder = "assets/"
output_folder = "output/"

# Function to apply filter to each image
def apply_filters_to_batch(input_folder, output_folder, filter_type="grayscale"):
    os.makedirs(output_folder, exist_ok=True)
    for file_name in os.listdir(input_folder):
        if file_name.endswith((".jpg", ".jpeg", ".png")):
            img = Image.open(os.path.join(input_folder, file_name))
            img = apply_filter(img, filter_type)
            img.save(os.path.join(output_folder, file_name))

# Apply the filters, then resize, rename, and compress
apply_filters_to_batch(input_folder, output_folder, filter_type="sepia")  # Example: Apply sepia filter
batch_resize(output_folder, output_folder, size=(800, 800))  # Resize after filter
batch_rename(output_folder, new_name="final_image")  # Rename after resizing
batch_compress(output_folder, output_folder, quality=80)  # Compress after renaming
from resize import batch_resize
from rename import batch_rename
from compress import batch_compress
from filters import apply_filter
from compress import batch_export
from PIL import Image # type: ignore

input_folder = "assets/"
output_folder = "output/"

# Apply the filters, then resize, rename, compress, and export
apply_filters_to_batch(input_folder, output_folder, filter_type="brightness")
batch_resize(output_folder, output_folder, size=(800, 800))
batch_rename(output_folder, new_name="final_image")
batch_compress(output_folder, output_folder, quality=80)
batch_export(output_folder, output_folder, new_format="PNG")  # Export as PNG
from filters import apply_grayscale, apply_sepia, apply_blur, adjust_brightness, adjust_contrast

def apply_filters_to_batch(input_folder, output_folder, filter_type):
    for file_name in os.listdir(input_folder):
        if file_name.endswith((".jpg", ".png", ".jpeg")):
            img = Image.open(os.path.join(input_folder, file_name))
            
            if filter_type == "grayscale":
                img = apply_grayscale(img)
            elif filter_type == "sepia":
                img = apply_sepia(img)
            elif filter_type == "blur":
                img = apply_blur(img)
            elif filter_type == "brightness":
                img = adjust_brightness(img, factor=1.2)
            elif filter_type == "contrast":
                img = adjust_contrast(img, factor=1.5)
            
            img.save(os.path.join(output_folder, file_name))

from filters import apply_grayscale, apply_sepia, apply_blur, adjust_brightness, adjust_contrast
from PIL import Image # type: ignore
from filters import apply_grayscale

# Test with a single image
img = Image.open("assets/ajeep.jpg")
img = apply_grayscale(img)
img.save("output/ajeep_grayscale.jpg")

