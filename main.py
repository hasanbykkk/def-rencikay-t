
öğrenciler=dict()


def ekleme(x):
    print("---öğrenci ekleme ekranın hoşgeldiniz---")
    eklenecek=input("öğrencinin ismi")
    numara=input("öğrencinin numarası")
    x=öğrenciler.setdefault(eklenecek,numara)

def silme(x):
    print("---öğrenci silme ekranın hoşgeldiniz---")
    kayıtsil=input("kaydı silinecek öğrenci")
    x=öğrenciler.pop(kayıtsil)

def gösterme(x):
    print("---öğrenci gösterme ekranına hoşgeldiniz---")
    for i,j in x.items():
        print(i,"",j)


while True:
    işlem=int(input("yapılacak işlemi seçiniz 1-kayıt başvurusu,2-silme işlemi,3-kayıt edilen öğrenciler"))

    if işlem==1:
        ekleme(öğrenciler)
    elif işlem==2:
        silme(öğrenciler)
    elif işlem==3:
        gösterme(öğrenciler)
    else:
        print("lütfen doğru seçim yapınız")