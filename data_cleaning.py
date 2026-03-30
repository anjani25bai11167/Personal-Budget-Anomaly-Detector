import pandas as pd

def load_and_clean_data(filepath):
    print(f"Loading data from {filepath}...")
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date').reset_index(drop=True)
    
    df['Day_of_Week'] = df['Date'].dt.dayofweek 
    df['Is_Weekend'] = df['Day_of_Week'].apply(lambda x: 1 if x >= 5 else 0)
    
    df['Category_Code'] = df['Category'].astype('category').cat.codes   
    print("Data cleaned and features engineered successfully.")
    return df