import os
import shutil

def sort_fasta_files_by_classification(fasta_directory, classification_dict, sorted_output_directory):
    for classification in classification_dict.keys():
        dest_directory = os.path.join(sorted_output_directory, classification)
        if not os.path.exists(dest_directory):
            os.makedirs(dest_directory)

    for filename in os.listdir(fasta_directory):
        src_filepath = os.path.join(fasta_directory, filename)
        if not os.path.isfile(src_filepath):
            continue

        file_base_name, file_extension = os.path.splitext(filename)
        for classification, patterns in classification_dict.items():
            for pattern in patterns:
                if pattern == file_base_name:  # Compare without the file extension
                    dest_directory = os.path.join(sorted_output_directory, classification)
                    dest_filepath = os.path.join(dest_directory, filename)
                    try:
                        shutil.copy(src_filepath, dest_filepath)
                    except FileNotFoundError:
                        print(f"Warning: File not found: {filename}. Skipping.")
                    break

    print("Fasta files sorted and moved successfully.")

# Example usage:
fasta_directory = 'G:\\Projects\\HIV_updated\\2nd_output_nt_no_con\\2021'  # Replace with the actual directory path containing FASTA files
sorted_output_directory = 'G:\\Projects\\HIV_updated\\2nd_output_nt_no_con_sorted\\2021'
classification_dict = {
    'pure': ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    'recom': ['AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AK', 'BC', 'BD', 'BF', 'BG', 'CD', 'CF', 'DF', 'DG'],
    'hybrid': ['0102', '0107', '0108', '0206', '0209', '0213', '0222', '0225', '0263', '0102A', '01A', '01ADF', 
               '01AF', '01AG', '01B', '01BC', '01C', '01FG', '02A', '02AF', '02AG', '02B', '02BF', '02BG', '02C', '02D', 
               '02F', '02FG', '02G', '02GK', '02H', '06A', '06B', '07B', '14F', '32A', '32G', '50B', 'ABD', 'ACD', 'ACG', 
               'ADG', 'AFG', 'AGH', 'BCF', 'BCG']
}

sort_fasta_files_by_classification(fasta_directory, classification_dict, sorted_output_directory)
