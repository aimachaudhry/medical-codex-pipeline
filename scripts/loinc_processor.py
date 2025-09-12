import pandas as pd
from datetime import datetime
from utils.common_functions import save_to_formats

# Define the file path
file_path = '/Users/aimachaudhry/Desktop/Python AHI2025/medical-codex-pipeline/input/Loinc.csv'


# Load the LOINC data into a DataFrame
loinc = pd.read_csv(file_path)


# Print a summary of the DataFrame
loinc.info()

# Strings 
loinc.STATUS.value_counts()

# Print the first row for a quick preview
print('First row:', loinc.iloc[0])

# Select only the columns we want
loinc_small = loinc[['LOINC_NUM', 'LONG_COMMON_NAME']].copy()

# Rename columns for output
loinc_small = loinc_small.rename(columns={
    'LOINC_NUM': 'code',
    'LONG_COMMON_NAME': 'description',
})

# Add a last_updated column with the current timestamp
loinc_small['last_updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Save the DataFrame to CSV using the reusable function
save_to_formats(loinc_small, 'output/loinc_codes')