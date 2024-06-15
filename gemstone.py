flawed = float(input("Flawed price: "))
fine = float(input("Fine price: "))
flawless = float(input("Flawless price: "))
print("")

flawed2 = flawed/80
fine2 = fine/6400
flawless2 = flawless/512000
list = [flawed2, fine2, flawless2]

print("Flawed is", flawed2, "coins per rough")
print("Fine is", fine2, "coins per rough")
print("Flawless is", flawless2, "coins per rough\n")

if(max(list) < 3):
    print("Rough is best")
else:
    print(max(list), "is best")
input()