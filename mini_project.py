
'''#HOTEL FOOD ORDER ....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
menu = {
    1: {"item": "Idli", "price": 40},
    2: {"item": "Dosa", "price": 60},
    3: {"item": "Vada", "price": 50},
    4: {"item": "Poori", "price": 70},
    5: {"item": "Tea", "price": 20},
    6: {"item": "Coffee", "price": 30}
}

customer_name = input("Enter customer name: ")
table=int(input("enter the table numbers:"))
order_items = []     
order_prices = []    

print("\n------ HOTEL MENU ------")
for key, value in menu.items():
    print(key, value["item"], "-", value["price"])

while True:
    choice = int(input("\nEnter item number to order (0 to stop): "))

    if choice == 0:
        break
    elif choice in menu:
        order_items.append(menu[choice]["item"])
        order_prices.append(menu[choice]["price"])
        print(menu[choice]["item"], "added to your order")
    else:
        print("Invalid choice")
        

total = sum(order_prices)
gst = total * 0.05
final_amount = total + gst

print("\n------ BILL ------")
print("Customer Name:", customer_name)
print("Ordered Items:", order_items)
print("Total Amount:", total)
print("GST (5%):", gst)
print("Final Amount to Pay:", final_amount)'''





#