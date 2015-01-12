from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	string = "\n\nHallo from Python to the World!"
	string += "\n-----------------------------------\n"
	return string

if __name__=='__main__':
	app.run(debug=True)

	