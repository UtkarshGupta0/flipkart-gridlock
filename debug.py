import pandas as pd

# Load the files
sub = pd.read_csv('submission_master_final6.csv')
sample = pd.read_csv('dataset/sample_submission.csv')

print("=== SUBMISSION DIAGNOSTIC REPORT ===")

# 1. Check Row Counts
print(f"1. Row Count Match: {len(sub) == len(sample)} (You: {len(sub)}, Expected: {len(sample)})")

# 2. Check Column Names
print(f"2. Headers Match: {list(sub.columns) == list(sample.columns)} (You: {list(sub.columns)}, Expected: {list(sample.columns)})")

# 3. Check for NaNs
nan_count = sub['demand'].isna().sum()
print(f"3. Missing Values (NaNs): {nan_count} found")

# 4. Check for Negatives
neg_count = (sub['demand'] < 0).sum()
print(f"4. Negative Values: {neg_count} found")

# 5. Check Index Match
if 'Index' in sub.columns and 'Index' in sample.columns:
    index_match = (sub['Index'] == sample['Index']).all()
    print(f"5. Row Order Matches Sample: {index_match}")
else:
    print("5. Row Order: Could not verify (Column names differ)")