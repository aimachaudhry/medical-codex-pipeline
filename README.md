# Medical Codex Data Pipeline Assignment

This assignment replicates work that is done health tech, and in companies such as Cerner and Epic. In this assignment, python scripts were created for the medical codexes listed below and processed into standardized CSV format. This was done through data cleaning, validation, and format conversion.

## Medical Codexes
The medical codexes files that were used are:
1. **SNOMED CT (US)** - https://www.nlm.nih.gov/healthit/snomedct/index.html
2. **ICD-10-CM (US)** - https://www.cms.gov/medicare/coding-billing/icd-10-codes
3. **ICD-10 (WHO)** - https://icdcdn.who.int/icd10/index.html
4. **HCPCS (US)** - https://www.cms.gov/medicare/coding-billing/hcpcscode
5. **LOINC (US)** -  https://loinc.org/downloads/
6. **RxNorm (US)** - https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html
7. **NPI (US)** - https://download.cms.gov/nppes/NPI_Files.html

### Process
- For each of the medical codexes, a python script was used to input the file, validate code formats, standardize text fields, and remove null values. 
- For the ouput file, columns were identified by codes (the primary identifier), description (human-readable description), and when it was last updated (processing timestamp)
- A utilities file with common functions was used to define the reusable function:
- `save_to_formats(df, base_filename)`: Save DataFrame to CSV 

This function ensured consistent formating

- Raw data files were ecluded in .gitignore 
- Sample output files were included as demonstration