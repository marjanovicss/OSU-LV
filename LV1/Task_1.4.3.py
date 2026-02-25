Numbers = []
NumberCount = 0
Sum = 0
while True:
    NumbersOrDone = input("Enter some numbers or Done: ")
    if NumbersOrDone == "Done":
        break
    if NumbersOrDone >= 'a' and 'z' >= NumbersOrDone and NumbersOrDone >= 'A' and 'Z' >= NumbersOrDone:
        continue
    Numbers.append(NumbersOrDone)
    NumberCount += 1


print(f"\nNumber count: {NumberCount}")
print(f"Max value: {max(Numbers)}")
print(f"Min value: {min(Numbers)}")

for i in range(0, len(Numbers)):
    Sum += int(Numbers[i])

print(f"Arithmetic mean: {Sum / NumberCount}")

Numbers.sort()
print(f"Sorted list: {Numbers}")
