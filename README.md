# Electronics shop CLI Application
This is a python based CLI application for managing an electronics shop's inventory using **SQLALchemy** ORM. Users can interact with the application to perform various operations such as creating, viewing, and deleting categories and products.

## Requirements
- Python 3.8+
- SQLAlchemy
- click
- pipenv

## Setup
- Install dependencies:
    ```bash
    pipenv install

## Project Structure
Here's how the project folder structure looks like:
electronics_shop_cli/
|-- cli.py
|-- database.py
|-- electronics_components_shop.db
|-- models.py
|-- Pipfile
|__ README.md

## Running the Project
1. **Activate the Virtual Environment:**
    ```bash
    pipenv shell

2. **Run the CLI**
    - Run the following command to invoke the CLI interface:
        **python cli.py**
    - This will launch a menu showing
        1. **Create Category** #Create a new category
        2. **Create Product** #Create a new product in a specific category
        3. **Show Categories** #Show a list of all categories
        4. **Show Products** #Show a list of all products
        5. **Show Products in Category** #Show a list of products in a category based on category ID
        6. **Find Category by Name** #Displays the category with the specified name
        7. **Find Product by Name** #Displays the product with the specified name
        8. **Delete Category** #Delete a category based on its ID
        9. **Delete Product** #Delete a category based on its ID
        0. **Exit** #Exit the application
    - A detailed explanation of how to navigate through the menu and interact with the application is given below.

3. **Application guideline**
    1. **Create Category**
        - This is for creating a new category.
        - Select option 1 (Create Category) i.e., type 1 when prompted then press enter.
        - You will then be prompted to enter a name of the category e.g., Resistors
        - The new category will now be stored in the database
    2. **Create Product**
        - This is for creating a new product in a specific category based on the category's ID.
        - Select option 2 (Create Product) i.e., type 2 when prompted then press enter.
        - You will be prompted to enter the product details (name, price, quantity, category ID).
    3. **Show Categories**
        - Select option 3 (Show Categories) i.e., type 3 when prompted then press enter.
        - This will show a list of all categories. It will be displayed above the next menu.
        - If no category exists you'll see a message: **No categories found** 
    4. **Show Products**
        - Select option 4 (Show Products) i.e., type 4 when prompted then press enter.
        - This shows a list of all products. It will be displayed above the next menu.
        - If no products exists you'll see a message: **No products found** 
    5. **Show Products in Category**
        - Select option 5 (Show Products in Category) i.e., type 5 when prompted then press enter.
        - You will then be prompted to enter the ID of the category.
        - This will then show you a list of all products in the category. This list is displayed    above the next menu.
    6. **Find Category by Name**
        - Select option 6 (Find Category by Name).
        - You will then be prompted to enter the category name
        - The category will be displayed above the next menu.
        - If the category does not exist you'll see a message **No category found with the name 'CATEGORY_NAME'**
    7. **Find Product by Name**
        - Select option 7 (Find Product by Name).
        - You will be prompted to enter the product name.
        - The product will be displayed above the next menu.
        - If the product does not exist you'll see a message **No product found with the name 'PRODUCT_NAME'**
    8. **Delete Category by ID**
        - Select option 8 (Delete Category).
        - You will be prompted to enter the category ID.
        - You can see that the deleted category is no longer in the database.
    9. **Delete Product by ID**
        - Select option 9 (Delete Product).
        - You will be prompted to enter the product ID.
        - You can see that the deleted product is no longer in the database.
        - If the product does not exist you'll see a message **Product with ID 'PRODUCT_ID' not found**
    0. **Exiting the application**
        - To exit the application, select option 0 (Exit).


