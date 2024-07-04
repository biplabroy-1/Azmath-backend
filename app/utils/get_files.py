import os

def list_files():
    directory_path = 'uploads'
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created.")
    
    try:
        files = os.listdir(directory_path)
        print(files)
        return files
    except Exception as e:
        return str(e), 500