import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_visualizations(input_path='data/cleaned_survey_data.csv'):
    """Generates and saves visualizations from cleaned survey data."""
    
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return
        
    df = pd.read_csv(input_path)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    # Set styling
    sns.set_theme(style="whitegrid")
    
    # Prepare charts directory
    os.makedirs('outputs/charts', exist_ok=True)
    
    # 1. Bar Chart: Satisfaction Score Distribution
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Satisfaction_Score', data=df, hue='Satisfaction_Score', palette='viridis', legend=False)
    plt.title('Distribution of Satisfaction Scores')
    plt.xlabel('Satisfaction Score (1-5)')
    plt.ylabel('Count')
    plt.savefig('outputs/charts/satisfaction_distribution.png')
    plt.close()
    
    # 2. Pie Chart: Region-wise Responses
    plt.figure(figsize=(8, 8))
    df['Region'].value_counts().plot.pie(autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Response Distribution by Region')
    plt.ylabel('')
    plt.savefig('outputs/charts/region_distribution.png')
    plt.close()
    
    # 3. Histogram: Age Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Age'], bins=15, kde=True, color='skyblue')
    plt.title('Age Distribution of Respondents')
    plt.savefig('outputs/charts/age_distribution.png')
    plt.close()
    
    # 4. Line Chart: Response Trends over Time
    # Group by date
    df['Date'] = df['Timestamp'].dt.date
    trends = df.groupby('Date').size().reset_index(name='Responses')
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Date', y='Responses', data=trends, marker='o', color='coral')
    plt.title('Daily Response Trends')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('outputs/charts/response_trends.png')
    plt.close()
    
    # 5. Stacked Bar: NPS Categories by Region
    nps_pivot = df.groupby(['Region', 'NPS_Category']).size().unstack(fill_value=0)
    # Normalize to get percentages
    nps_pct = nps_pivot.div(nps_pivot.sum(axis=1), axis=0) * 100
    
    nps_pct.plot(kind='bar', stacked=True, figsize=(12, 7), color=['#ff9999','#66b3ff','#99ff99'])
    plt.title('NPS Category Distribution by Region (%)')
    plt.ylabel('Percentage')
    plt.legend(title='NPS Category', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('outputs/charts/nps_by_region.png')
    plt.close()
    
    print("Static visualizations generated and saved to outputs/charts/")

if __name__ == "__main__":
    create_visualizations()
