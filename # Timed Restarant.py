def display_menu():
    print("\nBoudreaux & Thibodeauz's Restarant")
    print("-" * 35)
    print("1. Croissant: $3.95")
    print("2. King cake Slice: $4.95")
    print("3. CrawFish Pie (By the slice): $3.65")
    print("4. Catfish Poboy: $14.95")
    print("5. Roast Beef Poboy: $13.95")
    print("6. Sausage Poboy: $12.95")
    print("7. Gumbo: $5.95")
    print("-" * 35)

    def get_item_info(item_number):
        menu = {
            1: ("Croissant" , 3.95),
            2: ("King Cake Slice", 4.95),
            3: ("Crawfish Pie (By the slice)" , 3.65),
            4: ("Catfish Poboy", 14.95),
            5: ("Roast Beef Poboy", 13.95),
            6: ("Sausage Poboy", 12.95),
            7: ("Gumbo", 5.95)
        }
        return menu.get(item_number, (None,0))
    
    def calculate_crawfish_pie_cost(slices):
        SLICE_PRICE = 3.65
        PIE_PRICE = 22.00
        SLICES_PER_PIE = 8

        whole_pies = slices // SLICES_PER_PIE
        remaining_slices = slices % SLICES_PER_PIE
        
        total = (whole_pies * PIE_PRICE) + remaining_slices * SLICE_PRICE
        return total, whole_pies, remaining_slices
    
    def main():
        SALES_TAX_RATE = 0.10
        order = []

        display_menu()

        while True:
            try:
                print("\nWhat would you like to order? Type the appropriate number of the menu item or DONE when order is complete:", end="")
                user_input = input().strip()

                if user_input.upper() == "DONE":
                    break

                item_number = int(user_input)

                if item_number < 1 or item_number > 7:
                    print("Invalid menu item. Please choose a number from 1 to 7.")
                    continue
                
                item_name, itme_price = get_item_info(item_number)

                print("Quantity:", end =" ")
                quantity = int(input())

                if quantity <= 0:
                    print("Quanitiy must be greater than  0.")
                    continue

                if item_number == 3:
                    total_cost, whole_pies, remaining_slices = calculate_crawfish_pie_cost(quantity)
                    order.append(("Crawfish Pie", quantity,total_cost))

                    if whole_pies > 0 and remaining_slices > 0:
                        print(f"Item added: {whole_pies} x Crawfish Pie - ${whole_pies * 22.00:.2f} and {remaining_slices} x Crawfish Slice - ${remaining_slices * 3.65:.2f}")
                    elif whole_pies > 0:
                        print(f"Item added: {whole_pies} x Crawfish Pie - ${total_cost:.2f}")
                    else:
                        print(f"Item added: {quantity} x Crawfish Slice - ${total_cost:.2f}")
                else:
                    total_cost = itme_price * quantity
                    order.append((item_name * quantity, total_cost))
                    print(f"Item added: {quantity} x {item_name} - ${total_cost:.2f}")

                    display_menu()

            except ValueError:
                print("Invalid input. Please enter a number or DONE.")
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")

                if order:
                    print("\n" + "-" * 35)
                    subtotal = sum(item[2] for item in order)
                    tax = subtotal * SALES_TAX_RATE
                    total = subtotal + tax
                    
                    print(f"Your total is ${total:.2f}")
                else:
                    print("\nNo items ordered.")

                if __name__ == "__main__":
                    main()

            