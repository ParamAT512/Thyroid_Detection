
# Thyroid Detection System

## Overview
This project uses machine learning to predict thyroid disease risk based on medical and demographic data. The dataset includes features such as hormone levels, medical history, and demographic details to assess the likelihood of conditions like hyperthyroidism and hypothyroidism.

## Dataset
The dataset, downloaded from [Kaggle](https://www.kaggle.com/datasets/emmanuelfwerr/thyroid-disease-data), contains a combination of categorical and numerical data, including patient demographics, medical history, and thyroid-related hormone levels.

### Key Columns in the Dataset:
- **Demographics**: `age`, `sex`, `patient_id`
- **Medical History**: `on_thyroxine`, `query_on_thyroxine`, `on_antithyroid_meds`, `sick`, `pregnant`, `thyroid_surgery`, `I131_treatment`, `query_hypothyroid`, `query_hyperthyroid`, `lithium`, `goitre`, `tumor`, `hypopituitary`, `psych`
- **Thyroid Measurements**: 
  - `TSH_measured`, `TSH`
  - `T3_measured`, `T3`
  - `TT4_measured`, `TT4`
  - `T4U_measured`, `T4U`
  - `FTI_measured`, `FTI`
  - `TBG_measured`, `TBG`
- **Referral Information**: `referral_source`
- **Target**: `target` (Thyroid condition outcome)

## Key Features
- **Frontend**: A user-friendly interface where patients input their age, sex, medical history, and thyroid test results.
- **Backend**: Flask-based API that processes user inputs and provides thyroid condition predictions using machine learning.
- **Model**: A Random Forest classifier that is trained to predict thyroid conditions based on input features.
- **Deployment**: Hosted on Azure for web access with version control managed via GitHub.

## Project Structure

### 1. Data Preprocessing
- **Data Loading**: Load the dataset using Pandas, checking for inconsistencies, missing values, and erroneous data.
- **Data Cleaning**: Handle missing values, drop irrelevant columns, and encode categorical variables.
- **Feature Engineering**: Apply necessary transformations such as scaling and encoding of features.
- **Visualization**: Create histograms, boxplots, and correlation heatmaps using Seaborn and Matplotlib to explore feature relationships.

### 2. Model Training and Evaluation
- **Splitting Data**: The dataset is split into training, validation, and test sets.
- **Model Training**: Various models (e.g., Logistic Regression, Random Forest) are trained, and the best-performing model is selected.
- **Model Evaluation**: Performance metrics such as accuracy, precision, recall, and F1-score are used for evaluation.

### 3. API and Web Interface
- **Flask Backend**: Handles HTTP requests, loads the pre-trained model, processes inputs, and returns predictions.
- **User Interface**: A simple HTML form collects patient data, which is submitted for thyroid condition prediction.

### 4. Deployment
- **Azure Hosting**: The Flask app is deployed on Azure, allowing users to access the thyroid prediction system online.
- **Version Control**: The project is managed through GitHub for collaboration and tracking changes.

## Requirements
- Python 3.x
- Flask
- NumPy, Pandas, Scikit-learn
- Matplotlib, Seaborn
- Pickle (for model serialization)
- Azure services (for deployment)

## How to Run the Project
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/thyroid-detection.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Start the Flask web server:
    ```bash
    python app.py
    ```
4. Access the application in your browser at `http://localhost:5000`.

## Future Improvements
- Enhance the user interface for a better experience.
- Explore additional features for improved model accuracy.

## License
This project is licensed under the [MIT License](LICENSE).
