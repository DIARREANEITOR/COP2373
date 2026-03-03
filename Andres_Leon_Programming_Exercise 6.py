import re
# why exercise 6? what happen with 4 and 5 ? :(

def validate_phone(phone):
    # That wii be to matches like :(123) 456-7890, 123-456-7890, or 1234567890
    pattern = r'^(\(\d{3}\)\s?|\d{3}[-.\s]?)\d{3}[-.\s]?\d{4}$'
    return bool(re.match(pattern, phone))


def validate_ssn(ssn):
    # if Matches XXX-XX-XXXX
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(pattern, ssn))


def validate_zip(zip_code):
    # Matches 12345 or 12345-6789
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern, zip_code))


def run_tests():
    test_data = {
        "Phone": [("123-456-7890", True), ("(123) 456-7890", True), ("1234567", False)],
        "SSN": [("123-45-6789", True), ("123456789", False), ("12-345-6789", False)],
        "Zip": [("12345", True), ("12345-6789", True), ("1234", False)]
    }

    print("--- Imput permitted ---")
    for category, examples in test_data.items():
        for value, expected in examples:
            if category == "Phone":
                result = validate_phone(value)
            elif category == "SSN":
                result = validate_ssn(value)
            else:
                result = validate_zip(value)
            status = "PASS" if result == expected else "FAIL"
            print(f"[{category}] {value}: {status}")
    print("--- End of the list ---\n")


def main():
    run_tests()

    print("User Input Validation")
    user_phone = input("Enter Phone Number: ")
    user_ssn = input("Enter SSN (XXX-XX-XXXX): ")
    user_zip = input("Enter Zip Code: ")

    print("\n--- Results ---")
    print(f"Phone Valid: {validate_phone(user_phone)}")
    print(f"SSN Valid:   {validate_ssn(user_ssn)}")
    print(f"Zip Valid:   {validate_zip(user_zip)}")


if __name__ == "__main__":
    main()