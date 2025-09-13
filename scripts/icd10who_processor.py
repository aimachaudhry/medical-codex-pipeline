import pandas as pd
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


# Save only a sample of the first 1,000 rows to reduce file size
df_sample = df.head(1000)

# Add a last_updated column with the current timestamp
df_sample['last_updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Save the sampled DataFrame to CSV using the reusable function
output_base = 'output/icd102019syst_codes_sample.csv'
save_to_formats(df_sample, output_base)

# Print summary and preview for the sample
print(f"Successfully parsed {len(df_sample)} records from {file_path}")
print(f"Saved to {output_base}")
print(f"\nFirst 5 rows:")
print(df_sample.head())