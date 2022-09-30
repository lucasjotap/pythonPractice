import urllib.request, urllib.parse, urllib.error

file_hand = urllib.request.urlopen('https://data.pr4e.org/romeo.txt')

counts = dict()

for line in file_hand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(words)