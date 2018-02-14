# Python 3.6 Snippets

```
          .?77777777777777$.            
          777..777777777777$+           
         .77    7777777777$$$           
         .777 .7777777777$$$$           
         .7777777777777$$$$$$           
         ..........:77$$$$$$$           
  .77777777777777777$$$$$$$$$.=======.  
 777777777777777777$$$$$$$$$$.========  
7777777777777777$$$$$$$$$$$$$.========= 
77777777777777$$$$$$$$$$$$$$$.========= 
777777777777$$$$$$$$$$$$$$$$ :========+.
77777777777$$$$$$$$$$$$$$+..=========++~
777777777$$..~=====================+++++
77777777$~.~~~~=~=================+++++.
777777$$$.~~~===================+++++++.
77777$$$$.~~==================++++++++: 
 7$$$$$$$.==================++++++++++. 
 .,$$$$$$.================++++++++++~.  
         .=========~.........           
         .=============++++++           
         .===========+++..+++           
         .==========+++.  .++           
          ,=======++++++,,++,           
          ..=====+++++++++=.            
                ..~+=... 
```
[source](https://gist.github.com/xero/3555086)

---

## Manipulate clipboard
```python
from tkinter import Tk

r = Tk()
r.withdraw()                # Prevent window from opening

txt = r.clipboard_get()     # Get current clipboard string

r.clipboard_clear()         # Clear clipboard

r.clipboard_append("hello") # Add text to clipboard
r.update()                  # Save clipboard data (else it disapears after r.destroy())

r.destroy()                 # close hidded Tk window when done
```

## Base64/SHA512
**Python 3.6**
```python
import hashlib

# python 3.6 requires byte instead of string
print(hashlib.sha512(b"TEXT TO HASH").hexdigest())
```

```python
import base64

# python 3.6 requires byte instead of string
text = b"something something"

encoded = base64.b64encode(text)
decoded = base64.b64decode(encoded)
```

## Get battery percentage in windows
```python
from ctypes import *

class PowerClass(Structure):
    _fields_ = [('ACLineStatus', c_byte),
            ('BatteryFlag', c_byte),
            ('BatteryLifePercent', c_byte),
            ('Reserved1',c_byte),
            ('BatteryLifeTime',c_ulong),
            ('BatteryFullLifeTime',c_ulong)]    

powerclass = PowerClass()

# this call gets the new %
result = windll.kernel32.GetSystemPowerStatus(byref(powerclass))

# change print to make it work in python 3.6
print(powerclass.BatteryLifePercent)
```

## link + port is up check

```python
import socket

def check(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((ip, port))
        print(str(ip) + " - Port " + str(port) + " reachable")
    except socket.error as e:
        print(str(ip) + " - Error on connect for port " + str(port))
    s.close()
```