from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def hello():
    msg = {
        "name": "adam",
        "version": "1",
        "date": datetime.datetime.now()
    }
    return render_template("index.html", msg=msg)


if __name__ == '__main__':
    app.run(port=5001, host="0.0.0.0", debug=True)
