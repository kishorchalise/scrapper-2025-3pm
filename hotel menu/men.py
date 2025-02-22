menu = {
    "pizza": 400,
    "burger": 200,
    "fries": 100,
    "momo": 200,
    "jhol momo": 250,
}
print("welcome to kishor restaurants")
print("pizza: Rs400\nburger: Rs200\nfries: Rs100\nmomo: Rs200\njhol momo: Rs250")
order_total=0
item_1 = input("enter your first item:")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} is added")
else:
    print("item not available")
another_item=input('do you want to order another item? (yes/n0)')
if another_item=='yes':
    item_2 = input("enter your second item:")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"{item_2} is added")
    else:
        print("item not available")
        
        
print(f"total amount of the ordered is : {order_total}")
 


