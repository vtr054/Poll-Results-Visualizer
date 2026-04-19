import pandas as pd
import numpy as np
import os

def process_survey_data(input_path='data/raw_survey_data.csv'):
    """Cleans and processes raw survey data for analysis."""
    
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return
    
    df = pd.read_csv(input_path)
    print("Pre-cleaning analysis:")
    print(df.isnull().sum())

    # 1. Data Cleaning
    # Fill missing Age with median
    df['Age'] = df['Age'].fillna(df['Age'].median())
    
    # Fill missing Satisfaction Score with mode (most frequent)
    mode_sat = df['Satisfaction_Score'].mode()[0]
    df['Satisfaction_Score'] = df['Satisfaction_Score'].fillna(mode_sat)
    
    # 2. Feature Engineering
    # Age Groups
    bins = [18, 30, 50, 100]
    labels = ['18-30 (Youth)', '31-50 (Adult)', '51+ (Senior)']
    df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
    
    # NPS Classification
    # 0-6: Detractor, 7-8: Passive, 9-10: Promoter
    def classify_nps(score):
        if score >= 9: return 'Promoter'
        if score >= 7: return 'Passive'
        return 'Detractor'
    
    df['NPS_Category'] = df['NPS_Score'].apply(classify_nps)
    
    # Simple Sentiment Analysis based on keywords (for the processing phase)
    def simple_sentiment(text):
        pos_words = ['love', 'best', 'good', 'solid', 'excellent', 'great', 'intuitive']
        neg_words = ['terrible', 'waste', 'broken', 'frustrated', 'confusing', 'glitch', 'slow']
        
        text_lower = str(text).lower()
        if any(word in text_lower for word in pos_words):
            return 'Positive'
        if any(word in text_lower for word in neg_words):
            return 'Negative'
        return 'Neutral'
    
    df['Sentiment'] = df['Feedback_Text'].apply(simple_sentiment)
    
    # 3. Aggregations (Example: Satisfaction by Region)
    avg_sat_by_region = df.groupby('Region')['Satisfaction_Score'].mean().reset_index()
    avg_sat_by_region.columns = ['Region', 'Avg_Satisfaction']
    
    # 4. Save Cleaned Data
    output_path = 'data/cleaned_survey_data.csv'
    df.to_csv(output_path, index=False)
    
    # Save a summary report
    report_path = 'outputs/reports/data_summary.txt'
    with open(report_path, 'w') as f:
        f.write("Poll Results Visualization - Data Processing Summary\n")
        f.write("====================================================\n")
        f.write(f"Total Responses: {len(df)}\n")
        f.write(f"Processing Date: {pd.Timestamp.now()}\n\n")
        f.write("Average Satisfaction Score by Region:\n")
        f.write(avg_sat_by_region.to_string(index=False))
        f.write("\n\nNPS Distribution:\n")
        f.write(df['NPS_Category'].value_counts(normalize=True).to_string())
        
    print(f"Data processing complete. Cleaned data saved to: {output_path}")
    print(f"Summary report saved to: {report_path}")
    return df

if __name__ == "__main__":
    process_survey_data()
