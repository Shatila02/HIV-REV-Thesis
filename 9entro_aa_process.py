import os
from Bio import SeqIO

def filter_sequences_by_length(input_file, output_file, target_length=116):
    with open(output_file, "w") as out_handle:
        for record in SeqIO.parse(input_file, "fasta"):
            sequence = record.seq.rstrip('-')
            actual_length = len(sequence)
            if actual_length >= target_length:
                sequence = sequence[:target_length]
            elif len(sequence) < target_length:
                sequence = sequence + "-" * (target_length - len(sequence))
            record.seq = sequence
            SeqIO.write(record, out_handle, "fasta")

def process_directory(input_dir, output_dir, target_length=116):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through subdirectories in the input directory
    for subdir in os.listdir(input_dir):
        input_subdir = os.path.join(input_dir, subdir)
        output_subdir = os.path.join(output_dir, subdir)

        # Create the subdirectory in the output directory if it doesn't exist
        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)

        # Loop through fasta files in the subdirectory
        for fasta_file in os.listdir(input_subdir):
            input_file = os.path.join(input_subdir, fasta_file)
            output_file = os.path.join(output_subdir, fasta_file)

            # Apply the filtering function to the fasta file
            filter_sequences_by_length(input_file, output_file, target_length)

if __name__ == "__main__":
    input_directory = "G:\\Projects\\HIV_updated\\10th_output_entro_input"
    output_directory = "G:\\Projects\\HIV_updated\\test"
    target_length = 116

    process_directory(input_directory, output_directory, target_length)
