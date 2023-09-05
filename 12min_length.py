from Bio import SeqIO
import os

def find_minimum_sequence_length(fasta_file):
    min_length = float('inf')
    
    with open(fasta_file, "r") as file:
        for record in SeqIO.parse(file, "fasta"):
            sequence_length = len(record.seq)
            if sequence_length > min_length:
                min_length = sequence_length
    
    return min_length

# Replace "path_to_directory" with the path to your directory containing the fasta file.
directory_path = "G:\\Projects\\HIV_updated\\6th_output"

# Replace "fasta_file_name.fasta" with the name of your fasta file.
fasta_file_path = os.path.join(directory_path, "equal.fasta")

minimum_length = find_minimum_sequence_length(fasta_file_path)
print("Minimum sequence length:", minimum_length)
