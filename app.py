from flask import Flask, render_template, request
import pandas as pd
import joblib
from geopy.distance import geodesic
import webbrowser
import threading
import time

# Load model & encoder
model = joblib.load("fraud_detection_model.jb")
encoder = joblib.load("label_encoder.jb")

app = Flask(__name__)

def haversine(lat1, lon1, lat2, lon2):
    return geodesic((lat1, lon1), (lat2, lon2)).km


@app.route("/")
def main_dashboard():
    return render_template("Main dashboard.html")


@app.route("/dashboard")
def go_to_dashboard():
    return render_template("Go to Dashboard.html")


@app.route("/analytics")
def analytics():
    return render_template("Analytics.html")


@app.route("/upload", methods=["GET", "POST"])
def index():
    prediction_result = None
    error_message = None

    if request.method == "POST":
        merchant = request.form.get("merchant")
        category = request.form.get("category")
        amt = request.form.get("amt")
        lat = request.form.get("lat")
        long = request.form.get("long")
        merch_lat = request.form.get("merch_lat")
        merch_long = request.form.get("merch_long")
        hour = request.form.get("hour")
        day = request.form.get("day")
        month = request.form.get("month")
        gender = request.form.get("gender")
        cc_num = request.form.get("cc_num")

        # Check required fields
        if not merchant or not category or not cc_num:
            error_message = "Please fill all required fields."
        else:
            try:
                amt = float(amt)
                lat = float(lat)
                long = float(long)
                merch_lat = float(merch_lat)
                merch_long = float(merch_long)
                hour = int(hour)
                day = int(day)
                month = int(month)

                # Distance
                distance = haversine(lat, long, merch_lat, merch_long)

                # Prepare dataframe
                input_data = pd.DataFrame([[merchant, category, amt, distance,
                                            hour, day, month, gender, cc_num]],
                                          columns=['merchant', 'category', 'amt', 'distance',
                                                   'hour', 'day', 'month', 'gender', 'cc_num'])

                # Encode categorical data
                categorical_col = ['merchant', 'category', 'gender']
                for col in categorical_col:
                    try:
                        input_data[col] = encoder[col].transform(input_data[col])
                    except ValueError:
                        input_data[col] = -1  # unknown value

                # Hash cc number
                input_data['cc_num'] = input_data['cc_num'].apply(lambda x: hash(x) % (10 ** 2))

                # Predict
                prediction = model.predict(input_data)[0]
                prediction_result = "Fraudulent Transaction" if prediction == 1 else "Legitimate Transaction"

            except Exception as e:
                error_message = f"Error processing input: {str(e)}"

    return render_template("index.html", result=prediction_result, error=error_message)


if __name__ == "__main__":
    def open_browser():
        time.sleep(1.5)
        webbrowser.open('http://127.0.0.1:5000/')
    
    threading.Thread(target=open_browser).start()
    app.run(debug=True)
