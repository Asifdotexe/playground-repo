import io
import sys
import time
from collections.abc import Callable

import timeit
import numpy as np
import pandas as pd


def run_benchmark(functions_to_test: Callable,
                  input_sizes: list, num_runs: int =10):
    """Runs a benchmark for a set of functions over various input sizes.

    :param functions_to_test: A dictionary like {'name': function}.
    :param input_sizes: A list of input values to test.
    :param num_runs: The number of times to run each test for averaging.
    :return: A DataFrame with the results of the benchmarks.
    """
    benchmark_results = []
    print("Running benchmarks...")

    for name, function in functions_to_test.items():
        print(f"  Testing {name}...")
        for size in input_sizes:
            timer = timeit.Timer(lambda: function(size))
            total_time = timer.timeit(number=num_runs)
            avg_time = total_time / num_runs

            benchmark_results.append({
                'terms': size,
                'version': name,
                'time (s)': avg_time
            })
    print("Finished.")
    return pd.DataFrame(benchmark_results)


def format_value(value, position=None, precision=1):
    """
    Format a number into a human-readable string with K/M/B/T suffixes.

    :param value: The number to format.
    :param position: The tick position,
        defaults to None (It is required to be compatible with matplotlib; unused)
    :param precision: The number of decimal places to use,
        defaults to 1
    """
    if not isinstance(value, (int, float)):
        return TypeError("Value must be an int or float")
    if value == 0:
        return "0"

    number_suffixes = [
        (1_000_000_000_000, 'T'),
        (1_000_000_000, 'B'),
        (1_000_000, 'M'),
        (1_000, 'K'),
    ]

    for threshold, suffix in number_suffixes:
        if abs(value) >= threshold:
            return f"{value / threshold:.{precision}f} {suffix}"

    if isinstance(value, int):
        return f"{value}"
    else:
        return f"{value:.{precision}f}"


def format_time(value, position=None, precision=1):
    """
    Format a time duration in seconds into a human-readable string.

    :param value: The time duration in seconds
    :param position: The tick position,
        defaults to None (It is required to be compatible with matplotlib; unused)
    :param precision: The number of decimal places to use,
        defaults to 1
    """
    if not isinstance(value, (int, float)):
        return TypeError("Value must be an int or float")
    if value == 0:
        return "0 s"

    time_units = [
        (3600, 'hr'),
        (60, 'min'),
        (1, 's'),
        (0.001, 'ms'),
        (0.000001, 'μs'),
        (0.000000001, 'ns'),
    ]

    for threshold, unit in time_units:
        if abs(value) >= threshold:
            return f"{value / threshold:.{precision}f} {unit}"

    return f"{value:.{precision}f} s"


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
