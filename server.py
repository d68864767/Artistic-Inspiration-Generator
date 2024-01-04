```python
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai_api
import user_data
import community_features
import database_schema

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Artistic Inspiration Generator!"

@app.route('/generate_prompt', methods=['POST'])
def generate_prompt():
    data = request.get_json()
    response = openai_api.generate_prompt(data)
    return jsonify(response)

@app.route('/expand_idea', methods=['POST'])
def expand_idea():
    data = request.get_json()
    response = openai_api.expand_idea(data)
    return jsonify(response)

@app.route('/daily_challenge', methods=['GET'])
def daily_challenge():
    response = openai_api.daily_challenge()
    return jsonify(response)

@app.route('/submit_artwork', methods=['POST'])
def submit_artwork():
    data = request.get_json()
    response = community_features.submit_artwork(data)
    return jsonify(response)

@app.route('/rate_prompt', methods=['POST'])
def rate_prompt():
    data = request.get_json()
    response = user_data.rate_prompt(data)
    return jsonify(response)

@app.route('/get_user_data', methods=['GET'])
def get_user_data():
    response = user_data.get_user_data()
    return jsonify(response)

@app.route('/get_community_submissions', methods=['GET'])
def get_community_submissions():
    response = community_features.get_submissions()
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
```
