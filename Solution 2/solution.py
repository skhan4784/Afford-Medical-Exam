from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)

def fetch_numbers_from_url(url):
    try:
        response = requests.get(url, timeout=0.5)
        if response.status_code == 200:
            data = response.json()
            return data.get("numbers", [])
    except requests.Timeout:
        pass  # Ignore URLs that take too long to respond
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
    return []

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')
    unique_numbers = set()

    start_time = time.time()
    for url in urls:
        numbers = fetch_numbers_from_url(url)
        unique_numbers.update(numbers)
        if time.time() - start_time >= 0.5:
            break  # Respect the timeout limit

    sorted_numbers = sorted(unique_numbers)
    return jsonify(numbers=sorted_numbers)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
