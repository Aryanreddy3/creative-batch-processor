import os

def batch_rename(input_folder, new_name="image"):
    for i, file_name in enumerate(os.listdir(input_folder)):
        ext = file_name.split('.')[-1]
        new_file_name = f"{new_name}_{i + 1}.{ext}"
        os.rename(
            os.path.join(input_folder, file_name),
            os.path.join(input_folder, new_file_name)
        )
    print(f"Renamed images in {input_folder}.")
