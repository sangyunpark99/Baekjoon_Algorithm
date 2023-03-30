s = input()
suffix = []

for i in range(len(s)):
    suffix.append(s[i:])

suffix.sort()

for word in suffix:
    print(word)