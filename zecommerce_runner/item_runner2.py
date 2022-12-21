from zecommerce_package.item_module import Item

a=10
print(type(a))

a=[]
print(type(a))

item1 = Item()
print(type(item1))

item2 = Item()

item1.qty=6
item1.price=100
item1.desc = "Laptop"

item2.desc = "Mobile"

# item1.print_item_detail()
#
# item2.print_item_detail()

item1.print_discounted_price()