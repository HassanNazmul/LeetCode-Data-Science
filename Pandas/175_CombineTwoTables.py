# 175. Combine Two Tables

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

# # Another way to solve the problem
# def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
#     # Perform left join on person and address tables based on personId
#     result = person.merge(address, how='left', on='personId')

#     # Select only firstName, lastName, city, state columns 
#     result = result[['firstName', 'lastName', 'city', 'state']]

#     return result


# Test the function
person = pd.DataFrame({
    'personId': [1, 2, 3],
    'lastName': ['Doe', 'Smith', 'Johnson'],
    'firstName': ['John', 'Jane', 'Alice']
})

address = pd.DataFrame({
    'addressId': [1, 2],
    'personId': [1, 3],
    'city': ['New York', 'Chicago'],
    'state': ['NY', 'IL']
})

print(combine_two_tables(person, address))