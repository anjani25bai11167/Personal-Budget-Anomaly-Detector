from src.data_cleaning import load_and_clean_data
from src.anomaly_model import detect_anomalies
from src.visualizer import plot_anomalies

def main():
    data_path = 'data/raw_transactions_dummy.csv'    
    try:
        df = load_and_clean_data(data_path)
        df_analyzed = detect_anomalies(df, contamination=0.04) 
        print("\n--- ANOMALY REPORT ---")
        anomalies = df_analyzed[df_analyzed['Is_Anomaly'] == True]
        
        if not anomalies.empty:
            print(anomalies[['Date', 'Description', 'Category', 'Amount']])
        else:
            print("No anomalies detected in this dataset.")
            
        print("----------------------\n")
        

        plot_anomalies(df_analyzed)
        
    except FileNotFoundError:
        print(f"Error: Could not find the file at {data_path}.")
        print("Please ensure the 'data' folder exists and contains your CSV.")

if __name__ == "__main__":
    main()