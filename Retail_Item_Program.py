import Retail_Item_Class as rc

def main():

    item1 = rc.RetailItem('Jacket', 12, 59.95)
    item2 = rc.RetailItem('Designer Jeans', 40, 34.95)
    item3 = rc.RetailItem('Shirt', 20, 24.95)

    print(item1.get_descr())

main()