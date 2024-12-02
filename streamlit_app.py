import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import FunctionTransformer


def convert_to_dense(x):
    if hasattr(x, "toarray"):
        return x.toarray()
    return x

# Define the FunctionTransformer using the `convert_to_dense` function
dense_transformer = FunctionTransformer(convert_to_dense)

@st.cache_data
def load_data():
    """Load and cache the dataset"""
    try:
        # Use the same path and parameters as in your ML code
        df = pd.read_csv('data/Math.csv', sep=';', encoding='ISO-8859-1')
        return df
    except Exception as e:
        st.error(f"Error loading dataset: {str(e)}")
        return None

def load_model():
    """Load the trained model"""
    try:
        model = joblib.load('best_classification_model.pkl')
        return model
    except Exception as e:
        st.error("Error: Could not load the model. Please ensure 'best_classification_model.pkl' is in the same directory.")
        return None

def get_unique_values(df, column):
    """Get sorted unique values from a column"""
    if df is not None and column in df.columns:
        return sorted(df[column].unique().tolist())
    return []

def main():
    st.title("Math Question Answer Type Predictor")
    st.header("Select the variables to predict whether a student is a likely to answer a question correctly or not.", divider='rainbow')

    # Load data and model
    df = load_data()
    model = load_model()
    
    if df is None or model is None:
        st.stop()

    student_country = st.selectbox(
        "Student Country",
        get_unique_values(df, 'Student Country')
    )

    question_level = st.selectbox(
        "Question Level",
        get_unique_values(df, 'Question Level')
    )

    topic = st.selectbox(
        "Topic",
        get_unique_values(df, 'Topic'),
        key='topic_selector'
    )

    # Update subtopics based on selected topic
    if topic:
        subtopic_options = sorted(df[df['Topic'] == topic]['Subtopic'].unique())
    else:
        subtopic_options = []
    
    subtopic = st.selectbox(
        "Subtopic",
        subtopic_options,
        key='subtopic_selector'
    )

    # Keywords field
    keywords = st.text_input("Keywords (comma-separated)")

    # Create a button instead of a form
    predict_button = st.button("Predict Answer Type")


    # Make prediction when form is submitted
    if predict_button:
        try:
            # Create a DataFrame with the input data
            input_data = pd.DataFrame({
                'Student Country': [student_country],
                'Question Level': [question_level],
                'Topic': [topic],
                'Subtopic': [subtopic],
                'Keywords': [keywords]
            })

            # Make prediction
            prediction = model.predict(input_data)

            # Display result
            st.subheader("Prediction Result")
            result = "Correct" if prediction[0] == 1 else "Wrong"
            
            # Style the result
            st.markdown(f"""
            <div style='padding: 20px; border-radius: 10px; background-color: #f0f2f6; text-align: center;'>
                <h2 style='color: #1f77b4;'>Predicted Answer Type: {result}</h2>
            </div>
            """, unsafe_allow_html=True)

            # Add explanation
            with st.expander("What does this mean?"):
                st.write("""
                - Wrong: [Type of answer is 0]
                - Correct: [Type of answer is 1]
                """)

        except Exception as e:
            st.error(f"Error making prediction: {str(e)}")
            st.error("Details of input data:")
            st.write(input_data)

    # Add information about the model
    with st.sidebar:
        st.subheader("About", divider='rainbow')
        st.write("""
        This app predicts the type of answer for math questions based on:
        - Student's country
        - Question level
        - Topic
        - Subtopic
        - Keywords
        """)
        
        if df is not None:
            st.write("Dataset Statistics:")
            st.write(f"Total number of records: {len(df)}")
            st.write(f"Number of unique topics: {len(df['Topic'].unique())}")
            st.write(f"Number of unique subtopics: {len(df['Subtopic'].unique())}")

if __name__ == "__main__":
    main()