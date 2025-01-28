# 586. Customer Placing the Largest Number of Orders

# Pandas Solution 1:

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # Group by customer_number and count orders
    customer_orders = orders.groupby('customer_number').size().reset_index(name='order_count')
    
    # Get the customer(s) with maximum orders
    max_orders = customer_orders[customer_orders['order_count'] == customer_orders['order_count'].max()]
    
    # Return DataFrame with only customer_number column
    return max_orders[['customer_number']]

# Pandas Solution 2:
def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # Count occurrences of each customer_number
    customer_counts = orders['customer_number'].value_counts()
    
    # Get the customer(s) with maximum orders
    max_customers = customer_counts[customer_counts == customer_counts.max()].index
    
    # Create and return the result DataFrame
    return pd.DataFrame({'customer_number': max_customers})

# Test Cases
print(largest_orders(pd.DataFrame({'customer_number': [1, 2, 3, 1, 2, 1, 2, 3, 3, 3]})))

