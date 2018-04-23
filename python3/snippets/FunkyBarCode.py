import numpy as np
import matplotlib.pyplot as plt


def make_bin_img(text):
    # Turn text into bytes
    txtbin = ""
    for x in text:
        txtbin += bin(ord(x))[2:].rjust(8, '0')

    # Change bytes string to list
    s = [int(x) for x in txtbin]

    # Turn data into numpy
    s = np.array(s)

    # Make square in incrementions of 8
    s = s.reshape(-1)
    y = s.shape[0]
    sqrt = np.ceil(np.sqrt(y))
    while 1:
        if sqrt % 8 == 0:
            break
        sqrt += 1
    sqrt = int(sqrt)
    cube = sqrt ** 2
    diff = cube - y

    # Add missing data for square
    endz = np.zeros((int(diff), 1))
    s = np.append(s, endz)

    # Transform data (kinda reforms image)
    s = np.roll(s, int(s.sum()))

    # Reshape
    s = s.reshape(sqrt, -1)

    # Add orientation border
    fill = 1
    b = np.full((s.shape[0] + 2, s.shape[1] + 2), 1 if not fill else 0)
    b[1:-1, 1:-1] = s
    b[0, 0] = fill
    b[2, 0] = fill
    b[-1, 0] = fill
    b[-1, -1] = fill
    b[0, -1] = fill
    s = b

    # Needed when using png library
    s[s == 1] = 255  # replace 1 by 255 for

    # Display in ipython
    plt.imshow(s, cmap=plt.cm.binary)
    plt.axis('off')
    plt.show()
    return s


def decode_bin_matrix(matrix):
    # Ignore border and Shape per 8(byte)
    data = matrix[1:-1, 1:-1].reshape(-1, 8)

    # Turn 0/255 into 0/1
    data[data == 255] = 1  # replace 1 by 255

    # Transform data
    data = np.roll(data, -int(data.sum()))

    # Turn data into text
    text = ""
    for x in data:
        txtbin = ""
        for b in x:
            txtbin += str(b)
        text += chr(int(txtbin, 2))
    return text


x = make_bin_img("Hello World!\n\t- I\n\t- know\n\t...")
x = decode_bin_matrix(x)
print(x)
