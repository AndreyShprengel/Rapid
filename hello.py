from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/find' , methods = ['GET','POST'])
def find_classroom():
	course = request.args.get('course')
	if course == 'CSCI1300':	
			return 'Find a classroom for' + course + " ... ATLAS100"
	if course == 'CSCI2240':
			return 'Find a classroom for' + course + " ... ITLL1B50"	
	else:
		return 'Find a classroom for' + course + " ... Sorry. No result for" + course	
	
		
		
		
    
 
@app.route('/notification/')
def notif():
    return 'Get notification. To be implemented'
    
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
@app.route('/resume')
@app.route('/resume/<name>')
def resume(name = 'Andrey Shprengel'):
	return render_template('resume.html',name=name)

if __name__ == '__main__':
    app.run(debug = True)
