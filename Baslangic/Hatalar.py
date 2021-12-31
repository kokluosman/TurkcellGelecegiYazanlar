### Try Except hatası

# try:
#     a = int("asdasd")
#     print()
# except:
#     print('Buraya Çalıştırır')
# print("Sonra Buradan devammke")

# try:
#     a = int("asdasd")
#     print()
# except ValueError:
#     print('Buraya Çalıştırır')
# print("Sonra Buradan devammke")


# try:
#     a=input("Sayıyı Gir dayı")
#     b=input("Sayıyı Gir dayı")
# except ValueError:
#     print('Değişken tipi hatası')
# except ZeroDivisionError:
#     print('Sayı 0 a bölünmez')

#Mutlaka Çalışmasını istediğimiz durum varsa finally eklememiz gerekecek.

try:
    print("Dalgavuk")
except:
    print('Something went wrong')
finally:
    print('Mutlaka Çalışması Gereken Yer')


#Hata fırlatmak raise

def terscevir(s):
    if (type(s)!=str):
        raise ValueError("Lütfen string değer gönderin")
    
    else:
        s[::-1]

print(terscevir("python"))













    