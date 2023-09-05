import os
import shutil

def convert_codon_file_to_text(input_directory, output_directory):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Get the list of directories in the input directory
    directories = [name for name in os.listdir(input_directory) if os.path.isdir(os.path.join(input_directory, name))]

    # Iterate over each directory
    for directory in directories:
        # Get the files in the current directory
        files = os.listdir(os.path.join(input_directory, directory))

        # Find the "codon" file, regardless of the extension
        codon_file = next((file for file in files if file.startswith("codon")), None)

        if codon_file:
            # Get the full path of the "codon" file
            codon_file_path = os.path.join(input_directory, directory, codon_file)

            # Create the output file path in the output directory
            output_file_path = os.path.join(output_directory, f"{directory}.txt")

            # Copy the contents of the "codon" file to the output file
            with open(codon_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
                output_file.write(input_file.read())

            print(f"Converted {codon_file_path} to {output_file_path}")

# Specify the input directory path where the directories with "codon" files are located
input_directory_path = 'G:\\Projects\\HIV_updated\\snap_outputs\\2021'  # Replace with the actual path to the parent directory

# Specify the output directory path where the converted text files will be saved
output_directory_path = 'G:\\Projects\\HIV_updated\\snap_outputs\\text_converted_codons\\2021_converted_codons'  # Replace with the actual path to the output directory

# Call the function to convert the "codon" files to text files
convert_codon_file_to_text(input_directory_path, output_directory_path)
