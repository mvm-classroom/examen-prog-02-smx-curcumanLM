#Generador de noms incorrectes per Timothée Chalamet

# Posa aquí qualsevol import que necessitis com rand, math, time...
import random


def obtenir_nom():
    
    noms = ["Timotei", "Timonel", "Timbaler", "Tennebaum", "TaoPaiPai", "Teruel", "Tirolés", "Traginer", "Tourmalet"]
    cognoms = ["Chandalet", "Camembert", "Sabadell", "Chevrolet", "Caganer", "Bechamel", "Casteller", "Churumbel", "Cafeaulait", "Crivillé", "Charmander"]

    nom = random.choice(noms)
    cognom = random.choice(cognoms)

    return nom + "" + cognom
    # Aquí has de construir un nom amb un nomb aleatori i un cognom aleatori de les llistes
    # retornar el nom construït

def afegir_nom(llista):
    nou_nom = obtenir_nom()
    llista.append(nou_nom)
    print(f"S'ha afegit un nou nom:"{nou_nom})
    # Hem d'obtenir un nom aleatori, afegir-lo a la llista i mostrar per pantalla que hem afegit aquest nom

def llistar_noms(llista):
    print("PENDENT: llistar_noms")
    # Hem de mostrar per pantalla tots els noms que hem afegit a la llista

def ordenar_noms(llista):
    print("PENDENT: ordenar_noms")
    # Hem d'ordenar la llista de noms
    # Un cop ordenada la llista, llistem tots els noms

def mostrar_menu():
    print("----Menu----")
    print("(A)--Afegir-Nom")
    print("(L)--Llistar-Noms")
    print("(O)-Ordenar-Noms")
    print("(F)-Finalitzar")
    # Hem de mostrar el menú que ens demanen a l'enunciat


def demanar_opcio():
    opcions = ["A", "L", "O", "F"]
    while True:
        opcio = input("Selecciona una opció").lower()
    
    if opcio in opcions
    # Hem de demanar a l'usuari una de les opcions del menú
    # Si ens introdueix un valor incorrecte hem de tornar a mostrar el menú i tornar a demanar opció
    # Si ens introdueix la lletra correcta en minúscula, la donarem per bona
    # Retornarem l'opció correcta sel.leccionada        

def gestionar_opcio(opcio, llista):
    print("PENDENT: gestionar_opcio")
    match opcio:
        case "A":
            afegir_nom
        case "L":
            llistar_noms
        case "O":
            ordenar_noms
        case "F":



    # En funció de l'opció escollida per l'usuari, haurem de cridar a les funcions adients per fer el que ens demanen
    # Heu de fer servir `match`
    # Si no ho sabeu fer amb `match` podeu utilitzar altres estructures condicionals però no obtindreu tota la puntuació    



# Programa principal

print("PENDENT: programa principal")
# Heu de treballar amb una llista a la que li farem diverses operacions mostrades al menú
# Si ens introdueixen l'opció "F" acabarem el programa
# Si no ens introdueixen l'opció "F" farem l'acció corresponent i tornarem a preguntar
