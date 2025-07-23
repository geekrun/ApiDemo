from flask import Flask
import os
import datetime
app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now().isoformat()
    return f"Hello, World! Now: {now}"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
