from flask import Flask, redirect, url_for, redirect, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('index.html', content="This is a MY -> HTML page. You can add more content here.", myList=['Vlad', 'Edik', 'Jorzh'], content2="Copyright &copy; VLAD-2023, LLC")


if __name__ == "__main__":

	app.run()