"""
เขียนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน Array ด้วยภาษา python เช่น [1,2,1,3,5,6,4] 
ลำดับที่มีค่ามากที่สุด คือ index = 5 โดยไม่ให้ใช้ฟังก์ชั่นที่มีอยู่แล้ว ให้ใช้แค่ลูปกับการเช็คเงื่อนไข
"""

def find_max_index(arr):
    # กำหนดตัวแปรสำหรับเก็บค่าสูงสุดและ index ที่มีค่าสูงสุด
    max_num = arr[0]
    max_index = 0
    
    # วนลูปผ่าน Array เพื่อหาค่าที่มากที่สุดและ index ของมัน
    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
            max_index = i
    
    # คืนค่า index ของตัวเลขที่มากที่สุด
    return max_index

# ตัวอย่างการใช้งาน
arr = [1, 2, 1, 3, 5, 6, 4]
max_index = find_max_index(arr)
print("Index ของตัวเลขที่มีค่ามากที่สุด:", max_index)