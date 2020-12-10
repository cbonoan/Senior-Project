from flaskApp import app
import sys

if __name__ == '__main__':
    '''
    For testing purposes, include your IPV4 into the command when running app.py
    Ex: python run.py <IPV4 address>
    '''
    app.run(debug=True, host=sys.argv[1])