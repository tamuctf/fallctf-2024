from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    host = request.headers.get("Host")
    if host == "server.internal":
        return "Internal network position verified! gigem{h057_15_ju57_4_50c14l_c0n57ruc7}"
    else:
        return "ERROR: External Requests Denied. As a security measure, this site is only reachable by requests made from the internal network, where it can be reached through the server.internal domain."


app.run("0.0.0.0", 3000)
