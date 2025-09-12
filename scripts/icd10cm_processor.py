import pandas as pd
from datetime import datetime
from utils.common_functions import save_to_formats

# Define the file path
file_path = '/Users/aimachaudhry/Desktop/Python AHI2025/medical-codex-pipeline/input/icd10cm_codes_2025.txt'

# Initialize a list to hold parsed code dictionaries
codes = []


# Read and parse the ICD-10-CM codes from the text file
for idx, line in enumerate(open(file_path, encoding='utf-8'), start=1):
	# Remove trailing newline characters
	line = line.rstrip('\n\r')

	# Skip empty lines
	if not line.strip():
		continue

	# Split on whitespace: first part is code, rest is description
	parts = line.strip().split(None, 1)
	if len(parts) < 2:
		continue
	code = parts[0].strip().upper()
	description = parts[1].strip()


	codes.append({
		'label_number': idx,
		'code': code,
		'description': description
	})


# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(codes)


# Add a last_updated column with the current timestamp
last_updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
df['last_updated'] = last_updated


# Save the DataFrame to CSV using the reusable function
save_to_formats(df, 'output/icd10cm_2025_codes')


# Print a preview of the first few rows
print(df.head(15))


	
