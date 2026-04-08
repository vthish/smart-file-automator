import os
import shutil

def organize_folder(target_path):
    # Mapping file extensions to folder names
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
        'Audio': ['.mp3', '.wav', '.aac'],
        'Archives': ['.zip', '.rar', '.7z', '.tar']
    }

    if not os.path.exists(target_path):
        print("The provided path does not exist!")
        return

    for filename in os.listdir(target_path):
        file_path = os.path.join(target_path, filename)
        
        # Checking if it's a file and not a directory
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            
            moved = False
            for folder_name, extensions in file_types.items():
                if file_ext in extensions:
                    dest_folder = os.path.join(target_path, folder_name)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    print(f"Moved: {filename} -> {folder_name}")
                    moved = True
                    break
            
            # If extension is not in the list, move to 'Others'
            if not moved:
                other_folder = os.path.join(target_path, 'Others')
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))

if __name__ == "__main__":
    print("Starting organization process...")
    # Example usage: organize_folder('C:/Users/YourName/Downloads')
