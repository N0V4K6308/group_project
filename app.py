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

@app.route('/order_overview')
def order_overview_page():
    return render_template("order_overview.html")

@app.route('/payment')
def payment_page():
    return render_template("payment.html")

'''@app.route('/get_oven_data', Methods=['POST'])
def get_oven_data():
    return "Successful"'''


if __name__ == "__main__":
    app.run(host='0.0.0.0')
