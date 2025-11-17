import pandas as pd
import glob
import os

# Function to merge CSV files

def merge_csv_files(input_folder, output_file):
    # Use glob to find all the csv files in the input_folder
    all_files = glob.glob(os.path.join(input_folder, "*.csv"))
    
    # Create a list to hold dataframes
    dfs = []
    
    for filename in all_files:
        df = pd.read_csv(filename)
        dfs.append(df)
    
    # Concatenate all dataframes into one
    merged_df = pd.concat(dfs, ignore_index=True)
    
    # Save the merged dataframe to the output file
    merged_df.to_csv(output_file, index=False)

# Example usage:
# merge_csv_files('path/to/input_folder', 'path/to/output_file.csv')
