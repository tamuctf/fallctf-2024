from flask import Flask, request, render_template, jsonify
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    # Added by the HTTP reverse proxy to flag direct/non-TOR traffic
    direct_access = request.headers.get('direct-access-no-tor', 'false')
    if direct_access == 'true':
        return render_template('flag.html')
    else:
        return render_template('normal.html')

@app.route('/webhook', methods=['POST'])
def send_webhook():
    # Extract form data
    target_url = request.form['url']
    method = request.form['method']
    content_type = request.form['content_type']
    data = request.form.get('data', '')  # Optional, so provide a default empty string

    # Prepare headers for the request
    headers = {
        'Content-Type': content_type
    }

    # Send the webhook request based on the HTTP method
    try:
        if method == 'POST':
            response = requests.post(target_url, headers=headers, data=data)
        elif method == 'PUT':
            response = requests.put(target_url, headers=headers, data=data)
        elif method == 'DELETE':
            response = requests.delete(target_url, headers=headers)
        else:
            response = requests.get(target_url, headers=headers, params=data)

        # Return the response from the target webhook server
        return jsonify({
            'status_code': response.status_code,
            'response': response.text
        })

    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500


app.run("127.0.0.1", 3000)
