def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y



menu = 0
print("Välkommen till miniräknaren")
while menu < 5:
    print(" 1 Räkna med +\n 2 Räkna med -\n 3 Räkna med *\n 4 Valfritt arbete om du vill\n 5 Avsluta")
    menu = int(input("Välj meny inställning: "))
    if menu > 4:
        print("Ha det bra")
    else:
        print("Du valde " + str(menu))
while True:
    choice = input
    if choice in ('[1]', '[2]', '[3]', '[4]'):
        num1 = float(input("skriv in första numret: "))
        num2 = float(input("skriv in andra numret: "))
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))