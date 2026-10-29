
listHuman = {"Andzej:" : 13, "Kuba:" : 18, "Julka: " : 16, "Maks:" : 12}

while listHuman:
    highestAge = 0
    for human in listHuman:
        if listHuman[human] > highestAge:
            highestAge = listHuman[human]
            oldest = human
        
    print(oldest, highestAge)
    del listHuman[oldest]
    

