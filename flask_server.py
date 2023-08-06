from flask import Flask, jsonify

app = Flask(__name__)

# Define a route for the root endpoint
@app.route('/')
def hello():
    return jsonify({"message": "Hello, Flask API!"})

if __name__ == '__main__':
    app.run(debug=True)
