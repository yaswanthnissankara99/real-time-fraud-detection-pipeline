import pandas as pd
import os

# Step 1: Read input CSV
input_path = os.path.join('data', 'claims_837_sample.csv')
df = pd.read_csv(input_path)

# Step 2: Basic transformation
df['status'] = df['status'].str.upper().str.replace('PARTIALLY_PAID', 'PARTIAL')
df['claim_year'] = pd.to_datetime(df['claim_date']).dt.year
df['reimbursement_ratio'] = round(df['amount_paid'] / df['amount_billed'], 2)

# Step 3: Output the transformed data
output_path = os.path.join('processed', 'claims_cleaned.csv')
df.to_csv(output_path, index=False)

print("✅ ETL job completed. Output saved to:", output_path)
