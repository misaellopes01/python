word = input()
count_uppercase = 0
count_lowercase = 0

for letter in word:
    if letter.isupper():
        count_uppercase += 1
    elif letter.islower():
        count_lowercase += 1

if count_lowercase >= count_uppercase:
    print(word.lower())
else:
    print(word.upper())