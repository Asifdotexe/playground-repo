"""This is a general cli utility module that include useful functions for command line interface operations, like:
- Formatting DataFrames as PrettyTables for console output (PrettyTable).
"""

from typing import Optional

import pandas as pd
from prettytable import PrettyTable


def format_df_as_table(df: pd.DataFrame, top_n: Optional[int] = None, bottom_n: Optional[int] = None) -> PrettyTable:
    """Converts a pandas DataFrame to a PrettyTable object for clean console printing.
    Can optionally display only the top or bottom N rows.

    :patam df: The DataFrame to convert.
    :param top_n: If specified, only the top N rows will be displayed. Defaults to None.
    :param bottom_n: If specified, only the bottom N rows will be displayed. Defaults to None.

    Returns:
        A PrettyTable object containing the DataFrame's data.
    """
    if top_n is not None and bottom_n is not None:
        raise ValueError("Cannot specify both top_n and bottom_n. Please choose one.")

    display_df = df
    if top_n is not None:
        display_df = df.head(top_n)
    elif bottom_n is not None:
        display_df = df.tail(bottom_n)

    table = PrettyTable()
    table.field_names = display_df.columns.tolist()

    # Using the more efficient .values and add_rows() for better performance
    # This avoids the slow iterrows() method
    table.add_rows(display_df.values.tolist())

    return table
