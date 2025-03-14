import click
from database import session  
from models import Category, Product  

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """Electronics Components Shop CLI"""
    if ctx.invoked_subcommand is None:
        ctx.invoke(main_menu)

# Create a new category
@click.command()
@click.argument('name')
def create_category(name):
    """Create a new category (e.g., Resistors, Capacitors)"""
    category = Category(name=name)
    session.add(category)
    session.commit()
    click.echo(f"Category '{name}' created successfully.")

# Create a new product
@click.command()
@click.argument('name')
@click.argument('price', type=float)
@click.argument('quantity', type=int)
@click.argument('category_id', type=int)
def create_product(name, price, quantity, category_id):
    """Create a new product (electronic component)"""
    # Validate that the category ID exists
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        product = Product(name=name, price=price, quantity=quantity, category_id=category_id)
        session.add(product)
        session.commit()
        click.echo(f"Product '{name}' created successfully.")
    else:
        click.echo(f"Error: Category with ID {category_id} not found.")

# Show all categories
@click.command()
def show_categories():
    """Show all categories"""
    categories = session.query(Category).all()
    if categories:
        for category in categories:
            click.echo(f"{category.id}: {category.name}")
    else:
        click.echo("No categories found.")

# Show all products
@click.command()
def show_products():
    """Show all products"""
    products = session.query(Product).all()
    if products:
        for product in products:
            click.echo(f"{product.id}: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
    else:
        click.echo("No products found.")

# Show all products in a specific category
@click.command()
@click.argument('category_id', type=int)
def show_products_in_category(category_id):
    """Show all products in a specific category"""
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        click.echo(f"Products in category '{category.name}':")
        for product in category.products:
            click.echo(f"- {product.name}, Price: {product.price}, Quantity: {product.quantity}")
    else:
        click.echo(f"Category with ID {category_id} not found.")

# Find a category by name
@click.command()
@click.argument('name')
def find_category_by_name(name):
    """Find a category by name"""
    category = session.query(Category).filter_by(name=name).first()
    if category:
        click.echo(f"Found category: {category.id} - {category.name}")
    else:
        click.echo(f"No category found with the name '{name}'.")

# Find a product by name
@click.command()
@click.argument('name')
def find_product_by_name(name):
    """Find a product by name"""
    product = session.query(Product).filter_by(name=name).first()
    if product:
        click.echo(f"Found product: {product.id} - {product.name}, Price: {product.price}, Quantity: {product.quantity}")
    else:
        click.echo(f"No product found with the name '{name}'.")

# Delete a category by ID
@click.command()
@click.argument('category_id', type=int)
def delete_category(category_id):
    """Delete a category by ID"""
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        session.delete(category)
        session.commit()
        click.echo(f"Category with ID {category_id} deleted successfully.")
    else:
        click.echo(f"Category with ID {category_id} not found.")

# Delete a product by ID
@click.command()
@click.argument('product_id', type=int)
def delete_product(product_id):
    """Delete a product by ID"""
    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        session.delete(product)
        session.commit()
        click.echo(f"Product with ID {product_id} deleted successfully.")
    else:
        click.echo(f"Product with ID {product_id} not found.")

# Main menu command to handle user choices in a loop
@click.command()
def main_menu():
    """Main Menu"""
    while True:
        click.echo("\nElectronics Components Shop CLI")
        click.echo("1. Create Category")
        click.echo("2. Create Product")
        click.echo("3. Show Categories")
        click.echo("4. Show Products")
        click.echo("5. Show Products in Category")
        click.echo("6. Find Category by Name")
        click.echo("7. Find Product by Name")
        click.echo("8. Delete Category")
        click.echo("9. Delete Product")
        click.echo("0. Exit")
        
        choice = click.prompt("Please select an option", type=int)
        
        if choice == 1:
            name = click.prompt("Enter category name")
            create_category.callback(name)
        elif choice == 2:
            name = click.prompt("Enter product name")
            price = click.prompt("Enter product price", type=float)
            quantity = click.prompt("Enter product quantity", type=int)
            category_id = click.prompt("Enter category ID", type=int)
            create_product.callback(name, price, quantity, category_id)
        elif choice == 3:
            show_categories.callback()
        elif choice == 4:
            show_products.callback()
        elif choice == 5:
            category_id = click.prompt("Enter category ID", type=int)
            show_products_in_category.callback(category_id)
        elif choice == 6:
            name = click.prompt("Enter category name")
            find_category_by_name.callback(name)
        elif choice == 7:
            name = click.prompt("Enter product name")
            find_product_by_name.callback(name)
        elif choice == 8:
            category_id = click.prompt("Enter category ID", type=int)
            delete_category.callback(category_id)
        elif choice == 9:
            product_id = click.prompt("Enter product ID", type=int)
            delete_product.callback(product_id)
        elif choice == 0:
            click.echo("Exiting...")
            break
        else:
            click.echo("Invalid choice, please try again.")

# Registering the main_menu command to the cli group
cli.add_command(main_menu)

# Running the CLI with the main_menu as the default command
if __name__ == '__main__':
    cli()