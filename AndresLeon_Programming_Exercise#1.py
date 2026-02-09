TOTAL_TICKETS = 10
MAX_PER_BUYER = 4

def sell_tickets():
    # Initialize tickets remaining and buyers count
    remaining_tickets = TOTAL_TICKETS
    num_buyers = 0

    # Display welcome messages and instructions
    print("Welcome to the cinema pre-sale!")
    print(f"Total available: {TOTAL_TICKETS} tickets")
    print(f"Maximum per person: {MAX_PER_BUYER} tickets")
    print("Tip: Enter '0' at any time to close the sale.")

    # Main ticket selling loop
    while remaining_tickets > 0:
        print(f"\nTickets available: {remaining_tickets}")

        try:
            # Prompt user for ticket quantity
            user_input = input(f"Hello, welcome to Leon's cinema. How many tickets would you like to buy? (1-{MAX_PER_BUYER}): ")

            # Check if user wants to exit
            if user_input.lower() == '0':
                print("Closing pre-sale...")
                break

            # Convert input to integer
            tickets_requested = int(user_input)

            # Validate positive number
            if tickets_requested <= 0:
                print("Error: Please enter a positive number of tickets.")
                continue

            # Check maximum tickets per person
            if tickets_requested > MAX_PER_BUYER:
                print("Ticket limit exceeded.")
                continue

            # Check if enough tickets are available
            if tickets_requested > remaining_tickets:
                print("Sorry, not enough tickets available.")
                continue

            # Process purchase
            remaining_tickets -= tickets_requested
            num_buyers += 1
            print(f"Purchase successful: {tickets_requested} ticket(s) acquired.")

        except ValueError:
            # Handle invalid integer input
            print("Error: Please enter a valid integer.")

    # Final summary message
    if remaining_tickets == 0:
        print("\nALL TICKETS SOLD OUT! Pre-sale has ended.")
    else:
        print(f"\nPre-sale closed. {remaining_tickets} tickets remained unsold.")

    return num_buyers


def display_summary(total_buyers):
    # Display a summary of the ticket sales
    print("\nSALES SUMMARY")
    print(f"Total buyers served: {total_buyers}")
    print("Thank you for using the pre-sale system.")


# Main program execution
if __name__ == "__main__":
    # Call the function to sell tickets
    total_buyers = sell_tickets()

    # Call the function to display the summary
    display_summary(total_buyers)


