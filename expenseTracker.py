def menu():
   print("1.Add Expense")
   print("2.View Expenses")
   print("3.Total Expense")
   print("4.Exit")


def add_expense(iname,iprice):
    einame=input("Enter item name   :")
    eiprice=int(input("Enter item price :"))
    iname.append(einame)
    iprice.append(eiprice)
def view_expense(iname,iprice):
    for i in range(len(iname)):
        print("Item ",i+1,"Name :",iname[i])
        print("Item",i+1,"Price :",iprice[i])
def total_expense(iprice):
    tot=0
    for i in range(len(iprice)):
        tot=tot+iprice[i]
    
    print("Total  :",sum)


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
            total_expense(iprice)
        elif ch==4:
           search_expense()

        elif ch==5:
            print("Thanks")
            break
        else:
            print("Invalid Choice")

main()
    
    
