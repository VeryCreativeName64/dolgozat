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
        
def feladat_5():
    felhasznalo_tippje=input("Válassz kő, papír, vagy olló közül: ").lower()
    gep_tippje=int(random.random()*3+1)
    while(felhasznalo_tippje!="kő" and felhasznalo_tippje!="papír" and felhasznalo_tippje!="olló"):
        felhasznalo_tippje=input("Mondom válassz kő, papír, vagy olló közül: ").lower()
    else:
        if(felhasznalo_tippje=="kő" and gep_tippje==1):
            print("Döntetlen, ugyanúgy kőre gondoltunk!")
        elif(felhasznalo_tippje=="papír" and gep_tippje==2):
            print("Döntetlen, ugyanúgy papírra gondoltunk!")
        elif(felhasznalo_tippje=="olló" and gep_tippje==3):
            print("Döntetlen, ugyanúgy ollóra gondoltunk!")
        elif(felhasznalo_tippje=="kő" and gep_tippje==2):
            print("Te kőre, én papírra gondoltam, így nyertem!")
        elif(felhasznalo_tippje=="kő" and gep_tippje==3):
            print("Te kőre, én ollóra gondoltam, így nyertél!")
        elif(felhasznalo_tippje=="papír" and gep_tippje==1):
            print("Te papírra, én kőre gondoltam, így nyertél!")
        elif(felhasznalo_tippje=="papír" and gep_tippje==3):
            print("Te papírra, én ollóra gondoltam, így nyertem!")
        elif(felhasznalo_tippje=="olló" and gep_tippje==1):
            print("Te ollóra, én kőre gondoltam, így nyertem!")
        elif(felhasznalo_tippje=="olló" and gep_tippje==2):
            print("Te ollóra, én papírra gondoltam, így nyertél!")


    




