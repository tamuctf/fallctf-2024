from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    ua = request.headers.get("User-Agent")
    if ua is not None and "GPTBot" in ua:
        return render_template('robot.html')
    else:
        return render_template('human.html')


app.run("0.0.0.0", 3000)
