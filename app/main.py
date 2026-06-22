import logging
from flask import Flask, jsonify

app = Flask(__name__)

# Configure logging format for easy ingestion
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log") # This file can be monitored by forwarders
    ]
)

@app.route('/')
def home():
    app.logger.info("Home endpoint was hit successfully.")
    return jsonify({"status": "healthy", "message": "DevOps Sandbox API is live!"})

@app.route('/test-error')
def trigger_error():
    app.logger.error("Simulated failure endpoint reached!")
    return jsonify({"status": "error", "message": "This is a simulated failure."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)