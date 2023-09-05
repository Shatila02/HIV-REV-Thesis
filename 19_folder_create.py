import os

def create_directories_from_files(text_dir, output_dir):
    # Get a list of all text files in the text_dir
    text_files = [f for f in os.listdir(text_dir) if f.endswith('.txt')]

    for text_file in text_files:
        # Create a directory for each text file
        text_file_name = os.path.splitext(text_file)[0]
        text_file_dir = os.path.join(output_dir, text_file_name)
        os.makedirs(text_file_dir, exist_ok=True)

        # Read lines from the text file and create subdirectories
        with open(os.path.join(text_dir, text_file), 'r') as file:
            lines = file.readlines()
            for line in lines:
                sub_dir = os.path.join(text_file_dir, line.strip())
                os.makedirs(sub_dir, exist_ok=True)

if __name__ == "__main__":
    # Replace these paths with your actual directory paths
    text_files_directory = "G:\\Projects\\HIV_updated\\11mutation_impact_on protein\\monomer\\inputs\\dynamut_inputs"
    output_directory = "G:\\Projects\\HIV_updated\\11mutation_impact_on protein\\monomer\\outputs\\Dynamut\\outputs"

    create_directories_from_files(text_files_directory, output_directory)
