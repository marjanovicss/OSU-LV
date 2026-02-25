UniqueWords = {}
Song = open("song.txt")

for line in Song:
    words = line.split()
    for word in words:
        word = word.rstrip(",")
        if word in UniqueWords:
            UniqueWords[word] += 1
        else:
            UniqueWords[word] = 1

UniqueWordsCounter = 0

for word in UniqueWords:
    if UniqueWords[word] == 1:
        UniqueWordsCounter += 1

print(f"{UniqueWords.keys()}")
print(f"Unique Words: {UniqueWordsCounter}")

Song.close()
