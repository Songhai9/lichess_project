import pandas as pd

# Number of rows to extract (adjust this to get desired file size)
N_ROWS = 100000  # Start with 100k rows as a test

# Read first N rows of the dataset
try:
    # Read the CSV file with specified number of rows
    df = pd.read_csv('dataset.csv', nrows=N_ROWS)
    
    # Save to a new CSV file
    output_file = 'dataset_sample.csv'
    df.to_csv(output_file, index=False)
    
    # Get file size in MB
    import os
    file_size_mb = os.path.getsize(output_file) / (1024 * 1024)
    
    print(f"Successfully created sample dataset:")
    print(f"Number of rows: {len(df)}")
    print(f"Number of columns: {len(df.columns)}")
    print(f"File size: {file_size_mb:.2f} MB")
    
except FileNotFoundError:
    print("Error: dataset.csv file not found")
except Exception as e:
    print(f"An error occurred: {str(e)}")
