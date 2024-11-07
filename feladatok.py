import random

def feladat_1():
    paros:int=int(input("Kérek egy páros számot: "))
    while(paros%2!=0):
        paros:int=int(input("Ez nem páros! PÁROS számot kérek: "))
    if(paros%2==0):
        print(paros)

def feladat_2():
    lista=[]
    for i in range(0,14,1):
        szam:int=int(random.random()*141+10)
        lista.append(szam)
    i=0
    harmas=0
    while(i<len(lista)):
        if(lista[i]%3==0):
            harmas+=1
        i+=1
    if(i==len(lista)):
        print(f"A számok között {harmas} db 3-mal osztható van!")

def feladat_4():
    nevek=input("Adj meg tetszőleges számú nevet! Ha elég volt, írj @ karaktert! Már meg is adhatod az elsőt: ")
    db=0
    while(nevek!="@"):
        nevek=input("Add meg a következő nevet: ")
        db+=1
    if(nevek=="@"):
        print(f"A felhasználó {db} nevet adott meg.")
        




