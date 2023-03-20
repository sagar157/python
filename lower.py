test_str = "vidyasagar"

print("The original string is : " + str(test_str))
res = ""
for idx in range(len(test_str)):
    if not idx % 2:
        res = res + test_str[idx].upper()
    else:
        res = res + test_str[idx].lower()

print("The alternate case string is : " + str(res))
