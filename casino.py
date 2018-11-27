# -*- coding: utf-8 -*-

# import random
# secret = random.randint(1, 101)       "Kot dodatek, da je bolj zanimivo lahko dodamo naključno število.
#                                       Če dodamo naključno število, je potrebno izbrisati 7 vrstico"

secret = 25
guess = int(raw_input("Uganite število med 1 in 50: "))

if secret == guess:
    print("Čestitamo! Uganili ste število!")
else: print("Žal število ni pravilno, poizkusite ponovno. Število je bilo: "), secret