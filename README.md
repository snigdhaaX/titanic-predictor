# Titanic Survival Predictor

A Full-Stack Machine Learning web application that predicts whether a passenger would have survived the Titanic disaster based on their age, sex, ticket class, and other features.



## Live Demo
**Link:** [https://titanic-predictor-9njbmejvvpbi3lzgid8y5h.streamlit.app/]

## How it Works?
This project uses a **Decision Tree Classifier** trained on the famous Titanic dataset. 
- **Data Processing:** Handled missing values (Age/Fare) and encoded categorical data (Sex/Embarked) using Pandas.
- **Model:** A Decision Tree with a depth of 3 to balance accuracy and interpretability.
- **Interface:** Built with Streamlit for a sleek, interactive user experience.



##  Project Structure
```text
├── app.py                # Main Streamlit application script
├── titanic_model.pkl      # The trained AI model (saved brain)
├── requirements.txt       # List of Python dependencies for the server
├── tested.csv             # Raw Titanic dataset used for predictions
└── README.md              # Project documentation and guide
