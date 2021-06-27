import sys
import os
import pickle
from IPython.display import clear_output
#inventories={}
class product:
    def __init__(self):
        Name=input('Enter Product Name - >')
        Category=input('Enter Product Category - >')
        Id=input('Enter Product ID - >')
        Price=input('Enter Product Price - >')
        while True:
            try:
                Qty=int(input('Enter Product Quantity - >'))
            except:
                continue
            else:
                break
        self.name=Name
        self.category=Category
        self.ID=Id
        self.price=Price
        self.qty=Qty
    def change_name(self):
        Name=input('Enter new name->')
        self.name=Name
    def change_category(self):
        Category=input('Enter new category for the product->')
        self.category=Category
    def change_id(self):
        Id=input('Enter new ID->')
        self.ID=Id
    def change_price(self):
        Price=input('Enter new price->')
        self.price=Price
    def change_quantity(self,change):
        self.qty=self.qty+change
    def __str__(self):
        n='NAME'.ljust(9)
        c='CATEGORY'.ljust(9)
        i='ID'.ljust(9)
        p='PRICE'.ljust(9)
        q='QUANTITY'.ljust(9)
        return f'{n} : {self.name}\n{c} : {self.category}\n{i} : {self.ID}\n{p} : {self.price}\n{q} : {self.qty}'
    
class inventory():
    def __init__(self):
        self.name=input('Enter the name of your inventory - >')
        self.all_products=[]
    def add_purchase(self):
        purchase=list(input('Enter purchase in the format ID1 Qty1 ID2 Qty2....').split())
        for i in range(0,len(purchase),2):
            idofitem=purchase[i]
            qtyofitem=int(purchase[i+1])
            for p in self.all_products:
                if p.ID==idofitem:
                    p.change_quantity(qtyofitem)
                    break
        print('Purchase added successfully')
        nothing = input()
    def new_sale(self):
        sale=list(input('Enter sale in the format ID1 Qty1 ID2 Qty2....').split())
        for i in range(0,len(sale),2):
            idofitem=sale[i]
            qtyofitem=int(sale[i+1])
            for p in self.all_products:
                if p.ID==idofitem:
                    p.change_quantity(qtyofitem*(-1))
                    break
        print('Sale successful')
        nothing=input()
    def add_new_product(self):
        while True:
            new_prod=product()
            self.all_products.append(new_prod)
            print('New product added successfully')
            response=''
            while response not in ['Y','N']:
                response=input('Do you wish to add one more product ? (Y/N)')
            if response=='N':
                break
    def print_inventory(self):
        print("ID".ljust(10),'NAME'.ljust(20),'QUANTITY'.ljust(5),sep='     ')
        for p in self.all_products:
            print(p.ID.ljust(10),p.name.ljust(20),str(p.qty).ljust(5),sep='     ')
        nothing=input()
            
    def edit_a_product(self):
        prodid=''
        idlist=[p.ID for p in self.all_products]
        while prodid not in idlist:
            prodid=input('Enter product ID to edit the product information')
        producttochange=None
        for p in self.all_products:
            if p.ID==prodid:
                producttochange=p
                break
        while True:
            clear_output()
            print('Edit Product Page')
            print('1.Change Name')
            print('2.Change Category')
            print('3.Change ID')
            print('4.Change Price')
            print('5.Re-Enter new ID')
            print('6.Done')
            choice=''
            while choice not in ['1','2','3','4','5','6']:
                choice=input('Enter your choice (1 to 6)')
            if choice=='1':
                producttochange.change_name()
            elif choice=='2':
                producttochange.change_category()
            elif choice=='3':
                producttochange.change_id()
            elif choice=='4':
                producttochange.change_price()
            elif choice=='5':
                self.edit_a_product()
                break
            else:
                break
            

def main_page():
    while True:
        clear_output()
        print('MAIN PAGE')
        print('1.New Inventory')
        print('2.Open Inventory')
        print('3.Exit')
        choice=''
        while choice not in ['1','2','3']:
            choice=input('Enter your choice')
        if choice=='3':
            with open('inventories_file.bin', 'wb') as f:
                pickle.dump(inventories,f)
            sys.exit()
        if choice=='1':
            newinventory=inventory()
            inventories[newinventory.name]=newinventory
            inventory_open_page(newinventory)
        else:
            response=input('Enter the name of your inventory')
            while response not in list(inventories.keys()):
                response=input('Enter the name of your inventory')
            inventory_open_page(inventories[response])
            
def inventory_open_page(invent):
    while True:
        clear_output()
        print('INVENTORY OPEN PAGE')
        print('1.Add new purchase')
        print('2.Add new sale')
        print('3.Add new product')
        print('4.Edit a product')
        print('5.Display inventory')
        print('6.Back to the main menu')
        choice=''
        while choice not in ['1','2','3','4','5','6']:
            choice=input('Enter your choice')
        if choice=='1':
            invent.add_purchase()
        elif choice=='2':
            invent.new_sale()
        elif choice=='3':
            invent.add_new_product()
        elif choice=='4':
            invent.edit_a_product()
        elif choice=='5':
            invent.print_inventory()
        else:
            break
    
if __name__=='__main__':
    filesize = os. path. getsize("inventories_file.bin")
    if filesize != 0:
        with open('inventories_file.bin', 'rb') as f:
            inventories = pickle.load(f)
    else:
        inventories={}
    main_page()
