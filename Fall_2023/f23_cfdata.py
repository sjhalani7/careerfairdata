import pandas as pd

def create_df(filename):
    df=pd.read_csv(f"{filename}.csv")
    df = df.iloc[2:]
    # print(df.head())
    # print(df.columns)
    return df

def preprocess(df):
    cols_to_keep = ["RecipientLastName", "RecipientFirstName", "RecipientEmail", "Q19", 'Q12',	"Q14",	"Q16", "Q17", "Q20", 'Q18', "Q25_NPS_GROUP", "Q25", "Q18"]
    df = df[cols_to_keep]
    print(df.head())
    print(df.columns)
    return df


def execute():
    df=create_df('test')
    preprocess(df)
    #stats_responded(df)
    #stats_jobtypes(df)
    #stats_recemp(df)
    #stats_jobsearch(df)

execute()