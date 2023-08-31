from flask import Flask, redirect, url_for, redirect

app = Flask(__name__)

@app.route("/home")
def home():
	return "<p>Hello, World!</p>"

# @app.route('/index', methods=['GET', 'POST'])
# def index():
# 	return render('index.html')

@app.route("/<name>")
def user(name):
	return f"hello {name}!"

# @app.route("/admin")
# def admin():
# 	return redirect(url_for('home'))

# Better ver of prev function
@app.route("/admin")
def admin():
	return redirect(url_for('user', name='Admin!'))

if __name__ == "__main__":

	app.run()