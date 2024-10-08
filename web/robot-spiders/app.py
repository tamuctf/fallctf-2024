from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    ua = request.headers.get("User-Agent")
    if ua == "OAI-SearchBot" or ua == "ChatGPT-User" or ua == "GPTBot":
        return "Success Condition"
    else:
        return "News articles will only be served to OpenAI for training data [in article format]"


app.run("0.0.0.0", 3000)
