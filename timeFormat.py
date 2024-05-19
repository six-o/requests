month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
         "December"]

dic = {}
for m in month:
    if m == "February":
        dic[m] = 28
    elif m in ["April", "June", "September", "November"]:
        dic[m] = 30
    else:
        dic[m] = 31

for a in dic:
    print(a, "has", dic[a], "days.")
