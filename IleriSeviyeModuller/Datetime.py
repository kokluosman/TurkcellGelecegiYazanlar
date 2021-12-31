from datetime import datetime
import locale



locale.setlocale(locale.LC_ALL,"")

now = datetime.now()

print(now.year)
print(now.month)
print(now.microsecond)


print(datetime.ctime(now))


print(datetime.strftime(now,"%Y" +" "+ "%B")) # Yılı verir C programlamada ki gibi düşün

saniye = datetime.timestamp(now)

print(saniye)

#Fromtimestamp() saniyeyi tarihe çevirir.


