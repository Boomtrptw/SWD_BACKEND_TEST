
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
def convert_to_thai_text(number):
    thai_numbers = {
        0: 'ศูนย์',
        1: 'หนึ่ง',
        2: 'สอง',
        3: 'สาม',
        4: 'สี่',
        5: 'ห้า',
        6: 'หก',
        7: 'เจ็ด',
        8: 'แปด',
        9: 'เก้า',
        10: 'สิบ',
        100: 'ร้อย',
        1000: 'พัน',
        10000: 'หมื่น',
        100000: 'แสน',
        1000000: 'ล้าน'
    }

    def number_to_thai_text(num):
        if num <= 10:
            return thai_numbers[num]
        elif num < 100:
            return thai_numbers[num // 10] + thai_numbers[10] + thai_numbers[num % 10]
        elif num < 1000:
            return thai_numbers[num // 100] + thai_numbers[100] + number_to_thai_text(num % 100)
        elif num < 10000:
            return thai_numbers[num // 1000] + thai_numbers[1000] + number_to_thai_text(num % 1000)
        elif num < 100000:
            return thai_numbers[num // 10000] + thai_numbers[10000] + number_to_thai_text(num % 10000)
        elif num < 1000000:
            return thai_numbers[num // 100000] + thai_numbers[100000] + number_to_thai_text(num % 100000)
        else:
            return "Number out of range"

    if 0 <= number < 10000000:
        return number_to_thai_text(number)
    else:
        return "Number out of range"


# Test the function with user input
user_input = int(input("Enter a number between 0 and 10 million: "))
result = convert_to_thai_text(user_input)
print("Thai text representation:", result)
