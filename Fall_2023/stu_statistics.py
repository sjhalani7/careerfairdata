import pandas as pd

def read_data(filename):
    df_data=pd.read_csv(f"{filename}.csv")
    return df_data

def read_survey(filename):
    df_survey=pd.read_csv(f"{filename}.csv")
    return df_survey

def count_year(df):
    masters_count = df['School Year'].value_counts()['Masters']
    alumni_count = df['School Year'].value_counts()['Alumni']
    doctorate_count = df['School Year'].value_counts()['Doctorate']
    juniors_count = df['School Year'].value_counts()['Junior']
    seniors_count = df['School Year'].value_counts()['Senior']
    grad_count=doctorate_count+masters_count
    
    total_students= df.shape[0]+1

    undergrads= total_students-masters_count-alumni_count-doctorate_count
    undergrad_perc=(undergrads/total_students)*100

    junior_perc=(juniors_count/undergrads)*100
    senior_perc=(seniors_count/undergrads)*100
    
    grad_perc=(grad_count/total_students)*100
    alumni_perc=(alumni_count/total_students)*100

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
    ecp_count = df['College'].value_counts()['ECP']

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



def execute():
    df=read_data("04_12_23_Career Fair_Student Raw Data_37526")
    count_year(df)
    count_school(df)


execute()