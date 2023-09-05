from Bio import SeqIO
import os

def filter_sequences_by_length(input_file, output_file, target_length=116):
    with open(output_file, "w") as out_handle:
        for record in SeqIO.parse(input_file, "fasta"):
            sequence = record.seq.rstrip('-')  # Remove gaps that come after the last residue
            actual_length = len(sequence)
            if actual_length >= target_length:
                sequence = sequence[:target_length]
            elif len(sequence) < target_length:
                sequence = sequence + "-" * (target_length - len(sequence))
            record.seq = sequence
            SeqIO.write(record, out_handle, "fasta")

# Replace "input_directory_path" with the path to the directory containing the input fasta file.
input_directory_path = "G:\\Projects\\HIV_updated\\7th_output\\mutation"

# Replace "input_file_name.fasta" with the name of your input fasta file.
input_file_path = os.path.join(input_directory_path, "merged_all_aa.fasta")

# Replace "output_file_name.fasta" with the desired name for the output fasta file.
output_file_path = os.path.join(input_directory_path, "equal_len_aa.fasta")

# Filter sequences by length and save the modified file.
filter_sequences_by_length(input_file_path, output_file_path)
