import os
from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
	return 'Wake the fuck up Samurai, we have a city to burn.'
 
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
