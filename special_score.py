"""
เขียนโปรแกรมอะไรก็ได้ที่อยาก present Python's skill set เจ๋ง ๆ ของตัวเอง
ข้อนี้ไม่ต้องทำก็ได้ ไม่มีผลลบกับการให้คะแนน แต่ถ้าทำมาเเล้วเจ๋งจริง ก็จะพิจารณาเป็นพิเศษ

"""

def calculate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n + 1):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    return fibonacci_sequence[n]

def check_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def generate_prime_numbers(n):
    prime_numbers = []
    num = 2
    while len(prime_numbers) < n:
        if check_prime(num):
            prime_numbers.append(num)
        num += 1
    return prime_numbers

def convert_to_binary(decimal):
    return bin(decimal).replace("0b", "")

def convert_to_hexadecimal(decimal):
    return hex(decimal).replace("0x", "").upper()

def main():
    print("Welcome to Python's Skill Set Program!")
    print("1. Calculate Fibonacci Sequence")
    print("2. Check Prime Number")
    print("3. Generate Prime Numbers")
    print("4. Convert Decimal to Binary")
    print("5. Convert Decimal to Hexadecimal")

    choice = int(input("Enter your choice (1-5): "))
    if choice == 1:
        n = int(input("Enter the number of Fibonacci numbers to generate: "))
        result = calculate_fibonacci(n)
        print(f"The {n}th Fibonacci number is: {result}")
    elif choice == 2:
        number = int(input("Enter a number to check if it's prime: "))
        if check_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    elif choice == 3:
        n = int(input("Enter the number of prime numbers to generate: "))
        result = generate_prime_numbers(n)
        print(f"The first {n} prime numbers are: {result}")
    elif choice == 4:
        decimal = int(input("Enter a decimal number to convert to binary: "))
        result = convert_to_binary(decimal)
        print(f"The binary representation of {decimal} is: {result}")
    elif choice == 5:
        decimal = int(input("Enter a decimal number to convert to hexadecimal: "))
        result = convert_to_hexadecimal(decimal)
        print(f"The hexadecimal representation of {decimal} is: {result}")
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
