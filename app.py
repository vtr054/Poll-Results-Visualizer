import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

# Page Config
st.set_page_config(page_title="Poll Results Visualizer", layout="wide", page_icon="📊")

# Custom CSS for Premium Look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
        color: #1e3a8a;
    }
    </style>
    """, unsafe_allow_html=True)

# Load Data
@st.cache_data
def get_data():
    file_path = 'data/cleaned_survey_data.csv'
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        return df
    return None

df = get_data()

if df is not None:
    # Sidebar Filters
    st.sidebar.title("🔍 Filters")
    st.sidebar.markdown("Refine your analysis by selecting demographics.")
    
    region_filter = st.sidebar.multiselect("Select Region", options=df['Region'].unique(), default=df['Region'].unique())
    age_filter = st.sidebar.multiselect("Select Age Group", options=df['Age_Group'].unique(), default=df['Age_Group'].unique())
    gender_filter = st.sidebar.multiselect("Select Gender", options=df['Gender'].unique(), default=df['Gender'].unique())
    
    # Apply Filters
    filtered_df = df[
        (df['Region'].isin(region_filter)) &
        (df['Age_Group'].isin(age_filter)) &
        (df['Gender'].isin(gender_filter))
    ]

    # Header
    st.title("📊 Poll Results Visualizer")
    st.markdown(f"**Analyzing {len(filtered_df)} responses** across various demographics.")
    
    # KPI Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Responses", len(filtered_df))
    with col2:
        avg_sat = filtered_df['Satisfaction_Score'].mean()
        st.metric("Avg Satisfaction", f"{avg_sat:.2f}/5.0")
    with col3:
        # NPS Calculation: %Promoters - %Detractors
        nps_counts = filtered_df['NPS_Category'].value_counts(normalize=True) * 100
        nps_score = nps_counts.get('Promoter', 0) - nps_counts.get('Detractor', 0)
        st.metric("Net Promoter Score (NPS)", f"{nps_score:.1f}")
    with col4:
        top_feature = filtered_df['Most_Used_Feature'].mode()[0]
        st.metric("Top Feature", top_feature)

    # Main Dashboard Area
    tab1, tab2, tab3 = st.tabs(["📈 Quantitative Insights", "💬 Qualitative Analysis", "📋 Raw Data"])

    with tab1:
        st.subheader("Satisfaction & Usage Trends")
        c1, c2 = st.columns(2)
        
        with c1:
            # Satisfaction by Device (Interactive Plotly)
            fig_device = px.box(filtered_df, x='Primary_Device', y='Satisfaction_Score', 
                                title="Satisfaction Distribution by Device",
                                color='Primary_Device', template='plotly_white')
            st.plotly_chart(fig_device, use_container_width=True)
            
        with c2:
            # Satisfaction Score Histogram
            fig_sat = px.histogram(filtered_df, x='Satisfaction_Score', nbins=5,
                                   title="Satisfaction Score Frequency",
                                   color_discrete_sequence=['#4299E1'], template='plotly_white')
            st.plotly_chart(fig_sat, use_container_width=True)

        # Region-wise breakdown
        fig_region = px.bar(filtered_df.groupby('Region')['Satisfaction_Score'].mean().reset_index(),
                            x='Region', y='Satisfaction_Score',
                            title="Average Satisfaction by Region",
                            color='Satisfaction_Score', color_continuous_scale='Viridis',
                            template='plotly_white')
        st.plotly_chart(fig_region, use_container_width=True)

    with tab2:
        st.subheader("Feedback & Sentiment Analysis")
        col_fb1, col_fb2 = st.columns([2, 1])
        
        with col_fb1:
            # Word Cloud
            text = " ".join(filtered_df['Feedback_Text'].astype(str))
            if text:
                wordcloud = WordCloud(width=800, height=400, background_color='white', 
                                     colormap='Blues', max_words=100).generate(text)
                
                fig, ax = plt.subplots(figsize=(10, 5))
                ax.imshow(wordcloud, interpolation='bilinear')
                ax.axis('off')
                st.pyplot(fig)
            else:
                st.info("No feedback text available for the selected filters.")
        
        with col_fb2:
            # Sentiment Pie Chart
            sentiment_counts = filtered_df['Sentiment'].value_counts()
            fig_sent = px.pie(values=sentiment_counts.values, names=sentiment_counts.index, 
                              title="Overall Sentiment Distribution",
                              color_discrete_sequence=px.colors.qualitative.Pastel)
            st.plotly_chart(fig_sent, use_container_width=True)

    with tab3:
        st.subheader("Raw Survey Responses")
        st.dataframe(filtered_df, use_container_width=True)
        
        # Download Button
        csv = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Filtered Data as CSV",
            data=csv,
            file_name='filtered_poll_results.csv',
            mime='text/csv',
        )

else:
    st.error("Data not found. Please run the data generator and processor scripts first.")
    st.code("python scripts/data_generator.py\npython scripts/data_processor.py")

# Footer
st.divider()
st.markdown("Developed by **Antigravity AI** | Data Science Portfolio Project")
