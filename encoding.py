dict = {
    'a': '_|', 'b': '|_|', 'c': '|_', 'd': '-_|', 'e': '-|_|', 'f': '|_-',
    'g': '-|', 'h': '|-|', 'i': '|-', 'j': '._|', 'k': '.|_|.', 'm': '.|_',
    'n': '.-_|', 'l': '.|_|', 'o': '.|_-', 'p': '.-|', 'q': '.|-|', 'r': '.|-',
    's': '>', 't': 'v', 'u': '<', 'v': '^', 'w': '.>', 'x': '.v', 'y': '.<',
    'z': '.^',' ':'.^.'
}

file = open('message.txt','r')
text = file.read()
file.close()
text = text.lower()
steg = []

for i in range(len(text)):
    x = text[i]
    steg.append(dict[x])

file2 = open('stegmessage.txt','w')
file2.write(' '.join(steg))
print(' '.join(steg))
file2.close()