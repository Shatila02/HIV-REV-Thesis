import os
from Bio import SeqIO

def search_id_in_subdirectories(parent_directory, search_id):
    for root, dirs, files in os.walk(parent_directory):
        for file in files:
            if file.endswith(".fasta") or file.endswith(".fas"):
                fasta_path = os.path.join(root, file)
                with open(fasta_path, "r") as f:
                    for record in SeqIO.parse(f, "fasta"):
                        if record.id == str(29):
                            print(f"ID '{record.id}' greater than 12 found in: {fasta_path}")

if __name__ == "__main__":
    parent_directory = "G:\\Projects\\HIV_updated\\6th_output"
    search_id = 12  # Replace with the ID you want to search for
    search_id_in_subdirectories(parent_directory, search_id)
