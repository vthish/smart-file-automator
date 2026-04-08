import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

class FileAutomatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart File Automator - Venusha Thishan") 
        self.root.geometry("500x250")

        # UI Components
        self.label = tk.Label(root, text="Select Folder to Organize:", font=("Arial", 10))
        self.label.pack(pady=10)

        self.path_entry = tk.Entry(root, width=50)
        self.path_entry.pack(pady=5)

        self.browse_btn = tk.Button(root, text="Browse Folder", command=self.browse_folder)
        self.browse_btn.pack(pady=5)

        self.start_btn = tk.Button(root, text="Start Organizing", bg="green", fg="white", 
                                   command=self.run_organizer, font=("Arial", 10, "bold"))
        self.start_btn.pack(pady=20)

    def browse_folder(self):
        selected_path = filedialog.askdirectory()
        if selected_path:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, selected_path)

    def run_organizer(self):
        target = self.path_entry.get()
        if not target or not os.path.exists(target):
            messagebox.showerror("Error", "Please select a valid folder path!")
            return

        # Define file categories and their extensions
        file_types = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp'],
            'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.sql'],
            'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
            'Audio': ['.mp3', '.wav', '.aac'],
            'Archives': ['.zip', '.rar', '.7z', '.tar']
        }
        
        # Folders to exclude from being moved
        protected_folders = list(file_types.keys()) + ['Others']
        count = 0

        try:
            for item in os.listdir(target):
                item_path = os.path.join(target, item)
                
                # Skip the script itself and already organized folders
                if item == "organizer.py" or item in protected_folders:
                    continue
                
                moved = False
                try:
                    # Logic to handle FILES
                    if os.path.isfile(item_path):
                        file_ext = os.path.splitext(item)[1].lower()
                        for folder_name, extensions in file_types.items():
                            if file_ext in extensions:
                                dest_folder = os.path.join(target, folder_name)
                                os.makedirs(dest_folder, exist_ok=True)
                                shutil.move(item_path, os.path.join(dest_folder, item))
                                moved = True
                                break
                    
                    # Logic to handle SUB-FOLDERS (Move them to 'Others')
                    elif os.path.isdir(item_path):
                        other_folder = os.path.join(target, 'Others')
                        os.makedirs(other_folder, exist_ok=True)
                        shutil.move(item_path, os.path.join(other_folder, item))
                        moved = True

                    # Move unknown file types to 'Others'
                    if not moved:
                        other_folder = os.path.join(target, 'Others')
                        os.makedirs(other_folder, exist_ok=True)
                        shutil.move(item_path, os.path.join(other_folder, item))
                    
                    count += 1

                except Exception as e:
                    # Print error to terminal if a specific file is locked/busy
                    print(f"Skipped {item}: {e}")
            
            messagebox.showinfo("Success", f"Organization Complete! Processed {count} items.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileAutomatorApp(root)
    root.mainloop()