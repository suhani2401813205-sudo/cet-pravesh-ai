import pandas as pd

df = pd.read_csv('./data/kaggle_sw_raw.csv')
print("Total rows:", len(df))

# Filter — MHT-CET aur GOPENS only
filtered = df[
    (df['score_type'] == 'MHT-CET') &
    (df['seat_type'] == 'GOPENS')
].copy()

print(f"After filter: {len(filtered)} rows")

# Har college + branch ke liye MAX percentile
cutoffs = filtered.groupby(['college_name', 'branch'])['percentile'].max().reset_index()
cutoffs.columns = ['college_name', 'branch', 'cutoff_2022']
cutoffs['cutoff_2022'] = cutoffs['cutoff_2022'].round(2)

# City extract
def get_city(name):
    name = name.lower()
    if any(x in name for x in ['mumbai','matunga','andheri','bandra','chembur','kandivali','malad','wadala','vidyavihar','vile parle','borivali','goregaon']):
        return 'Mumbai'
    elif any(x in name for x in ['navi mumbai','nerul','panvel','kharghar','airoli']):
        return 'Navi Mumbai'
    elif any(x in name for x in ['thane','kalyan','dombivli']):
        return 'Thane'
    elif any(x in name for x in ['pune','pimpri','chinchwad','sinhgad']):
        return 'Pune'
    elif 'nagpur' in name:
        return 'Nagpur'
    elif 'nashik' in name:
        return 'Nashik'
    elif any(x in name for x in ['aurangabad','sambhajinagar']):
        return 'Aurangabad'
    elif 'kolhapur' in name:
        return 'Kolhapur'
    else:
        return 'Other'

cutoffs['city'] = cutoffs['college_name'].apply(get_city)

# Branch standardize
branch_map = {
    'Computer Engineering': 'Computer Engineering',
    'Computer Science and Engineering': 'Computer Engineering',
    'Computer Science and Engineering(Artificial Intelligence and Machine Learning)': 'AIML',
    'Computer Science and Engineering(Data Science)': 'AIDS',
    'Computer Science and Engineering(Artificial Intelligence)': 'AIDS',
    'Artificial Intelligence and Data Science': 'AIDS',
    'Artificial Intelligence and Machine Learning': 'AIML',
    'Information Technology': 'Information Technology',
    'Mechanical Engineering': 'Mechanical Engineering',
    'Civil Engineering': 'Civil Engineering',
    'Electrical Engineering': 'Electrical Engineering',
    'Electronics and Telecommunication Engineering': 'Electronics & Telecom',
    'Electronics Engineering': 'Electronics & Telecom',
    'Electronics & Telecommunication Engineering': 'Electronics & Telecom',
}

cutoffs['branch'] = cutoffs['branch'].map(branch_map)
cutoffs = cutoffs[cutoffs['branch'].notna()]
cutoffs = cutoffs[cutoffs['city'] != 'Other']

cutoffs = cutoffs.sort_values(['city','college_name','branch'])

print(f"\nFinal rows: {len(cutoffs)}")
print(cutoffs.head(20))

cutoffs.to_csv('./data/real_cutoffs_2022.csv', index=False)
print("\nSaved! data/real_cutoffs_2022.csv")