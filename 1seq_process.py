from Bio import SeqIO
from os.path import join
import os

# Dictionary for ambiguous bases
ambiguity = {
    "R": "N",
    "Y": "N",
    "K": "N",
    "S": "N",
    "W": "N",
    "M": "N",
    "B": "N",
    "D": "N",
    "H": "N",
    "V": "N",

    # Add other ambiguities here if needed
}

def process_sequence(sequence):
    # Convert sequence to upper case
    sequence = sequence.upper()
    
    # Replace ambiguous bases
    for ambig, replacement in ambiguity.items():
        sequence = sequence.replace(ambig, replacement)
    
    # Replace '-' with 'N'
    sequence = sequence.replace('-', 'N')

    # Return processed sequence
    return sequence


def process_fasta(year):
    input_directory_path = join("G:\\Projects\\HIV_updated\\4th_output_nt", str(year)) # input directory
    output_directory_path = join("G:\\Projects\\HIV_updated\\snap_inputs", str(year)) # output directory
    os.makedirs(output_directory_path, exist_ok=True) # create output directory if it doesn't exist
    
    # Rest of the code remains the same

    
    # Loop over all files in directory
    for filename in os.listdir(input_directory_path):
        if filename.endswith(".fas"):
            # Define output file name
            output_filename = f"{filename[:-4]}.txt"
            output_path = join(output_directory_path, output_filename)
            
            # Parse the fasta file
            fasta_sequences = SeqIO.parse(join(input_directory_path, filename), 'fasta')
            
            # Create/open output file
            with open(output_path, 'w') as outfile:
                # Process each sequence
                for fasta in fasta_sequences:
                    name, sequence = fasta.id, str(fasta.seq)
                    
                    # Truncate sequence name to 10 characters to match SNAP's requirement
                    name = name[:10]
                    
                    # Process sequence
                    sequence = process_sequence(sequence)
                    
                    # Write to output file
                    outfile.write(f"{name} {sequence}\n")

for year in range(2021, 2022):
    process_fasta(year)
    
print(" All file process")
