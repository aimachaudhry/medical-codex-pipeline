import pandas as pd
from datetime import datetime
from utils.common_functions import save_to_formats

# Define the file path
file_path = '/Users/aimachaudhry/Desktop/Python AHI2025/medical-codex-pipeline/input/HCPC2025_OCT_ANWEB_v3.txt'

# Define column specifications and names for fixed-width file
colspecs = [(0, 11), (11, 90), (90, 180), (180, 200), (200, 220), (220, 240), (240, 260), (260, 280)]

# Define column names
column_names = ["Code", "Description1", "Description2", "Type", "Unknown1", "Unknown2", "Unknown3", "Unknown4"]
df = pd.read_fwf(file_path, colspecs=colspecs, names=column_names)

# Save only a sample of the first 1,000 rows to reduce file size
df_sample = df.head(1000)

# Add a last_updated column with the current timestamp
df_sample['last_updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Save the sampled DataFrame to CSV using the reusable function
output_base = 'output/hcpcs_codes_sample'
save_to_formats(df_sample, output_base)

# Print summary information for the sample
print(f"Successfully parsed {len(df_sample)} records from {file_path}")
print(f"Saved to {output_base}.csv")
print("\nFirst 5 rows:")
print(df_sample.head())

