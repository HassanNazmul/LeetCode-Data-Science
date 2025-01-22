# 175. Combine Two Tables

# Table: Person
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | personId    | int     |
# | lastName    | varchar |
# | firstName    | varchar |
# +-------------+---------+

# Table: Address
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | addressId   | int     |
# | personId    | int     |
# | city        | varchar |
# | state       | varchar |
# +-------------+---------+

import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:

    # Merge person and address tables with selected columns using left join
    # This will keep all persons even if they don't have an address
    result = pd.merge(
        person[['personId', 'firstName', 'lastName']], # Select required columns from person
        address[['personId', 'city', 'state']], # Select required columns from address
        on='personId', # Join on personId column
        how='left' # Use left join to keep all persons
    )[['firstName', 'lastName', 'city', 'state']] # Select final output columns
    
    return result


    # # Perform left join on person and address tables based on personId
    # result = person.merge(address, how='left', on='personId')

    # # Select only firstName, lastName, city, state columns 
    # result = result[['firstName', 'lastName', 'city', 'state']]

    # return result