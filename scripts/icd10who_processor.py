import pandas as pd
import re
from datetime import datetime
from utils.common_functions import save_to_formats


# Define the file path
file_path = '/Users/aimachaudhry/Desktop/Python AHI2025/medical-codex-pipeline/input/icd102019syst_codes.txt'

# List of column names for the ICD-10 WHO codes data
columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
           'morbidity_code3', 'morbidity_code4']

# Read the input file into a DataFrame, using ';' as the separator and the columns list as headers
df = pd.read_csv(file_path, sep=';', header=None, names=columns)


# Path to save the output CSV file
output_csv = 'output/icd102019syst_codes.csv'

# Add a last_updated column with the current timestamp and move it to the end
last_updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
df['last_updated'] = last_updated
cols = [col for col in df.columns if col != 'last_updated'] + ['last_updated']
df = df[cols]

# # Save the DataFrame to CSV using the reusable function
save_to_formats(df, output_csv)


# Print summary and preview
print(f"Successfully parsed {len(df)} records from {file_path}")
print(f"Saved to {output_csv}")
print(f"\nFirst 5 rows:")
print(df.head())