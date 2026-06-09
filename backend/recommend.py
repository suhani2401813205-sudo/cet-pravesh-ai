import pandas as pd
import json
import sys

# Data load karo
df = pd.read_csv('./data/colleges.csv')

def get_recommendations(percentile, branch, 
                         city=None, max_fees=None, 
                         priority='placement'):
    
    filtered = df[df['branch'] == branch].copy()
    filtered = filtered[filtered['cutoff_2023'] <= percentile]
    
    if city:
        filtered = filtered[filtered['city'] == city]
    if max_fees:
        filtered = filtered[filtered['fees'] <= max_fees]
    
    if filtered.empty:
        return {"error": "No colleges found — try different criteria"}
    
    filtered['score_placement'] = filtered['avg_package'] / filtered['avg_package'].max()
    filtered['score_rating']    = filtered['rating'] / filtered['rating'].max()
    filtered['score_fees']      = 1 - (filtered['fees'] / filtered['fees'].max())
    
    if priority == 'placement':
        w1, w2, w3 = 0.5, 0.3, 0.2
    elif priority == 'fees':
        w1, w2, w3 = 0.2, 0.3, 0.5
    else:
        w1, w2, w3 = 0.33, 0.34, 0.33
    
    filtered['final_score'] = (
        w1 * filtered['score_placement'] +
        w2 * filtered['score_rating'] +
        w3 * filtered['score_fees']
    )
    
    filtered = filtered.sort_values('final_score', ascending=False)
    
    result = []
    for _, row in filtered.iterrows():
        result.append({
            "college_name": row['college_name'],
            "branch": row['branch'],
            "city": row['city'],
            "cutoff_2023": row['cutoff_2023'],
            "fees": int(row['fees']),
            "avg_package": int(row['avg_package']),
            "rating": row['rating'],
            "score": round(row['final_score'], 2)
        })
    
    return result

# Command line se arguments lo
if __name__ == "__main__":
    percentile = float(sys.argv[1])
    branch     = sys.argv[2]
    city       = sys.argv[3] if len(sys.argv) > 3 else None
    max_fees   = max_fees = int(sys.argv[4]) if len(sys.argv) > 4 and sys.argv[4] != '' else None
    priority   = sys.argv[5] if len(sys.argv) > 5 else 'placement'
    
    result = get_recommendations(percentile, branch, city, max_fees, priority)
    print(json.dumps(result))