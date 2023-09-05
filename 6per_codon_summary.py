import pandas as pd

# Read the Excel file
output_filepath = 'G:\\Projects\\HIV_updated\\snap_outputs\\avg_percodons\\1998.xlsx'
excel_file = pd.ExcelFile(output_filepath, engine='openpyxl')

# Initialize a dictionary to store the sheet names and non/syn values
non_syn_values = {}
avg_syn_values = {}
avg_non_values = {}

# Iterate over each sheet in the Excel file
for sheet_name in excel_file.sheet_names:
    # Read the sheet into a DataFrame
    df = pd.read_excel(output_filepath, sheet_name=sheet_name)

    # Calculate the average for each column
    avg_syn = df['syn'].mean()
    avg_non = df['non'].mean()

    # Calculate non/syn
    non_syn_ratio = avg_non / avg_syn

    # Store the non/syn value in the dictionary
    non_syn_values[sheet_name] = non_syn_ratio

    # Store the syn value in the dictionary
    avg_syn_values[sheet_name] = avg_syn

    # Store the non value in the dictionary
    avg_non_values[sheet_name] = avg_non

# Create a new DataFrame with the sheet names and non/syn values
summary_df = pd.DataFrame(list(non_syn_values.items()), columns=['Subtypes', 'dn/ds'])

# Add 'syn' and 'non' columns with corresponding values
summary_df['ds'] = summary_df['Subtypes'].map(avg_syn_values)
summary_df['dn'] = summary_df['Subtypes'].map(avg_non_values)

# Open the existing Excel file
with pd.ExcelWriter(output_filepath, mode='a', engine='openpyxl') as writer:
    # Write the summary DataFrame to a new sheet
    summary_df.to_excel(writer, sheet_name='Summary', index=False)
