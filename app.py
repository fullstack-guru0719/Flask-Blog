from flask import Flask

app = Flask(__name__)


# @app.route('/home/<name>')
# def home(name):
#     return "hello," + name


def about():
    return "This is about Page"


app.add_url_rule("/about", "about", about)

if __name__ == '__main__':
    app.run(debug=True)
