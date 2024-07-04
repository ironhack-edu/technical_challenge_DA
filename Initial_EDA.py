import pandas as pd

def explore_df(df):
    """
    Explores the dataframe via its dims, dtypes, null counts of each column,
    and value counts for each columns

    Arguments: df (pd.Dataframe) - Dataframe to explore
    Returns: tuple(pd.Dataframe*2) - dataframes of numerical & categorical columns
    """
    sep_lines = '\n' + '-'*50 + '\n'
    end_lines = '\n' + '='*50 + '\n'
    
    print("Dataframe shape: ")
    print(f"{df.shape[0]} rows X {df.shape[1]} columns", end=end_lines)

    print("Dataframe data types")
    print(df.dtypes,end=end_lines)

    print(f"Null Count:")
    null_df = pd.concat([df.isnull().sum(), df.isnull().mean()],axis=1)
    null_df.columns = ['count','normalize_count']
    print(null_df, end=end_lines)

    print(f"{df.columns}", end=end_lines)

    cat_from_num = df.select_dtypes("number").loc[:, df.select_dtypes("number").nunique() < 20]
    df_categorical = pd.concat([df.select_dtypes("object"), cat_from_num ], axis=1)
    df_categorical = df_categorical.astype(str) # convert to object type for printing
    df_numerical = df.drop(df_categorical.columns, axis=1)
    
    if not df_categorical.empty:
        print("Value counts for each categorical column:")

    for col in df_categorical.columns:
        print(df[col].value_counts(dropna=False),end=sep_lines)

    print(end_lines.strip('\n'))
    if not df_categorical.empty:
        print(df_numerical.describe(include='number'), end=sep_lines)
        print(df_categorical.describe(include='object'))
    else:
        print(df.describe(include='all'))

    return df_numerical, df_categorical


def nulls_in_col(data, col:str):
    """
    print null counts in dataframe column

    Arguments: data (pd.DataFrame) - dataframe
               col = dataframe column
    Returns: None
    """
    print(f"Number of nulls in {col}: {data[col.isna().sum()]}")