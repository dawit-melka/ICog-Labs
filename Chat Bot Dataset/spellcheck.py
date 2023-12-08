import os
from spellchecker import SpellChecker

def spell_checker_correction_hunspell(text, language='en_US'):
    spellchecker = SpellChecker()
    words = text.split()
    corrected_text = [ spellchecker.correction(word) if spellchecker.correction(word) != None else "" for word in words]
    corrected_text = ' '.join(corrected_text)
    return corrected_text

def process_files_in_directory(directory_path, output_directory):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Create a Hunspell instance for English
    spellchecker = SpellChecker()

    # Iterate over files in the specified directory
    for filename in os.listdir(directory_path):
        print(filename)
        if filename.endswith(".txt"):
            input_file_path = os.path.join(directory_path, filename)
            output_file_path = os.path.join(output_directory, filename)
            
            # Check if the output file already exists
            if os.path.exists(output_file_path):
                print(f"Output file already exists. Skipping: {input_file_path}")
                continue

            # Read the content of the input file
            with open(input_file_path, 'r', encoding='utf-8') as file:
                text = file.read()

            # Perform spell checking and correction
            corrected_text = spell_checker_correction_hunspell(text)

            # Write the corrected text to the output file
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(corrected_text)

            print(f"Processed: {input_file_path}")

# Example usage
input_directory = 'raw data/pdf to txt files/'
output_directory = 'clean data/pdf files/'

process_files_in_directory(input_directory, output_directory)

