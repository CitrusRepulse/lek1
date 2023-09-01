# Denna uppgift ska vi öva variabler, vilkor och loopar!
import random
import os
os.system("cls" if os.name == "nt" else "clear")

print("\m-----------------------------------------------------------------------")
print(".:Gissa:.")

print("gissa ett tal mellan 1 & 10 & pröva lyckan, du får 3 försök!\n")

slumptal = random.randint(1, 10)

#print(slumptal)

i=0
hitta = False

#loop

while i < 3:

    gissatal = input("mata in tal: ")

    if slumptal == int(gissatal):
        hitta = True
        print("\n Rätt svar!\n")
        break

    i += 1


if hitta:
    print("\n Bra jobbat, här har du en anka")


else:
    print("Ajajaj nu får du nog försöka igen lycka till lilla du...")

print("\n----------------------------------------------------------------------------")