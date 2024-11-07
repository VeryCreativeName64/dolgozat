def feladat_1():
    paros:int=int(input("Kérek egy páros számot: "))
    while(paros%2!=0):
        paros:int=int(input("Ez nem páros! PÁROS számot kérek: "))
    if(paros%2==0):
        print(paros)