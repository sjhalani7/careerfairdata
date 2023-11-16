import pandas as pd

def create_df(filename):
    df=pd.read_csv(f"{filename}.csv")
    # ref_df = df.iloc[0:1]
    df = df.iloc[2:]
    # print(ref_df)
    print(df.head())
    print(df.tail())

    # print(df.columns)
    return df

def preprocess(df):
    cols_to_keep = ["RecipientLastName", "RecipientFirstName", "RecipientEmail", "Q19", 'Q12',	"Q14",	"Q16", "Q17", "Q20", 'Q18', "Q25_NPS_GROUP", "Q25", "Q18"]
    df = df[cols_to_keep]
    # print(df.head())
    # print(df.columns)
    return df



def stats_responded(df):
    # number of students responded
    # count exceeded/far exceeded/equalled
    # exceeded expectations
    total_students = df.shape[0]
    print("\nTotal students responded to Survey #1: ", total_students)
    equal = df['Q12'].value_counts()['Equaled expectations']
    exceed = df['Q12'].value_counts()['Exceeded expectations']
    far_exceed = df['Q12'].value_counts()[
        'Far exceeded expectations']
    good = equal + exceed + far_exceed

    print(f'% Exceeded or equaled expectations: {(good / total_students) * 100}\n')

def stats_jobtypes(df):
    total_students= df.shape[0]
    blanks_count = df["Q17"].isnull().sum()

    denom=total_students-blanks_count
    sm_agree=df["Q17"].value_counts()['Somewhat agree']
    strong_agree=df["Q17"].value_counts()['Strongly agree']

    agree=sm_agree+strong_agree

    print(f'Jobs & companies - % better understand: {(agree/denom)*100}\n')

def stats_recemp(df):
    total_students= df.shape[0]
    blanks_count = df["Q20"].isnull().sum()
    denom=total_students-blanks_count

    sm_agree=df["Q20"].value_counts()['Somewhat agree']
    strong_agree=df["Q20"].value_counts()['Strongly agree']
    agree=sm_agree+strong_agree

    print(f'Recruiters & employers - % better understand: {(agree/denom)*100}\n')

def stats_jobsearch(df):
    total_students= df.shape[0]
    blanks_count = df["Q18"].isnull().sum()
    denom=total_students-blanks_count

    sm_agree=df["Q18"].value_counts()['Somewhat agree']
    strong_agree=df["Q18"].value_counts()['Strongly agree']
    agree=sm_agree+strong_agree

    print(f'Job search process - % better understand: {(agree/denom)*100}\n')

def execute():
    df=create_df('stem_student')
    preprocess(df)
    stats_responded(df)
    stats_jobtypes(df)
    stats_recemp(df)
    stats_jobsearch(df)

execute()