from flask import Flask
import os
import datetime
import hashlib
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now().isoformat()
    return f"Hello, World! Now: {now}"

@app.route("/gen_key", methods=["GET", "POST"])
def gen_key():
    license_str = (
        (request.args.get("license") if request.method == "GET" else request.form.get("license"))
        or ""
    )
    md5_key = hashlib.md5(license_str.encode("utf-8")).hexdigest()
    return {"license": license_str, "key": md5_key}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
