# menu of restaurants.
class restaurantsystem:
    def __init__(self):

        # declaring the menu.
        self.menu = {
            "passta" : 120,
            "chicken pizza" : 160,
            "corn pizza" : 120,
            "egg pizza" : 130,
            "chicken sandwich" : 90,
            "grilled sandwich" : 100,
            "cold coffee" : 100,
            "virgin mojito" : 120
        }

    # initializing global values in the __init__ function.
        self.order_list = []
        self.total_price = 0
        
    # displaying the menu.
    def display_menu(self):
        print("\n------ Our Menu ------")
        for name, price in self.menu.items():
            print(f"{name} : {price}")
        print('-' * 40)

    # adding order.
    def addingorder(self):
        while True:
            userchoice = input("Enter food to order: (q to quit): ").lower()
            if userchoice == "q":
                break
            elif userchoice in self.menu:
                self.order_list.append(userchoice)
                self.total_price += self.menu[userchoice]
                print(f"added {userchoice} in your order.")
            else:
                print("wrong food.")
        
    # removing order.
    def removingorder(self):
        while True:
            removingchoice = input("enter food name to remove: (ok to exit): ").lower()
            if removingchoice == 'ok':
                break

            elif len(self.menu) == 0:
                print(f"your orderlist is empty.")
                print(f"enter some food to order.")
                self.addingorder()

            elif removingchoice in self.order_list:
                self.order_list.remove(removingchoice)
                self.total_price -= self.menu[removingchoice]
                print(f"you've removed {removingchoice} from your list, which was {self.menu[removingchoice]} rupees.")
            else:
                print(f"you don't have {removingchoice} in your order list.")

    # displaying ordered items.
    def displaytotalorder(self):
        print(f"----- your orders -----")
        if not self.order_list:
            print("you haven't ordered anything.")
        elif self.order_list:
            for name in self.order_list:
                print(f"you've ordered {name}.")
            print(f"Your Total is rupees {self.total_price}.")
            print('-' * 40)

# main driver.
def main():

    # create an instance of the class.
    system = restaurantsystem()
    print("\n----------- Welcome to our restaurant -----------")
    while True:
        print("1. show me the menu")
        print("2. take some orders")
        print("3. remove some orders")
        print("4. total bill")
        print("5. exit")
        choice = input("enter your choice: ")
        if choice == '1':
            system.display_menu()
        elif choice == '2':
            system.addingorder()
        elif choice == '3':
            system.removingorder()
        elif choice == '4':
            system.displaytotalorder()
        elif choice == '5':
            print("Go away, you've wasted my time.")
            break

#running the main driver.
if __name__ == "__main__":
    main()