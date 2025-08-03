"""Test script for converting a DataFrame to a PrettyTable.
This script loads the Titanic dataset using seaborn, converts it to a PrettyTable,
and prints the table to the console.
"""

import time

import seaborn as sns

from src.cli import format_df_as_table

# Visual test
start_time = time.time()
titanic = sns.load_dataset("titanic").head(10)
table = format_df_as_table(titanic)
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Time taken to format the table: {elapsed_time:.6f} seconds")

print(titanic)
