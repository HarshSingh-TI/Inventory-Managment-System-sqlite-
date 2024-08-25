import sqlite3


class Product:
    def __init__(self, sku, name, brand, quantity):
        self.sku = sku
        self.name = name
        self.brand = brand
        self.quantity = quantity


class InventoryManager:
    def __init__(self, db_name="inventory.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Creates the product table if it does not exist."""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                                sku TEXT PRIMARY KEY,
                                name TEXT,
                                brand TEXT,
                                quantity INTEGER)''')
        self.conn.commit()

    def add_product(self):
        """Adds a new product to the inventory."""
        sku = input("Enter product SKU: ")

        if self.product_exists(sku):
            print(f"Product with SKU {sku} already exists.")
            return

        name = input("Enter product name: ")
        brand = input("Enter product brand: ")
        try:
            quantity = int(input("Enter product quantity: "))
            if quantity < 0:
                raise ValueError("Quantity must be a positive integer.")
        except ValueError as e:
            print(e)
            return

        new_product = Product(sku, name, brand, quantity)
        self.cursor.execute("INSERT INTO products (sku, name, brand, quantity) VALUES (?, ?, ?, ?)",
                            (new_product.sku, new_product.name, new_product.brand, new_product.quantity))
        self.conn.commit()
        print(f"Product {name} added to inventory.")

    def list_products(self):
        """Displays all products in the inventory."""
        self.cursor.execute("SELECT * FROM products")
        products = self.cursor.fetchall()

        if products:
            print(f"{'SKU':<10} {'Name':<20} {'Brand':<20} {'Quantity':<10}")
            print("-" * 60)
            for product in products:
                print(f"{product[0]:<10} {product[1]:<20} {product[2]:<20} {product[3]:<10}")
        else:
            print("Inventory is empty.")

    def update_product(self):
        """Updates the details of an existing product."""
        sku = input("Enter product SKU to update: ")

        if not self.product_exists(sku):
            print(f"Product with SKU {sku} not found.")
            return

        name = input("Enter new name (leave blank to keep current): ")
        brand = input("Enter new brand (leave blank to keep current): ")
        quantity = input("Enter new quantity (leave blank to keep current): ")

        if name:
            self.cursor.execute("UPDATE products SET name = ? WHERE sku = ?", (name, sku))
        if brand:
            self.cursor.execute("UPDATE products SET brand = ? WHERE sku = ?", (brand, sku))
        if quantity:
            try:
                quantity = int(quantity)
                if quantity < 0:
                    raise ValueError("Quantity must be a positive integer.")
                self.cursor.execute("UPDATE products SET quantity = ? WHERE sku = ?", (quantity, sku))
            except ValueError as e:
                print(e)
                return

        self.conn.commit()
        print(f"Product {sku} updated.")

    def delete_product(self):
        """Deletes a product from the inventory."""
        sku = input("Enter product SKU to delete: ")

        if not self.product_exists(sku):
            print(f"Product with SKU {sku} not found.")
            return

        self.cursor.execute("DELETE FROM products WHERE sku = ?", (sku,))
        self.conn.commit()
        print(f"Product {sku} deleted.")

    def search_products(self):
        """Searches for products by name or brand."""
        search_term = input("Enter product name or brand to search: ").lower()
        self.cursor.execute("SELECT * FROM products WHERE LOWER(name) LIKE ? OR LOWER(brand) LIKE ?",
                            (f"%{search_term}%", f"%{search_term}%"))
        results = self.cursor.fetchall()

        if results:
            print(f"{'SKU':<10} {'Name':<20} {'Brand':<20} {'Quantity':<10}")
            print("-" * 60)
            for product in results:
                print(f"{product[0]:<10} {product[1]:<20} {product[2]:<20} {product[3]:<10}")
        else:
            print("No products found.")

    def sort_products(self):
        """Sorts products by SKU, Name, or Quantity in ascending or descending order."""
        print("Sort by:\n1. SKU\n2. Name\n3. Quantity")
        choice = input("Enter your choice: ")

        if choice == '1':
            column = "sku"
        elif choice == '2':
            column = "name"
        elif choice == '3':
            column = "quantity"
        else:
            print("Invalid choice.")
            return

        order = input("Choose order:\n1. Ascending\n2. Descending\nEnter your choice: ")
        if order == '1':
            order_by = "ASC"
        elif order == '2':
            order_by = "DESC"
        else:
            print("Invalid choice.")
            return

        query = f"SELECT * FROM products ORDER BY {column} {order_by}"
        self.cursor.execute(query)
        sorted_products = self.cursor.fetchall()

        if sorted_products:
            print(f"{'SKU':<10} {'Name':<20} {'Brand':<20} {'Quantity':<10}")
            print("-" * 60)
            for product in sorted_products:
                print(f"{product[0]:<10} {product[1]:<20} {product[2]:<20} {product[3]:<10}")
        else:
            print("No products found.")

    def product_exists(self, sku):
        """Checks if a product with the given SKU exists."""
        self.cursor.execute("SELECT 1 FROM products WHERE sku = ?", (sku,))
        return self.cursor.fetchone() is not None

    def close_connection(self):
        """Closes the database connection."""
        self.conn.close()


def main():
    inventory_manager = InventoryManager()

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Search Products")
        print("6. Sort Products")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            inventory_manager.add_product()
        elif choice == '2':
            inventory_manager.list_products()
        elif choice == '3':
            inventory_manager.update_product()
        elif choice == '4':
            inventory_manager.delete_product()
        elif choice == '5':
            inventory_manager.search_products()
        elif choice == '6':
            inventory_manager.sort_products()
        elif choice == '7':
            inventory_manager.close_connection()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
