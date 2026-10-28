

i = input("Podaj liczbe: ")
tab = []

for num in i:
    num = int(num)
    tab.append(num)

wynik = sum(tab)
print(wynik)