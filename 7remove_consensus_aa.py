import os
from Bio import SeqIO

def remove_first_sequence_and_save(parent_directory, output_directory):
    for root, dirs, files in os.walk(parent_directory):
        for file in files:
            if file.endswith((".fas", ".fasta")):
                input_fasta_path = os.path.join(root, file)
                output_subdirectory = os.path.relpath(root, parent_directory)
                output_subdirectory_path = os.path.join(output_directory, output_subdirectory)
                os.makedirs(output_subdirectory_path, exist_ok=True)
                output_fasta_path = os.path.join(output_subdirectory_path, file)

                updated_sequences = []
                with open(input_fasta_path, "r") as f:
                    first_sequence_skipped = False
                    for record in SeqIO.parse(f, "fasta"):
                        if not first_sequence_skipped:
                            first_sequence_skipped = True
                            continue
                        updated_sequences.append(f">{record.description}\n{record.seq}")

                with open(output_fasta_path, "w") as f:
                    f.write("\n".join(updated_sequences))

if __name__ == "__main__":
    parent_directory = "G:\\Projects\\HIV_updated\\2nd_output_nt_con"
    output_directory = "G:\\Projects\\HIV_updated\\2nd_output_nt_no_con"
    remove_first_sequence_and_save(parent_directory, output_directory)
