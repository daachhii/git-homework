x = input()

MyList = []
TrueOrFalse = True

for i in range(len(x)):
    MyList.append(x[i])

for i in range(len(MyList)):
    for k in range(i + 1, len(MyList)):
        if MyList[i] == MyList[k]:
            TrueOrFalse = False

if TrueOrFalse:
    print(True)
else:
    print(False)
