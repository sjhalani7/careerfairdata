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
    print(df.tail())
    print(df.columns)
    return df

def stats_ec_satisfy(df):
    total_students= df.shape[0]
    blanks_count = df["Q16"].isnull().sum()

    denom=total_students-blanks_count
    sm_sat=df["Q16"].value_counts()['Somewhat satisfied']
    strong_sat=df["Q16"].value_counts()['Extremely satisfied']

    agree=sm_sat+strong_sat

    print(f'EC team - % satisfaction: {(agree/denom)*100}\n')

def stats_emp_sponsor(df):
    total_students= df.shape[0]
    blanks_count = df["Q11"].isnull().sum()

    denom=total_students-blanks_count
    agree_to_sponsor=df["Q11"].value_counts()['Yes']


    print(f'Emp Sponsorship - % Yes: {(agree_to_sponsor/denom)*100}\n')

def execute():
    df=create_df('emp_test')
    df = preprocess(df)
    stats_ec_satisfy(df)
    stats_emp_sponsor(df)
    df.to_csv("test_out.csv")

execute()