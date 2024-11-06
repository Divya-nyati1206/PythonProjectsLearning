l = []
print("Enter name of three friends : ")
for i in range(3):
    name = input()
    l.append(name)

file = open('people.txt', 'r')
file_write = open('friends.txt', 'w')
data = file.read()
for i in range(3):
    if l[i] in data:
        file_write.write(l[i]+'\n')
file.seek(0)
print(file.read())

file.close()
file_write.close()
