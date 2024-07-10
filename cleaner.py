""" This File is Made by Dylan Sedeno to help with cleaning files for
for data analytics. Started: 6/21/2024 Last Modified: 7/2024"""

# Imports Needed.
import pandas as pd
from googletrans import Translator
import builtins
import re
from re import escape


# Reading a csv file to a data frame. Takes in name for the csv file.
def read_csv(name: str) -> pd.DataFrame:
    file = pd.read_csv(name)
    return file

# Saves a data frame as a CSV file.
def save_csv(df: pd.DataFrame, file_name: str) -> None:
    df.to_csv(file_name, index=False)

# Takes a number of data frames and merges them together.
def merge_files(*dfs: pd.DataFrame) -> pd.DataFrame:
    return pd.concat(dfs)

# Takes a column in a data frame and turns it into a list 
def to_list(df: pd.DataFrame, column:str, list:list) -> None:
    for item in df[column]:
        if item not in list:
            list.append(item)

# strips the white spaces from a selected column in a data frame
def ws_gone(df: pd.DataFrame, column: str) -> None:
    df[column] = df[column].str.strip()

# Changes the column name to lowercase. Takes in a data frame.
def col_low(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.lower()

# Renames specified columns.
def new_col_name(df: pd.DataFrame, new_names: list) -> pd.DataFrame:
    df.columns = new_names

# Removes specified columns.
def drop_col(df: pd.DataFrame, columns_to_drop: list) -> pd.DataFrame:
    df.drop(columns_to_drop, axis=1, inplace=True)

# Reorders columns, takes in a list of names
def col_order(df: pd.DataFrame, name_order: list) -> pd.DataFrame:
    df = df[name_order]
    return df

# Returns information on a specific column 
# Put ; at the end of the function so none doesn't display
def col_info(df: pd.DataFrame, column: str) -> None:
    print( f"\nUnique:\n {df[column].unique()}")
    print( f"\nDescribe:\n {df[column].describe()}")
    print( f"\nValue Counts:\n {df[column].value_counts()}")
    
# Returns information on a specific column 
# Put ; at the end of the function so none doesn't display
def col_val_count(df: pd.DataFrame, column: str) -> None:
    print( f"\nValue Counts:\n {df[column].value_counts()}")

# This returns the average of a column, it asks for the column
# and you specify if the data frame has nan's
def cal_col_mean(df: pd.DataFrame, column: str, nan_yn: str) -> float:
    try:

           # Convert the column to numeric type
        df[column] = pd.to_numeric(df[column], errors='coerce')

        if nan_yn.lower() in ['yes', 'y', 'true', '1']:
            average = df[column].mean(skipna=True)
        else:
            average = df[column].mean()
        return average
    except KeyError:
        print(f"Error: Column '{column}' not found in the DataFrame.")
        return None

# takes in a data frame, a column name and a type class, and changes the columns data
# type to the specified type
def col_type(df: pd.DataFrame, column: str, type_str:str) -> None:
    type_obj = getattr(builtins, type_str)
    df[column] = df[column].astype(type_obj)

# Shows if there is and duplicated rows and if there are null values.
def dup_nul(df: pd.DataFrame) -> None:
    print(f"Duplicate Rows: {df.duplicated().sum()}")
    print(f"Null Values:\n{df.isnull().sum()}")

# Returns a data frame with the duplicated rows.
def duplicated_set(df: pd.DataFrame) -> pd.DataFrame:
    dup = df.duplicated(keep=False)
    dup_rows = df[dup]
    return dup_rows

# Returns a data frame with the duplicated rows based off specific columns.
def duplicated_col_set(df: pd.DataFrame, col_1: str) -> pd.DataFrame:
    dup = df.duplicated(subset=[col_1],keep=False)
    dup_rows = df[dup]
    return dup_rows

# Removes rows from a data frame.
def drop_dup(df: pd.DataFrame) -> None:
    df.drop_duplicates(inplace=True)

# Removes rows from a data frame based off a specific column.
def drop_dup_col(df: pd.DataFrame, col_1: str) -> None:
    df.drop_duplicates(subset=[col_1], inplace=True) 

# Fill NaN values in a column with a specified value.
def fill_nan(df: pd.DataFrame, column:str, value:any)-> pd.DataFrame:
    df[column].fillna(value, inplace=True)
    return df

# Removes characters you dont want in a column.
def clean_column(df: pd.DataFrame, column: str, away: str) -> pd.DataFrame:
    chars_to_remove = str.maketrans("", "", away)  # create a translation table
    df[column] = df[column].str.translate(chars_to_remove)
    return df

# Takes in a data frame, column name and a list of words and then removes 
# the words from the data frame column
def remove_words(df: pd.DataFrame, column: str, words: list) -> pd.DataFrame:
    pattern = '|'.join(re.escape(word) for word in words)
    df[column] = df[column].str.replace(pattern, '', regex=True)
    return df

# Removes whitespaces from a column in a data frame
def remove_space(df: pd.DataFrame, column: str) -> None:
    df[column] = df[column].str.strip()

# Replaces a specified value in a column with another value
def replace_val(df: pd.DataFrame, column: str, old: any, replace: any) -> pd.DataFrame:
    df[column] = df[column].str.replace(old, replace)
    return df

# Maps values in a column based on a dictionary.
def map_values(df: pd.DataFrame, column: str, mapping_dict: dict, default_value='Unknown') -> pd.DataFrame:
    """
    Maps values in a column based on a dictionary.

    Parameters:
    - df (pandas.DataFrame): The DataFrame containing the column to be mapped.
    - column (str): The name of the column to be mapped.
    - mapping_dict (dict): A dictionary where keys are the original values and values are the mapped values.
    - default_value (str, optional): The value to return if the original value is not found in the mapping_dict. Defaults to 'Unknown'.

    Returns:
    - pandas.Series: The mapped values as a Series.
    """
    def map_value(x):
        for key, value in mapping_dict.items():
            if x.startswith(key):
                return value
        return default_value

    return df[column].apply(map_value)

def create_column_based_on_dict(df: pd.DataFrame, target_column: str, new_column: str, dict_column: dict, delimiter=',') -> pd.DataFrame:
    """
    Creates a new column based on the values in the target column and a dictionary.

    Parameters:
    - df (pandas.DataFrame): The DataFrame containing the "Target" column.
    - target_column (str): The name of the "Target" column.
    - new_column (str): The name of the new column to be created.
    - dict_column (dict): A dictionary where keys are the values in the target column and values are the corresponding values for the new column.
    - delimiter (str): The delimiter used to separate multiple values in the target column.

    Returns:
    - pandas.DataFrame: The DataFrame with the new column.
    """
    def get_value(x):
        if delimiter is None:
            if x in dict_column:
                return dict_column[x]
            else:
                return 'Unknown'
        else:
            for value in x.split(delimiter):
                value = value.strip()
                if value in dict_column:
                    return dict_column[value]
            return 'Unknown'

    df[new_column] = df[target_column].apply(get_value)
    return df

translator = Translator()
 
# Function to translate text to english for df do df['col_name'].apply(cleaner.text_to_en)
def text_to_en(text: str, src='auto', dest: str ='en') -> str:
    if pd.isna(text):
        return text
    try:
        translated = translator.translate(text, src=src, dest=dest)
        return translated.text
    except Exception as e:
        print(f"Error translating text: {e}")
        return text
