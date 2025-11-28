"""Example of flask main file."""
import os
import logging
from flask import Flask
app = Flask(__name__)


LOG_DIR = "/tmp/logs"
os.makedirs(LOG_DIR, exist_ok=True)
log_file = os.path.join(LOG_DIR, "app.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

app.logger.addHandler(logging.FileHandler(log_file))
app.logger.setLevel(logging.INFO)


@app.route('/api/hello')
def hello_world():
    """Returns Hello, EDP!"""
    return 'Hello, EDP!'


if __name__ == '__main__':
    app.run()