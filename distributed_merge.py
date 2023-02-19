#definiranje merge sort algoritma u 2 funkcije

def merge_sort(list):
    list_length = len(list) #spremamo duljinu liste
    
    if list_length==1: #provjeravamo da li smo došli do zadnjeg elementa
        return list    #vraćamo sortiranu listu

    mid_point = list_length//2 #pronalazimo srednji element liste te djelimo listu na lijevu i desnu particiju
    left_partition=merge_sort(list[:mid_point]) #rekurzivno pozivamo merge_sort funkciju
    right_partition=merge_sort(list[mid_point:])

    return merge(left_partition, right_partition) #pozivamo merge funkciju za sortiranu particije

#Funkcija merge uzima dvije liste i vraća ih kao jednu sortiranu listu
def merge(left, right):
    output = []
    i = j = 0

    while i<len(left) and j<len(right): #Petlja se izršava dok su definirani "i" i "j" manji od duljine lijeve i desne liste
        if left[i]<right[j]: #Uspoređujemo obje liste za svaku iteraciju
            output.append(left[i]) #U output listu dodajemo manju vrijednost
            i+=1 
        else:
            output.append(right[j]) 
            j+=1
            
    output.extend(left[i:]) #U output se pohranjuju ostale vrijednosti na kraj liste
    output.extend(right[j:])

    return output

import math
from mpi4py import MPI

comm = MPI.COMM_WORLD 
rank = comm.Get_rank() #dohvacamo rang procesa

root = 0
max_processes = comm.size #dohvacamo ukupan broj procesa
data = []

with open("Random.txt") as file: #Otvaramo kreiranu datoteku s random brojevima i spremamo je u listu
    while line := file.readline().rstrip():
        data.append(int(line))

new_list = []

bin_size = math.floor(int((max(data)-min(data))/comm.size)) #Oduzimamo max i min element te ih dijelimo s brojem procesa

for rank in range(max_processes): #Kreiramo listu koja sadrzi 4 podliste (jer smo definirali 4 procesa)
    new_list.append([x for x in data if (x>=bin_size*rank+rank) and x<=(bin_size+bin_size*rank+rank)]) #pomocu bin_size odredujemo koji element pridruzujemo kojoj listi

v = comm.scatter(new_list,root) #scatter funkcija daje svakom procesu jednu od podlisti
#print("Rank:",comm.rank, " ", v)

mrgSort = merge_sort(v) #pozivanje merge_sort funkcije

g = comm.gather(mrgSort,root) #gather funkcija vraca listu podlisti koje su sortirane
g2 = [item for sublist in g for item in sublist] #pretavaranje u jednu listu bez podlista

file.close()

"""
if comm.rank==0:
    
    print(g2)
"""