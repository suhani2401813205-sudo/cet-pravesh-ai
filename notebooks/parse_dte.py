import pdfplumber
import pandas as pd
import re

def extract_college_data(pdf_path):
    results = []
    
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"
    
    # College blocks split karo
    college_blocks = re.split(r'\d{5} - ', full_text)
    
    for block in college_blocks:
        if not block.strip():
            continue
            
        lines = block.strip().split('\n')
        college_name = lines[0].strip()
        
        # Branch blocks
        branch_pattern = r'\d{10} - (.+?)(?:\n|Status)'
        branches = re.findall(branch_pattern, block)
        
        # GOPENS percentile
        gopens_pattern = r'I\s+\d+\s*\((\d+\.\d+)\)'
        gopens_matches = re.findall(gopens_pattern, block)
        
        for i, branch in enumerate(branches):
            if i < len(gopens_matches):
                results.append({
                    'college_name': college_name[:60],
                    'branch': branch.strip(),
                    'cutoff_2025': float(gopens_matches[i])
                })
    
    return results

# Run
pdf_path = r"C:\Users\joysh\Desktop\2025cutoff.pdf"
print("PDF reading...")

data = extract_college_data(pdf_path)
df = pd.DataFrame(data)

print(f"Total rows extracted: {len(df)}")
print(df.head(20))

df.to_csv("./data/dte_extracted.csv", index=False)
print("CSV saved on Desktop!")