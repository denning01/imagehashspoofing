import sys
import hashlib
import random
import string
from PIL import Image
import os

def modify_image_for_hash_prefix(target_prefix, input_path, output_path, hash_function="sha512"):
    """
    Modify an image file to generate a hash starting with a specific prefix.
    """
    # Load the image
    image = Image.open(input_path)
    
    # Save a temporary copy to start
    image.save(output_path)
    
    # Append metadata and modify until hash matches prefix
    prefix_length = len(target_prefix)
    with open(output_path, "ab") as f:
        while True:
            # Generate random metadata
            random_data = ''.join(random.choices(string.ascii_letters + string.digits, k=10)).encode('utf-8')
            f.write(random_data)
            
            # Calculate hash
            with open(output_path, "rb") as img_file:
                data = img_file.read()
                hash_value = hashlib.new(hash_function, data).hexdigest()
            
            # Check prefix
            if hash_value.startswith(target_prefix):
                print(f"Match found! Hash: {hash_value}")
                break

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python hashspoofing.py <target_prefix> <input_image_path> <output_image_path>")
        sys.exit(1)
    
    target_prefix = sys.argv[1]
    input_image = sys.argv[2]
    output_image = sys.argv[3]
    
    modify_image_for_hash_prefix(target_prefix, input_image, output_image)
