from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template("index.html")

@app.route('/menu')
def menu_page():
    return render_template("menu.html")

@app.route('/history')
def history_page():
    return render_template("history.html")

'''@app.route('/get_oven_data', Methods=['POST'])
def get_oven_data():
    return "Successful"'''


if __name__ == "__main__":
    app.run(debug=True)
