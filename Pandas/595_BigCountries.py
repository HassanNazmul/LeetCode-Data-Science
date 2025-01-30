# 595. Big Countries

# Pandas Solution 1

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    world = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)] # Filter the data
    return world[['name', 'population', 'area']] # Return the required columns


# Pandas Solution 2

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world.query('area >= 3000000 or population >= 25000000')[['name', 'population', 'area']] # Filter the data and return the required columns