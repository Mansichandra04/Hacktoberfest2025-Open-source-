n = int(input("Enter number: "))
s = sum(int(d)**len(str(n)) for d in str(n))
print("Armstrong!" if s == n else "Not Armstrong!")
