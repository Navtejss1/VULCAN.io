from flask import Flask, request, jsonify, render_template
import requests


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    url = request.form['url']
    headers = requests.get(url).headers

    results = {
        "Content-Security-Policy": "not VULNERABLE" if "Content-Security-Policy" in headers else "VULNERABLE",
        "Referrer-Policy": "not VULNERABLE" if "Referrer-Policy" in headers else "VULNERABLE",
        "Strict-Transport-Security": "not VULNERABLE" if "Strict-Transport-Security" in headers else "VULNERABLE",
        "X-Content-Type-Options": "not VULNERABLE" if "X-Content-Type-Options" in headers else "VULNERABLE",
        "X-Frame-Options": "not VULNERABLE" if "X-Frame-Options" in headers else "VULNERABLE",
        "Permissions-Policy": "not VULNERABLE" if "Permissions-Policy" in headers else "VULNERABLE"
    }

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
