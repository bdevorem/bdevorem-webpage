from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

@app.route('/Random')
def showRandom():
    return render_template('random.html')

@app.route('/Home')
def showHome():
    return render_template('index.html')

@app.route('/Resume')
def showResume():
    return render_template('resume.html')

@app.route('/Links')
def showLinks():
    return render_template('links.html')

if __name__ == "__main__":
	app.debug = True #don't have to restart code to show changes in browser
	app.run() #runs on local host given no parameters
