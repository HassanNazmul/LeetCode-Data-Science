# 511. Game Play Analysis I

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Group by player_id and get the minimum event_date for each player
    result = activity.groupby('player_id')['event_date'].min().reset_index()
    
    # Rename the column for clarity
    result.rename(columns={'event_date': 'first_login'}, inplace=True)
    
    return result

# Test the function
activity = pd.DataFrame({
    'player_id': [1, 1, 2, 3, 3],
    'device_id': [2, 2, 3, 1, 4],
    'event_date': ['2016-03-01', '2016-05-02', '2017-06-25', '2016-03-02', '2018-07-03'],
    'games_played': [5, 6, 1, 0, 5]
})

print(game_analysis(activity))