
text = "abracadabra"

result = {}

for char in text:
    if char in result:
        result[char] = result[char] + 1
    else:
        result[char] = 1

for i in range(3):
    highest = 0
    most_common = ""
    for maxChar in result:
        if result[maxChar] > highest or (
            result[maxChar] == highest and maxChar < most_common
        ):
            highest = result[maxChar]
            most_common = maxChar
    print(most_common, ": ", highest)
    del result[most_common]
