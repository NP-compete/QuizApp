import pandas as pd
from pandas.io.json import json_normalize

QUIZ_FILE = 'quiz.json'

def parseNformat_json():
    df = pd.read_json(QUIZ_FILE)
    pd.concat([pd.DataFrame(d) for d in df['quiz']], axis=0, keys=df['quiz'].index, sort=True)
    df1 = json_normalize(df['quiz'])
    df1.set_index(df['quiz'].index, inplace=True)
    col_list = list(df1)
    col_list[0], col_list[2] = col_list[2], col_list[0]
    col_list[3], col_list[5] = col_list[5], col_list[3]
    df1 = df1.loc[:,col_list]
    #print(df2)
    return df1
