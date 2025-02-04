#flaskbackend
# app.py
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Store the latest location
current_location = {"latitude": 0.0, "longitude": 0.0}

@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.json
    current_location["latitude"] = data["latitude"]
    current_location["longitude"] = data["longitude"]
    return jsonify({"status": "success"})

@app.route('/get_location', methods=['GET'])
def get_location():
    return jsonify(current_location)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
