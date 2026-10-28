
import random

liczbaPrób = 6 #liczba prób
liczbaGuessow = 1

losowaLiczba = random.randrange(1, 101) #losowanie jednej liczby od 1 do 100

user = int(input("Zgadnij liczbe: "))


while user != losowaLiczba:
    if user > losowaLiczba:
            print("Za dużo") 
    else:
            print("za mało")
    user = int(input("Zgadnij liczbe: "))
    liczbaGuessow += 1
    liczbaPrób -= 1 
    if liczbaPrób == 0:
           print("nie udało sie cie zgadnąć")
           break
    

if user == losowaLiczba:
    print("Brawo zgadłes w ", liczbaGuessow , "próbach")   
    print("Liczba było: ", losowaLiczba)   





