#Đề 1
#bài 4:Giả sử có một chuỗi như sau: “0001;10:18:25;0983876207;0918295063”, tách chuỗi trên thành từng phần riêng biệt
print('-'*20,"Bài 4 Đề 1",'-'*20)
def tinhtiendienthoai(chuoi):
    
    chuoi1 = chuoi.split(";")
    tg = chuoi1[1].split(":")
    tong_so_phut = float(tg[0]) * 60 + float(tg[1]) + float(tg[2]) / 60
    money = tong_so_phut * 2500
    return int(money)
if __name__ == "__main__":
    chuoi=str(input("nhap vao mot chuoi bat ki: "))
    print("tính giá cước trên là: ",tinhtiendienthoai(chuoi))
    