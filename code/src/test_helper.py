import io
import sys
import time

import numpy as np
import pandas as pd


def generate_mixed_type_df(num_rows: int, num_cols: int) -> pd.DataFrame:
    """Generates a DataFrame with a mix of data types.
    Sets a random seed for reproducibility.
    """
    # Set a seed for reproducibility of random data
    np.random.seed(42)

    data = {}
    for i in range(num_cols):
        col_type = i % 3
        col_name = f"Column_{i+1}"
        if col_type == 0:  # String
            data[col_name] = [f"string_{j}_{i}" for j in range(num_rows)]
        elif col_type == 1:  # Integer
            data[col_name] = np.random.randint(0, 1000, size=num_rows)
        else:  # Boolean
            data[col_name] = np.random.choice([True, False], size=num_rows)
    return pd.DataFrame(data)


def time_operation(func, *args, **kwargs):
    """A simple function to time another function's execution."""
    # Redirect stdout to suppress printing during timing
    original_stdout = sys.stdout
    sys.stdout = io.StringIO()

    start_time = time.perf_counter()
    func(*args, **kwargs)
    end_time = time.perf_counter()

    # Restore stdout
    sys.stdout = original_stdout

    return end_time - start_time
