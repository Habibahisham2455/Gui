from tkinter import *
from tkinter import messagebox, simpledialog

class RestaurantProject:
    # Initializing TAX_RATE and DELIVERY_FEE
    TAX_RATE = 0.14
    DELIVERY_FEE = 5.99

    def __init__(self, window):
        self.window = window
        self.window.title("Restaurant Project")
        self.window.minsize(1000, 500)  # Set the minimum size of the window

        # Title Label
        self.label = Label(window, text="Welcome To FeastBeast", font=("Arial", 24, "bold"))
        self.label.grid(row=0, column=1, columnspan=2)

        # Initialize radio state
        self.pickup_delivery_radio_state = IntVar(value=1)  # default value
        self.payment_radio_state = IntVar(value=1)  # default value

        # Create frames
        self.create_frames()

        # Call the details method to display the restaurant details
        self.details()

        # Initialize the order list
        self.order = []

        # Initialize total display
        self.customer_display()

    def create_frames(self):
        # frame for details
        self.details_frame = Frame(self.window, relief="groove", highlightbackground="black", highlightthickness=5)
        self.details_frame.grid(row=1, column=0, sticky="nw", padx=10, pady=10)

        # frame for order
        self.order_frame = Frame(self.window, relief="groove")
        self.order_frame.grid(row=1, column=2, padx=10, pady=10)

        # frame for menu
        self.menu_frame = Frame(self.window, relief="groove")
        self.menu_frame.grid(row=1, column=1, padx=10, pady=10)

        # frame for total
        self.total_frame = Frame(self.window, relief="groove", highlightbackground="black", highlightthickness=5)
        self.total_frame.grid(row=1, column=3, padx=10, pady=10)

        # frame for customer 
        self.customer_frame = Frame(self.window, relief="groove", highlightbackground="black", highlightthickness=5)
        self.customer_frame.grid(row=1, column=0, padx=10, pady=200)

    def customer_display(self):
        # Create Name label
        self.customer_name_label = Label(self.customer_frame, text="Name:", font=("Arial", 14, "bold"))
        self.customer_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        # Create Name Entry
        self.customer_name_entry = Entry(self.customer_frame)
        self.customer_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Create Phone number label
        self.customer_phone_number_label = Label(self.customer_frame, text="Phone Number:", font=("Arial", 14, "bold"))
        self.customer_phone_number_label.grid(row=1, column=0, padx=5, pady=5)

        # Create Phone number Entry
        self.customer_phone_number_entry = Entry(self.customer_frame)
        self.customer_phone_number_entry.grid(row=1, column=1, padx=5, pady=5)

        # Create Address Label
        self.customer_address_label = Label(self.customer_frame, text="Address:", font=("Arial", 14, "bold"))
        self.customer_address_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        # Create Address Entry
        self.customer_address_entry = Entry(self.customer_frame)
        self.customer_address_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Calling the function to display the Total
        self.init_total_display()

        self.total_label = Label(self.window, text="Total Check", font=("Arial", 14, "bold"))
        self.total_label.grid(row=1, column=3, sticky="nw", pady=170)

    def init_total_display(self):
        self.subtotal_label = Label(self.total_frame, text="Subtotal: $0.00", font=("Arial", 14, "bold"))
        self.subtotal_label.pack(anchor="w")

        self.tax_label = Label(self.total_frame, text="Taxes: $0.00", font=("Arial", 14, "bold"))
        self.tax_label.pack(anchor="w")

        self.delivery_fee_label = Label(self.total_frame, text="Delivery Fee: $0.00", font=("Arial", 14, "bold"))
        self.delivery_fee_label.pack(anchor="w")

        self.total_with_tax_label = Label(self.total_frame, text="Total: $0.00", font=("Arial", 14, "bold"))
        self.total_with_tax_label.pack(anchor="w")

    def details(self):
        restaurant_name = Label(self.details_frame, text="Restaurant Name: FastBeast", font=("Arial", 12, "bold"))
        restaurant_name.grid(row=0, column=0, sticky="w", pady=(0, 5))

        address = Label(self.details_frame, text="Address: ----------", font=("Arial", 12, "bold"))
        address.grid(row=1, column=0, sticky="w", pady=(0, 5))

        phone_number1 = Label(self.details_frame, text="Phone:-----------", font=("Arial", 12, "bold"))
        phone_number1.grid(row=2, column=0, sticky="w", pady=(0, 5))

        phone_number2 = Label(self.details_frame, text="Phone: -------------", font=("Arial", 12, "bold"))
        phone_number2.grid(row=3, column=0, sticky="w", pady=(0, 5))

        # Calling the function to display the menu
        self.menu()

    def menu(self):
        """Display the menu items."""
        self.menu_items = {
            "1": ("Pizza", 11.99),
            "2": ("Burger", 9.99),
            "3": ("Steak", 19.99),
            "4": ("Fries", 5.99),
            "5": ("Soda", 3.99),
            "6": ("Salad", 3.00),
        }

        self.menu_label = Label(self.menu_frame, text="Menu", font=("Arial", 14, "bold"))
        self.menu_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        self.menu_listbox = Listbox(self.menu_frame, height=12, width=30, font=("Arial", 12, "bold"))
        self.menu_listbox.grid(row=1, column=0, sticky="w", padx=10, pady=10)

        for key, value in self.menu_items.items():  # Loop over each item and display it in the menu
            self.menu_listbox.insert(END, f"{key}. {value[0]} --------- ${value[1]:.2f}")

        self.quantity_label = Label(self.menu_frame, text="Choose the Quantity:", font=("Arial", 12, "bold"))
        self.quantity_label.grid(row=2, column=0, sticky="w", padx=10)

        self.quantity_spinbox = Spinbox(self.menu_frame, from_=1, to=10, width=4, font=("Arial", 18, "bold"), state="readonly")
        self.quantity_spinbox.grid(row=2, column=0, sticky="e")

        self.add_to_order_button = Button(self.menu_frame, text="Add to Order", command=self.add_order, font=("Arial", 12, "bold"), width=15)
        self.add_to_order_button.grid(row=4, column=0, sticky="w", padx=10, pady=55)

        self.order_label = Label(self.window, text="Your Order", font=("Arial", 14, "bold"))
        self.order_label.grid(row=1, column=2, sticky="nw", padx=20, pady=20)

        self.order_listbox = Listbox(self.window, height=12, width=30, font=("Arial", 12, "bold"))
        self.order_listbox.grid(row=1, column=2, sticky="nw", padx=20, pady=70)

        self.checkout_button = Button(self.window, text="Checkout", command=self.checkout, font=("Arial", 12, "bold"), width=15)
        self.checkout_button.grid(row=2, column=1, sticky="nw", padx=20, pady=20)

        self.update_menu_button = Button(self.window, text="Update Menu (Admin Only)", font=("Arial", 12, "bold"), command=self.update_menu)
        self.update_menu_button.grid(row=2, column=0, sticky="w", padx=20, pady=10)

        self.pickup_Radiobutton = Radiobutton(text="Pick Up", value=1, variable=self.pickup_delivery_radio_state, command=self.total, font=("Arial", 12, "bold"))
        self.pickup_Radiobutton.grid(row=1, column=3, sticky="sw")

        self.delivery_Radiobutton = Radiobutton(text="Delivery", value=2, variable=self.pickup_delivery_radio_state, command=self.total, font=("Arial", 12, "bold"))
        self.delivery_Radiobutton.grid(row=2, column=3, sticky="w")

        self.payment_Radiobutton = Radiobutton(text="Cash", value=1, variable=self.payment_radio_state, command=self.payment_radio_used, font=("Arial", 12, "bold"))
        self.payment_Radiobutton.grid(row=1, column=4, sticky="sw")

        self.card_Radiobutton = Radiobutton(text="Card", value=2, variable=self.payment_radio_state, command=self.payment_radio_used, font=("Arial", 12, "bold"))
        self.card_Radiobutton.grid(row=2, column=4, sticky="w")

    def payment_radio_used(self):
        """Handle payment method selection and show details."""
        self.payment_method = self.payment_radio_state.get()
        if self.payment_method == 1:  # Cash payment
            messagebox.showinfo("Payment Method", "You have selected Cash as your payment method.")
        elif self.payment_method == 2:  # Card payment
            card_number = simpledialog.askinteger("Input", "Card number:")
            card_pin = simpledialog.askstring("Input", "Card Pin:")
            if card_number and card_pin:  # Ensure both inputs are provided
                messagebox.showinfo("Payment Method", f"Payment Method: Card ending in {str(card_number)[-4:]}\nPayment processed successfully.")
            else:
                messagebox.showwarning("Input Error", "Please enter both card number and pin.")

    def update_menu_list(self):
        # Deleting the previous listbox items before adding new ones
        self.menu_listbox.delete(0, END)  
        for key, (item_name, price) in self.menu_items.items():
            self.menu_listbox.insert(END, f"{key}: {item_name} - ${price:.2f}")  # Then insert the new one 

    def add_order(self):
        """Add selected menu item to the order."""
        selected_index = self.menu_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Add to Order", "Please select a menu item.")
            return

        item_index = selected_index[0]  # Get the index of the item that was selected
        item_key = str(item_index + 1)  # Adjust for 1-based keys in menu_items
        quantity = self.quantity_spinbox.get()  # Get the number of the quantity from the spinbox

        if item_key in self.menu_items:  # Ensure the key exists in the dictionary
            quantity = int(quantity)
            item_name, item_price = self.menu_items[item_key]
            self.order.append((item_name, item_price, quantity))  # Add the item and quantity to the order
            
            # Add the item to the order listbox
            self.order_listbox.insert(END, f"{item_name}: {quantity} x ${item_price:.2f} = ${item_price * quantity:.2f}")
        else:
            messagebox.showwarning("Invalid Item", "The selected item is not valid.")

        self.quantity_spinbox.delete(0, END)
        self.quantity_spinbox.insert(0, 1)  # Reset to 1

        # Calling the function to display
        self.total()

    def total(self):
        """Calculate and display the total amount for the order."""
        if not self.order:
            messagebox.showwarning("Your order is empty!", "Please add items to your order before checking out.")
            return

        total = sum(item[1] * item[2] for item in self.order)  # Calculate the total sum of the order
        tax = total * self.TAX_RATE  # Adding taxes
        total_with_tax = total + tax  # Assigning the new total
        delivery_fee = self.DELIVERY_FEE if self.pickup_delivery_radio_state.get() == 2 else 0  # Assigning the delivery fee based on the radio button state
        total_delivery = total_with_tax + delivery_fee

        # Update total display labels
        self.subtotal_label.config(text=f"Subtotal: ${total:.2f}")
        self.tax_label.config(text=f"Taxes : ${tax:.2f}")
        self.delivery_fee_label.config(text=f"Delivery Fee: ${delivery_fee:.2f}")
        self.total_with_tax_label.config(text=f"Total : ${total_delivery:.2f}")

    def checkout(self):
        # Ensure customer address is provided for delivery
        if self.pickup_delivery_radio_state.get() == 2:
            if not self.customer_address_entry.get():  # Check if the address entry is empty
                messagebox.showwarning("Please Add your Details", "Address is required for delivery.")
                return  # Exit the method if address is missing

        # Ensure customer name and phone number are provided
        if not self.customer_name_entry.get() or not self.customer_phone_number_entry.get():
            messagebox.showwarning("Please Add your Details", "Name and phone number are required.")
            return  # Exit the method if any details are missing

        # Calculate and display the total amount for the order
        if not self.order:
            messagebox.showwarning("Your order is empty!", "Please add items to your order before checking out.")
            return

        total = sum(item[1] * item[2] for item in self.order)  # Calculate the total sum of the order
        tax = total * self.TAX_RATE  # Adding taxes
        delivery_fee = self.DELIVERY_FEE if self.pickup_delivery_radio_state.get() == 2 else 0
        total_delivery = total + tax + delivery_fee  # Total including delivery fee

        # Prepare checkout summary
        check = f"Your Check for {self.customer_name_entry.get()} - {self.customer_phone_number_entry.get()}\n" 
        for item in self.order:
            check += f"{item[0]}: {item[2]} x ${item[1]:.2f} = ${item[1] * item[2]:.2f}\n"
        check += f"\nSubtotal: ${total:.2f}\n"
        check += f"Taxes: ${tax:.2f}\n"
        check += f"Total: ${total_delivery:.2f}\n"

        if self.payment_radio_state.get() == 1:
            check += f"Payment Method: Cash \n"
            check += "Payment processed successfully.\n"
        elif self.payment_radio_state.get() == 2:
            card_number = simpledialog.askinteger("Input", "Card number:")
            card_pin = simpledialog.askstring("Input", "Card Pin:")
            check += f"Payment Method: Card ending in {str(card_number)[-4:]}\n"
            check += "Payment processed successfully.\n"

        if self.pickup_delivery_radio_state.get() == 2:
            check += f"The order will arrive at {self.customer_address_entry.get()} in 45 min.\n"
        else:
            check += "Pickup at the store in 15 min.\n"
        
        messagebox.showinfo("Checkout Summary", check)

        self.order_listbox.delete(0, END)  # Clear current list

    def update_menu(self):
        """Allow admin to update the menu."""
        password = simpledialog.askstring("Update Menu", "Please enter the password to update the menu:")
        if password == "Python_Program":  # Check the password
            while True:
                action = simpledialog.askstring("Update Menu", "Type 'a' to add, 'r' to remove, 'q' to quit:")
                if action == "a":
                    dish = simpledialog.askstring("Add Dish", "Enter the name of the dish:")
                    price = simpledialog.askfloat("Add Dish", "Enter the price of the dish:")
                    if dish and price is not None:  # Ensure valid input
                        self.menu_items[str(len(self.menu_items) + 1)] = (dish, price)
                        self.update_menu_list()  # Refresh the menu list
                        messagebox.showinfo("Menu Updated", f"{dish} has been added to the menu.")
                elif action == "r":
                    key = simpledialog.askstring("Remove Dish", "Please enter the key of the dish to remove:")
                    if key in self.menu_items:
                        del self.menu_items[key]
                        self.update_menu_list()  # Refresh the menu list
                        messagebox.showinfo("Menu Updated", "Dish removed from the menu.")
                    else:
                        messagebox.showwarning("Invalid Input", "Dish not found.")
                elif action == 'q':
                    messagebox.showinfo("Update Menu", "Exiting menu update.")
                    break
                else:
                    messagebox.showwarning("Invalid Input", "Please enter a valid action.")
        else:
            messagebox.showwarning("Access Denied", "Incorrect password.")

if __name__ == "__main__":
    root = Tk()
    app = RestaurantProject(root)
    root.mainloop()