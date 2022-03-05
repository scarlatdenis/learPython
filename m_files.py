try:
    f = open("test.txt", encoding="utf-8")

finally:
    f.close()


with open("test.txt", "w", encoding="utf-8") as f:
    f.write("this is my first file open in py\n")
    f.write("This is second line write in file from py\n")
    f.write("This is third line in this file\n")
    f.close()

f = open("test.txt", "r", encoding="utf-8")

f.read()

print(f.tell())
print(f.read(4))
f.seek(0)      # cursor to zero, to the first line
print(f.read(4))  # reading 4 caracters after position of cursor

for line in f:
     print(line)
