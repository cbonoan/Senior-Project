from flask import Flask, render_template
import sys
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    '''
    For testing purposes, include your IPV4 into the command when running app.py
    Ex: python app.py <IPV4 address>
    '''
    app.run(debug=True, host=sys.argv[1])