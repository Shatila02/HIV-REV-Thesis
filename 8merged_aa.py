import os
from Bio import SeqIO

def merge_fasta_files(source_directory, destination_directory, merged_filename):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    merged_sequences = []
    for filename in os.listdir(source_directory):
        if filename.endswith('.fasta') or filename.endswith('.fas'):
            filepath = os.path.join(source_directory, filename)
            for record in SeqIO.parse(filepath, 'fasta'):
                merged_sequences.append(record)

    merged_filepath = os.path.join(destination_directory, merged_filename)
    with open(merged_filepath, 'w') as merged_file:
        SeqIO.write(merged_sequences, merged_file, 'fasta')

    print("Merging completed. Merged file saved to:", merged_filepath)

# Example usage:
source_dir = 'G:\\Projects\\HIV_updated\\10th_output_entro_input\\pure'  # Replace with the actual source directory path
destination_dir = 'G:\\Projects\\HIV_updated\\10th_output_entro_input\\merged'  # Replace with the actual destination directory path
merged_filename = 'pure_merged.fasta'  # Replace with the desired name of the merged file

merge_fasta_files(source_dir, destination_dir, merged_filename)
