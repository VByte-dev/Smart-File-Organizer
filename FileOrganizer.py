import os
import shutil

try:
    # Specify the directory to organize
    path = input('[+] Enter the Path of Directory: ')
    directory = path

    # Create folders for different file types
    folders = {
        '.doc': 'Documents',
        '.docx': 'Documents',
        '.txt': 'Documents',
        '.pdf': 'Documents',
        '.jpg': 'JPG Folder',
        '.jpeg': 'JPG Folder',
        '.png': 'PNG Folder',
        '.gif': 'GIF Folder',
        '.mp4': 'Videos',
        '.avi': 'Videos',
        '.mov': 'Videos',
        '.mp3': 'Music',
        '.wav': 'Music',
        '.py': 'Python Folder'
    }

    # Check if the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError("Directory not found.")

    # Iterate through the directory
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            # Get the file extension
            file_ext = os.path.splitext(filename)[1].lower()

            # Move the file to the corresponding folder
            if file_ext in folders:
                folder_name = folders[file_ext]
                folder_path = os.path.join(directory, folder_name)
                os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist
                shutil.move(os.path.join(directory, filename), os.path.join(folder_path, filename))

    print("[+] File organization complete!")

except FileNotFoundError:
    print("[-] Error: Directory not found.")
except Exception as e:
    print("[-] An error occurred:", str(e))

e = input()
