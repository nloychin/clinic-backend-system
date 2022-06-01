from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/abount-us')
def abount_us():
    return '<p>Abount us</p>'


if __name__ == '__main__':
    app.run(debug=True)
