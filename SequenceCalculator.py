
n = int(input("Veuillez entrer un entier n : "))
U0 = 0


for i in range(1, n + 1):
    Un = 4 * U0 + 10
    U0 = Un

print("Alors Un est égale à :", Un)
