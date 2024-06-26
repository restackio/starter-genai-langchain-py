from flask import Flask, abort, render_template, jsonify
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/ask")
def ask():
    try:
        llm = OpenAI(temperature=0.7)
        text = "Tell me a joke about artificial intelligence."
        response = llm(text)
        return response
    except Exception as e:
        return jsonify(error=str(e)), 500


@app.route("/<path:any_path>")
def catch_all(any_path):
    abort(404)


if __name__ == "__main__":
    app.run()