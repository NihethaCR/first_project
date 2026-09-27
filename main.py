import json
import admin
import user



def load_data():

    with open("products.json", "r") as file:
        data = json.load(file)

    return data


def save_data(data):

    with open("products.json", "w") as file:
        json.dump(data, file, indent=4)


data = load_data()


while True:

    print("\n==============================")
    print(" INVENTORY MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Admin")
    print("2. User")
    print("3. Exit")

    choice = input("Choose: ")


    # ADMIN
    if choice == "1":

        if admin.login():

               while True:

                print("\n========== ADMIN MENU ==========")
                print("1. View all products")
                print("2. Add new product")
                print("3. Search product")
                print("4. Delete product")
                print("5. Confirm booking")
                print("6. Logout")

                option = input("Choose: ")


                if option == "1":

                    admin.view_products(data["products"])


                elif option == "2":

                    admin.add_product(data["products"])
                    save_data(data)


                elif option == "3":

                    admin.search_product(data["products"])


                elif option == "4":

                    admin.delete_product(data["products"])
                    save_data(data)


                elif option == "5":

                    admin.confirm_booking(data["bookings"])
                    save_data(data)


                elif option == "6":

                    print("Admin logged out")
                    break


                else:

                    print("Invalid choice")


    # USER
    elif choice == "2":

        while True:

            print("\n========== USER ==========")
            print("1. Signup")
            print("2. Login")
            print("3. Back")

            user_choice = input("Choose: ")


            if user_choice == "1":

                user.signup(data["users"])
                save_data(data)


            elif user_choice == "2":

                username = user.login(data["users"])


                if username is not None:

                    while True:

                        print("\n========== USER MENU ==========")
                        print("1. View products")
                        print("2. Search product")
                        print("3. Book product")
                        print("4. Logout")

                        option = input("Choose: ")


                        if option == "1":

                            admin.view_products(data["products"])


                        elif option == "2":

                            admin.search_product(data["products"])


                        elif option == "3":

                            user.book_product(
                                data["products"],
                                data["bookings"],
                                username
                            )

                            save_data(data)


                        elif option == "4":

                            print("User logged out")
                            break


                        else:

                            print("Invalid choice")


            elif user_choice == "3":

                break


            else:

                print("Invalid choice")


    # EXIT
    elif choice == "3":

        print("Thank you for using Inventory Management System")
        break


    else:

        print("Invalid choice")