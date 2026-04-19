import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def generate_synthetic_data(num_responses=500):
    """Generates a synthetic dataset for a Product Satisfaction Survey."""
    
    np.random.seed(42)
    
    # 1. Base Demographics
    regions = ['North America', 'Europe', 'Asia-Pacific', 'Latin America', 'ME-Africa']
    genders = ['Male', 'Female', 'Non-Binary', 'Prefer not to say']
    devices = ['Mobile', 'Desktop', 'Tablet', 'Smart Watch']
    usage_freq = ['Daily', 'Weekly', 'Monthly', 'Rarely']
    features = ['User Interface', 'Performance', 'Customer Support', 'Pricing', 'Feature Set']
    
    data = {
        'Response_ID': [f'RES_{i:04d}' for i in range(1, num_responses + 1)],
        'Timestamp': [datetime.now() - timedelta(days=np.random.randint(0, 30), 
                                                hours=np.random.randint(0, 24)) for _ in range(num_responses)],
        'Age': np.random.randint(18, 75, size=num_responses),
        'Gender': np.random.choice(genders, size=num_responses, p=[0.45, 0.45, 0.05, 0.05]),
        'Region': np.random.choice(regions, size=num_responses),
        'Education_Level': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], size=num_responses),
        'Satisfaction_Score': np.random.choice([1, 2, 3, 4, 5], size=num_responses, p=[0.05, 0.1, 0.2, 0.4, 0.25]),
        'NPS_Score': np.random.randint(0, 11, size=num_responses),
        'Primary_Device': np.random.choice(devices, size=num_responses),
        'Usage_Frequency': np.random.choice(usage_freq, size=num_responses),
        'Most_Used_Feature': np.random.choice(features, size=num_responses),
    }

    # Generate synthetic feedback based on satisfaction score
    feedback_options = {
        5: ["Love the interface, very intuitive!", "Best app I've used this year.", "Exceeded my expectations.", "Highly recommended."],
        4: ["Good experience overall.", "Works well but interface could be cleaner.", "Solid performance.", "Decent features for the price."],
        3: ["It's okay, does what it needs to do.", "Average experience.", "Some bugs but manageable.", "Needs more updates."],
        2: ["A bit frustrated with the glitches.", "Interface is confusing.", "Slow performance at times.", "Expected more."],
        1: ["Terrible experience.", "Waste of money.", "Completely broken.", "Customer support was unhelpful."]
    }

    data['Feedback_Text'] = [np.random.choice(feedback_options[score]) for score in data['Satisfaction_Score']]

    # Introduce some "raw" data issues (Missing values to be cleaned later)
    df = pd.DataFrame(data)
    
    # Introduce ~5% missing values in Satisfaction_Score and Age for cleaning demonstration
    null_indices_age = np.random.choice(df.index, size=int(num_responses * 0.05), replace=False)
    null_indices_sat = np.random.choice(df.index, size=int(num_responses * 0.03), replace=False)
    
    df.loc[null_indices_age, 'Age'] = np.nan
    df.loc[null_indices_sat, 'Satisfaction_Score'] = np.nan
    
    # Save to data folder
    os.makedirs('data', exist_ok=True)
    file_path = 'data/raw_survey_data.csv'
    df.to_csv(file_path, index=False)
    print(f"Synthetic data generated successfully: {file_path}")
    return df

if __name__ == "__main__":
    generate_synthetic_data()
