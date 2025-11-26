def print_menu():
    print("\nBoudreaux & Thibodeaux's Restaurant")
    print("------------------------------------")
    print("1. Croissant: $3.95")
    print("2. King Cake Slice: $4.95")
    print("3. Crawfish Pie (By the Slice): $3.65")
    print("4. Catfish Poboy: $14.95")
    print("5. Roast Beef Poboy: $13.95")
    print("6. Sausage Poboy: $12.95")
    print("7. Gumbo: $5.95")
    print("-------------------------------------")

def calculate_crawfish_pie(slices):
    whole_pies = slices // 8
    remaining_slices = slices % 8
    total_cost = (whole_pies * 22.0) + (remaining_slices * 3.65)
    return whole_pies, remaining_slices, total_cost

def main():
    menu = {
        1: ("Croissant", 3.95),
        2: ("King Cake Slice", 4.95),
        3: ("Crawfish Pie (By the Slice)", 3.65),
        4: ("Catfish Poboy", 14.95),
        5: ("Roast Beef Poboy", 13.95),
        6: ("Sausage Poboy", 12.95),
        7: ("Gumbo", 5.95)
    }
    
    subtotal = 0.0
    sales_tax_rate = 0.0945
    
    print_menu()
    
    while True:
        user_input = input("\nWhat would you like to order? Type the appropriate number of the menu item or DONE when order is complete: ")
        
        if user_input.lower() == "done":
            break
        
        try:
            item_num = int(user_input)
            if item_num not in menu:
                print("Invalid menu item. Please try again.")
                print_menu()
                continue
        except ValueError:
            print("Invalid input. Please enter a number or DONE.")
            print_menu()
            continue
        
        try:
            quantity = int(input("Quantity: "))
            if quantity <= 0:
                print("Quantity must be positive. Please try again.")
                print_menu()
                continue
        except ValueError:
            print("Invalid quantity. Please try again.")
            print_menu()
            continue
        
        item_name, item_price = menu[item_num]
        
        if item_num == 3:
            whole_pies, remaining_slices, cost = calculate_crawfish_pie(quantity)
            if whole_pies > 0:
                print(f"Item added: {whole_pies} x Crawfish Pie - ${whole_pies * 22.0:.2f}")
            if remaining_slices > 0:
                print(f"Item added: {remaining_slices} x Crawfish Slice - ${remaining_slices * 3.65:.2f}")
            subtotal += cost
        else:
            cost = quantity * item_price
            print(f"Item added: {quantity} x {item_name} - ${item_price:.2f} each")
            subtotal += cost
        
        print_menu()
    
    total = subtotal * (1 + sales_tax_rate)
    print("\n------------------------")
    print(f"Your total is ${total:.2f}")

if __name__ == "__main__":
    main()
            
