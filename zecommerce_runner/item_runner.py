from zecommerce_package.item_module import Item

item1 = Item()
item2 = Item()

item_lists=[item1,item2]

for item in item_lists:
    item.print_item_detail()

item1.desc = "Laptop"

item2.desc = "Mobile"

print(item1)
print(item2)

item1=item2

print(item1)
print(item2)

# print(item1.desc)
# print(item2.desc)
