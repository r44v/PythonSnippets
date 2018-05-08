# Python snippets for flask (webserver libary)

```python
from flask import Flask, jsonify, request, redirect, url_for
app = Flask(__name__)

print("Flask server")

@app.route('/')
def index():
	return "Hello, World!"

@app.route('/test', methods=['GET','POST'])
def test():
	return "Hello, Test!"

@app.route('/json/<string:name>', defaults={'lastname': 'Smith'})
@app.route('/json/<string:name>/<lastname>')
def json_route(name, lastname):
	return jsonify({'username': name, 'lastname': lastname})

@app.route('/redirectme')
def redirectme():
    return redirect(url_for('json_route', name='testuser'))

@app.route('/postroute', methods=['POST'])
def postroute():
	data = request.form.get("goal") # request.form["bla"] -> KeyError
	if data is not None:
		return "Posted data for goal: " + str(data)
	else:
		return "Enter use goal parameter"

if __name__ == '__main__':
	app.run(port=5000, host='127.0.0.1', debug=False)
```