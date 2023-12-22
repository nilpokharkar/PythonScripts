import os

def rename_images(folder_path):
    # Get the list of files in the folder
    files = os.listdir(folder_path)
    
    # Filter only image files (you can customize the extension list)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Rename the files
    for i, old_name in enumerate(image_files):
        # Create the new name using the format 'new_name_{i}.extension'
        extension = os.path.splitext(old_name)[1]
        new_name = f"{i}{extension}"

        # Construct the full paths for the old and new names
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)
        print(f'Renamed: {old_path} -> {new_path}')

# Replace 'path_to_your_folder' with the path to the folder containing your images
folder_path = 'D:\\Nilakshi\\Fall2023\\Data\\Rename_1COderTest\\4'
rename_images(folder_path)
