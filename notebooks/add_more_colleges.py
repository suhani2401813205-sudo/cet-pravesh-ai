import pandas as pd

df = pd.read_csv('./data/colleges.csv')
print(f"Current rows: {len(df)}")

# More Mumbai/Navi Mumbai colleges with lower cutoffs
new_colleges = [
    # Mumbai
    ["SAKEC Mumbai", "Computer Engineering", "Mumbai", 88.5, 88.9, 89.3, 89.7, 175000, 520000, "No", 3.8],
    ["SAKEC Mumbai", "Information Technology", "Mumbai", 86.2, 86.6, 87.0, 87.4, 175000, 490000, "No", 3.8],
    ["SAKEC Mumbai", "Electronics & Telecom", "Mumbai", 82.1, 82.5, 82.9, 83.3, 175000, 460000, "No", 3.8],
    ["Fr CRCE Mumbai", "Computer Engineering", "Mumbai", 90.5, 90.9, 91.3, 91.7, 210000, 560000, "No", 4.0],
    ["Fr CRCE Mumbai", "Information Technology", "Mumbai", 88.3, 88.7, 89.1, 89.5, 210000, 530000, "No", 4.0],
    ["Fr CRCE Mumbai", "Electronics & Telecom", "Mumbai", 84.2, 84.6, 85.0, 85.4, 210000, 490000, "No", 4.0],
    ["Fr CRCE Mumbai", "Mechanical Engineering", "Mumbai", 78.5, 78.9, 79.3, 79.7, 210000, 420000, "No", 4.0],
    ["Atharva Mumbai", "Computer Engineering", "Mumbai", 85.3, 85.7, 86.1, 86.5, 155000, 470000, "No", 3.7],
    ["Atharva Mumbai", "Information Technology", "Mumbai", 83.1, 83.5, 83.9, 84.3, 155000, 450000, "No", 3.7],
    ["Atharva Mumbai", "Electronics & Telecom", "Mumbai", 79.4, 79.8, 80.2, 80.6, 155000, 420000, "No", 3.7],
    ["Thadomal Shahani Mumbai", "Computer Engineering", "Mumbai", 91.2, 91.6, 92.0, 92.4, 195000, 580000, "No", 4.1],
    ["Thadomal Shahani Mumbai", "Information Technology", "Mumbai", 89.1, 89.5, 89.9, 90.3, 195000, 550000, "No", 4.1],
    ["Thadomal Shahani Mumbai", "Electronics & Telecom", "Mumbai", 85.3, 85.7, 86.1, 86.5, 195000, 500000, "No", 4.1],
    ["KJSCE Mumbai", "Computer Engineering", "Mumbai", 87.4, 87.8, 88.2, 88.6, 230000, 510000, "No", 3.9],
    ["KJSCE Mumbai", "Information Technology", "Mumbai", 85.2, 85.6, 86.0, 86.4, 230000, 490000, "No", 3.9],
    ["KJSCE Mumbai", "Electronics & Telecom", "Mumbai", 81.3, 81.7, 82.1, 82.5, 230000, 460000, "No", 3.9],
    ["KJSCE Mumbai", "Mechanical Engineering", "Mumbai", 75.6, 76.0, 76.4, 76.8, 230000, 400000, "No", 3.9],
    ["DYPE Mumbai", "Computer Engineering", "Mumbai", 83.5, 83.9, 84.3, 84.7, 145000, 450000, "No", 3.6],
    ["DYPE Mumbai", "Information Technology", "Mumbai", 81.2, 81.6, 82.0, 82.4, 145000, 430000, "No", 3.6],
    ["DYPE Mumbai", "Mechanical Engineering", "Mumbai", 72.3, 72.7, 73.1, 73.5, 145000, 380000, "No", 3.6],
    # Navi Mumbai
    ["RAIT Navi Mumbai", "Computer Engineering", "Navi Mumbai", 89.5, 89.9, 90.3, 90.7, 165000, 530000, "No", 4.0],
    ["RAIT Navi Mumbai", "Information Technology", "Navi Mumbai", 87.3, 87.7, 88.1, 88.5, 165000, 500000, "No", 4.0],
    ["RAIT Navi Mumbai", "Electronics & Telecom", "Navi Mumbai", 83.1, 83.5, 83.9, 84.3, 165000, 460000, "No", 4.0],
    ["RAIT Navi Mumbai", "Mechanical Engineering", "Navi Mumbai", 77.4, 77.8, 78.2, 78.6, 165000, 410000, "No", 4.0],
    ["MGM Navi Mumbai", "Computer Engineering", "Navi Mumbai", 85.2, 85.6, 86.0, 86.4, 170000, 470000, "Yes", 3.8],
    ["MGM Navi Mumbai", "Information Technology", "Navi Mumbai", 83.1, 83.5, 83.9, 84.3, 170000, 450000, "Yes", 3.8],
    ["MGM Navi Mumbai", "Mechanical Engineering", "Navi Mumbai", 74.5, 74.9, 75.3, 75.7, 170000, 390000, "Yes", 3.8],
    ["SIES Navi Mumbai", "Computer Engineering", "Navi Mumbai", 84.3, 84.7, 85.1, 85.5, 175000, 460000, "No", 3.8],
    ["SIES Navi Mumbai", "Information Technology", "Navi Mumbai", 82.1, 82.5, 82.9, 83.3, 175000, 440000, "No", 3.8],
    # Thane
    ["VESIT Thane", "Computer Engineering", "Thane", 87.2, 87.6, 88.0, 88.4, 185000, 500000, "No", 3.9],
    ["VESIT Thane", "Information Technology", "Thane", 85.1, 85.5, 85.9, 86.3, 185000, 480000, "No", 3.9],
    ["VESIT Thane", "Electronics & Telecom", "Thane", 81.3, 81.7, 82.1, 82.5, 185000, 450000, "No", 3.9],
    ["Rajiv Gandhi Thane", "Computer Engineering", "Thane", 83.4, 83.8, 84.2, 84.6, 155000, 450000, "No", 3.7],
    ["Rajiv Gandhi Thane", "Information Technology", "Thane", 81.2, 81.6, 82.0, 82.4, 155000, 430000, "No", 3.7],
    ["Rajiv Gandhi Thane", "Mechanical Engineering", "Thane", 72.1, 72.5, 72.9, 73.3, 155000, 380000, "No", 3.7],
]

cols = ['college_name','branch','city','cutoff_2022','cutoff_2023',
        'cutoff_2024','cutoff_2025','fees','avg_package','hostel','rating']

df_new = pd.DataFrame(new_colleges, columns=cols)
df_final = pd.concat([df, df_new], ignore_index=True)

print(f"New total rows: {len(df_final)}")
print(f"Cities: {df_final['city'].value_counts().to_dict()}")

df_final.to_csv('./data/colleges.csv', index=False)
print("colleges.csv updated!")