
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

# Mathematical Representation of Continuous and Discrete Signals

## Continuous Signals

### 1. Continuous Sinusoidal Signal
The continuous sinusoidal signal is represented mathematically as:
$x(t) = A \sin(2 \pi f t + \phi)$
Where:
- $x(t)$ is the amplitude of the signal in time $t$.
- $A$ is the maximum amplitude of the signal.
- $f$ is the frequency of the signal in Hz.
- $phi$ is the phase of the signal in radians.

### 2. Continuous Square Signal
The continuous square signal can be defined using the sign function of the sinusoidal signal:
$x(t) = A \cdot \text{sgn}(\sin(2 \pi f t + \phi))$
Where:
- $\text{sgn}(x)$ is the sign function, which returns 1 if $x$ is positive, -1 if $x$ is negative, and 0 if $x$ is zero.

### 3. Continuous Triangular Signal
The continuous triangular signal can be represented using the sine arc function of the sinusoidal signal:
\[ x(t) = \frac{2A}{\arcsin(\sin(2 \pi f t + \phi)) \]

## Discrete signals

### 1. Discrete Sinusoidal Signal
The discrete sinusoidal signal is represented mathematically as:
$x[n] = A \sin(2 \pi f n T + \phi))$.
Where:
- $x[n]$ is the amplitude of the signal at the sampling instant $n$.
- $A$ is the maximum amplitude of the signal.
- $f$ is the frequency of the signal in Hz.
- $T$ is the sampling period (the inverse of the sampling frequency $f_s$.
- $\phi$ is the phase of the signal in radians.

### 2. Discrete Square Signal
The discrete square signal can be defined by using the sign function of the sinusoidal signal:
$x[n] = A \text{sgn}(2 \pi f n T + \phi))$
Where:
- $\text{sgn}(x)$ is the sign function, which returns 1 if $x$ is positive, -1 if $x$ is negative, and 0 if $x$ is zero.

### 3. Discrete Triangular Signal
The discrete triangular signal can be represented using the sine arc function of the sinusoidal signal:
$x[n] = \arcsin(2 \sin(2 \pi f n T + \phi))$

