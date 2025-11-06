import os
import shutil

def sort_images_from_drive(source_drive_path, destination_folder_path):
    """
    Scans a specified drive for image files and copies them to a destination folder.

    Args:
        source_drive_path (str): The path to the drive or folder to scan (e.g., 'C:\\', '/mnt/data').
        destination_folder_path (str): The path to the folder where images will be copied.
    """
    # Define common image file extensions (case-insensitive)
    IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.webp', '.heic')

    print(f"Starting image sorting process...")
    print(f"Source: {source_drive_path}")
    print(f"Destination: {destination_folder_path}")
    print("-" * 40)

    # Validate source path
    if not os.path.isdir(source_drive_path):
        print(f"Error: Source path '{source_drive_path}' is not a valid directory or does not exist.")
        return

    # Create destination folder if it doesn't exist
    try:
        os.makedirs(destination_folder_path, exist_ok=True)
        print(f"Destination folder '{destination_folder_path}' ensured.")
    except OSError as e:
        print(f"Error: Could not create destination folder '{destination_folder_path}'. Reason: {e}")
        return

    found_images_count = 0
    copied_images_count = 0
    skipped_count = 0

    # Walk through the source drive/folder
    for root, _, files in os.walk(source_drive_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            # Get the file extension and convert to lowercase for case-insensitive comparison
            file_extension = os.path.splitext(filename)[1].lower()

            if file_extension in IMAGE_EXTENSIONS:
                found_images_count += 1
                try:
                    # Construct the destination path for the image
                    destination_file_path = os.path.join(destination_folder_path, filename)

                    # Check if a file with the same name already exists in the destination
                    # If it does, you might want to rename it (e.g., add a timestamp)
                    # For simplicity, this script will overwrite if names conflict.
                    # To avoid overwriting, you could add:
                    # if os.path.exists(destination_file_path):
                    #     base, ext = os.path.splitext(filename)
                    #     new_filename = f"{base}_{int(time.time())}{ext}"
                    #     destination_file_path = os.path.join(destination_folder_path, new_filename)

                    shutil.copy2(file_path, destination_file_path) # copy2 preserves metadata
                    copied_images_count += 1
                    print(f"Copied: '{file_path}' to '{destination_file_path}'")
                except shutil.SameFileError:
                    print(f"Skipped: '{file_path}' - Source and destination are the same file.")
                    skipped_count += 1
                except FileNotFoundError:
                    print(f"Error: Source file '{file_path}' not found during copy. It might have been moved or deleted.")
                    skipped_count += 1
                except PermissionError:
                    print(f"Permission Denied: Could not copy '{file_path}'. Check permissions.")
                    skipped_count += 1
                except Exception as e:
                    print(f"An unexpected error occurred while copying '{file_path}': {e}")
                    skipped_count += 1
            else:
                # Optionally, you can print files that are not images
                # print(f"Skipping non-image file: {file_path}")
                pass

    print("-" * 40)
    print(f"Image sorting complete!")
    print(f"Total images found: {found_images_count}")
    print(f"Total images copied: {copied_images_count}")
    print(f"Total files skipped/errors: {skipped_count}")
    print(f"Note: Some files might be skipped due to permissions or other issues.")

if __name__ == "__main__":
    # --- Configuration ---
    # IMPORTANT: Replace these paths with your actual drive and destination folder.
    # On Windows, it might be something like 'D:\\' or 'E:\\Users\\YourUser\\Pictures'
    # On macOS/Linux, it might be '/home/youruser/my_drive' or '/Volumes/MyExternalDrive'

    # Example for Windows:
    # source_path = 'C:\\Users\\YourUser\\Documents'
    # destination_path = 'D:\\SortedImages'

    # Example for macOS/Linux:
    # source_path = '/Users/youruser/Documents'
    # destination_path = '/Users/youruser/SortedImages'

    # You can also use a relative path for the destination, e.g., 'SortedImages'
    # which will create the folder in the same directory as the script.

    # Get source path from user input
    source_path_input = input("Enter the full path of the drive/folder to scan (e.g., C:\\ or /home/user/my_drive): ")
    # Get destination path from user input
    destination_path_input = input("Enter the full path of the folder where images should be stored: ")

    # Normalize paths to handle different OS path separators
    source_path = os.path.normpath(source_path_input)
    destination_path = os.path.normpath(destination_path_input)

    sort_images_from_drive(source_path, destination_path)