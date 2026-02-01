def calculate_discount(price, discount_rate):
    """Calculate the discount amount based on price and rate."""
    # No changes needed here, but it now receives validated numeric data
    discount_amount = price * discount_rate
    return discount_amount


def apply_discount(price, discount_amount):
    """Subtract the discount amount from the original price."""
    return price - discount_amount


def main():
    # The list contains a mix of integers and one problematic string ("500")
    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": "500", "discount_rate": 0.2},  # BUG: price is a string
        {"name": "Headphones", "price": 200, "discount_rate": 0.05}
    ]

    for product in products:
        # CHANGE 1: Wrapped logic in a try-except block to handle data errors gracefully
        try:
            # CHANGE 2: Explicitly cast values to float.
            # This converts "500" to 500.0, fixing the TypeError in calculate_discount.
            price = float(product["price"])
            discount_rate = float(product["discount_rate"])

            discount_amount = calculate_discount(price, discount_rate)
            final_price = apply_discount(price, discount_amount)

            print(f"Product: {product['name']}")
            # CHANGE 3: Added string formatting (:.2f) for professional currency display
            print(f"Original Price: ${price:.2f}")
            print(f"Discount Amount: ${discount_amount:.2f}")
            print(f"Final Price: ${final_price:.2f}")

        # CHANGE 4: Added specific error handling for invalid number formats
        except ValueError:
            print(f"Error in '{product['name']}': Price or rate is not a valid number.")
        # CHANGE 5: Generic exception handling to catch any other unforeseen issues
        except Exception as e:
            print(f"An unexpected error occurred with {product['name']}: {e}")

        # Visual separator for cleaner console output
        print("-" * 30)


if __name__ == "__main__":
    main()