# creating class
class shop:
    def __init__(self):
        self.shoe_data = [
        {"shoe_id": 1, "shoe_name": "Nike Air Max", "sizes": [7, 8, 9, 10, 11], "price": 120, "gender": "Men"},
        {"shoe_id": 2, "shoe_name": "Adidas Ultraboost", "sizes": [6, 7, 8, 9, 10, 11], "price": 180, "gender": "Unisex"},
        {"shoe_id": 3, "shoe_name": "Puma RS-X", "sizes": [7, 8, 9, 10], "price": 110, "gender": "Women"},
        {"shoe_id": 4, "shoe_name": "Reebok Classic", "sizes": [5, 6, 7, 8, 9], "price": 90, "gender": "Unisex"},
        {"shoe_id": 5, "shoe_name": "Under Armour HOVR", "sizes": [8, 9, 10, 11], "price": 140, "gender": "Men"},
        {"shoe_id": 6, "shoe_name": "Converse Chuck Taylor", "sizes": [6, 7, 8, 9], "price": 50, "gender": "Unisex"},
        {"shoe_id": 7, "shoe_name": "New Balance 990", "sizes": [9, 10, 11, 12], "price": 160, "gender": "Men"},
        {"shoe_id": 8, "shoe_name": "Vans Old Skool", "sizes": [6, 7, 8, 9, 10], "price": 65, "gender": "Women"},
        {"shoe_id": 9, "shoe_name": "Nike ZoomX", "sizes": [7, 8, 9, 10, 11], "price": 200, "gender": "Men"},
        {"shoe_id": 10, "shoe_name": "Asics Gel-Kayano", "sizes": [8, 9, 10, 11], "price": 150, "gender": "Unisex"}
    ]
        
        # global self values with a total_order list and a iterator value of prices.
        self.total_order = []
        self.total_price = 0

    #function to display all options based on user input.
    def displayitem(self):
        gender_choice = input("which product you want? men, women or unisex: ").lower()
        
        valid_gender = ["men", "women", "unisex"]
        if gender_choice not in valid_gender:
            print(f"Invalid input. Choose from {valid_gender}.")
        
        filtered_shoes = list(filter(lambda items: items['gender'].lower() == gender_choice, self.shoe_data))
        
        # # looping through items to print out.
        if filtered_shoes:
            for items in filtered_shoes:
                print(f"id : {items['shoe_id']}, shoe : {items['shoe_name']}, size: {items['sizes']}, price : {items['price']} rupees for all {len(items['sizes'])} pieces.")
            print()
        else:
            print(f"no item available for {gender_choice} category.")

    # cart function where user can add items to their cart.
    # after that there will be showcart function where users will have carted items stored and the total price calculated.

    def addToCart(self):
        idchoice = int(input("Enter the ID of the shoe: "))
        sizechoice = int(input("Enter the size of the shoe: "))

        # local scopes for temporarily store data.
        temp_price = 0
        temp_shoe = []

        # flags.
        shoe_found = False
        size_found = False


        for id in self.shoe_data:
            if idchoice == id['shoe_id']:
                shoe_found = True # changing the flags.
                temp_price += id['price'] # storing the price of the shoe temporarily.

                # storing the shoe in an temp list.
                if sizechoice in id['sizes']:
                    size_found = True
                    temp_shoe.append({
                        "shoe_id" : idchoice,
                        "shoe_name" : id['shoe_name'],
                        "price" : temp_price,
                        "size" : sizechoice
                    })
                    
                    print(f"you've bagged {id['shoe_name']} in your cart 🛍️.")
                    print("-" * 35)
                    
                    # sum of total price.
                    self.total_price += temp_price
                    # extending the main list.
                    self.total_order.extend(temp_shoe)
                    break
            
        if not shoe_found or not size_found:
            print("Item isn't available at the moment.")

    # remove function.
    def removeitem(self, shoe_id):
        shoe_found = False # def flag.

        for shoe in self.total_order:
            if shoe_id == shoe['shoe_id']:
                shoe_found = True # changing the flag.
                self.total_order.remove(shoe) # removing the whole item.
                break

        # if the shoe_id is not found.
        if not shoe_found:
            return False

        return True

    # view cart function.
    def viewcart(self):
        if len(self.total_order) == 0:
            print("    YOUR CART IS EMPTY    ")
            print()
        else:
            print("------ Your cart 🛒 ------")
            for each in self.total_order:
                print(f"shoe_id : {each['shoe_id']}, shoe : {each['shoe_name']}, size: {each['size']}, price(rupees) : {each['price']}.")
            print()
            print(f"your total (rupees) 💵 --> {self.total_price} /-")
            print("-" * 35)

        # removing item if necessary.
        while True:
            remove_choice = input("Do you want to remove any item (y to yes q to exit): ").lower()
            # up local scope.
            temp_price = 0
        
            if remove_choice == 'q':
                print("-" * 30)
                print("-------- Invoice --------")

                # looping through each items in the total.order.
                for shoes in self.total_order:
                    print(f"shoe : {shoes['shoe_name']} -- size : {shoes['size']} -- price : {shoes['price']} /-")
                    print()

                print(f"Total Bill (in rupees): {self.total_price} /-")                
                print("Thank you for shopping with us! 🙏")
                print("-" * 40)
                break

            elif remove_choice == 'y':
                shoe_id = int(input("Enter the shoe ID of the shoe that you wants to remove: "))

                for shoes in self.total_order:
                    if shoe_id == shoes['shoe_id']:

                        # calling the functions.
                        self.removeitem(shoes)
                        temp_price += shoes['price'] # storing the price temporarily.
                        print(f"you've removed {shoe_id}, {shoes['shoe_name']} from your cart 🛒")
                        print()
                    
                        # re-calculating the total price.
                        self.total_price -= temp_price
                        print(f"your Total (rupees): {self.total_price} /-")
                        print()
                        break
                    else:
                        print("your selected item is not in the cart.")


# main driver to run.
def main():

    shopsystem = shop()
    while True:
        print("------ Welcome to our shop ------")
        print("1. Display items.")
        print("2. Add to cart.")
        print("3. Show cart option.")

        choice = input("Enter your choice: ")

        if choice == "1":
            shopsystem.displayitem()
        elif choice == "2":
            shopsystem.addToCart()
        elif choice == "3":
            shopsystem.viewcart()
        else:
            print("Invalid option. Try again from the menu.")


# running the main program.
if __name__ == "__main__":
    main()