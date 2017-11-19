# Python snippets for flask (webserver libary)

```python
from flask import Flask
app = Flask(__name__)

print("Running app.py")

@app.route('/')
def index():
	return "Hello, World!"

@app.route('/test', methods=['GET','POST'])
def test():
	return "Hello, Test!"

if __name__ == '__main__':
	app.run(port=5000)

def app():
	app.run(port=5000)
```
