import os
def remove_webp_extension(folder_path):
    # List all files in the folder path
    files = os.listdir(folder_path)
    # Loop through each file
    for filename in files:
        try:
            # Check if the file ends with .webp
            if filename.endswith(".webp"):
                # Define the original and new file paths
                original_path = os.path.join(folder_path, filename)
                new_filename = filename[:-5]  # Remove the last 5 characters (".webp")
                # new_filename = f"{new_filename}.png"
                new_path = os.path.join(folder_path, new_filename)
                # Rename the file
                os.rename(original_path, new_path)
                print(f"Renamed {filename} to {new_filename}")
        except Exception as e:
            print(f"Failed to rename {filename}: {e}")
# Folder path containing the images
folder_path = 'D:/Programing/ProjectsTest/New folder'
# Run the function
remove_webp_extension(folder_path)