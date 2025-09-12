import polars as pl
from datetime import datetime
from utils.common_functions import save_to_formats

# Define the file path
file_path = '/Users/aimachaudhry/Desktop/Python AHI2025/medical-codex-pipeline/input/sct2_Description_Full-en_US1000124_20250901.txt'

# Read the SNOMED CT file as a polars DataFrame
df = pl.read_csv(
    file_path,
    separator='\t',
    has_header=True,
    quote_char=None,
    encoding='utf8-lossy',
    truncate_ragged_lines=True,
    dtypes={
        'id': pl.Utf8,
        'effectiveTime': pl.Utf8,
        'active': pl.Int32,
        'moduleId': pl.Utf8,
        'conceptId': pl.Utf8,
        'languageCode': pl.Utf8,
        'typeId': pl.Utf8,
        'term': pl.Utf8,
        'caseSignificanceId': pl.Utf8
    }
)

# Print unique language codes present in the DataFrame
print(f"\nActive terms count: {df.filter(pl.col('active') == 1).height}")
lang_series = df.get_column('languageCode')
print(f"Language codes: {lang_series.unique().to_list()}")

# Add a last_updated column with the current timestamp
df = df.with_columns([
    pl.lit(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).alias('last_updated')
])

# Save the DataFrame to CSV using the reusable function
output_base = 'output/snomed_descriptions'
save_to_formats(df, output_base)


# Print summary and preview
print(f"Successfully parsed {df.height} records from SNOMED CT file")
print(f"Saved to {output_base}.csv")
print(f"Dataset shape: {df.shape}")
print(f"\nColumn names: {df.columns}")
print(f"\nFirst 5 rows:")
print(df.head())
