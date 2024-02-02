Credit=int(input("insert credit: "))


def change(Credit):
    Money = [10,5,1]
    billsReturned = []

    for i in Money:
        while Credit >=i:
            billsReturned.append(i)
            Credit -= i
    print(billsReturned)

change(Credit)