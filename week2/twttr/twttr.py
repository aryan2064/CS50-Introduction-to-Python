text = input("Input: ")
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
ans = ''
for c in text:
    if c in vowel:
        continue

    ans += c

print (f"Output: {ans}")
