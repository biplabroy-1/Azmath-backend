
import shutil
import os
import uuid

def upload_file(file):
    UPLOAD_DIR = "uploads"
    if not os.path.exists(UPLOAD_DIR):  
        os.makedirs(UPLOAD_DIR)
    # Generate a unique identifier
    unique_id = str(uuid.uuid4())
    
    # Extract the original file extension
    file_extension = os.path.splitext(file.filename)[1]
    
    # Create a new file name with the unique identifier and original extension
    new_file_name = f"{unique_id}{file_extension}"
    
    # Set the full file path
    file_location = f"{UPLOAD_DIR}/{new_file_name}"
    
    # Save the file
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    print(new_file_name)
    
    return f"{new_file_name}"