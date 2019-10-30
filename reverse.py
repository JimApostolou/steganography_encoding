dict = {
    'a': '_|', 'b': '|_|', 'c': '|_', 'd': '-_|', 'e': '-|_|', 'f': '|_-',
    'g': '-|', 'h': '|-|', 'i': '|-', 'j': '._|', 'k': '.|_|.', 'm': '.|_',
    'n': '.-_|', 'l': '.|_|', 'o': '.|_-', 'p': '.-|', 'q': '.|-|', 'r': '.|-',
    's': '>', 't': 'v', 'u': '<', 'v': '^', 'w': '.>', 'x': '.v', 'y': '.<',
    'z': '.^',' ':'.^.'
}

file = open('stegmessage.txt','r')
text = file.read()
file.close()
x = text.split()
clear = ''

for i in x:
    for x,y in dict.items():
        if i == y:
            clear += x

print(clear)