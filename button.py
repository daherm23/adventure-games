from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def index():
	return render_template("index2.html")

@app.route('/index3.html')

def gameOver():
	return render_template("index3.html")

@app.route('/index4.html')

def anotherRoom(): 
	return render_template("index4.html")

@app.route('/index5.html')

def redDoor():
	return render_template("index5.html")

@app.route('/index6.html')

def blackDoor(): 
	return render_template("index6.html")

app.run(debug=True)