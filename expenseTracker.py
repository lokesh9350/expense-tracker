def menu():
   print("1.Add Expense")
   print("2.View Expenses")
   print("3.Exit")


def add_expense(iname,iprice):
    einame=input("Enter item name   :")
    eiprice=int(input("Enter item price :"))
    iname.append(einame)
    iprice.append(eiprice)
def view_expense(iname,iprice):
    for i in range(len(iname)):
        print("Item ",i+1,"Name :",iname[i])
        print("Item",i+1,"Price :",iprice[i])


def main():
    iname=[]
    iprice=[]
    while True:
        menu()
        ch=int(input("Enter choice :"))
        if ch==1:
            add_expense(iname,iprice)
        elif ch==2:
            view_expense(iname,iprice)
        elif ch==3:
            print("Thanks")
            break
        else:
            print("Invalid Choice")

main()
    
    
