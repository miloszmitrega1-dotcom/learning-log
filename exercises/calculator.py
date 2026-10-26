
a = float(input("podaj A: "))
b = float(input("podaj B: "))

dodaw = a + b
odej = a - b
multi = a * b

if b != 0:
    dziel = a / b
else:
    dziel = "Nie dziel przez 0"

print("wyniki dodawnia: ", dodaw)
print("wyniki odejmowania: ", odej)
print("wyniki mnozenia: ", multi)
print("wyniki dzielenia: ", dziel)
