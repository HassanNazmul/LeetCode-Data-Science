# 584. Find Customer Referee

# Pandas Solution 1
import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    return customer[~customer['referee_id'].isin([2])][['name']] # 2 is the referee_id
