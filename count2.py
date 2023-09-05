name = input('Enter file name: ')
fhand = open(name)

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, value in counts.items():
    newtup = (value, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)
for val, key in lst[:10]:
    print(key, val)
