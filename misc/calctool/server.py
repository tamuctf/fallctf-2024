from flask import Flask, request, jsonify, render_template
from sympy import sympify

app = Flask(__name__)


@app.route('/calc', methods=['POST'])
def calc():
    expr = request.json['expr']
    try:
        result = sympify(expr)
        if isinstance(result, int) or isinstance(result, float) or result.is_number: # a calculator should only return numeric results!
            return jsonify({'result': str(result)})
    except:
        pass
    return jsonify({'error': 'Invalid expression'}), 400


@app.get('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8080)
