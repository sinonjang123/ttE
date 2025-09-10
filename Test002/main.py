
from myfunc import add_numbers

def main():
    
    A = float(input("กรุณาป้อนค่า A: "))
    B = float(input("กรุณาป้อนค่า B: "))
    
    
    result = add_numbers(A, B)
    
    
    print(f"ผลลัพธ์ของ {A} + {B} คือ: {result}")

if __name__ == "__main__":
    main()

