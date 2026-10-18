# Spam-or-Ham-AI

## Project Overview

The Spam–Ham Detection System is a machine learning project that classifies text messages into two categories: Spam and Ham (legitimate messages). It uses a trained machine learning model and a Streamlit web interface to make predictions from user input.

## Features

- Binary text classification: Spam or Ham
- Interactive web interface built with Streamlit
- Machine learning model trained using Python
- Real-time predictions for user-entered messages
- Simple and user-friendly interface

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- SciPy
- Pickle for model serialization

## Project Structure

```text
spam-ham-detection/
├── spam_ham_code.py
├── spam_ham_app.py
├── model.pkl
├── requirements.txt
├── README.md
└── screenshots/
```
## How to Run Locally
1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL
cd spam-ham-detection

2. Install dependencies

python -m pip install -r requirements.txt

3. Train the model (if required)

python train_model.py

Make sure the training script generates the model file expected by the application.
4. Run the application

python -m streamlit run spam_ham_app.py

The application will open in your browser.



## Challenges Faced

- Loading the trained model correctly in the application.
- Managing Python library dependencies and version compatibility.
- Connecting the machine learning model with the Streamlit interface.
- Testing predictions with different text messages.

## What I Learned

- Fundamentals of binary classification.
- Training and saving a machine learning model.
- Integrating a trained model into a Streamlit application.
- Managing Python dependencies.
- Testing and documenting a software project.
- Using GitHub for source code management and project sharing.

## Future Improvements

- Improve model accuracy with additional training data.
- Evaluate the model using appropriate classification metrics.
- Enhance the interface and display prediction confidence when supported by the model.

## Author

Nathiyashree

