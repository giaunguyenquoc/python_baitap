#b1
chuoi=input("nhap chuoi:")
def manual_replace(s, char, index):
    return s[:index] + char + s[index +1:]
print(manual_replace(chuoi,"$", 0))

#b2
chuoi=input("nhap chuoi:")
def remove_char_m(str, n):
      phan_dau=str[:n] 
      phan_cuoi=str[n+1:]
      return phan_dau + phan_cuoi
print(remove_char_m(chuoi,int(input("thu tu muon xoa:"))))

#b3
chuoi = input("nhap chuoi:")
def even_values_string(str):
  ketqua = "" 
  for i in range(len(str)):
    if i % 2 != 0:
      ketqua = ketqua + str[i]
  return ketqua
print(even_values_string(chuoi))

#b4
chuoi = input("nhap chuoi:")
def dau_va_duoi(str):
  if len(str) < 2:
    return "chuoi rong"
  return str[0:2] + str[-2:]
print(dau_va_duoi(chuoi))

#b5
chuoi = input("nhap chuoi:")
print("ki tu lon nhat cua chuoi:", max(chuoi))
print("ki tu nho nhat cua chuoi:", min(chuoi))

#b6
chuoi = input("nhap chuoi:")
print(chuoi.swapcase())