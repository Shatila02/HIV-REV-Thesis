import os
from Bio import SeqIO
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict, Counter
import matplotlib.font_manager as fm

font_path = fm.findfont(fm.FontProperties(family="Arial"))
custom_font = fm.FontProperties(fname=font_path)

fasta_file = "G:\\Projects\\HIV_updated\\8th_output_graphs\\freq_logo_input_files\\merged_all_aa.fasta"  # Update with the path to your FASTA file

sequences = []
seq_count = 0
amino_acid_freq = defaultdict(int)

motifs = {
    # your motifs
}
motif_positions = {position: motif for motif, positions in motifs.items() for position in positions}

for record in SeqIO.parse(fasta_file, "fasta"):
    sequence = str(record.seq)
    if len(sequence) == 116:
        sequences.append(sequence[1:117])
        seq_count += 1
        for i, aa in enumerate(sequence):
            amino_acid_freq[(i + 1, aa)] += 1

color_dict = {
    'A': '#1b9e77', 'C': '#d95f02', 'D': '#7570b3', 'E': '#e7298a',
    'F': '#79cd1b', 'G': '#e64d39', 'H': '#e6ab02', 'I': '#7f570c',
    'K': '#2eccf6', 'L': '#984ea3', 'M': '#00ff2b', 'N': '#fb9a99',
    'P': '#8dd3c7', 'Q': '#ffff99', 'R': '#80b1d3', 'S': '#fdb462',
    'T': '#b3b3b3', 'V': '#fccde5', 'W': '#d9d9d9', 'Y': '#7c48c7',
    '-': '#000000', '*': '#808080'
}

stack_wild_type = False

consensus_seq = "MAGRSGDSDEDLLKAVRLIKFLYQSNPPPNPEGTRQARRNRRRRWRERQRQIHSISERILSTYLGRSADAVPLQLPPLERLTLDCDEDCGTSGTQGVGSPQILVESPTILESGAKE*"

start = 1
end = 116
bar_width = 0.8
fig, ax = plt.subplots(figsize=(30, 15))
bottom = [0] * (end - start + 1)
ax.tick_params(axis='x', which='both', length=0)
ax.set_xticklabels([])

for pos in range(start, end + 1):
    aa_freqs_at_pos = {aa: freq for (p, aa), freq in amino_acid_freq.items() if p == pos}
    aa_freqs = sorted(aa_freqs_at_pos.items(), key=lambda x: x[1], reverse=True)
    if not stack_wild_type and aa_freqs:
        aa_freqs.pop(0)
    for aa, count in aa_freqs:
        freq = count / seq_count * 100
        ax.bar(pos, freq, bottom=bottom[pos - start], label=aa, color=color_dict[aa], width=bar_width)
        bottom[pos - start] += freq

    # Rotate the position numbers to be vertical
    ax.text(pos, bottom[pos - start] + 0.5, pos, ha='center', va='bottom', fontsize=12, rotation=90, fontproperties=custom_font)
    ax.text(pos, -.3, consensus_seq[pos-1], ha='center', va='top', fontsize=12, fontproperties=custom_font)

handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True,
           ncol=22)
plt.subplots_adjust(bottom=0.1)

# Title modification
ax.set_title(f'Mutations along REV protein of HIV-1 M groups (1997-2021)', pad=20, fontsize=50, fontproperties=custom_font)

#n = {seq_count} sequences'

ax.set_xlabel('Consensus Amino Acid for Given Position', labelpad=20, fontsize=15, fontproperties=custom_font)
ax.set_ylabel('Frequency (%)', fontsize=15, rotation=90, fontproperties=custom_font)


plt.savefig("G:\\Projects\\HIV_updated\\8th_output_graphs\\freq_logo\\freq\\freq.jpg", dpi=600, format="jpg", bbox_inches='tight')
plt.savefig("G:\\Projects\\HIV_updated\\8th_output_graphs\\freq_logo\\freq\\freq.svg", dpi=600, bbox_inches='tight')
plt.show()
