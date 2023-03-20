def reverse(str):
    str = str[::-1]
    return str
vowels = ["a", "e", "i", "o", "u"]
count = 0


for character in str:
    if character in vowels:
        count += 1


s = "Jkt training"

print(reverse(s))