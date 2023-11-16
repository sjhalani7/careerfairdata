import pandas as pd

def create_df(filename):
    df=pd.read_csv(f"{filename}.csv")
    df = df.iloc[2:]
    # print(df.head())
    # print(df.columns)
    return df

def preprocess(df):
    cols_to_keep = ["RecipientEmail", "Q21", 'Q3',	"Q4", "Q5", "Q6", "Q8", 'Q9', "Q10", "Q13", "Q16", "Q18", "Q20_NPS_GROUP", "Q20", "Q14", "Q11"]
    df = df[cols_to_keep]
    print(df.head())
    print(df.columns)
    return df

def execute():
    df=create_df('emp_test')
    df = preprocess(df)
    #stats_responded(df)
    #stats_jobtypes(df)
    #stats_recemp(df)
    #stats_jobsearch(df)
    df.to_csv("test_out.csv")

execute()