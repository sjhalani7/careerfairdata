import pandas as pd

career_fair_number= '37526'
career_fair_date='04_12_23'

def create_df(filename):
    df=pd.read_csv(f"{filename}.csv")
    return df

def delete_col(df):
    del_lis=['Created at', 'Updated at', 'Career Fair', 'Description', 'Website', 'Division', 'Created By Name', 'Created By Email', 
    'Assigned Booth Options', 'Assigned Booth Numbers', 'Assigned Booth Rooms', 'Payment Method', 'Message', 'Refund Policy Agreement',
    'Jobs on Handshake', 'Job Titles', 'Majors', 'Major Groups', 'Combined Majors', 'Located in US?', 'Work Authorizations', 'Last Charge',
    'Discounts', 'Sessions', 'What are the top three skills you are seeking in our candidates?', 'SCU students are very interested in organizations whose values align with their own. We encourage highlighting your Diversity, Equity and Inclusion practices, any Social Justice statements or programs, Environmental/sustainability initiatives, and/or Black Lives Matter support your organization represents. Please share anything related to these effort you would like to highlight.',
    'Are you a third party recruiter? ', 'Please provide a contact name, email & number for the fair.', 'Number of Group Sessions', 
    'Number of Group Session No Shows', 'Number of 1:1 Sessions', 'Number of 1:1 No Shows', 'Registrations with Required Preferences'
    ]
    for column in del_lis:
        try:
            df.drop(f'{column}', axis=1, inplace=True)
        except: 
            print(f"No Column '{column}'")

def execute():
    df=create_df('emp')
    delete_col(df)
    df.to_csv(f'{career_fair_date}_Career Fair_Employer Raw Data_{career_fair_number}.csv', index=False)

execute()