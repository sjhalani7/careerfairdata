import pandas as pd

career_fair_number= '37526'
career_fair_date='04_12_23'

def create_df(filename):
    df=pd.read_csv(f"{filename}.csv")
    return df

def drop_rows(df):
    try:
        df.drop('Username', axis=1, inplace=True)
    except: 
        print('No column Username')
    try:
        df.drop('Institution Name', axis=1, inplace=True)
    except: 
        print('No column Institution Name')
    try:
        df.drop('Registered', axis=1, inplace=True)
    except: 
        print('No column Registered')
    try:
        df.drop('Number of group no shows', axis=1, inplace=True)
    except: 
        print('No column Number of group no shows')
    try:
        df.drop('Number of 1:1 sessions', axis=1, inplace=True)
    except: 
        print('No column Number of 1:1 sessions')
    try:
        df.drop('Number of group sessions', axis=1, inplace=True)
    except: 
        print('No column Number of group sessions')
    try:
        df.drop('Number of Number of 1:1 no shows', axis=1, inplace=True)
    except: 
        print('No column Number of 1:1 no shows')



def checked_in(df):
    mask_remove = df['Checked In'].str.startswith('N')
    df.drop(df[mask_remove].index, inplace=True)
    df['Checked In'] = 'Yes'


def remove_ccstaff(df):
    staff_email=['skreidler@scu.edu', 'dhoule@scu.edu', 'sbarber@scu.edu', 'vtong@scu.edu', 'mbartz2@scu.edu', 'charris2@scu.edu', 'cwithers@scu.edu','abizuneh@scu.edu', 'agupton@scu.edu', 'mthiriez@scu.edu']
    emails_cf=df['Email Address']
    for email in emails_cf:
        if email in staff_email:
            df.drop(df[df['Email Address']==email].index, inplace=True)

def acronyms(df):
    dict={'School of Engineering':'ENG', 'College of Arts and Sciences':'CAS', 'Leavey School of Business':'LSB', 'School of Education and Counseling Psychology':'ECP', '':''}
    colleges=df['College']
    for college in colleges:
        if college in dict.keys():
            df.loc[df['College'] == f'{college}', 'College']=dict[college]

def change_symbols(df): #convert ampersand to 'and'...reduce symbols 
     df['Majors'] = df['Majors'].apply(lambda x: x.replace('&', 'and'))

def fill_blanks(df):
    cas_majors= ['Ancient Studies', 'Anthropology', 'Art History', 'Biochemistry', 'Biology', 'Chemistry', 'Child Studies', 'Classical Studies', 'Communication', 'Computer Science', 'Economics (BS)', 'Economics' 'Engineering Physics', 'English', 'Environmental Studies and Sciences', 'Ethnic Studies', 'Greek Language and Literature', 'History', 'Individual Studies', 'Latin and Greek', 'Latin Language and Literature', 'Mathematics', 'Military Science', 'Modern Languages and Literatures', 'Arabic', 'Chinese', 'French', 'German', 'Italian', 'Japanese', 'Spanish', 'Music', 'Neuroscience', 'Philosophy', 'Physics', 'Political Science', 'Psychology', 'Public Health Science', 'Religious Studies', 'Sociology', 'Studio Art', 'Theatre and Dance', "Women's and Gender Studies", "Environmental Science"]
    lsb_majors= ['Accounting', 'Accounting & Information Systems', 'Economics', 'Finance', 'Individual Studies', 'Management & Entrepreneurship', 'Management Information Systems', 'Marketing', 'Information Systems', 'MBA', 'STEM MBA', 'On-line MBA', 'Business Analytics (Online)', 'Business Analytics', 'Finance and Analytics', 'Economics (Bsc)']
    for index, row in df.iterrows():
        if pd.isna(df.loc[index, 'College']) or df.loc[index, 'College'] == '':
            major = df.loc[index, 'Majors']
            if major in cas_majors:
                df.loc[index, 'College']="CAS"
            elif major in lsb_majors:
                df.loc[index, 'College']="LSB"
            elif 'engineering' in major.lower() or 'engr.' in major.lower():
                df.loc[index, 'College']="ENG"
            else: 
                df.loc[index, 'College']="XXXXXXXXXXXXX" #### Temp solution for comma separated majors

def gender_race(df1):
    df2=pd.read_csv('gender.csv')
    merged_df=pd.merge(df1, df2[['Student Attendees Email - Institution', 'Student Attendees Gender', 'Student Attendees Ethnicity']], left_on='Email Address', right_on='Student Attendees Email - Institution', how='left')
    merged_df.drop('Student Attendees Email - Institution', axis=1, inplace=True)
    merged_df.to_csv(f'{career_fair_date}_Career Fair_Student Raw Data_{career_fair_number}.csv', index=False)

def execute():
    df=create_df('37526')
    drop_rows(df)
    checked_in(df)
    remove_ccstaff(df)
    acronyms(df)
    change_symbols(df)
    fill_blanks(df)
    gender_race(df) #converts to CSV in function
    
execute()