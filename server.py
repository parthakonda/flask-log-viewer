from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello(name=None):
    data = []
    with open("payload.txt", "r") as openedfile:
        for line in reversed(openedfile.readlines()):
            data.append(line)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)