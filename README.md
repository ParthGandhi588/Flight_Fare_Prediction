# ✈️ Flight Fare Prediction Application

This repository contains a Flask-based web application that predicts flight fares based on user input. The project utilizes a machine learning model trained on historical flight data to provide fare predictions.

## 🌟 Features
- 🖥️ **User-friendly web interface** for entering flight details.
- 🔍 **Predicts flight fares** based on various factors like airline, class, source, destination, number of stops, and travel date.
- 🛠️ **Preprocessing of input data** for compatibility with the machine learning model.

## 📂 Files

### 1. **`app.py`**
The main Flask application file containing routes and logic for handling user inputs and predicting flight fares.

### 2. **`form.html`**
A simple HTML form for user interaction. Users can input their flight details and get fare predictions.

### 3. **`requirement.txt`**
A list of required Python packages for the project. Install these using the command:
```bash
pip install -r requirement.txt
```

### 4. **`Cleaned_dataset.csv`**
A dataset used for cleaning and feature engineering during the model training phase.

### 5. **`preprocessing.pkl`**
A serialized preprocessing object used to transform user inputs into the format expected by the model.

### 6. **`.gitignore`**
Specifies files and directories to be ignored by Git, such as large model files.

### 7. **`model.pkl`**
The trained machine learning model file. Run the model training script to generate this file.

## 🗂️ Directory Structure
```
Flight-Fare-Prediction/
├── app.py                # Flask application file
├── requirement.txt       # List of Python dependencies
├── notebooks/            # Folder for dataset and Jupyter notebooks
│   ├── Cleaned_dataset.csv   # Dataset used for feature engineering
│   ├── Flight_Fare_Prediction.ipynb  # Python notebook for training
├── templates/            # Folder for HTML templates
│   ├── form.html         # HTML form for user input
├── model/                # Directory for model files
│   ├── preprocessing.pkl # Preprocessing object
│   ├── model.pkl         # Trained machine learning model
├── .gitignore            # Git ignore file
```

## 🚀 How to Run the Application

### Prerequisites
- 🐍 Python 3.7 or higher
- 🌐 Flask
- ⚙️ scikit-learn
- 📦 Other dependencies listed in `requirement.txt`

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <repository-folder>
   ```
3. Install dependencies:
   ```bash
   pip install -r requirement.txt
   ```
4. Run the model training script to generate the `model.pkl` file.
5. Run the Flask application:
   ```bash
   python app.py
   ```
6. Open your browser and navigate to `http://127.0.0.1:5000/predict` to access the application.

## 📝 Input Details
- **✈️ Airline**: Select from the dropdown list (e.g., Indigo, Air India, etc.).
- **🛋️ Class**: Choose the travel class (e.g., Economy, Business, etc.).
- **📍 Source and Destination**: Select departure and arrival cities.
- **🔄 Total Stops**: Indicate the number of layovers.
- **📅 Date**: Specify the travel date.

## 📊 Output
- The predicted flight fare is displayed after submitting the form.

