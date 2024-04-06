def find_trailing_zeros_in_factorial(n):
    # คำนวณ factorial ของจำนวน n
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    
    # นับจำนวนเลข 0 ที่ติดกันหลังสุดของผลลัพธ์ factorial
    count_zeros = 0
    while factorial_result % 10 == 0:
        count_zeros += 1
        factorial_result //= 10
    
    return count_zeros

# ตัวอย่างการใช้งาน
n = 7
zeros_count = find_trailing_zeros_in_factorial(n)
print(f"จำนวนเลข 0 ที่ติดกันหลังสุดของ {n}! คือ {zeros_count}")