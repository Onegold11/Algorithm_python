word = input()
print(word[1:3:1])
print(word[4:1:-1])
print(1) if word[::-1] == word else print(0)