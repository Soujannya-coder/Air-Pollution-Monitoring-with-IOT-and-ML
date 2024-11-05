# Air Pollution Monitoring System

## Overview

This project is an Air Pollution Monitoring System for visualizing and predicting air quality based on humidity, temperature, and location data. The dashboard is built using Flask for the backend, handling data processing and machine learning predictions, and a modern HTML/CSS/JavaScript front-end for an interactive user interface.

## Features

- **Interactive Visualizations**: Displays plots of Humidity vs Air Quality and Temperature vs Air Quality for the selected location.
- **Air Quality Prediction**: Predicts air quality based on user inputs for humidity, temperature, and location.
- **Responsive Design**: The dashboard is designed to be responsive and visually appealing on various devices.

## Prerequisites

- Python 3.7+
- Flask
- pandas
- matplotlib
- seaborn
- scikit-learn
- jQuery
- Bootstrap

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/air-pollution-monitoring-system.git
   cd air-pollution-monitoring-system
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install the required Python packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure the `model.pkl` file is in the `artifact` directory and `combined_data.csv` is in the `data` directory.**

## Usage

1. **Run the Flask application:**

   ```bash
   python app.py
   ```

2. **Open a web browser and navigate to:**

   ```
   http://127.0.0.1:5000
   ```

3. **Interact with the dashboard:**

   - Select a location from the dropdown to view the plots.
   - Use the prediction form to input humidity, temperature, and location to predict the air quality.

## File Structure

```
.
├── artifact
│   └── model.pkl
├── data
│   └── combined_data.csv
├── templates
│   └── index.html
├── app.py
├── requirements.txt
└── README.md
```

## Example Data

Ensure that `combined_data.csv` contains columns for `Location`, `Humidity`, `Temperature(C)`, and `Air_Quality(PPM)`. An example row might look like:

```
Location,Humidity,Temperature(C),Air_Quality(PPM)
Liluah,70,25,60
Shibpur,65,30,55
```

## Model Training

If you need to retrain the machine learning model:

1. **Prepare your data in a CSV file with the necessary columns.**
2. **Use the following script as an example to train and save your model:**

   ```python
   import pandas as pd
   from sklearn.model_selection import train_test_split
   from sklearn.linear_model import LinearRegression
   import pickle

   # Load data
   df = pd.read_csv('data/combined_data.csv')

   # Preprocess data
   df = pd.get_dummies(df, columns=['Location'], drop_first=True)

   # Define features and target
   X = df.drop('Air_Quality(PPM)', axis=1)
   y = df['Air_Quality(PPM)']

   # Split data
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

   # Train model
   model = LinearRegression()
   model.fit(X_train, y_train)

   # Save model
   with open('artifact/model.pkl', 'wb') as f:
       pickle.dump(model, f)
   ```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

Developed by Soujannya Deb,Aftab Mallick, Sagnik Banerjee.
Guided By Avijit Bose, HOD CSE MCKVIE.

