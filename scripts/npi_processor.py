import polars as pl
from datetime import datetime
from utils.common_functions import save_to_formats

# Define the file path
file_path = '/Users/aimachaudhry/Desktop/Python AHI2025/medical-codex-pipeline/input/npidata_pfile_20050523-20250907.csv'


# Load the first 1000 rows
df = pl.read_csv(file_path, n_rows=1000)


# Select and rename columns
df_small = df.select([
    pl.col('NPI').alias('code'),
    pl.col('Provider Last Name (Legal Name)').alias('description')
])

# Add a last_updated column with the current timestamp
df_small = df_small.with_columns([
    pl.lit(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).alias('last_updated')
])

# Remove rows where description is blank
df_small = df_small.filter(
    (pl.col('description').is_not_null()) & (pl.col('description').str.strip_chars() != "")
)

# Save the DataFrame to CSV using the reusable function
output_base = 'output/npi_data'
save_to_formats(df_small, output_base)

# Print summary and preview
print(f"Successfully parsed {df_small.height} records from {file_path}")
print(f"Saved to {output_base}.csv")
print(f"\nFirst 10 rows:")
print(df_small.head())
