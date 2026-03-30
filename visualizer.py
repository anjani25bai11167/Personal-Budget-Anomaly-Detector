import matplotlib.pyplot as plt
import seaborn as sns

def plot_anomalies(df):
    print("Generating visualization...")
    
    plt.figure(figsize=(12, 6))
    sns.set_theme(style="whitegrid")

    normal_tx = df[df['Is_Anomaly'] == False]
    plt.scatter(normal_tx['Date'], normal_tx['Amount'], 
                color='blue', label='Normal', alpha=0.6, s=50)
    
    anomaly_tx = df[df['Is_Anomaly'] == True]
    plt.scatter(anomaly_tx['Date'], anomaly_tx['Amount'], 
                color='red', label='Anomaly', alpha=0.9, s=100, edgecolor='black')
    plt.title('Personal Budget Anomaly Detection', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Transaction Amount (INR)', fontsize=12)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()