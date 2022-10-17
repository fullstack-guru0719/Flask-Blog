from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "hello, this is our first flask website"


if __name__ == '__main__':
    app.run(debug=True)
