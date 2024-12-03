README: Hash Spoofing Tool

Overview

This project implements a Python script (hashspoofing.py) that adjusts an image file such that:

The file's hash (SHA-512) begins with a specified hexadecimal prefix.

The visual representation of the image remains unchanged when viewed in standard image viewers.

The script operates by iteratively modifying metadata in the image until the desired hash prefix is achieved.

How It Works

Input Parameters

The script requires the following inputs:

Target Prefix: The desired hexadecimal prefix for the hash (e.g., 24).

Input Image Path: The file path to the original image to be modified.

Output Image Path: The file path where the modified image will be saved.

Process

Image Loading: The script uses the Python Imaging Library (Pillow) to load the input image.

Iterative Hash Modification:

The script calculates the SHA-512 hash of the image file.

If the hash does not start with the target prefix, the script appends random data to the image's metadata to change the hash.

This process repeats until a hash is found that matches the desired prefix.

Saving the Modified Image: Once the target hash is achieved, the modified image is saved to the specified output path.

Output

The script outputs the modified image file.

It prints the matched hash to the console for verification.

Usage

Prerequisites

Install Python 3.6 or higher.

Install the required libraries:

pip install pillow

Command

To run the script, use the following command:

python hashspoofing.py <target_prefix> <input_image_path> <output_image_path>

Example:

python hashspoofing.py 24 "C:\Users\Bran\OneDrive\Desktop\strath\Pictures\Every Artwork in Beyonce and Jay-Z’s Newest Music Video.png" "C:\Users\Bran\Desktop\hash.py\altered.png"

Output Verification

Use PowerShell or another tool to verify the hash of the output file:

Get-FileHash -Algorithm SHA512 -Path "C:\Users\Bran\Desktop\hash.py\altered.png"

Ensure the hash begins with the target prefix.

Detailed Example

Input

Target Prefix: 24

Input Image Path: C:\Users\Bran\OneDrive\Desktop\strath\Pictures\Every Artwork in Beyonce and Jay-Z’s Newest Music Video.png

Output Image Path: C:\Users\Bran\Desktop\hash.py\altered.png

Execution

Command:

python hashspoofing.py 24 "C:\Users\Bran\OneDrive\Desktop\strath\Pictures\Every Artwork in Beyonce and Jay-Z’s Newest Music Video.png" "C:\Users\Bran\Desktop\hash.py\altered.png"

Console Output:

Match found! Hash: 24745a6cabe600be51a0b9d4885eab138043cf24f99c1a05cbe60cad2b7531a1c229b26feef0b4490ef2a93b71ef38755df293a012f23411994d0d28a47914b0

Output File

Modified file: C:\Users\Bran\Desktop\hash.py\altered.png

Verified hash: Begins with 24.

Script Details

Code Structure

modify_image_for_hash_prefix(target_prefix, input_path, output_path): Main function that handles the hash modification process.

hash_file(file_path): Helper function to compute the SHA-512 hash of a file.

append_metadata(image): Helper function to append random metadata to the image.

Libraries Used

Pillow: For image manipulation.

Hashlib: For computing SHA-512 hashes.

OS: For file system operations.

Notes and Limitations

Processing Time: The time required depends on the length of the prefix and randomness of hash generation.

Compatibility: The script preserves image compatibility with standard viewers but may not work with highly restrictive formats.

Metadata Changes: The script modifies metadata but avoids altering visible content.

Supported Formats: The script works best with formats like PNG, JPEG, and BMP.

Acknowledgments

This project was developed to explore hash manipulation and metadata-based file adjustments. It highlights how digital files can be engineered to meet specific hash-based constraints without altering their visual integrity.

