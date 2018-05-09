# PythonSnippets
Some python snippets from non native libraries

## Simple url request
[pypi](https://pypi.python.org/pypi/requests)

[Python requests guide](http://docs.python-requests.org/en/master/)

[Stack overflow with source of code](http://stackoverflow.com/questions/4476373/simple-url-get-post-function-in-python)

```python
import requests

# request url
url = "http://httpbin.org/post"

# post data
payload = {'key1': 'value1', 'key2': 'value2'}

# POST with form-encoded data
r = requests.post(url, data=payload)

# OR

# GET simple get request
url = "http://httpbin.org/get"
r = requests.get(url)

# Response, status etc
print(r.status_code, r.reason)
print(r.text)
```

## Raspberry Pi GPIO
```python
# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
pinC    = 4    # P7
pinB    = 25   # P6
pinRed  = 24   # P5
pinA    = 23   # P4

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(pinA, GPIO.OUT) # LED pin set as output
GPIO.setup(pinB, GPIO.OUT) # LED pin set as output
GPIO.setup(pinC, GPIO.OUT) # LED pin set as output
GPIO.setup(pinRed, GPIO.OUT) # LED pin set as output

# Initial state for LEDs:

GPIO.output(pinA, GPIO.HIGH)
GPIO.output(pinB, GPIO.HIGH)
GPIO.output(pinC, GPIO.HIGH)
GPIO.output(pinRed, GPIO.HIGH)

time.sleep(5)

GPIO.output(pinA, GPIO.LOW)
GPIO.output(pinB, GPIO.LOW)
GPIO.output(pinC, GPIO.LOW)
GPIO.output(pinRed, GPIO.LOW)

print("Here we go! Press CTRL+C to exit")
try:
    while True:
        time.sleep(1)
        GPIO.output(pinA, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pinB, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pinC, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pinA, GPIO.LOW)
        GPIO.output(pinB, GPIO.LOW)
        GPIO.output(pinC, GPIO.LOW)
        GPIO.output(pinRed, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pinRed, GPIO.LOW)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO

```

## Basic barchart in Matplotlib and Numpy
[pypi](https://pypi.python.org/pypi/matplotlib)

```python
import matplotlib.pyplot as plt
import numpy as np

# data = [] | labels = []
def make_chart(data, labels, ylabel='', title=''):
    #data -> data for each bar
    N = len(data)  # amount of bars

    ind = np.arange(N)  # the x locations for the bars
    width = 0.6         # the width of the bars

    # prepare diagram
    fig, ax = plt.subplots()
    bar1 = ax.bar(ind, data, width, color='r')

    # x labels
    ax.set_xticks(ind)  # label location
    ax.set_xticklabels(labels, rotation='vertical')  # label for each bit of data

    # more labels
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    # open graph window
    plt.show()

make_chart([1,2,3,4,5],["1","2","3","4","5"])
```


## Easygui - really simple gui
[pypi](https://pypi.python.org/pypi/easygui)

```python
import easygui
easygui.msgbox("yes, yes it works")
value = easygui.enterbox("Enter text:")
easygui.textbox(title="Output", text="Window title blablabla")
# there is more on the man page
```

## PyYaml
[Pypi](https://pypi.python.org/pypi/PyYAML)

```python
import yaml

config_file = 'config.yml'
data = {"api": {"secret": 'YXBpc2VjcmV0'}, "user": {"fname": "John", "lname": "Smith"}}

with open(config_file, 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)

with open(config_file, 'r') as infile:
    config = yaml.load(infile)

# this line displays the dict again as read from the file
# {'api': {'secret': 'YXBpc2VjcmV0'}, 'user': {'fname': 'John', 'lname': 'Smith'}}
print(config)
```

This generates and reads the following file (config.yml)
```yaml
api:
  secret: YXBpc2VjcmV0
user:
  fname: John
  lname: Smith
```

## Paramiko (ssh + scp)
[Official website](http://www.paramiko.org/installing.html)
[scp module](https://github.com/jbardin/scp.py)

```python
import paramiko
from scp import SCPClient

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    '<host>',
    username='<username>',
    password='<password>'
    )

cmd = "echo -n \"name:? \";read answer; echo \"You entered: $answer\""
stdin, stdout, stderr = ssh.exec_command(cmd)
stdin.write('user\n') # Always break
stdin.flush()
print({
    'out': stdout.readlines(),
    'err': stderr.readlines(),
    'retval': stdout.channel.recv_exit_status()
    })

ssh.exec_command('echo it works > test.txt')
scp = SCPClient(ssh.get_transport())
scp.get('test.txt')

scp.close()
ssh.close()
```