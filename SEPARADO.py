def vestido(total):
    while True:
        print ("""|=============================|
|          VESTIDOS           |
|=============================|
| A |LYOCELL    | S/40.00     |
| B |CANALÉ     | S/35.00     |
| C |CAMISERO   | S/45.00     |
| D |DRAPEADO   | S/40.00     |
| E |======== SALIR===========|
|=============================|""")
        ido=input ("|OPCIÓN:...:").upper()
        if ido=="A":
            total+=40.00
        elif ido=="B":
            total+=35.00
        elif ido=="C":
            total+=45.00
        elif ido=="D":
            total+=40.00
        elif ido=="E":
            break
        else:
            print ("OPCIÓN INCORRECTA")
        return total
def blusas(total):
    while True:
        print ("""|=============================|
|           BLUSAS            |
|=============================|
| A |LYOCELL    | S/30.00     |
| B |OVERSIZE   | S/35.00     |
| C |ANUDADO    | S/35.00     |
| D |POPELINA   | S/40.00     |
| E |======== SALIR===========|
|=============================|""")
        usas=input ("|OPCIÓN:...:").upper()
        if usas=="A":
            total+=30.00
        elif usas=="B":
            total+=35.00
        elif usas=="C":
            total+=35.00
        elif usas=="D":
            total+=40.00
        elif usas=="E":
            break
        else:
            print ("OPCIÓN INCORRECTA")
        return total
def faldas(total):
    while True:
        print ("""|=============================|
|           FALDAS            |
|=============================|
| A |CRUZADA    | S/50.00     |
| B |DENIM      | S/30.00     |
| C |EVASÉ      | S/35.00     |
| D |ESTAMPADA  | S/40.00     |
| E |======== SALIR===========|
|=============================|""")
        aldas=input ("|OPCIÓN:...:").upper()
        if aldas=="A":
            total+=50.00
        elif aldas=="B":
            total+=30.00
        elif aldas=="C":
            total+=35.00
        elif aldas=="D":
             total+=40.00
        elif aldas=="E":
            break
        else:
            print ("OPCIÓN INCORRECTA")
        return total
def cardigans(total):
    while True:
        print ("""|=============================|
|         CARDIGANS           |
|=============================|
| A |POINTELLE  | S/27.00     |
| B |CANALÉ     | S/30.00     |
| C |ESCOTE     | S/25.00     |
| D |GOFRADO    | S/28.00     |
| E |======== SALIR===========|
|=============================|""")
        digans=input ("|OPCIÓN:...:").upper()
        if digans=="A":
            total+=27.00
        elif digans=="B":
            total+=30.00
        elif digans=="C":
             total+=25.00
        elif digans=="D":
             total+=28.00
        elif digans=="E":
            break
        else:
            print ("OPCIÓN INCORRECTA")
        return total


total=0
vestidoss=0
blusass=0
cardiganss=0
faldass=0
while True:
    print ("""|=============================|
|         CATEGORÍAS          |
|=============================|
| A |VESTIDO                  |
| B |BLUSAS                   |
| C |CARDIGANS                |
| D |FALDAS                   |
| E |======== SALIR===========|
|=============================|""")
    mu=input ("|OPCIÓN:...:").upper()
    if mu=="A":
        vestidoss=vestido(total)
    elif mu=="B":
        blusass=blusas(total)
    elif mu=="C":
        cardiganss=cardigans(total)
    elif mu=="D":
        faldass=faldas(total)
    elif mu=="E":
         break
    else:
            print ("OPCIÓN INCORRECTA")
          
neto=vestidoss+blusass+cardiganss+faldass
print(vestidoss);print(blusass);print(cardiganss);print(faldass)
print("|===TOTAL A PAGAR: S/","{0:.2f}".format(neto),"===|")
print("|==GRACIAS POR SU PREFERENCIA=|")
print("|=============================|")



##################################################################
##################################################################

def polos(total):
    while True:
        print("""|=================================|
|       POLOS OVERSIZE        |
|=============================|
| A |SLIM     |S/15.00        |
| B |CAMISERO |S/17.00        |
| C |OVERSIZE |S/20.00        |
| D |========= SALIR =========|
|=============================|""")
        opa=input("|OPCION:..:").upper()
        if opa=="A":
            total+=15.00
        elif opa=="B":
            total+=17.00
        elif opa=="C":
            total+=20.00
        elif opa=="D":
            break
        else:
            print("OPCION INCORRECTA")
        return total
def poleras(total):
    while True:
        print("""|=================================|
|        POLERAS              |
|=============================|
| A |OVERSIZE    |S/40.00     |
| B |CON CAPUCHA |S/42.00     |
| C |SIN CAPUCHA |S/45.00     |
| D |========= SALIR =========|
|=============================|""")
        opb=input("|OPCION:..:").upper()  
        if opb=="A": 
             total+=40.00
        elif opb=="B":
             total+=42.00
        elif opb=="C":
             total+=45.00
        elif opb=="D":
            break
        else:
            print("OPCION INCORRECTA")
        return total

 

def pantalones(total):
    while True:
        print("""|============
|       PANTALONES            |
|=============================|
| A |JOGGER |S/25.00          |
| B |BUZOS  |S/40.00          |
| C |JEANS  |S/45.00          |
| D |========= SALIR =========|
|=============================|""")
        opn=input("|OPCION:..:").upper()
        if opn=="A":
             total+=25.00
        elif opn=="B":
             total+=40.00
        elif opn=="C":
             total+=45.00
        elif opn=="D":
            break
        else:
             print("OPCION INCORRECTA")
        return total


def casacas(total):
    while True:
        print("""|============
|       CASACAS               |
|=============================|
| A |BLAZER    |S/25.00       |
| B |PARKA     |S/40.00       |
| C |CHAQUETA  |S/45.00       |
| D |========= SALIR =========|
|=============================|""")
        opm=input("|OPCION:..:").upper() 
        if opm=="A":
             total+=25.00
        elif opm=="B":
             total+=40.00
        elif opm=="C":
             total+=45.00
        elif opm=="D":
            break
        return total
poloss=0
polerass=0
pantaloness=0
casacass=0
while True:
    print ("""|=============================|
|         CATEGORÍAS          |
|=============================|
| A |POLOS                    |
| B |POLERAS                  |
| C |PANTALONES               |
| D |CASACAS                  |
| E |======== SALIR===========|
|=============================|""")
    ho=input ("|OPCIÓN:...:").upper()
    if ho=="A":
        poloss=polos(total)
    elif ho=="B":
        polerass=poleras(total)
    elif ho=="C":
        pantaloness=pantalones(total)
    elif ho=="D":
        casacass=casacas(total)
    elif ho=="E":
        break
    else:
         print ("OPCIÓN INCORRECTA")
         
neto=poloss+polerass+pantaloness+casacass
print(poloss);print(polerass);print(pantaloness);print(casacass)
print("|===TOTAL A PAGAR: S/","{0:.2f}".format(neto),"===|")
print("|==GRACIAS POR SU PREFERENCIA=|")
print("|=============================|")









        
    


        





