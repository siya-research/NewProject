from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    word_count = 0
    char_count = 0
    if request.method == "POST":
        text = request.form["text"]
        word_count = len(text.split())
        char_count = len(text)
    return render_template("index.html", word_count=word_count, char_count=char_count)

if __name__ == "__main__":
    app.run(debug=True)
