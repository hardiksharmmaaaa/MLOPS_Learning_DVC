import pandas as pd 
import os

# Data to be written into the CSV file
data = [
    {"Name": "Alice", "Age": 25, "City": "New York"},
    {"Name": "Bob", "Age": 30, "City": "San Francisco"},
    {"Name": "Charlie", "Age": 35, "City": "Los Angeles"}
]

# Directory and file name for the CSV file
output_dir = "output"
csv_file = "output.csv"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Full file path
csv_file_path = os.path.join(output_dir, csv_file)

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)

print(f"Data has been written to {csv_file_path}")