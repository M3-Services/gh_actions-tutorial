from flask import Flask, request

app = Flask(__name__)

@app.route('/reverse', methods=['POST'])
def reverse_string():
    data = request.get_json()
    string = data['string']
    reversed_string = string[::-1]
    return {'reversed_string': reversed_string,
            'status': 200}

@app.route('/square', methods=['POST'])
def square_number():
    data = request.get_json()
    number = data['number']
    square = number ** 2
    return {'square': square}

if __name__ == '__main__':
    app.run()


