
# Base Conversion Script

This Python script allows you to convert a number from one base to another. It takes the number in its current base and the target base as inputs and returns the converted number.

## How It Works

The script consists of two main functions:

1. `convert_base(number, from_base, to_base)`: This function converts a number from its original base to the target base.
2. `base_10_to_target(number, base)`: This helper function converts a base 10 number to the target base.

### Function: `convert_base`

- **Parameters**:
  - `number`: The number to be converted (as a string).
  - `from_base`: The base of the input number (an integer).
  - `to_base`: The target base to convert to (an integer).

- **Returns**:
  - The number converted to the target base (as a string).

- **Process**:
  1. Converts the input number from its original base to base 10 using `int(str(number), from_base)`.
  2. If the target base is 10, it directly returns the base 10 number as a string.
  3. Otherwise, it calls `base_10_to_target` to convert the base 10 number to the target base.

### Function: `base_10_to_target`

- **Parameters**:
  - `number`: The base 10 number to be converted (an integer).
  - `base`: The target base (an integer).

- **Returns**:
  - The number converted to the target base (as a string).

- **Process**:
  1. Uses a loop to divide the base 10 number by the target base, storing the remainder as a digit.
  2. Repeats the process until the number is 0.
  3. Constructs the result string from the remainders.

### Main Function

The `main` function provides an interactive way to input the number, the current base, and the target base, and then prints the converted number.

## Usage

1. Run the script.
2. Enter the number you want to convert.
3. Enter the base of the input number.
4. Enter the target base.

The script will output the converted number.

## Example

- Input:
  - Number: `1010`
  - From Base: `2`
  - To Base: `10`

- Output:
  - `10`

## Code

```python
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

# Main function for testing
def main():
    number = input("Enter the number: ")
    from_base = int(input("Enter the current base of the number: "))
    to_base = int(input("Enter the base to convert to: "))
    
    converted_number = convert_base(number, from_base, to_base)
    print(f"The number {number} in base {from_base} converted to base {to_base} is: {converted_number}")

if __name__ == "__main__":
    main()
```

## License

This project is licensed under the MIT License.
