

---

# Inventory Management System

This is a simple Inventory Management System written in Python. It uses SQLite as a backend database to perform CRUD (Create, Read, Update, Delete) operations on product data. The system allows users to manage products by adding, viewing, updating, deleting, searching, and sorting them.

## Features

- **Add Product**: Add a new product to the inventory with details like SKU, name, brand, and quantity.
- **View All Products**: Display all products currently in the inventory.
- **Update Product**: Update the details of an existing product.
- **Delete Product**: Remove a product from the inventory using its SKU.
- **Search Products**: Search for products by name or brand.
- **Sort Products**: Sort the list of products by SKU, name, or quantity in ascending or descending order.

## Requirements

- Python 3.x
- SQLite (built-in with Python)

## Getting Started

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Run the application**:

   ```bash
   python main.py
   ```

### Usage

1. When the program starts, you will see a menu with several options:
   - Add Product
   - View All Products
   - Update Product
   - Delete Product
   - Search Products
   - Sort Products
   - Exit

2. Select the desired operation by entering the corresponding number.

3. Follow the prompts to complete the operation.

### Example

- **Adding a Product**:
  - Enter the product SKU, name, brand, and quantity when prompted.

- **Viewing Products**:
  - Choose the option to view all products to see a list of all items in the inventory.

## Code Structure

- `Product` class: Represents a product with SKU, name, brand, and quantity.
- `InventoryManager` class: Manages the inventory operations such as adding, listing, updating, deleting, searching, and sorting products.
- `main` function: Entry point of the application that displays the menu and handles user input.

