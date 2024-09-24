from flask import Flask,  render_template, send_from_directory, make_response, Response, request

app = Flask(__name__)

@app.route('/',  methods=["GET"])
def home():
    robots = [
        {"name": "Dead or Alive: Miku", "image": "https://i.pinimg.com/736x/c8/9e/64/c89e644dda55fb10e89d9220c0a13f7d.jpg"},
        {"name": "Dead: The Terminator", "image": "https://nofilmschool.com/media-library/t2-judgement-day.jpg?id=34060202&width=1245&height=700&quality=90&coordinates=33%2C0%2C34%2C0"},
        {"name": "Dead or Alive: Iron Giant", "image": "http://orig03.deviantart.net/f94a/f/2011/346/a/4/iron_giant_by_vadeg-d4ivzfy.jpg"},
    ]
    return render_template('robots.html', robots=robots)


@app.route('/secrets.html',  methods=["GET"])
def secrets():  
    resp = make_response(render_template('secrets.html'))
    resp.set_cookie('celsius', "The secret is celsius! And the rest of the flag is l41n_s1t3}")
    return resp




@app.route('/robots.txt',  methods=["GET"])
def robots_txt():
    return send_from_directory(app.static_folder, 'robots.txt')

if __name__ == '__main__':
    app.run('0.0.0.0', port=8000)