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

## Some basic manipulations

|Input|Result|
|-----|------|
|[2]*5|[2, 2, 2, 2, 2]|
|2**3|8|
|[1,2]+[3,4]|[1, 2, 3, 4]|
|"gg" in "eggs"|True|
|map(func, input)|\<map iteratable\>|
|[*map(func, input)]|[ \<list\> ]|
|list(map(func, input))|[ \<list\> ]|
|ord() \<-\> chr()|ASCII <-> INT|
|str.join(".", ['a','b','c','d'])|"a.b.c.d"|
|chr(int('01100001', 2))|'a'|
|int('01100001', 2)|97|
|bin(104)[2:]|'1101000'|

## Pretty header

```python
head = "index\tint\toct\thex".expandtabs(8)
print(head + "\n" + "-"*len(head))
```

```
index   int     oct     hex
---------------------------
```

## Range example

The range syntax is range(\<start\>, \<stop\>, \<step\>)

```python
for i in range(1,8,3):
    print(i)
```

```
1
4
7
```

## Interesting line splits

```python
# First example
('Hello '

'World')

# Second example
print("a" 
      + "b" 
      + "c")

# Third example
txt = "b" \
      + "c" \
    .upper()\
    .lower()
print("a"
      + txt)

```

```
# First result
'Hello World'

# Second result
abc

# Third result
abc
```

## Mysql timestamp

```python
import time

t = time.gmtime() # current time
print(time.strftime("%Y-%m-%d %H:%M:%S", t))
```