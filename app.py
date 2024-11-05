from flask import Flask, render_template, request, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import pickle

app = Flask(__name__)

# Load the machine learning model
with open('artifact/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Sample DataFrame
df = pd.read_csv("data/combined_data.csv")

# Set Matplotlib backend
import matplotlib
matplotlib.use('Agg')

@app.route('/')
def index():
    locations = df['Location'].unique()
    return render_template('index.html', locations=locations)

@app.route('/plot', methods=['POST'])
def plot():
    location = request.form['location']
    filtered_df = df[df['Location'] == location]

    img1 = create_plot(filtered_df, 'Humidit', 'Air_Quality(PPM)')
    img2 = create_plot(filtered_df, 'Temperature(C)', 'Air_Quality(PPM)')

    return jsonify({'img1': img1, 'img2': img2})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    humidity = data['humidity']
    temperature = data['temperature']
    location = data['location']

    a = [0] * 4
    a[0] = humidity
    a[1] = temperature
    if location.lower() == 'liluah':
        a[2] = 1
    elif location.lower() == 'shibpur':
        a[3] = 1

    pred_data = pd.DataFrame([a], columns=['Humidit', 'Temperature(C)', 'Location_Liluah', 'Location_Shibpur'])
    prediction = model.predict(pred_data)
    air_quality = round(prediction[0],0)
    if air_quality < 75:
        s= str(air_quality) + " Good"
    elif air_quality >= 75 and air_quality < 150:
        s= str(air_quality) + " Moderate"
    else:
        s= str(air_quality) + " Bad"


    return jsonify({'air_quality': s})

def create_plot(data, x_col, y_col):
    plt.figure(figsize=(10, 6))
    plt.scatter(data[x_col], data[y_col], c='blue', alpha=0.5)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f'{x_col} vs {y_col}')
    plt.grid(True)

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    return base64.b64encode(img.getvalue()).decode()

if __name__ == '__main__':
    app.run(debug=True)
