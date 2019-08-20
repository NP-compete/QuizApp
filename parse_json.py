import pandas as pd
from pandas.io.json import json_normalize

def parseNformat_json(QUIZ_FILE):
    df = pd.read_json(QUIZ_FILE)
    # Parse JSON
    pd.concat([pd.DataFrame(d) for d in df['quiz']], axis=0, keys=df['quiz'].index, sort=True)
    df1 = json_normalize(df['quiz'])
    df1.set_index(df['quiz'].index, inplace=True)
    # Format JSON
    col_list = list(df1)
    col_list[0], col_list[2] = col_list[2], col_list[0]
    col_list[3], col_list[5] = col_list[5], col_list[3]
    df1 = df1.loc[:,col_list]
    return df1
