from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Register your company
registration_data = {
    "companyName": "Train Central",
    "ownerName": "Rahul",
    "rollNo": "1",
    "ownerEmail": "rahul@abc.edu",
    "accessCode": "FROL"
}

registration_response = requests.post("http://20.244.56.144/train/register", json=registration_data)
registration_response_data = registration_response.json()
client_id = registration_response_data["clientID"]
client_secret = registration_response_data["clientSecret"]

# Obtain authorization token
auth_data = {
    "companyName": "Train Central",
    "clientID": client_id,
    "ownerName": "Rahul",
    "ownerEmail": "rahul@abc.edu",
    "rollNo": "1",
    "clientSecret": client_secret
}

auth_response = requests.post("http://20.244.56.144/train/auth", json=auth_data)
auth_token = auth_response.json()["access_token"]

# Define API route
@app.route('/trains', methods=['GET'])
def get_trains():
    headers = {'Authorization': f'Bearer {auth_token}'}
    trains_response = requests.get("http://20.244.56.144/train/trains", headers=headers)
    trains_data = trains_response.json()

    # Process train data
    processed_trains = []  # Processed train data will be stored here

    # Implement the filtering and sorting logic here

    return jsonify(processed_trains)

if __name__ == '__main__':
    app.run(debug=True)
