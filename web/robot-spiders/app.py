from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    ua = request.headers.get("User-Agent")
    if ua == "OAI-SearchBot" or ua == "ChatGPT-User" or ua == "GPTBot":
        return render_template('flag.html')
    else:
        return render_template('denied.html')


app.run("0.0.0.0", 3000)
