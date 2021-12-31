# Upper() ve Lower() Bunları  Biliyorsun

# replace() İlk harfi ikinci harfe çevirir
print("Herkes ana bacı gardas".replace("a", "o"))

stringe="Python Programlama Dili"
print(stringe.replace(" ", "-"))

#Startswith(x) String x ile başlıyorsa True başlamıyorsa False
#endswith(x) String x ile bitiyorsa True, bitmiyorsa False

# Split(a) a değerine string parçalara ayrılıp listelere ayrılır.

print(stringe.split(" "))

#Strip(x) Stringin başında ve sonunda bulunan x değerlerini siler
#Istrip(x) Stringin başında bulunan x değerlerini siler
#rstrip(x) Stringin sonunda bulunan x değerlerini siler
print(stringe.strip("P")) # Büyük Küçük harf duyarlı

# join() Listenin elemanlarını bir string değer ile birleştirmemizi sağlar

liste = ["21","02","2014"]

print("/".join(liste))

a = "TBMM"
print(".".join(a))

#count(x) x değerlerinin string içinde kaç defa geçtiğini sayar
#count(x,index) String içindeki x değerlerini verilen index değerinden başlayarak saymaya başla

a = "ada pazarı yandan çarklı"
print(a.count("a",0)) # 7

#find(x) x değerini baştan itibaren string içinde arar ve bulursa ilk bulduğu index değerini döner. Bulamazsa -1 döner
#rfind(x) x değerini sondan bşlayarak arar ve söyler

print(a.find("d"))












