from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    host = request.headers.get("Host")
    if host == "server.internal":
        return render_template('flag.html')
    else:
        return render_template('denied.html')


app.run("0.0.0.0", 3000)
