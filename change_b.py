def convert_base(number, from_base, to_base):
    # Convert the number from the original base to base 10
    base_10_number = int(str(number), from_base)
    
    # Convert the base 10 number to the target base
    if to_base == 10:
        return str(base_10_number)
    else:
        return base_10_to_target(base_10_number, to_base)

def base_10_to_target(number, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if number == 0:
        return "0"
    result = ""
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result

# Main Function
def main():
    number = input("Enter number: ")
    from_base = int(input("Enter current base number: "))
    to_base = int(input("Enter the base to which you want to convert: "))
    
    converted_number = convert_base(number, from_base, to_base)
    print(f"Number {number} on the basis of {from_base} converted to {to_base} is: {converted_number}")

if __name__ == "__main__":
    main()
