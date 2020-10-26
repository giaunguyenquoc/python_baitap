#Đề 1
#bài 3: Tính tổng giá trị từ 1 đến n (n>13, n nhập từ bàn phím, xử lý điều kiện n>13),nếu chạy đến số 13 thì không chạy nữa (không cộng số 13) và xuất kết quả
b = int(input('Nhap gia tri ='))
tong = 0
for i in range (1,b+1):
    if (i == 13 ):
        break
    else:
        tong += i
        print(i, tong)
print (tong)
