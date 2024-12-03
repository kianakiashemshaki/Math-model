[Comprehensive Analysis of Factors Affecting Mathematics Learning in Higher Education](https://prediction-answer.streamlit.app "Comprehensive Analysis of Factors Affecting Mathematics Learning in Higher Education")


## Group Members
1. Borketey, Humphrey
2. Kiashemshaki, Kiana
3. Nwala, Uchechi

---

project-directory/
├── data/
│   └── Math.csv          
├── notebooks/
│   └── analysis.ipynb      
├── Presentation/
│   └── slide.pdf     
├── README.md               
├── requirements.txt        
└── .gitignore


## 📋 Table of Contents
1. [About the Project](#about-the-project)
2. [Key Results](#key-results)
3. [Why This Matters](#why-this-matters)
4. [Methods and Tools](#methods-and-tools)
5. [How to Use This Project](#how-to-use-this-project)
6. [Project Structure](#project-structure)


---


## About the Project
About the Project
This project investigates the factors that influence students' performance in mathematics education in higher education institutions. Using a dataset of over 9,500 records, we performed data exploration, statistical analysis, and machine learning to derive meaningful insights. The analysis focused on uncovering trends, identifying challenges, and leveraging predictive models to support educators in improving student outcomes.

### 🎯 Goals:
1. Analyze performance trends across countries.
2. Discover which topics and subtopics are most challenging for students.
3. Examine the relationship between question difficulty levels and success rates.
4. Develop predictive models using machine learning to identify patterns and improve decision-making in education..

### Summary of Approach:
This project combines data exploration, statistical analysis, and machine learning to uncover actionable insights. Visualizations highlight trends, while machine learning models predict performance and identify key factors.
---

## 🚀 Key Results
- **Country-Level Insights:** Slovenia and Romania had the highest success rates, while Russia and Spain struggled the most.
- **Topic-Level Performance:** "Set Theory" and "Graph Theory" were the easiest topics for students, while "Linear Optimization" and "Partial Differentiation" were the hardest.
- **Question Difficulty:** Advanced-level questions had a higher success rate (~50%) compared to basic-level questions (~46%).
- **Machine Learning Performance:** Gaussian Naïve Bayes emerged as the best-performing model, achieving an F1 score of 0.62 after hyperparameter tuning.

---

## 🌍 Why This Matters
Mathematics is foundational to many academic and professional disciplines, yet disparities in learning outcomes persist across regions, topics, and teaching methods. This project aims to:
- **Pinpoint Challenges:** Identify areas where students face difficulties.
- **Empower Educators:** Provide data-driven insights to improve teaching methods.
- **Guide Policymakers:** Support equitable and effective educational strategies.

---
## 🛠 Methods and Tools
### Data Analysis:
- **EDA:** Investigated distributions and patterns across countries, topics, and question levels.
- **Statistical Testing:** Used chi-squared tests to assess significant differences.

### Machine Learning:
- **Algorithms Used:** 
  - Logistic Regression
  - Gaussian Naïve Bayes
  - Decision Tree Classifier
  - Random Forest Classifier
  - XGBoost
- **Evaluation Metrics:** Accuracy, Precision, Recall, and F1 Score.
- **Hyperparameter Tuning:** Applied GridSearchCV on the Gaussian Naïve Bayes model.

### Visualization:
- **Tools:** Plotly, Matplotlib, Pandas.
- **Examples:** Bar charts for topic and subtopic performance, stacked bar plots for country-wise correct vs incorrect answers.

### Tools and Libraries:
- **Programming Language:** Python
- **Key Libraries:** Pandas, NumPy, Scikit-learn, XGBoost, SciPy, Plotly.

## 🖥 How to Use This Project
### Getting Started
To explore the analysis or run the code yourself:

1. Clone this repository to your local machine:
   git clone (https://gitlab.com/kianakia399/cs6010_fa2024_project_g10.git)
2. pip install -r requirements.txt

3. jupyter notebook analysis.ipynb




