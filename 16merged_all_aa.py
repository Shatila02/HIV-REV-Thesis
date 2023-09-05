import os
from Bio import SeqIO

def merge_fasta_files(parent_directory, output_directory, output_file):
    merged_sequences = []

    for root, _, files in os.walk(parent_directory):
        for file in files:
            if file.endswith(".fas"):
                fasta_path = os.path.join(root, file)

                with open(fasta_path, "r") as f:
                    records = list(SeqIO.parse(f, "fasta"))
                    merged_sequences.extend(records)

    output_file_path = os.path.join(output_directory, output_file)
    with open(output_file_path, "w") as f:
        SeqIO.write(merged_sequences, f, "fasta")

if __name__ == "__main__":
    parent_directory = "G:\\Projects\\HIV_updated\\10th_output_entro_input\\processed"
    output_directory = "G:\\Projects\\HIV_updated\\8th_output_graphs\\freq_logo_input_files"
    output_file = "merged_all_aa.fasta"
    merge_fasta_files(parent_directory, output_directory, output_file)
