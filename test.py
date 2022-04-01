a = ["Aku sudah gila", "Kamu sudah gila", "Aku dan Kamu", "Kita"]

for i in range(len(a)):
    if ("Aku" not in a[i]):
        a[i] = "x"
    else:
        pass

print(a)
