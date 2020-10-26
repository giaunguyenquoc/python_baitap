#Đề 1
#bài 2:Viết hàm với tham số truyền vào là một tháng và trả về mùa tương ứng trong năm. Sử dụng hàm vừa cài đặt, nhập vào một tháng và in ra màn hình mùa trong năm.
def nhap():
    while True:
        n = input("Nhập vào tháng: ")
        if n.isnumeric():
            n = int(n)
            if 1 <= n <= 12:
                print(f"Bạn đã nhập tháng: {n}")
                return n
            print("Nhập sai! Nhập lại")
        print("Xin vui lòng nhập lại theo đúng định dạng (1 -> 12)")

def cac_mua(thang):
    if 1 <= thang <= 3:
        return 1
    elif 4 <= thang <= 6:
        return 2
    elif 7 <= thang <= 9:
        return 3
    else:
        return 4

c_thang = nhap()
kq = cac_mua(c_thang)
if kq == 1:
    print("Mùa xuân")
elif kq == 2:
    print("Mùa hạ")
elif kq == 3:
    print("Mùa Thu")
else:
    print("Mùa đông")


b = input("Nhập vào cái gì đó: ")
print(type(b))