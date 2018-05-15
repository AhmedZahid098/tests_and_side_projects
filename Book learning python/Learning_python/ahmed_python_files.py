# Creating a text file --> open('filename.type', 'w') --> 'w' is write
# Creating a text file --> open('filename.type', 'r') --> 'r' is read
f = open('name.txt', 'w')

# Writing data --> always remain string type in document
f.write('Allah\nis\nall\nseeing')

# Flush buffers the output data to your hard drive
f.close()

# 'r' (read) is the default processing mode
f = open('name.txt')

# Read entire file into a string
text = f.read()

# print interprets control characters
print(text)

# Read files line by line with help of a loop
for line in open('name.txt'):
    print(line)

# There many function used for the interpretation of files
print(dir(f))

# Look for seek
help(f.seek)

# Binary bytes files
import struct
# Create packed binary data
packed = struct.pack('>i4sh', 7, b'spam', 8)

# 10 bytes, not objects or text
print (packed)

# Open binary output file
file = open('data.bin', 'wb')

# Write packed binary data
file.write(packed)

file.close()

# Open/read binary data file
data = open('data.bin', 'rb').read()
print (data)

# Slice bytes in the middle
data[4:8]

# A sequence of 8-bit bytes
print (list(data))

# Unpack into objects again
struct.unpack('>i4sh', data)

# Unicode text files
# Non-ASCII unicode text
s = 'sp\xc4m'
print(s)
print(s[2])

# Write/Encode UTF-8 text file
file = open('unidata.txt', 'w', encoding='utf-8')

# Four characters written
file.write(s)
file.close()

# Read/Decode UTF-8 text files
text = open('unidata.txt', encoding='utf-8').read()
print (text)

# Four characters code point
print (len(text))
