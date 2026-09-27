def login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if username == "nihetha" and password == "1555":
        print("Admin login successful")
        return True
    else:
        print("Invalid username or password")
        return False


def view_products(products):
    print("\n===== ALL PRODUCTS =====")

    if len(products) == 0:
        print("No products available")
        return

    for product in products:
        print("----------------------")
        print("Product ID:", product["product_id"])
        print("Name:", product["name"])
        print("Price:", product["price"])
        print("Quantity:", product["quantity"])


def add_product(products):
    print("\n===== ADD PRODUCT =====")

    product_id = int(input("Enter product ID: "))
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    product = {
        "product_id": product_id,
        "name": name,
        "price": price,
        "quantity": quantity
    }

    products.append(product)

    print("Product added successfully")


def search_product(products):
    print("\n===== SEARCH PRODUCT =====")

    product_id = int(input("Enter product ID: "))

    for product in products:
        if product["product_id"] == product_id:
            print("----------------------")
            print("Product ID:", product["product_id"])
            print("Name:", product["name"])
            print("Price:", product["price"])
            print("Quantity:", product["quantity"])
            return

    print("Product not found")


def delete_product(products):
    print("\n===== DELETE PRODUCT =====")

    product_id = int(input("Enter product ID: "))

    for product in products:
        if product["product_id"] == product_id:
            products.remove(product)
            print("Product deleted successfully")
            return

    print("Product not found")


def confirm_booking(bookings):
    print("\n===== BOOKINGS =====")

    if len(bookings) == 0:
        print("No bookings available")
        return

    for booking in bookings:

        print("----------------------")
        print("Booking ID:", booking["booking_id"])
        print("Username:", booking["username"])
        print("Product:", booking["product_name"])
        print("Status:", booking["status"])

        if booking["status"] == "Pending":

            choice = input("Confirm booking? (y/n): ")

            if choice.lower() == "y":
                booking["status"] = "Confirmed"
                print("Booking confirmed")
                