# Personal Budget Anomaly Detector 💸

## Project Overview
Managing daily expenses as a student—from hostel essentials and campus kiosk snacks to online software subscriptions—can easily become disorganized. Traditional banking apps provide a balance, but they do not automatically flag out-of-character spending based on personal habits. 

This project is an **AI-powered anomaly detection tool** built for the AI Fundamentals course. It analyzes personal transaction history to automatically flag unusual spending behavior, such as accidental UPI double-charges, hidden subscription auto-renewals, or uncharacteristic spending spikes. 

It prioritizes privacy by running entirely locally, ensuring no personal financial data is uploaded to the cloud.

## 🧠 Technical Approach & Methodology
This project deliberately avoids overly complex deep learning models in favor of foundational, highly interpretable machine learning techniques suitable for tabular data.

1. **Feature Engineering: Raw transaction amounts aren't enough to define an anomaly. The pipeline extracts time-based context from the transaction date (`Day_of_Week`, `Is_Weekend`). A ₹150 late-night food charge might be normal on a Saturday, but highly anomalous on a Tuesday morning.
2. **The AI Model (Isolation Forest):** The core engine utilizes Scikit-Learn's `Isolation Forest` algorithm. Instead of trying to model "normal" behavior, it explicitly isolates anomalies by randomly partitioning the data features. Outliers (anomalies) are isolated closer to the root of the decision trees, making them easy to flag.
3. **Data Visualization:** The results are rendered using Matplotlib and Seaborn, creating a clear chronological scatter plot where anomalies are distinctly highlighted for user review.

## 📂 Repository Structure
The project follows a modular, professional architecture separating data processing, modeling, and visualization.

```text
personal-budget-anomaly-detector/
│
├── data/
│   ├── raw_transactions_dummy.csv          # Sample dataset for immediate testing
│
├── notebooks/
│   └── exploratory_data_analysis.ipynb     # Jupyter notebook detailing initial data exploration
│
├── src/
│   ├── data_cleaning.py                    # Handles date parsing and feature engineering
│   ├── anomaly_model.py                    # Contains the Isolation Forest ML logic
│   └── visualizer.py                       # Generates the analytical scatter plots
│
├── main.py                                 # Master script to execute the pipeline
├── requirements.txt                        # Project dependencies
└── README.md                               # Project documentation