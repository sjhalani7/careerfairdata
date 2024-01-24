import pandas as pd

def read_data(filename):
    df_data=pd.read_csv(f"{filename}.csv")
    print(df_data.shape)
    return df_data

def read_survey(filename):
    df_survey=pd.read_csv(f"{filename}.csv")
    return df_survey

def count_year(df):
    try:
        masters_count = df['School Year'].value_counts()['Masters']
    except:
        masters_count = 0
    try:
        alumni_count = df['School Year'].value_counts()['Alumni']
    except:
        alumni_count = 0
    try:
        doctorate_count = df['School Year'].value_counts()['Doctorate']
    except:
        doctorate_count = 0
    try:
        juniors_count = df['School Year'].value_counts()['Junior']
    except:
        juniors_count = 0
    try:
        seniors_count = df['School Year'].value_counts()['Senior']
    except:
        seniors_count = 0

    grad_count = doctorate_count+masters_count
    
    total_students = df.shape[0]+1

    undergrads = total_students-masters_count-alumni_count-doctorate_count
    undergrad_perc = (undergrads/total_students)*100

    junior_perc = (juniors_count/undergrads)*100
    senior_perc = (seniors_count/undergrads)*100
    
    grad_perc = (grad_count/total_students)*100
    alumni_perc = (alumni_count/total_students)*100

    print("# undergrad: ", undergrads)
    print("'%' undergrad: ", undergrad_perc)
    print()

    print("# Masters: ", masters_count)
    print("'%' doc: ", doctorate_count)
    print()

    print("# Juniors: ", juniors_count)
    print("'%' juniors: ", junior_perc)
    print()

    print("# Seniors: ", seniors_count)
    print("'%' senior: ", senior_perc)
    print()

    print("'%' senior/junior: ", senior_perc+junior_perc)
    print()

    print("# Grad: ", grad_count)
    print("'%' Grad: ", grad_perc)
    print()

    print("# Alumni: ", alumni_count)
    print("'%' alumni: ", alumni_perc)
    print()

def count_school(df):
    
    cas_count = df['College'].value_counts()['CAS']
    lsb_count = df['College'].value_counts()['LSB']
    eng_count = df['College'].value_counts()['ENG']
    try:
        ecp_count = df['College'].value_counts()['ECP']
    except:
        ecp_count = 0

    total_students= df.shape[0]+1

    cas_perc=(cas_count/total_students)*100
    lsb_perc=(lsb_count/total_students)*100
    
    eng_perc=(eng_count/total_students)*100
    ecp_perc=(ecp_count/total_students)*100


    print("# CAS: ", cas_count)
    print("'%' CAS: ", cas_perc)
    print()

    print("# LSB: ", lsb_count)
    print("'%' LSB: ", lsb_perc)
    print()

    print("# ENG: ", eng_count)
    print("'%' ENG: ", eng_perc)
    print()

    print("# ECP: ", ecp_count)
    print("'%' ECP: ", ecp_perc)
    print()


def gender(df):
    # print(df[""])
    male_count = df['Student Attendees Gender'].value_counts()['Male']
    female_count = df['Student Attendees Gender'].value_counts()['Female']

    #####CHECK df['Student Attendees Gender'].unique() to get actual labels
    try:
        trans_count = df['Student Attendees Gender'].value_counts()['Transgender']
    except:
        trans_count = 0
    try:
        non_bin_count = df['Student Attendees Gender'].value_counts()['Non-Binary']
    except:
        non_bin_count = 0



    known_count = male_count+female_count


    total_students = df.shape[0] + 1
    perc_gend_known = known_count/total_students

    print("% gender known: ", perc_gend_known*100)

    male_perc = (male_count / known_count) * 100
    female_perc = (female_count / known_count) * 100
    trans_perc = (trans_count / known_count) * 100
    non_bin_perc = (non_bin_count / known_count) * 100


    print("# Male: ", male_perc)
    print("'%' Male: ", male_count)
    print()

    print("# Female: ", female_count)
    print("'%' Female: ", female_perc)
    print()

    print("# Transgender: ", trans_count)
    print("'%' Transgender: ", trans_perc)
    print()

    print("# Non-binary: ", non_bin_count)
    print("'%' Non-binary: ", non_bin_perc)
    print()


def race(df):
    #####CHECK df['Student Attendees Gender'].unique() to get actual labels and change this accordingly
    print(df["Student Attendees Ethnicity"].unique())
    white_count = df['Student Attendees Ethnicity'].value_counts()['White'] + df['Student Attendees Ethnicity'].value_counts()['White/Caucasian'] + df['Student Attendees Ethnicity'].value_counts()['White (United States Of America)']
    black_count = df['Student Attendees Ethnicity'].value_counts()['Black or African American']
    asian_count = df['Student Attendees Ethnicity'].value_counts()['Asian'] + df['Student Attendees Ethnicity'].value_counts()['Asian/Asian American']
    hisp_count = df['Student Attendees Ethnicity'].value_counts()['Hispanic Or Latino']
    try:
        native_count = df['Student Attendees Ethnicity'].value_counts()['American Indian Or Alaska Native']
    except:
        native_count = 0
    pac_isl_count = df['Student Attendees Ethnicity'].value_counts()['Native Hawaiian Or Other Pacific Islander']

    mult_count = df['Student Attendees Ethnicity'].value_counts()['Multi Ethnic']
   #####CHECK df['Student Attendees Gender'].unique() to get actual labels



    known_count = white_count+black_count+asian_count+hisp_count+native_count+pac_isl_count+mult_count

    total_students = df.shape[0] + 1
    perc_gend_known = known_count/total_students

    print("% race known: ", perc_gend_known*100)

    white_perc = (white_count / known_count) * 100
    black_perc = (black_count / known_count) * 100
    asian_perc = (asian_count / known_count) * 100
    hisp_perc = (hisp_count / known_count) * 100
    native_perc = (native_count / known_count) * 100
    pac_isl_perc = (pac_isl_count / known_count) * 100
    mult_perc = (mult_count / known_count) * 100


    print("# White: ", white_count)
    print("'%' White: ", white_perc)
    print()

    print("# Black: ", black_count)
    print("'%' Black: ", black_perc)
    print()

    print("# Asian: ", asian_count)
    print("'%' Asian: ", asian_perc)
    print()

    print("# Hispanic: ", hisp_count)
    print("'%' Hispanic: ", hisp_perc)
    print()

    print("# Native: ", native_count)
    print("'%' Native: ", native_perc)
    print()

    print("# Pacific Islander: ", pac_isl_count)
    print("'%' Pacific Islander: ", pac_isl_perc)
    print()

    print("# Multiple: ", mult_count)
    print("'%' Multple: ", mult_perc)
    print()

def execute():
    df=read_data("10_11_23_Career Fair_Student Raw Data_42510")
    print(df.columns)
    count_year(df)
    count_school(df)
    gender(df)
    race(df)


execute()