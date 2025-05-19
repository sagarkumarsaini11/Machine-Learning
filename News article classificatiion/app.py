from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("news_classifier.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")  
@app.route("/predict", methods=["POST"])
def predict():
    text = request.form["news_text"]
    prediction = model.predict([text])[0]
    return jsonify({"category": prediction})

if __name__ == "__main__":
    app.run(debug=True)

