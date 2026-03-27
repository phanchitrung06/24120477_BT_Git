print("hello, world")

def la_so_nguyen_to(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def thong_ke_day_so():
    n = int(input("Nhập số lượng phần tử: "))
    
  
    danh_sach_so = []
    
 
    for i in range(n):
        x = int(input(f"Nhập số thứ {i + 1}: "))
        danh_sach_so.append(x)
    
    
   
    dem_nguyen_to = 0
    
    for x in danh_sach_so:
      
        if la_so_nguyen_to(x):
            dem_nguyen_to += 1
            
  
    print(f"\nDãy số bạn đã nhập là: {danh_sach_so}")
  
    print(f"Số lượng số nguyên tố: {dem_nguyen_to}")

if __name__ == "__main__":
    thong_ke_day_so()