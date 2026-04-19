# Interview Preparation - Poll Results Visualizer

This document prepares you to explain this project during technical and HR interviews.

## 🧠 Technical Interview Questions (Data Science & Analyst)

1. **How did you handle missing values in the dataset?**
   - **Answer**: I identified missing values in the 'Age' and 'Satisfaction_Score' columns. I used **median imputation** for Age to avoid bias from outliers and **mode imputation** for Satisfaction_Score since it is a categorical/ordinal value.

2. **What is the difference between NPS and Satisfaction Score?**
   - **Answer**: Satisfaction Score (CSAT) measures short-term happiness with a specific interaction. **NPS (Net Promoter Score)** measures long-term loyalty and the likelihood of recommendation. NPS is calculated by subtracting %Detractors (0-6) from %Promoters (9-10).

3. **Why did you use Age Bins instead of raw Age?**
   - **Answer**: Binning continuous data like Age into categories (18-30, 31-50, etc.) makes the analysis more interpretable for business stakeholders and helps in identifying demographic-specific trends more clearly.

4. **Explain the data pipeline architecture of this project.**
   - **Answer**: It follows a modular structure: **Input** (CSV/Synthetic) -> **Processing** (pandas cleaning/feature engineering) -> **Storage** (Cleaned CSV) -> **Output** (Static PNG charts + Interactive Streamlit Dashboard).

5. **Why use Streamlit instead of a static report?**
   - **Answer**: Streamlit allows for **bi-directional interaction**. Users can filter data themselves (e.g., by Region), empowering stakeholders to find specific insights without needing to request new static charts from the data team.

6. **How would you scale this project for millions of records?**
   - **Answer**: I would move from pandas to **PySpark** or **Dask** for distributed processing, and use a database like **PostgreSQL** or **BigQuery** instead of CSV files for faster querying.

7. **What visualization would you use for a Likert scale (Strongly Disagree to Strongly Agree)?**
   - **Answer**: A **Stacked Horizontal Bar Chart** is the industry standard for Likert scales as it shows the balance of sentiment across multiple questions in a single view.

8. **What kind of biases could exist in survey data?**
   - **Answer**: **Non-response bias** (certain groups not answering), **Social desirability bias** (answering what looks good), and **Selection bias** (if the survey was only sent to mobile users).

9. **How did you implement sentiment analysis?**
   - **Answer**: In this version, I used a **keyword-based rule engine**. For a more advanced version, I would use **VADER** or a **transformer-based model (HuggingFace)** to capture nuance.

10. **What is the most critical metric in this project?**
    - **Answer**: It depends on the business goal, but **NPS** is often the "North Star" metric for product-led growth companies.

---

## 👔 HR & Behavioral Interview Questions

1. **Why did you choose this project?**
   - **Answer**: I wanted to demonstrate how Data Science can be applied to direct human feedback, which is crucial for any customer-centric business.

2. **What was the biggest challenge you faced?**
   - **Answer**: Structuring the data for the Dashboard while keeping the cleaning process modular and repeatable.

3. **How do you explain technical charts to a non-technical manager?**
   - **Answer**: I focus on the **"So What?"**. Instead of saying "The mean is 4.2," I say "Customers in Asia are 20% more satisfied than other regions, suggesting our launch there was successful."

4. **What would you do if the data showed a very negative trend?**
   - **Answer**: I would treat it as an opportunity. I would deep-dive into the "Feedback_Text" using NLP to identify the root causes (e.g., specific bugs or pricing issues) and suggest actionable fixes.

5. **How did you ensure the project is professional and GitHub-ready?**
   - **Answer**: By implementing coding best practices (PEP8), modularity, comprehensive documentation, and a user-friendly UI.

6. **What is your favorite tool in the Python Data Science stack?**
   - **Answer**: Pandas, because of its versatility in data manipulation, but Streamlit is a close second for its ability to bring data to life.

7. **How do you stay updated with data visualization trends?**
   - **Answer**: I follow blogs like Information is Beautiful and the Streamlit community gallery to see modern UI patterns.

8. **If a stakeholder wants a chart that you think is misleading, what do you do?**
   - **Answer**: I would provide the requested chart but also present a more accurate alternative, explaining why the latter provides a better basis for decision-making.

9. **Describe a feature you'd like to add in the future.**
   - **Answer**: Integration with a live API (like Google Forms API) to make the dashboard update in real-time as people respond.

10. **What does "clean code" mean to you in a Data Science context?**
    - **Answer**: It means code that is readable, well-commented, modular, and produces reproducible results.
