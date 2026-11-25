from flask import Flask, render_template, jsonify, request
import json, random
app = Flask(__name__)
with open ("data.json") as f:
     CAPSULES = json.load(f)

@app.route ("/")
def home():
     return render_template("index.html")
@app.route ("pull") 
def pull():
     cat = request.args.get("cat")
     items = CAPSULES.get(cat, [])
     if not items:
          return jsonify({"error": "empty"}), 404
     return jsonify({"item": random.choice(items)})
if __name__ == "__main__":
     app.run(debug=True)