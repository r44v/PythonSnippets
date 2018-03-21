# cryptography

## AES CBC mode

### encrypt

```python
import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

text = input("Input\t: ")
text = bytes(text, 'utf-8')

if len(text) % 128 != 0:
    width = (len(text))//128 * 128 + 128
    print("Lenght\t: %s" % str(len(text)))
    print("Width\t: %s" % str(width))
    text = text.ljust(width, b'\0')

input_data = text

backend = default_backend()
key = os.urandom(32)
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
encryptor = cipher.encryptor()
ct = encryptor.update(input_data) + encryptor.finalize()

with open("locked_away", "wb") as fileout:
    fileout.write(ct)

key = str(base64.b16encode(key), 'utf-8')
iv = str(base64.b16encode(iv), 'utf-8')

print("Key\t: " + key)
print("IV\t: " + iv)
print()
print("Copy\t: %s_%s" % (key, iv))


```

This scripts outputs a line what the next script can use to decode the created file content

### decrypt

```python
import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()

#key = input('Key\t: ')
#iv  = input('IV\t: ')

key  = input('Key\t: ')
key, iv = str.split(key, "_")

key = base64.b16decode(key)
iv = base64.b16decode(iv)


cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)

with open("locked_away", "rb") as filein:
    data = filein.read()

decryptor = cipher.decryptor()
result = decryptor.update(data) + decryptor.finalize()
print("Lenght\t: %s" % str(len(result)))

outfilename = 'decrypted'
if os.path.exists(outfilename):
    os.remove(outfilename)

with open(outfilename, "wb") as fileout:
    fileout.write(result)

txt = str(result, 'utf-8')
print("Lenght\t: %s" % str(len(result)))
print(txt)

```

### Hex view

A try at a kind of hex viewer, used on the decrypted file contents

```python
import base64
import string

with open("decrypted", "rb") as filein:
    data = filein.read()

def hex_line(data, print_txt=True):
    linewidth = len(data)
    step = 2
    txt = ""
    for i in range(0, len(data)-1, step):
        # Print HEX pair
        print(data[i:i+2], end=' ')
        # Convert hex to text
        if print_txt:
            char = chr(int(data[i:i+2], 16))
            if char in string.printable.replace("\t\n\r\x0b\x0c", ""):
                txt += " " + char
            else:
                txt += "  "
        # print text conversion at end of line
        if (i+step) % (linewidth) == 0:
            print(' | ', end='')
            print(txt, end=' ')
            txt = ""
            print()

# bytes per line
linewidth = 8
for x in range(0, len(data), linewidth):
    hex_line(data[0+x:x+linewidth].hex().upper())
```