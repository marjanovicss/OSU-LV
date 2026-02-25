HamCounter = 0
WordsAfterHam = 0
SpamCounter = 0
WordsAfterSpam = 0
ExclamationMarkCounter = 0

fhand = open("SMSSpamCollection.txt")

for line in fhand:
    line = line.strip()

    if line.startswith("ham"):
        HamCounter += 1
        WordsAfterHam += len(line.split()) - 1

    elif line.startswith("spam"):
        SpamCounter += 1
        WordsAfterSpam += len(line.split()) - 1

        if line.endswith("!"):
            ExclamationMarkCounter += 1

fhand.close()

print(f"Average words in ham messages: {WordsAfterHam / HamCounter}")
print(f"Average words in spam messanges: {WordsAfterSpam / SpamCounter}")
print(f"Spam messages that end with '!': {ExclamationMarkCounter}")
