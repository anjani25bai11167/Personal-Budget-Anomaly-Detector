from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(df, contamination=0.05):
    print("Training Isolation Forest model...")
    features = ['Amount', 'Category_Code', 'Day_of_Week', 'Is_Weekend']
    X = df[features] 
    model = IsolationForest(contamination=contamination, random_state=42)

    df['Anomaly_Score'] = model.fit_predict(X)
    df['Is_Anomaly'] = df['Anomaly_Score'] == -1
    df = df.drop(columns=['Anomaly_Score'])
    
    anomalies_count = df['Is_Anomaly'].sum()
    print(f"Model complete. Found {anomalies_count} anomalies.")
   
    return df