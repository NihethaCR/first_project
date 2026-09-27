def signup(users):

    print("\n===== SIGNUP =====")

    username = input("Create username: ")
    password = input("Create password: ")

    for user in users:
        if user["username"] == username:
            print("Username already exists")
            return

    new_user = {
        "username": username,
        "password": password
    }

    users.append(new_user)

    print("Signup successful")


def login(users):

    print("\n===== USER LOGIN =====")

    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:

        if user["username"] == username and user["password"] == password:
            print("Login successful")
            return username

    print("Invalid username or password")
    return None


def book_product(products, bookings, username):

    print("\n===== BOOK PRODUCT =====")

    product_id = int(input("Enter product ID: "))

    for product in products:

        if product["product_id"] == product_id:

            if product["quantity"] > 0:

                product["quantity"] = product["quantity"] - 1

                booking = {
                    "booking_id": len(bookings) + 1,
                    "username": username,
                    "product_name": product["name"],
                    "status": "Pending"
                }

                bookings.append(booking)

                print("Product booked successfully")
                print("Waiting for admin confirmation")
                return

            else:
                print("Product is out of stock")
                return

    print("Product not found")