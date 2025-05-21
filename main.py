from flask import Flask, jsonify, render_template
from config import key
import openai

openai.api_key = key
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generateimages/<prompt>')
def generate(prompt):
    print("prompt:", prompt)
    try:
        response = openai.Image.create(prompt=prompt, n=5, size="256x256")
        print(response)
        return jsonify(response)
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
