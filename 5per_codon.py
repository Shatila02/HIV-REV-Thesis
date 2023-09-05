#this code reads the text files of codons generated from SNAP.pl
#the output gives an excel file of per codon dn, ds for each subtype
import os
import numpy as np
import pandas as pd

# Specify the directory containing the text files
directory = 'G:\\Projects\\HIV_updated\\snap_outputs\\text_converted_codons\\1998_converted_codons'

# Initialize a dictionary to store the results for each file
results = {}

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        # Read the input text file
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            input_text = file.read()

        comparisons = input_text.split('This is comparison')
        # Initialize a list to store the matrices
        matrices = []

        # Process each comparison
        for comparison in comparisons:
            # Skip empty comparisons
            if not comparison.strip():
                continue

            # Split the comparison into lines
            lines = comparison.strip().split('\n')

            # Extract the comparison header
            header = lines[0].split(':')[1].strip()

            # Extract the comparison data
            data = [line.split() for line in lines[2:]]
            # Fill blank cells with zeros in the "syn" and "non" columns
            for i in range(len(data)):
                while len(data[i]) < 8:
                    data[i].append('0.00')

            # Convert the comparison data to a matrix
            matrix = np.array(data)[:, 6:8].astype(float)

            # Append the matrix to the list
            matrices.append(matrix)

        # Calculate the sum of the matrices
        sum_matrix = np.sum(matrices, axis=0)

        # Divide the sum by the total number of comparisons
        avg_matrix = sum_matrix / len(matrices)
        
        # Round the values in the average matrix to two decimal places
        avg_matrix = np.round(avg_matrix, 2)

        # Create a DataFrame from the average matrix
        df = pd.DataFrame(avg_matrix, columns=['syn', 'non'])

        # Add the index numbers as a column
        df['codon'] = np.arange(1, len(df) + 1)

        # Reorder the columns
        df = df[['codon', 'syn', 'non']]

        # Store the DataFrame in the results dictionary with the filename as the key
        results[filename] = df

# Create a new Excel file
output_filepath = os.path.join(directory, 'G:\\Projects\\HIV_updated\\snap_outputs\\avg_percodons\\1998.xlsx')
with pd.ExcelWriter(output_filepath) as writer:
    # Write each DataFrame to a separate sheet in the Excel file
    for filename, df in results.items():
        # Extract the sheet name from the filename (without the extension)
        sheet_name = os.path.splitext(filename)[0]
        df.to_excel(writer, sheet_name=sheet_name, index=False)
