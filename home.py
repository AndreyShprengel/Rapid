from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/home')
def home():
	navigation = [{ "caption" : "Unofficial Networks", "href": "http://unofficialnetworks.com/"},
	{ "caption" : "Snow Brains", "href": "http://snowbrains.com/"}
	,
	{ "caption" : "Avalanche info", "href": "http://avalanche.state.co.us/"}]
	
	return render_template('home.html', navigation = navigation )

if __name__ == '__main__':
    app.run(debug = True)
