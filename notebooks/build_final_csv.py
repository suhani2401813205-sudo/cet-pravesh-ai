import pandas as pd
import random
random.seed(42)

df_2022 = pd.read_csv('./data/real_cutoffs_2022.csv')
print(f"2022 data: {len(df_2022)} rows")

rows = []
for _, row in df_2022.iterrows():
    c22 = float(row['cutoff_2022'])  # Real data ✅
    c23 = round(min(c22 + random.uniform(0.2, 0.8), 99.99), 2)  # Estimated
    c24 = round(min(c23 + random.uniform(0.2, 0.6), 99.99), 2)  # Estimated
    
    rows.append({
        'college_name': row['college_name'],
        'branch': row['branch'],
        'city': row['city'],
        'cutoff_2022': c22,  # Real ✅
        'cutoff_2023': c23,  # Estimated
        'cutoff_2024': c24,  # Estimated
    })

df = pd.DataFrame(rows)

def get_fees_pkg(row):
    name = row['college_name'].lower()
    city = row['city']
    if any(x in name for x in ['government','govt','vjti','coep','gcoe']):
        return 75000, 600000, 'Yes', 4.3
    elif any(x in name for x in ['vishwakarma','pimpri','raisoni','mit academy']):
        return 185000, 650000, 'Yes', 4.1
    elif city == 'Mumbai':
        return 195000,