#change machine
try:
    Credit=int(input("insert credit: "))


    Money = [10,5,1]
    billsReturned = []

    def change(Credit):
        for i in Money:
            while Credit >=i:
                billsReturned.append(i)
            Credit -= i
    print(billsReturned)


    change(Credit)

except ValueError:
    print("need a number")
#deployed by bryan Moreno