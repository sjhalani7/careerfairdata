import pandas as pd

career_fair_number= '37526'
career_fair_date='04_12_23'

def create_df(filename):
    df=pd.read_csv(f"{filename}.csv")
    return df

def stats_responded(df):
    #number of students responded
    #count exceeded/far exceeded/equalled
    #exceeded expectations 
    total_students= df.shape[0]
    print("\nTotal students responded to Survey #1: ", total_students)
    equal=df['To what extent did this career fair meet your expectations?'].value_counts()['Equaled expectations']
    exceed=df['To what extent did this career fair meet your expectations?'].value_counts()['Exceeded expectations']
    far_exceed=df['To what extent did this career fair meet your expectations?'].value_counts()['Far exceeded expectations']
    good=equal+exceed+far_exceed
    
    print(f'% Exceeded or equaled expectations: {(good/total_students)*100}\n')

    #the following code prints out the qualitative feedback for exceeded expectations, but it may just be better to open the sheet
    # and copy the column from there.    
    '''
    print("Qualitative feedback - Exceeded expectations: Results: \n")
    non_null_fdbk = df.loc[df["That's great! Please share what specifically about the career fair exceeded your expectations. We'll use your feedback to improve our events in the future."].notnull(), "That's great! Please share what specifically about the career fair exceeded your expectations. We'll use your feedback to improve our events in the future."]
    print(non_null_fdbk)
    ''' 
def stats_jobtypes(df):
    total_students= df.shape[0]
    blanks_count = df["I gained a better understanding of the types of jobs and companies that might interest me."].isnull().sum()

    denom=total_students-blanks_count
    sm_agree=df["I gained a better understanding of the types of jobs and companies that might interest me."].value_counts()['Somewhat agree']
    strong_agree=df["I gained a better understanding of the types of jobs and companies that might interest me."].value_counts()['Strongly agree']

    agree=sm_agree+strong_agree

    print(f'Jobs & companies - % better understand: {(agree/denom)*100}\n')

def stats_recemp(df):
    total_students= df.shape[0]
    blanks_count = df["I gained a better understanding of what recruiters and employers are looking for in prospective candidates."].isnull().sum()
    denom=total_students-blanks_count

    sm_agree=df["I gained a better understanding of what recruiters and employers are looking for in prospective candidates."].value_counts()['Somewhat agree']
    strong_agree=df["I gained a better understanding of what recruiters and employers are looking for in prospective candidates."].value_counts()['Strongly agree']
    agree=sm_agree+strong_agree

    print(f'Recruiters & employers - % better understand: {(agree/denom)*100}\n')

def stats_jobsearch(df):
    total_students= df.shape[0]
    blanks_count = df["I gained a better understanding of the job search process."].isnull().sum()
    denom=total_students-blanks_count

    sm_agree=df["I gained a better understanding of the job search process."].value_counts()['Somewhat agree']
    strong_agree=df["I gained a better understanding of the job search process."].value_counts()['Strongly agree']
    agree=sm_agree+strong_agree

    print(f'Job search process - % better understand: {(agree/denom)*100}\n')








def execute():
    df=create_df('stusurvey')
    stats_responded(df)
    stats_jobtypes(df)
    stats_recemp(df)
    stats_jobsearch(df)

execute()
