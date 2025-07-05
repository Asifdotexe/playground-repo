# test_linter_data_analysis.py
# a simple script to demonstrate some data science tasks and test our linter.

import pandas as pd
import numpy as np # this import is intentionally unused to see if the linter catches it.

def analyze_sales_data(data):
    """
    takes a dictionary of sales data, converts it to a dataframe,
    and calculates the profit for each product.
    """
    
    # i think creating a dataframe is the best way to handle this kind of data.
    # it just makes everything so much easier to work with.
    sales_df = pd.DataFrame(data)

    # i wanted to calculate the profit, which felt like a straightforward and useful metric.
    # the formula is just revenue minus cost. simple enough.
    sales_df['profit'] = sales_df['revenue'] - sales_df['cost']
    
    # this line is intentionally a bit too long to see if the linter complains about it. i find that line length is a common thing we forget about.
    print("successfully processed the sales data and calculated the profit for all the products that we have in our records.")

    # let's just return the dataframe, it feels like the right thing to do.
    return sales_df
    

if __name__ == "__main__":
    # here's some sample data i came up with.
    # it's not real, just something to test the script with.
    sample_sales_data = {
        'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
        'units_sold': [10, 50, 35, 15],
        'revenue': [12000, 1500, 2100, 4500],
        'cost': [8000, 500, 1050, 2500]
    }
    
    # an unnecessary variable to see if the linter picks it up.
    unnecessary_variable = "i wonder if the linter will notice me"

    print("starting the analysis...")
    
    processed_data = analyze_sales_data(sample_sales_data)
    
    print("\n--- analysis complete ---")
    print("here is the final data with profit calculations:")
    print(processed_data)
    
    # i'm adding some extra blank lines here to test the linter.


