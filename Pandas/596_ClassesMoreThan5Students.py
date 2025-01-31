# 596. Classes More Than 5 Students

# Pandas Solution 1
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # Group by class and count students
    class_counts = courses.groupby('class').size().reset_index(name='count')
    
    # Filter classes with at least five students and return as DataFrame
    result = class_counts[class_counts['count'] >= 5][['class']]
    return result