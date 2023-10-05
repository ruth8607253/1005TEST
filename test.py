from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def main():
    a=["aaa","bbb","ccc"]
    return render_template('main.jinja.html',a=a)

@app.route("/feature")
def feature():
    return render_template('feature.jinja.html')

@app.route("/child")
def child():
    return render_template('child.jinja.html')

@app.route("/book")
def book():
    return render_template('book.jinja.html')