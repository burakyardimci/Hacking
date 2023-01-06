with open("products.txt","r") as file:
    products=[]
    for line in file:
        stripped=line.strip()
        splitted=stripped.split(" ")
        products.append(splitted)
with open("purchases.txt","r") as purch:
    purchases=[]
    for char in purch:
        fstripped=char.strip()
        fsplitted=fstripped.split(" ")
        purchases.append(fsplitted)
    a=0
    suspicious=[]
    for eleman in range(len(products)):
        for karakter in range(len(purchases)):
            if purchases[karakter][0]==products[eleman][0]:
                if purchases[karakter][1]!=products[eleman][1]:
                    suspicious.append(purchases[karakter])
                    suspicious[a].append(products[eleman][1])
                    a+=1

    print("suspicious transactions list")
    print()
    for eleman in range(len(suspicious)):
        print(f"Product code: {suspicious[eleman][0]}")
        print(f"Official dealer: {suspicious[eleman][2]}")
        print(f"Dealer List: {str(suspicious[eleman][1])} {str(suspicious[eleman][2])}")
        print()










