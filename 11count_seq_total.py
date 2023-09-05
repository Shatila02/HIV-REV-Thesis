#count total number of sequences
import os
from Bio import SeqIO
import pandas as pd

#count sequence from a file
# def count_sequences_in_fasta(fasta_file):
#     count = 0
#     with open(fasta_file, "r") as f:
#         for record in SeqIO.parse(f, "fasta"):
#             count += 1
#     return count


# if __name__ == "__main__":
#     fasta_file_path = "G:\\Projects\\HIV_updated\\8th_output_graphs\\freq_logo_input_files\\merged_all_aa.fasta"
#     total_sequences = count_sequences_in_fasta(fasta_file_path)
#     print("Total number of sequences:", total_sequences)

#count sequences from yearwise subdirectories
# def count_sequences_in_fasta(file_path):
#     with open(file_path, "r") as fasta_file:
#         return sum(1 for _ in SeqIO.parse(fasta_file, "fasta"))

# def process_directory(directory_path):
#     subdirectory_data = []
#     for subdir in os.listdir(directory_path):
#         subdir_path = os.path.join(directory_path, subdir)
#         if os.path.isdir(subdir_path):
#             total_sequences = 0
#             for file in os.listdir(subdir_path):
#                 file_path = os.path.join(subdir_path, file)
#                 if file.endswith((".fasta", ".fas")):
#                     total_sequences += count_sequences_in_fasta(file_path)
#             subdirectory_data.append((subdir, total_sequences))
#     return subdirectory_data


# def create_excel_file(data, output_path):
#     df = pd.DataFrame(data, columns=["Subdirectory", "Total Sequences"])
#     df.to_excel(output_path, index=False)

# if __name__ == "__main__":
#     # Replace 'your_directory_path' with the path to your main directory
#     main_directory = 'G:\\Projects\\HIV_updated\\3rd_output_nt_aligned'
#     excel_output_path = 'G:\\Projects\\HIV_updated\\4th_output_nt\\3year_nt_count.xlsx'

#     subdirectory_data = process_directory(main_directory)
#     create_excel_file(subdirectory_data, excel_output_path)


#seq count for each subtype
def count_sequences_in_fasta(file_path):
    with open(file_path, "r") as fasta_file:
        return sum(1 for _ in SeqIO.parse(fasta_file, "fasta"))

def process_fasta_files(directory_path):
    fasta_data = []
    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file)
        if file.endswith((".fasta", ".fas")):
            num_sequences = count_sequences_in_fasta(file_path)
            fasta_data.append((file, num_sequences))
    return fasta_data

def create_excel_file(data, output_path):
    df = pd.DataFrame(data, columns=["Fasta File", "Sequence Number"])
    df.to_excel(output_path, index=False)

if __name__ == "__main__":
    # Replace 'your_directory_path' with the path to your directory containing the fasta files
    fasta_directory = 'G:\\Projects\\HIV_updated\\2nd_output_nt_con\\2020'
    excel_output_path = 'G:\\Projects\\HIV_updated\\2nd_output_nt_con\\2020\\2seq_count.xlsx'

    fasta_data = process_fasta_files(fasta_directory)
    create_excel_file(fasta_data, excel_output_path)