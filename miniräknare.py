menu = 0
print("Välkommen till miniräknaren")
while menu < 5:
    print(" [1] Räkna med +\n [2] Räkna med -\n [3] Räkna med *\n [4] Valfritt arbete om du vill\n [5] Avsluta")
    menu = int(input("Välj meny inställning: "))
    if menu > 4:
        print("Ha det bra")
    else:
        print("Du valde " + str(menu))