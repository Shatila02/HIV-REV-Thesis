from Bio import SeqIO
import logomaker
import matplotlib.pyplot as plt

def get_color_scheme():
    # Define a color scheme for the one-letter codes of the 20 standard amino acids
    color_scheme = {
        'A': 'black',
        'R': 'blue',
        'N': 'green',
        'D': 'red',
        'C': 'green',
        'Q': 'green',
        'E': 'red',
        'G': 'green',
        'H': 'blue',
        'I': 'black',
        'L': 'black',
        'K': 'blue',
        'M': 'black',
        'F': 'black',
        'P': 'black',
        'S': 'green',
        'T': 'green',
        'W': 'black',
        'Y': 'green',
        'V': 'black'
    }
    return color_scheme

def extract_region(alignment, start_pos, end_pos):
    return [seq[start_pos:end_pos] for seq in alignment]

fasta_file = "G:\\Projects\\HIV_updated\\8th_output_graphs\\freq_logo_input_files\\merged_all_aa.fasta"
alignment = [str(record.seq) for record in SeqIO.parse(fasta_file, "fasta")]
pfm = logomaker.alignment_to_matrix(alignment)
# Define the region of interest (positions 50 to 60 in this case)
start_pos = 84
end_pos = 116
# Extract the region of interest from each sequence in the alignment
region_alignment = extract_region(alignment, start_pos - 1, end_pos)


# Convert the extracted region to a position frequency matrix (pfm)
pfm_selected = logomaker.alignment_to_matrix(region_alignment)

# Get the custom color scheme
color_scheme = get_color_scheme()


# Set the desired height of the plot window (in inches)
#plot_height = 8

# Increase the height of the window by adjusting the figure size
#plt.figure(figsize=(pfm.shape[1], plot_height))

logo = logomaker.Logo(pfm_selected, color_scheme=color_scheme)
logo.style_spines(visible=False)  # Optional: Hide spines for a cleaner look

sequence = "MAGRSGDSDEDLLKAVRLIKFLYQSNPPPNPEGTRQARRNRRRRWRERQRQIHSISERILSTYLGRSADAVPLQLPPLERLTLDCDEDCGTSGTQGVGSPQILVESPTILESGAKE"
sequence = sequence[83:116]

# Set the x-axis labels to show selected positions
logo.ax.set_xticks(range(0, end_pos - start_pos + 1))
logo.ax.set_xticklabels(range(start_pos, end_pos + 1), fontsize=7.5)

# Calculate the position to align the sequence with the logo
sequence_length = len(sequence)
logo_width = logo.ax.get_xlim()[1]
scale_factor = logo_width / sequence_length
font_size = 8 * scale_factor 

# Add the sequence below the x-axis label and align with the logo
for i, residue in enumerate(sequence):
    pos = ((i + 1) * scale_factor) - (scale_factor/1.08)  # Add offset to center the letter under the x-axis position
    logo.ax.text(pos, -7000, residue, ha='center', fontsize=font_size, fontfamily='monospace', color=color_scheme[residue])

# Add a title to the plot
#logo.ax.set_title("Sequence Logo for REV")
#logo.ax.set_title("Nterminal (61-74), becomes structured during the functionality of REV")

# Adjust the figure size before saving figures
#logo.ax.figure.set_size_inches(pfm.shape[1], plot_height)

plt.ylabel("bits")

# Save the plot in SVG format
logo.ax.figure.savefig("G:\\Projects\\HIV_updated\\8th_output_graphs\\freq_logo\\logos\\Cterm_logo.svg", format="svg", dpi=600, bbox_inches='tight')

# Save the plot in JPG format (adjust the DPI as needed)
#logo.ax.figure.savefig("G:\\Projects\\HIV_updated\\8th_output_graphs\\freq_logo\\logos\\ARM_logo1.svg", format="jpg", dpi=600, bbox_inches='tight')

# Display the plot
plt.show()
