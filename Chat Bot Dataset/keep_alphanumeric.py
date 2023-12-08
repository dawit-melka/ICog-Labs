import os
import re

def keep_alphanumeric_and_dot(text):
    # Keep only alphanumeric characters and dots
    cleaned_text = re.sub(r'[^a-zA-Z0-9.]', ' ', text)
    return cleaned_text

def process_files_remove_non_alphanumeric_except_dot(directory_path, output_directory):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterate over files in the specified directory
    for filename in os.listdir(directory_path):
        print(filename)
        if filename.endswith(".txt"):
            input_file_path = os.path.join(directory_path, filename)
            output_file_path = os.path.join(output_directory, filename)

            # Read the content of the input file
            with open(input_file_path, 'r', encoding='utf-8') as file:
                text = file.read()

            # Keep only alphanumeric characters and dots
            cleaned_text = keep_alphanumeric_and_dot(text)

            # Write the cleaned text to the output file
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(cleaned_text)

            print(f"Processed: {input_file_path}")

# Example usage
input_directory = 'clean data/pdf files/'
output_directory = 'clean data/txt files/'

process_files_remove_non_alphanumeric_except_dot(input_directory, output_directory)
