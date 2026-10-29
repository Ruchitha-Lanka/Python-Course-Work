word = input("Enter a word:")
rev = ""
for i in range(len(word)-1,-1,-1):
    rev = rev+ word[i]

if word == rev:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
