import os
import subprocess

# Path to the SNAP.pl script
snap_script = "G:/Projects/HIV_updated/python_codes/2SNAP.pl"

# Directory containing the input files
input_directory = "G:/Projects/HIV_updated/snap_inputs/2021"

# Directory to store the output files
output_directory = "G:/Projects/HIV_updated/snap_outputs/2021"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# List all input files in the input directory
input_files = [f for f in os.listdir(input_directory) if os.path.isfile(os.path.join(input_directory, f)) and f.endswith(".txt")]

# Loop over each input file
for input_file in input_files:
    # Create a directory with the same name as the input file
    file_directory = os.path.join(output_directory, os.path.splitext(input_file)[0])
    os.makedirs(file_directory, exist_ok=True)
    
    # Path to the input file
    input_file_path = os.path.join(input_directory, input_file)
    
    # Execute SNAP.pl with the input file
    command = ["perl", snap_script, input_file_path]
    subprocess.run(command, cwd=file_directory)
