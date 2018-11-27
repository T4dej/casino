# -*- coding: utf-8 -*-

import random
secret = random.randint(1, 101)

guess = 0
tr = 0

while True:
    guess = int(raw_input("Uganite število med 1 in 100: "))
    tr = tr + 1

    if secret == guess:
        print("Čestitamo! Uganili ste število " + str(secret) + " v " + str(tr) + ". poizkusu!")
        break
    elif secret>guess:
        print("Žal, iskano število je večje. Poizkusite ponovno.")
    elif secret<guess:
        print("Žal, iskano število je manjše. Poizkusite ponovno")