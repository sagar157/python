def reverse_string(str):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for i in str:
        if i in vowels:
            count = count + 1
            if count > 2:
                return true
            else:
                return false

