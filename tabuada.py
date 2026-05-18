tab = int(input("Tabuada de qual numero? "))
print(f"--- Tabuada do {tab}---")
for i in range(1,11):
    res = tab * i
    print(f"{tab} x {i} = {res}")