import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import subprocess

# Database configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="retail_billing_system"
)

# Function to authenticate user
def authenticate(username, password):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM admin WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    return user

# Function to fetch items and prices from database
def get_items_prices():
    cursor = db.cursor()
    cursor.execute("SELECT items, price FROM items_price")
    items_prices = cursor.fetchall()
    cursor.close()
    return items_prices

# Function to get price of a specific item
def get_price(item):
    cursor = db.cursor()
    cursor.execute("SELECT price FROM items_price WHERE items = %s", (item,))
    price = cursor.fetchone()[0]
    cursor.close()
    return price

# Function to update rate in the database
def update_rate():
    item = item_entry.get()
    new_price = new_price_entry.get()
    cursor = db.cursor()
    cursor.execute("UPDATE items_price SET price = %s WHERE items = %s", (new_price, item))
    db.commit()
    cursor.close()
    update_display()
    item_entry.delete(0, tk.END)
    new_price_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

def update_display(items_prices=None):
    for row in tree.get_children():
        tree.delete(row)
    if items_prices is None:
        items_prices = get_items_prices()
    for item_price in items_prices:
        tree.insert('', 'end', values=item_price)

def search_item():
    item = search_entry.get()
    if item:
        cursor = db.cursor()
        cursor.execute("SELECT items, price FROM items_price WHERE items LIKE %s", ('%' + item + '%',))
        items = cursor.fetchall()
        cursor.close()
        if items:
            update_display(items)
            search_entry.delete(0, tk.END)  # Clear the search entry after searching
            # Select the first item found
            tree.selection_set(tree.get_children()[0])
        else:
            # Handle case when no items are found
            pass

def search_all_items():
    items_prices = get_items_prices()
    update_display(items_prices)

def on_item_select(event):
    selected_item = tree.item(tree.selection())['values']
    if selected_item:
        item_entry.delete(0, tk.END)
        item_entry.insert(0, selected_item[0])
        price_entry.delete(0, tk.END)
        price_entry.insert(0, selected_item[1])

def go_to_billing_page():
    subprocess.Popen(['python', 'billing.py'])
    root.destroy()

def login():
    username = username_entry.get()
    password = password_entry.get()
    user = authenticate(username, password)
    if user:
        login_page.pack_forget()
        billing_page.pack()
        billing_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    else:
        login_error_label.pack()

# Create the main window
root = tk.Tk()
root.title("Admin Section")
root.attributes('-fullscreen', True)  # Set fullscreen mode

# Login Page
login_page = tk.Frame(root, bg='gray20')
login_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

login_frame = tk.LabelFrame(login_page, text="LOGIN", font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
login_frame.pack(pady=20,padx=20)

username_label = tk.Label(login_frame, text="Username:", font=('arial', 14, 'bold'), bg='gray20', fg='white')
username_label.grid(row=0, column=0, padx=10, pady=20)
username_entry = tk.Entry(login_frame, font=('arial', 14), bd=2, relief='ridge')
username_entry.grid(row=0, column=1, padx=10, pady=20)

password_label = tk.Label(login_frame, text="Password:", font=('arial', 14, 'bold'), bg='gray20', fg='white')
password_label.grid(row=1, column=0, padx=10, pady=20)
password_entry = tk.Entry(login_frame, show="*", font=('arial', 14), bd=2, relief='ridge')
password_entry.grid(row=1, column=1, padx=10, pady=20)

login_button = tk.Button(login_frame, text="Login", font=('arial', 14, 'bold'), command=login, bd=2, relief='ridge')
login_button.grid(row=2, columnspan=2, pady=20)

login_error_label = tk.Label(login_frame, text="Invalid username or password", fg="red",bg="white")


# Billing Page
billing_page = tk.Frame(root)
search_frame = tk.Frame(billing_page)
search_frame.pack(pady=20)

search_label = tk.Label(search_frame, text="Search Item:", font=('arial', 14, 'bold'), bd=0, relief='ridge', height=2)
search_label.grid(row=0, column=0,padx=5)

search_entry = tk.Entry(search_frame, width=50, font=('arial', 14), bd=3, relief='ridge')
search_entry.grid(row=0, column=1)

search_button = tk.Button(search_frame, text="Search", font=('arial', 14, 'bold'), bd=2, relief='ridge', command=search_item)
search_button.grid(row=0, column=2, padx=10)

# Add a button to display all items
search_all_button = tk.Button(search_frame, text="Show All", font=('arial', 14, 'bold'), bd=2, relief='ridge', command=search_all_items)
search_all_button.grid(row=0, column=3, padx=10)


tree = ttk.Treeview(billing_page, columns=('Item', 'Price'), show='headings')
# Set the width of each column
tree.column('Item', width=500)  # Adjust the width as needed
tree.column('Price', width=300)  # Adjust the width as needed
tree.heading('Item', text='Item')
tree.heading('Price', text='Price')
tree.pack()

update_display()
# Create a frame for the labels, entries, and button
input_frame = tk.Frame(billing_page)
input_frame.pack(pady=20)

# Item Label and Entry
item_label = tk.Label(input_frame, text="Item:", font=('arial', 14, 'bold'))
item_label.grid(row=0, column=0, padx=10, pady=10)
item_entry = tk.Entry(input_frame, font=('arial', 14), bd=2, relief='ridge')
item_entry.grid(row=0, column=1, padx=10, pady=10)

# Price Label and Entry
price_label = tk.Label(input_frame, text="Price:", font=('arial', 14, 'bold'))
price_label.grid(row=0, column=2, padx=10, pady=10)
price_entry = tk.Entry(input_frame, font=('arial', 14), bd=2, relief='ridge')
price_entry.grid(row=0, column=3, padx=10, pady=10)

# New Price Label and Entry
new_price_label = tk.Label(input_frame, text="New Price:", font=('arial', 14, 'bold'))
new_price_label.grid(row=1, column=0, padx=10, pady=10)
new_price_entry = tk.Entry(input_frame, font=('arial', 14), bd=2, relief='ridge')
new_price_entry.grid(row=1, column=1, padx=10, pady=10)

# Update Button
update_button = tk.Button(input_frame, text="Update", font=('arial', 14, 'bold'), command=update_rate, bd=2, relief='ridge')
update_button.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

tree.bind('<<TreeviewSelect>>', on_item_select)

# Go to Billing Page Button
go_to_billing_button = tk.Button(root, text="Go to Billing Page", font=('arial', 14, 'bold'), command=go_to_billing_page, bd=2, relief='ridge')
go_to_billing_button.pack(side=tk.BOTTOM, padx=10, pady=10)


root.mainloop()
