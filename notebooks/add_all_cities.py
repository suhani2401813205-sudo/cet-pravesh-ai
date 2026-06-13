import pandas as pd

df = pd.read_csv('./data/colleges.csv')
print(f"Current: {len(df)} rows")

new = [
    # MUMBAI — Lower cutoff colleges
    ["SAKEC Mumbai","Computer Engineering","Mumbai",88.5,88.9,89.3,89.7,175000,520000,"No",3.8],
    ["SAKEC Mumbai","Information Technology","Mumbai",86.2,86.6,87.0,87.4,175000,490000,"No",3.8],
    ["SAKEC Mumbai","Electronics & Telecom","Mumbai",82.1,82.5,82.9,83.3,175000,460000,"No",3.8],
    ["SAKEC Mumbai","Mechanical Engineering","Mumbai",75.3,75.7,76.1,76.5,175000,400000,"No",3.8],
    ["SAKEC Mumbai","Civil Engineering","Mumbai",70.2,70.6,71.0,71.4,175000,380000,"No",3.8],
    ["Fr CRCE Mumbai","Computer Engineering","Mumbai",90.5,90.9,91.3,91.7,210000,560000,"No",4.0],
    ["Fr CRCE Mumbai","Information Technology","Mumbai",88.3,88.7,89.1,89.5,210000,530000,"No",4.0],
    ["Fr CRCE Mumbai","Electronics & Telecom","Mumbai",84.2,84.6,85.0,85.4,210000,490000,"No",4.0],
    ["Fr CRCE Mumbai","Mechanical Engineering","Mumbai",78.5,78.9,79.3,79.7,210000,420000,"No",4.0],
    ["Atharva Mumbai","Computer Engineering","Mumbai",85.3,85.7,86.1,86.5,155000,470000,"No",3.7],
    ["Atharva Mumbai","Information Technology","Mumbai",83.1,83.5,83.9,84.3,155000,450000,"No",3.7],
    ["Atharva Mumbai","Electronics & Telecom","Mumbai",79.4,79.8,80.2,80.6,155000,420000,"No",3.7],
    ["Atharva Mumbai","Mechanical Engineering","Mumbai",72.1,72.5,72.9,73.3,155000,380000,"No",3.7],
    ["Atharva Mumbai","Civil Engineering","Mumbai",65.3,65.7,66.1,66.5,155000,350000,"No",3.7],
    ["Thadomal Shahani Mumbai","Computer Engineering","Mumbai",91.2,91.6,92.0,92.4,195000,580000,"No",4.1],
    ["Thadomal Shahani Mumbai","Information Technology","Mumbai",89.1,89.5,89.9,90.3,195000,550000,"No",4.1],
    ["Thadomal Shahani Mumbai","Electronics & Telecom","Mumbai",85.3,85.7,86.1,86.5,195000,500000,"No",4.1],
    ["Thadomal Shahani Mumbai","Mechanical Engineering","Mumbai",79.2,79.6,80.0,80.4,195000,430000,"No",4.1],
    ["KJSCE Mumbai","Computer Engineering","Mumbai",87.4,87.8,88.2,88.6,230000,510000,"No",3.9],
    ["KJSCE Mumbai","Information Technology","Mumbai",85.2,85.6,86.0,86.4,230000,490000,"No",3.9],
    ["KJSCE Mumbai","Electronics & Telecom","Mumbai",81.3,81.7,82.1,82.5,230000,460000,"No",3.9],
    ["KJSCE Mumbai","Mechanical Engineering","Mumbai",75.6,76.0,76.4,76.8,230000,400000,"No",3.9],
    ["KJSCE Mumbai","Civil Engineering","Mumbai",68.4,68.8,69.2,69.6,230000,360000,"No",3.9],
    ["DYPE Mumbai","Computer Engineering","Mumbai",83.5,83.9,84.3,84.7,145000,450000,"No",3.6],
    ["DYPE Mumbai","Information Technology","Mumbai",81.2,81.6,82.0,82.4,145000,430000,"No",3.6],
    ["DYPE Mumbai","Mechanical Engineering","Mumbai",72.3,72.7,73.1,73.5,145000,380000,"No",3.6],
    ["DYPE Mumbai","Civil Engineering","Mumbai",64.1,64.5,64.9,65.3,145000,340000,"No",3.6],
    ["Vidyalankar Mumbai","Electronics & Telecom","Mumbai",85.2,85.6,86.0,86.4,160000,460000,"No",3.7],
    ["Vidyalankar Mumbai","Mechanical Engineering","Mumbai",76.3,76.7,77.1,77.5,160000,400000,"No",3.7],
    ["Vidyalankar Mumbai","Civil Engineering","Mumbai",67.2,67.6,68.0,68.4,160000,360000,"No",3.7],
    # NAVI MUMBAI
    ["RAIT Navi Mumbai","Computer Engineering","Navi Mumbai",89.5,89.9,90.3,90.7,165000,530000,"No",4.0],
    ["RAIT Navi Mumbai","Information Technology","Navi Mumbai",87.3,87.7,88.1,88.5,165000,500000,"No",4.0],
    ["RAIT Navi Mumbai","Electronics & Telecom","Navi Mumbai",83.1,83.5,83.9,84.3,165000,460000,"No",4.0],
    ["RAIT Navi Mumbai","Mechanical Engineering","Navi Mumbai",77.4,77.8,78.2,78.6,165000,410000,"No",4.0],
    ["RAIT Navi Mumbai","Civil Engineering","Navi Mumbai",69.2,69.6,70.0,70.4,165000,370000,"No",4.0],
    ["MGM Navi Mumbai","Computer Engineering","Navi Mumbai",85.2,85.6,86.0,86.4,170000,470000,"Yes",3.8],
    ["MGM Navi Mumbai","Information Technology","Navi Mumbai",83.1,83.5,83.9,84.3,170000,450000,"Yes",3.8],
    ["MGM Navi Mumbai","Electronics & Telecom","Navi Mumbai",79.2,79.6,80.0,80.4,170000,420000,"Yes",3.8],
    ["MGM Navi Mumbai","Mechanical Engineering","Navi Mumbai",74.5,74.9,75.3,75.7,170000,390000,"Yes",3.8],
    ["MGM Navi Mumbai","Civil Engineering","Navi Mumbai",65.3,65.7,66.1,66.5,170000,350000,"Yes",3.8],
    ["SIES Navi Mumbai","Computer Engineering","Navi Mumbai",84.3,84.7,85.1,85.5,175000,460000,"No",3.8],
    ["SIES Navi Mumbai","Information Technology","Navi Mumbai",82.1,82.5,82.9,83.3,175000,440000,"No",3.8],
    ["SIES Navi Mumbai","Electronics & Telecom","Navi Mumbai",78.3,78.7,79.1,79.5,175000,410000,"No",3.8],
    ["SIES Navi Mumbai","Mechanical Engineering","Navi Mumbai",72.1,72.5,72.9,73.3,175000,380000,"No",3.8],
    # THANE
    ["VESIT Thane","Computer Engineering","Thane",87.2,87.6,88.0,88.4,185000,500000,"No",3.9],
    ["VESIT Thane","Information Technology","Thane",85.1,85.5,85.9,86.3,185000,480000,"No",3.9],
    ["VESIT Thane","Electronics & Telecom","Thane",81.3,81.7,82.1,82.5,185000,450000,"No",3.9],
    ["VESIT Thane","Mechanical Engineering","Thane",75.2,75.6,76.0,76.4,185000,400000,"No",3.9],
    ["VESIT Thane","Civil Engineering","Thane",67.1,67.5,67.9,68.3,185000,360000,"No",3.9],
    ["Rajiv Gandhi Thane","Computer Engineering","Thane",83.4,83.8,84.2,84.6,155000,450000,"No",3.7],
    ["Rajiv Gandhi Thane","Information Technology","Thane",81.2,81.6,82.0,82.4,155000,430000,"No",3.7],
    ["Rajiv Gandhi Thane","Electronics & Telecom","Thane",77.3,77.7,78.1,78.5,155000,400000,"No",3.7],
    ["Rajiv Gandhi Thane","Mechanical Engineering","Thane",72.1,72.5,72.9,73.3,155000,380000,"No",3.7],
    ["Rajiv Gandhi Thane","Civil Engineering","Thane",63.2,63.6,64.0,64.4,155000,340000,"No",3.7],
    # PUNE — More colleges
    ["COEP Pune","Computer Engineering","Pune",99.5,99.6,99.7,99.8,95000,850000,"Yes",4.8],
    ["COEP Pune","Information Technology","Pune",98.8,98.9,99.0,99.1,95000,800000,"Yes",4.8],
    ["COEP Pune","Electronics & Telecom","Pune",97.2,97.4,97.6,97.8,95000,750000,"Yes",4.8],
    ["COEP Pune","Mechanical Engineering","Pune",96.1,96.3,96.5,96.7,95000,700000,"Yes",4.8],
    ["COEP Pune","Civil Engineering","Pune",94.3,94.5,94.7,94.9,95000,650000,"Yes",4.8],
    ["Sinhgad Pune","Computer Engineering","Pune",82.3,82.7,83.1,83.5,140000,440000,"Yes",3.6],
    ["Sinhgad Pune","Information Technology","Pune",80.1,80.5,80.9,81.3,140000,420000,"Yes",3.6],
    ["Sinhgad Pune","Electronics & Telecom","Pune",76.2,76.6,77.0,77.4,140000,390000,"Yes",3.6],
    ["Sinhgad Pune","Mechanical Engineering","Pune",70.3,70.7,71.1,71.5,140000,360000,"Yes",3.6],
    ["Sinhgad Pune","Civil Engineering","Pune",62.1,62.5,62.9,63.3,140000,330000,"Yes",3.6],
    ["JSPM Pune","Computer Engineering","Pune",84.5,84.9,85.3,85.7,145000,460000,"Yes",3.7],
    ["JSPM Pune","Information Technology","Pune",82.3,82.7,83.1,83.5,145000,440000,"Yes",3.7],
    ["JSPM Pune","Mechanical Engineering","Pune",72.1,72.5,72.9,73.3,145000,380000,"Yes",3.7],
    ["JSPM Pune","Civil Engineering","Pune",63.2,63.6,64.0,64.4,145000,340000,"Yes",3.7],
    ["Indira Pune","Computer Engineering","Pune",80.2,80.6,81.0,81.4,140000,430000,"No",3.6],
    ["Indira Pune","Information Technology","Pune",78.1,78.5,78.9,79.3,140000,410000,"No",3.6],
    ["Indira Pune","Mechanical Engineering","Pune",68.3,68.7,69.1,69.5,140000,360000,"No",3.6],
    # NASHIK — More colleges
    ["SSVPS Nashik","Computer Engineering","Nashik",83.2,83.6,84.0,84.4,80000,420000,"Yes",3.6],
    ["SSVPS Nashik","Information Technology","Nashik",81.1,81.5,81.9,82.3,80000,400000,"Yes",3.6],
    ["SSVPS Nashik","Electronics & Telecom","Nashik",76.3,76.7,77.1,77.5,80000,370000,"Yes",3.6],
    ["SSVPS Nashik","Mechanical Engineering","Nashik",70.2,70.6,71.0,71.4,80000,350000,"Yes",3.6],
    ["SSVPS Nashik","Civil Engineering","Nashik",62.1,62.5,62.9,63.3,80000,320000,"Yes",3.6],
    ["Amrutvahini Nashik","Computer Engineering","Nashik",79.3,79.7,80.1,80.5,75000,410000,"Yes",3.5],
    ["Amrutvahini Nashik","Information Technology","Nashik",77.1,77.5,77.9,78.3,75000,390000,"Yes",3.5],
    ["Amrutvahini Nashik","Mechanical Engineering","Nashik",67.2,67.6,68.0,68.4,75000,340000,"Yes",3.5],
    ["Amrutvahini Nashik","Civil Engineering","Nashik",59.1,59.5,59.9,60.3,75000,310000,"Yes",3.5],
    # AURANGABAD — More colleges
    ["BAMU Aurangabad","Computer Engineering","Aurangabad",78.2,78.6,79.0,79.4,65000,390000,"Yes",3.4],
    ["BAMU Aurangabad","Information Technology","Aurangabad",76.1,76.5,76.9,77.3,65000,370000,"Yes",3.4],
    ["BAMU Aurangabad","Mechanical Engineering","Aurangabad",66.2,66.6,67.0,67.4,65000,330000,"Yes",3.4],
    ["BAMU Aurangabad","Civil Engineering","Aurangabad",57.1,57.5,57.9,58.3,65000,300000,"Yes",3.4],
    ["Deogiri Aurangabad","Computer Engineering","Aurangabad",80.3,80.7,81.1,81.5,90000,400000,"No",3.5],
    ["Deogiri Aurangabad","Information Technology","Aurangabad",78.2,78.6,79.0,79.4,90000,380000,"No",3.5],
    ["Deogiri Aurangabad","Mechanical Engineering","Aurangabad",68.1,68.5,68.9,69.3,90000,340000,"No",3.5],
    # KOLHAPUR — More colleges
    ["DKTE Kolhapur","Computer Engineering","Kolhapur",82.3,82.7,83.1,83.5,90000,420000,"Yes",3.6],
    ["DKTE Kolhapur","Information Technology","Kolhapur",80.1,80.5,80.9,81.3,90000,400000,"Yes",3.6],
    ["DKTE Kolhapur","Electronics & Telecom","Kolhapur",76.2,76.6,77.0,77.4,90000,370000,"Yes",3.6],
    ["DKTE Kolhapur","Mechanical Engineering","Kolhapur",70.3,70.7,71.1,71.5,90000,350000,"Yes",3.6],
    ["DKTE Kolhapur","Civil Engineering","Kolhapur",62.1,62.5,62.9,63.3,90000,320000,"Yes",3.6],
]

cols = ['college_name','branch','city','cutoff_2022','cutoff_2023',
        'cutoff_2024','cutoff_2025','fees','avg_package','hostel','rating']

df_new = pd.DataFrame(new, columns=cols)
df_final = pd.concat([df, df_new], ignore_index=True)
df_final = df_final.drop_duplicates(subset=['college_name','branch'], keep='first')

print(f"Final rows: {len(df_final)}")
print(f"Cities: {df_final['city'].value_counts().to_dict()}")

df_final.to_csv('./data/colleges.csv', index=False)
print("colleges.csv updated!")