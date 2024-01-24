import pandas as pd



def create_df(filename):
    df = pd.read_csv(f"{filename}.csv")
    df = df.drop(df.index[0:2])
    return df

def preprocess(df):
    cols_to_keep = ["RecipientLastName", "RecipientFirstName", "RecipientEmail", "Q1", 'Q3',	"Q3_6_TEXT",	"Q3_1", "Q3_2", "Q3_3", 'Q3_4', "Q3_5", "Q3_6", "Q5"]
    df = df[cols_to_keep]
    # print(df.head())
    # print(df.columns)
    return df


def stats_responded(df):
    # number of students responded
    # count exceeded/far exceeded/equalled
    # exceeded expectations
    total_students = df.shape[0]
    print("\nTotal students responded to Survey #2: ", total_students)
    help_achieve_count = df[df['Q3'].str.contains("Increased my interest in/awareness of employment opportunities offered through the Career Center", na=False)].shape[0]
    submit_app_count = df[df['Q3'].str.contains("Submitted applications to participating career fair employer\(s\)", regex=True, na=False)].shape[0]

    interviewed_count = df[df['Q3'].str.contains("Interviewed with participating career fair employer\(s\)", regex=True, na=False)].shape[0]

    offer_count = df[df['Q3'].str.contains(
        "Received a job or internship offer from participating career fair employer\(s\)", regex=True,
        na=False)].shape[0]

    hired_count = df[df['Q3'].str.contains(
        "Hired by a participating career fair employer",
        na=False)].shape[0]
    none_count = df[df['Q3'].str.contains(
        "None of the above",
        na=False)].shape[0]




    print("Increased interest / awareness: ", help_achieve_count)
    print("Submitted applications: ", submit_app_count)
    print("Interviewed: ", interviewed_count)
    print("Offered job / internship: ", offer_count)
    print("Hired: ", hired_count)
    print("None of the above: ", none_count)



def stats_jobtypes(df):
    total_students = df.shape[0]
    blanks_count = df[
        "I gained a better understanding of the types of jobs and companies that might interest me."].isnull().sum()

    denom = total_students - blanks_count
    sm_agree = \
    df["I gained a better understanding of the types of jobs and companies that might interest me."].value_counts()[
        'Somewhat agree']
    strong_agree = \
    df["I gained a better understanding of the types of jobs and companies that might interest me."].value_counts()[
        'Strongly agree']

    agree = sm_agree + strong_agree

    print(f'Jobs & companies - % better understand: {(agree / denom) * 100}\n')


def stats_recemp(df):
    total_students = df.shape[0]
    blanks_count = df[
        "I gained a better understanding of what recruiters and employers are looking for in prospective candidates."].isnull().sum()
    denom = total_students - blanks_count

    sm_agree = df[
        "I gained a better understanding of what recruiters and employers are looking for in prospective candidates."].value_counts()[
        'Somewhat agree']
    strong_agree = df[
        "I gained a better understanding of what recruiters and employers are looking for in prospective candidates."].value_counts()[
        'Strongly agree']
    agree = sm_agree + strong_agree

    print(f'Recruiters & employers - % better understand: {(agree / denom) * 100}\n')


def stats_jobsearch(df):
    total_students = df.shape[0]
    blanks_count = df["I gained a better understanding of the job search process."].isnull().sum()
    denom = total_students - blanks_count

    sm_agree = df["I gained a better understanding of the job search process."].value_counts()['Somewhat agree']
    strong_agree = df["I gained a better understanding of the job search process."].value_counts()['Strongly agree']
    agree = sm_agree + strong_agree

    print(f'Job search process - % better understand: {(agree / denom) * 100}\n')


def execute():
    df = create_df('survey_2')
    df = preprocess(df)
    stats_responded(df)
    # stats_jobtypes(df)
    # stats_recemp(df)
    # stats_jobsearch(df)


execute()
