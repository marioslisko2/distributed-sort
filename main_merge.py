import os
import time
import random

print("\nUsporedba merge sorta:")
print("Elemenata:\t Distribuirano:\t Normalno:")

n = 1000 #definiramo broj elemenata

while(n<=2000000): #petlja se izvršava dok broj elemenata ne dode do dva milijuna

    afile = open("Random.txt", "w" ) #kreiramo datoteku Random.txt

    for i in range(n): #u kreiranu datoteku se sprema n random brojeva
        line = str(random.randint(1, n))
        afile.write(line)
        afile.write("\n")

    afile.close()

    start1 = time.time() #biljezimo vrijeme prije pocetka distribuiranog sorta
    os.system("mpiexec -np 4 py distributed_merge.py") #u terminalu se poziva datoteka distributed_merge.py pomoći mpiexec funkcije s 4 procesa
    end1 = time.time() #i vrijeme nakon zavrsetka

    start2 = time.time() #pohranjujemo vrijeme prije obicnog sorta
    os.system("py normal_merge.py") #u terminalu normalno pozivamo datoteku funkcijom py
    end2 = time.time() #i opet vrijeme nakon zavrsetka

    print("%i\t\t %.2fs\t\t %.2fs"%(n, float(end1-start1), float(end2-start2))) #ispisujemo koliko elemenata se koristilo i razliku vremena prije pocetka i nakon zavrsetka

    if(n==1000000): #samo ako je broj elemenata milijun mnozi se s 2
        n*=2
    else:
        n*=10 #u svakoj iteraciji broj elemenata se mnozi sa 10
    
    afile = open("Random.txt", "w" ) #ponovo otvaramo file kako bi ga ocistili od podataka i time pripremili za iduce pokretanje petlje
    afile.truncate(0) #funkcija truncate(0) brise sve podatke iz datoteke
    afile.close()

"""
#afile = open("Random.txt", "r")
#print(afile.read())
#afile.close()
"""
