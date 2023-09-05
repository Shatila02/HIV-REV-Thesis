from Bio import SeqIO
import pandas as pd
from collections import Counter

def compare_sequences_to_consensus(consensus, fasta_file):
    mutations = {}
    constant = 0

    # Read the FASTA file and compare sequences to the consensus
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequence_id = record.id
        sequence = str(record.seq)
        constant += 1

        # Compare the sequences to the consensus
        for pos, (cons_char, seq_char) in enumerate(zip(consensus, sequence), start=1):
            if cons_char != seq_char:
                mutation = f"{cons_char}{pos}{seq_char}"
                mutations.setdefault(mutation, {"Wild Type": cons_char, "Position": pos, "Mutant": set(), "Count": 0})
                mutations[mutation]["Mutant"].add(seq_char)
                mutations[mutation]["Count"] += 1

    # Create DataFrame for mutations
    df = pd.DataFrame(mutations.values())

    # Form the "Mutation" column
    df["Mutation"] = df.apply(lambda row: f"{row['Wild Type']}{row['Position']}{','.join(row['Mutant'])}", axis=1)

    # Calculate the percentage of consensus and sequence letters in each position
    df["Consensus Percentage"] = df["Count"].apply(lambda x: (constant-x) / constant * 100)
    df["Sequence Percentage"] = df["Count"].apply(lambda x: x / constant * 100)



    return df

if __name__ == "__main__":
    # Replace the consensus_seq with your provided consensus sequence as a string
    consensus_seq = "MAGRSGDSDEDLLKAVRLIKFLYQSNPPPNPEGTRQARRNRRRRWRERQRQIHSISERILSTYLGRSADAVPLQLPPLERLTLDCDEDCGTSGTQGVGSPQILVESPTILESGAKE"
    fasta_file_path = "G:\\Projects\\HIV_updated\\8th_output_graphs\\freq_logo_input_files\\merged_all_aa.fasta"
    
    # Compare sequences to consensus and get the DataFrame
    mutation_df = compare_sequences_to_consensus(consensus_seq, fasta_file_path)

    # Write DataFrame to Excel
    mutation_df.to_excel("G:\\Projects\\HIV_updated\\mutations1.xlsx", index=False)
