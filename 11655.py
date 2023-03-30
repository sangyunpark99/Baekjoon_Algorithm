s = list(input())
ans = ''

for word in s:
    if word.islower():
        if ord(word) + 13 > 122:
            ans += chr((ord(word)+13) % 122 + 96)
        else:
            ans += chr(ord(word) + 13)
    elif word.isupper():
        if ord(word) + 13 > 90:
            ans += chr((ord(word) + 13) % 90 + 64)
        else:
            ans += chr(ord(word) + 13)
    elif not word.isalpha():
        ans += word
print(ans)