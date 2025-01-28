from models import session, Product, Order, CartItem, OrderItem
from datetime import datetime


def view_cart():
    cart_items = session.query(CartItem).all()
    if cart_items:
        for item in cart_items:
            product = session.query(Product).filter_by(
                id=item.product_id).first()
            print(f"\nName: {product.name}, Quantity: {item.quantity}")
    else:
        print("\nCart is empty")


def add_to_cart():
    products = session.query(Product).all()
    if products:
        print("\nAvailable Products:")
        for product in products:
            print(f"ID: {product.id} - {product.name} (Price: {product.price})")

    prod_id = int(input("\nEnter the product ID: "))

    try:
        product = session.query(Product).filter_by(id=prod_id).first()
        if product:
            quantity = int(input("Enter the quantity: "))
            item = CartItem(product_id=prod_id, quantity=quantity)
            session.add(item)
            session.commit()
            print("\nItem added to cart")
        else:
            print("Invalid product ID. No product found with that ID.")
    except ValueError:
        print("Please enter a valid integer for the product ID.")


def remove_from_cart():
    cart_item_id = int(input("Enter the cart item ID: "))
    item = session.query(CartItem).filter_by(id=cart_item_id).first()
    if item:
        session.delete(item)
        session.commit()
        print("\nProduct successfully removed from cart")
    else:
        print("Invalid cart item ID. Item not found")


def place_order():
    cart_items = session.query(CartItem).all()
    if cart_items:
        total_amount = 0

        for item in cart_items:
            product = session.query(Product).filter_by(
                id=item.product_id).first()
            if product:
                total_amount += item.quantity * product.price

        order = Order(order_date=datetime.now(), total_amount=total_amount)
        session.add(order)
        session.commit()

        for item in cart_items:
            product = session.query(Product).filter_by(
                id=item.product_id).first()
            if product:
                order_item = OrderItem(
                    order_id=order.id,
                    product_id=item.product_id,
                    quantity=item.quantity,
                    price_per_item=product.price
                )
                session.add(order_item)
            session.delete(item)

        session.commit()
        print("Your order has been successfully placed")
    else:
        print("No items in the cart")


def view_orders():
    orders = session.query(Order).all()
    for order in orders:
        print(f"\nOrder ID: {order.id}, Date: {
              order.order_date.strftime('%Y-%m-%d %H:%M:%S')}, Total amount:{order.total_amount}")
        order_items = session.query(
            OrderItem).filter_by(order_id=order.id).all()

        for item in order_items:
            product = session.query(Product).filter_by(
                id=item.product_id).first()
            print(f"\nName: {product.name}, quantity: {
                  item.quantity}, price: {item.price_per_item}")


# Main Interface
while True:
    print("\nPlease select an action:")
    print("1. View Items in Cart")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. Place Order")
    print("5. View Your Orders")
    print("0. Exit the Application")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_cart()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        remove_from_cart()
    elif choice == "4":
        place_order()
    elif choice == "5":
        view_orders()
    elif choice == "0":
        break
    else:
        print("Invalid choice")