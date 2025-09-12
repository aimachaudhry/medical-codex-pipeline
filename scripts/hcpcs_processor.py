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

# Add a last_updated column with the current timestamp
df['last_updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Save the DataFrame to CSV using the reusable function
output_base = 'output/hcpcs_codes'
save_to_formats(df, output_base)

# Print summary information
print(f"Successfully parsed {len(df)} records from {file_path}")
print(f"Saved to {output_base}.csv")
print("\nFirst 5 rows:")
print(df.head())

