a = int(input("Ievadiet cilvēka masu: "))
b = int(input("Ievadiet cilvēka masu: "))
c = int(input("Ievadiet cilvēka masu: "))
print(a + b + c)
print(a + b + c / 3)

if a + b + c > 300:
  print("Cilvēki nedrīkst braukt liftā")
if a + b + c < 300:
  print("Cilvēki drīksts braukt liftā")