#def yosh_hisoblash(ism, yosh, joriy_yil = 2023):
#    """" Foydalanuvchidan yoshini so'rab undan tug'ilgan yilini hisoblash"""
#    print(f"Qadirli {ism.title()} {joriy_yil - yosh} yil tug'ilgansiz")
#yosh_hisoblash('dilshod', 19)
#import json
#import cv2
#def toliq_ism_yasa(ism, familya, otasining_ismi = ''):
#    """" to'liq ism qaytaruvchi funksiya """
#    if otasining_ismi:
#        toliq_ism = f"{ism} {otasining_ismi} {familya}"
#    else:
#        toliq_ism = f"{ism} {familya}"
#    return toliq_ism.title()
#talaba1 = toliq_ism_yasa("olim", "hakimov")
#talaba2 = toliq_ism_yasa('dilshod', 'ahmadov', 'soxibovich')
#print(f"darsga kelmagan talabalar: {talaba1} va {talaba2}")

#def avto_info(kompaniya, model, rangi, karobka, yili, narxi):
#    avto = {"kompaniya" : kompaniya,
#            "model" : model,
#            "rang" : rangi,
#            "karobka" : karobka,
#            "yili" : yili,
#            "narxi" : narxi
#            }
#    return avto

#print("Saytimizdagi avto mashinalar ro'yxatini shakllantiramiz.")
#avtolar = []
#while True:
#    print("\nQuyidagi malumotlarni kiriting", end=' ')
#    kompaniya = input("Ishlab chiqaruvchi: ")
#    model = input("Modeli: ")
#    rangi = input("Rangi: ")
#    karobka = input("Karobka: ")
#    yili = input("Ishlab chiqarilgan yili: ")
#    narxi = input("Narxi: ")
#    avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili, narxi))

#    javob = input("Yana avto qo'shasizmi (ha / yo'q): ")
#    if javob != "ha":
#        break
#print(avtolar)

#def foydalanuvchi_haqida_malumotlar(ism, familya, tugilgan_yil, tugilgan_joy, emanzil='', telraqam=''):
#    """foydalanuvchidan u haqida malumotlar so'rovchi dastur """
#    malumot = {
#        'ismi' : ism,
#        'familya' : familya,
#        't_yil' : tugilgan_yil,
#        'yosh' : 2023 - tugilgan_yil,
#        't_joy' : tugilgan_joy,
#        'e_manzil' : emanzil,
#        'raqam' : telraqam
#    }
#    return malumot
#print('Foydalanuvchi haqida malumotlarni kiriting')
#malumotlar = []
#while True:
#    print("Quyidagi malimotlarni kiriting: ", end='')
#    ism = input("Ismingini kiriting: ")
#    familya = input("Familyangizni kiriting: ")
#    tugilgan_yil = input("Tug'ilgan yilingizni kiriting: ")
#    tugilgan_yil = int(tugilgan_yil)
#    tugilgan_joy = input("tug'ilgan joyingizni kiriting: ")
#    emanzil = input("Email manzilingizni kiriting: ")
#    telraqam = input("Telefon raqamingizni kiriting: ")
#    malumotlar.append(foydalanuvchi_haqida_malumotlar(ism.title(), familya.title(), tugilgan_yil, tugilgan_joy, emanzil, telraqam))

#    javob = input("Yana davom etishni xohlaysizmi? (ha/yo'q)")
#    if javob != 'ha':
#        break
#print("Mijozlar:")
#for malumot in malumotlar:
#    print(
#        f"{malumot['ismi'].title()} {malumot['familya'].title()},"
#        f"{malumot['yosh']} yoshda, telefoni: {malumot['raqam']}"
#    )

#def sonlar(x, y, z):
#    """uchta sondan kattasini qaytaruvchi dastur"""
#    max = x
#    if y > max:
#        max = y
#    if z > max:
#        max = z
#    return max

#def aylana_info(radius, pi = 3.14159):
#    """aylana haqida malumot"""
#    aylana = {
#        'radius' : radius,
#        'diametr' : radius * 2,
#        'perimetr' : radius * 2 * pi
#        'yuza' : pi * radius ** 2
#    }
#    return  aylana

#def tub_sonlar_top(min, max):
#    tub_sonlar = []
#    for n in range(min, max+1):
#        tub = True
#        if n == 1:
#            tub = False
#        elif n == 2:
#            tub = True
#        else:
#            for x in range(2, n):
#                if n % x == 0:
#                    tub = False
#        if tub:
#            tub_sonlar.append(n)
#    return tub_sonlar
#print(tub_sonlar_top(2, 100))
#print(tub_sonlar_top(2, 1000))

#print(sum(tub_sonlar_top(2, 10)))

#def bahola(ismlar):
#    baholar = {}
#    while ismlar:
#        ism = ismlar.pop()
#        baho = input(f"{ism.title()}ning bahosini kiriting: ")
#        baholar[ism] = baho
#    return baholar
#talabalar = ['ali', 'vali', 'hasan', 'husan']
#baholar = bahola(talabalar)
#print(baholar)

#def kopaytir(*sonlar):
#    kopaytma = 1
#    for son in sonlar:
#        kopaytma = kopaytma * son
#    return kopaytma
#print(kopaytir(4, 5, 6, 7, 8, 100))

#def info_student(ism, familya, **boshqa_info):
#    boshqa_info['ismi'] = ism
#    boshqa_info['familyasi'] = familya
#    return boshqa_info
#student1 = info_student('dilshod', 'axmadov', t_yil = 2004, kurs = 'ikkinchi')
#student2 = info_student("a'zamjon", 'adhamov', t_yil = 2005, kurs = 'ikkinchi')
#print(student1)

#sonlar = list(range(11))
#def daraja2(x):
#    return x * x
#print(list(map(daraja2, sonlar)))

#kvadratlar = list(map(lambda x : x * x, sonlar))
#print(kvadratlar)

#kvadrats = []
#for son in sonlar:
#    kvadrats.append(son * son)
#print(kvadrats)

#import random as r
#sonlar = r.sample(range(100), 10)
#def juftmi(x):
#    """x juft bo'lsa True, noto'g'ri bo'lsa false qaytaramiz"""
#    return x%2==0
#juft_sonlar = list(filter(juftmi, sonlar))
#print(sonlar)
#print(juft_sonlar)

#mevalar = ['olma', "o'rik", 'anjir', 'behi', 'gilos', 'ananas', 'alvoli']
#mevA = list(filter(lambda meva: meva.startswith('a'), mevalar))
#mevB = list(filter(lambda meva: len(meva)<= 4, mevalar))
#mevaV = list(filter(lambda meva: meva.startswith('a') and meva.endswith('r'), mevalar))
#print(mevaV)
#print(mevB)
#print(mevA)

#multiplication = lambda x: x * 10
#print(multiplication(20))

#yigindi = lambda x, y: x + y
#print(yigindi(20, 50))

#from random import sample
#from math import sqrt
#x = list(range(0, 1001))
#y = sample(x, k=10)
#print(y)
#ildizlar = list(map(lambda n: sqrt(n), y))
#toq_sonlar = list(filter(lambda n: n%2, y))
#kvadratlar = list(map(lambda n: n**2, y))
#print(toq_sonlar)
#print(ildizlar)
#print(kvadratlar)

#def tubmi(x):
#    if x%2==0 and x<2:
#        return False
#    if x==2 or x==3:
#        return True
#    for i in range(3, x, 2):
#        if x%i == 0:
#            return False
#    return True
#tub = list(filter(tubmi, range(10001)))
#print(tub)

#OBJECT ORIENTED PROGRAMMING BASICS
#class Talaba:
#    """Talaba nomli class yaratish"""
#    def __init__(self, ism, familya, tyil):
#        """Talabaning xususiyatlari"""
#        self.ism = ism
#        self.familya = familya
#        self.tyil = tyil
#
#    def tanishtir(self):
#        print(f"Ismim {self.ism} familyam {self.familya}."
#              f"{self.tyil} da tug'ilganman")
#Shablon tayyor endi obyekt yaratishga o'tamiz
#talaba1 = Talaba('Dilshod', "Axmadov", 2004)
#talaba1.tanishtir()

#class Talaba:
#    def __init__(self, ism, familya, tyil):
#        """Talabaning xususiyatlari"""
#        self.ism = ism
#        self.familya = familya
#        self.tyil = tyil
#    def get_name(self):
#        """Talabaning ismini qaytaradi"""
#        return self.ism
#    def get_lastname(self):
#        """Talabaning familyasini qaytaradi"""
#        return self.familya
#    def get_fullname(self):
#        """Talabaning ism-familyasini qaytaradi"""
#        return f"{self.ism} {self.familya}"
#    def get_age(self, yil):
#        """Talabaning yoshini qaytaradi"""
#        return yil-self.tyil
#talaba2 = Talaba('Dilmurod', "Axmadov", 2011)
#print(talaba2.get_fullname())
#print(talaba2.get_name())
#print(talaba2.get_age(2021))

#class User:
#    def __init__(self, ism, familya, f_ismi, email, birthYear):
#        self.ismi = ism
#        self.familya = familya
#        self.foyism = f_ismi
#        self.mail = email
#        self.year = birthYear

#    def get_info(self):
#        """Foydalanuvchi kimligini chiqaradi"""
#        return f"Foydalanuvchi: {self.foyism.title()}" f" ismi: {self.ismi} {self.familya}" f" email: {self.mail}"
#    def get_ism(self):
#        return f"Foydalanuvchi ismi: {self.ismi}"
#    def get_familya(self):
#        return f"Familyasi: {self.familya}"
#    def get_fismi(self):
#        return f"Foylalanuvchi ismi: {self.foyism}"
#    def get_mail(self):
#        return f"Foydalanuvchi emaili: {self.mail}"
#    def get_age(self, yil):
#        return yil - self.year
#user1 = User('Dilshod', 'Axmadov', 'axmadov6929', 'axmadovdilshod777@gmail.com', 2004)
#user2 = User('Dilmurod', "Axmadov", 'dilmurod1120', 'dilmurodjon111@gmail.com', 2011)
#print(user2.get_info())
#print(user1.get_age(2023))

#class Talaba:
#    """Talaba nomli class yaratish"""
#    def __init__(self, ism, familya, tyil):
#        """Talabaning xususiyatlari"""
#        self.ism = ism
#        self.familya = familya
#        self.tyil = tyil
#        self.bosqich = 1

#    def get_info(self):
#        return f"{self.ism} {self.familya}. {self.bosqich} - bosqich talabasi"#

#    def set_bosqich(self, bosqich):
#        """Talabaning kursini yangilovchi dastur"""
#        self.bosqich = bosqich
#    def update_bosqich(self):
#        """Talabaning bosqichini bittaga ko'paytirish"""
#        self.bosqich += 1

#talaba1 = Talaba("Dilshod", "Axmadov", "2004")
#print(talaba1.get_info())
#talaba1.update_bosqich()
#print(talaba1.get_info())
#talaba1.update_bosqich()
#print(talaba1.get_info())
#talaba1.update_bosqich()
#print(talaba1.get_info())


#class Fan():
#    def __init__(self, nomi):
#        self.nomi = nomi
#        self.talabalar_soni = 0
#        self.talabalar = []
#    def add_student(self, talaba):
#        """FAnga talabalar qo'shish"""
#        self.talabalar.append(talaba)
#        self.talabalar_soni += 1
#    def get_students(self):
#        return [talaba.get_info() for talaba in self.talabalar]
#def see_methods(klass):
#    return [method for method in dir(klass) if method.startswith('__') is False]


#matematika = Fan('OLiy Matematika')
#talaba2 = Talaba('Dilmurod', 'Axmadov', 2011)
#talaba3 = Talaba('Sunnatillo', 'Yoqubjonov', 2005)
#talaba4 = Talaba('Iskandar', 'Tojiyev', 2006)

#matematika.add_student(talaba2)
#matematika.add_student(talaba3)
#matematika.add_student(talaba4)

#mat_talabalar = matematika.get_students()
#print(mat_talabalar)

#print(dir(Talaba))
#print(see_methods(Talaba))
#print(see_methods(talaba1))
#print(talaba4.__dict__)
#print(talaba4.__dict__.keys())
#print(talaba4.__dict__.values())

#class Avto():
#    def __init__(self, make, model, rang, korobka, narx):
#        self.make = make
#        self.model = model
#        self.rang = rang
#        self.korobka = korobka
#        self.narx = narx
#        self.kilometr = 0

#    def get_make(self):
#        return self.make

#    def get_model(self):
#        return self.model

#    def get_rang(self):
#        return self.rang

#    def get_narx(self):
#        return self.narx

#    def get_info(self):
#        return f"Ishlab chiqargan kompaniya: {self.make}, Model: {self.model}, rang: {self.rang}, \"" \
#               f"Korobka: {self.korobka}, narx: {self.narx}"

#    def update_car(self):
#        pass

#    def update_km(self):
#        yol = float(input("kmda yo'lni uzunligini kiriting: "))
#        self.kilometr += yol
#        return yol

#class Shaxs:
#    """Shaxslar haqida malumot"""
#    def __init__(self, ism, familya, passport, tyil):
#        self.ism = ism
#        self.familya = familya
#        self.passport = passport
#        self.tyil = tyil

#    def get_info(self):
#        """Shaxs haqida malumot"""
#        info = f"{self.ism} {self.familya}. "
#        info += f"Passport: {self.passport}, {self.tyil} - yilda tug'ilgan"
#        return info

#    def get_age(self, yil):
#        """Shaxsning yoshini qaytaruvchi dastur"""
#        return yil - self.tyil

#inson = Shaxs('Dilshod', 'Axmadov', 'AD1012906', 2004)
#print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda")

#class Talaba(Shaxs):
#    """Talaba klassi"""
#    def __init__(self, ism, familya, passport, tyil, id, manzil):
#        """Talabaning xussiyatlari"""
#        super().__init__(ism, familya, passport, tyil)
#        self.idraqam = id
#        self.bosqich = 1
#        self.manzil = manzil
#        self.fanlar = []

#    def get_id(self):
#        """Talabaing id raqami"""
#        return self.idraqam

#    def get_bosqich(self):
#        return self.bosqich

#    def get_info(self):
#        """Talaba haqida malumot"""
#        info = f"{self.ism} {self.familya}. "
#        info += f"{self.get_bosqich()} - bosqich. ID: {self.idraqam}"
#        return info

#class Manzil:
#    """Manzil saqlash uchun klass"""
#    def __init__(self, uy, kocha, tuman, viloyat):
#        """Manzil xususiyatlari"""
#        self.uy = uy
#        self.kocha = kocha
#        self.tuman = tuman
#        self.viloyat = viloyat

#    def get_manzil(self):
#        """Manzilni ko'rish"""
#        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
#        manzil += f"{self.kocha} ko'chasi, {self.uy} - uy"
#        return manzil

#class Fan:
#    """Fan degan klass yaratamiz"""
#    def __init__(self, matematika, fizika, ingliz_tili, ona_tili, tarix):
#        self.maatematika = matematika
#        self.fizika = fizika
#        self.ingtili = ingliz_tili
#        self.onatili = ona_tili
#        self.tarix = tarix

#    def fanga_yozil(self):
#        pass

#    def remove_fan(self):
#        pass

#manzil = Manzil(336, 'Amir Temur', 'Urgut', "Samarqand")
#talaba = Talaba('Dilmurod', 'Axmadov', 'AD1001878', 2011, '00166', manzil)

#print(talaba.get_info())
#print(talaba.get_age(2023))
#print(f"{talaba.get_info()}. ID: {talaba.get_id()}")
#print(talaba.get_info())
#print(talaba.manzil.get_manzil())
#print(talaba.manzil.tuman)

#from uuid import uuid4
#class Avto:
#    """Avtomobil klassi"""
#    def __init__(self, make, model, rang, yil, narx, km = 0):
#        """Avtomobilning xususiyatlari"""
#        self.make = make
#        self.model = model
#        self.rang = rang
#        self.yil = yil
#        self.narx = narx
#        self.__km = km
#        self.__id = uuid4()

#    def get_km(self):
#        return self.__km
#    def get_id(self):
#        return self.__id
#    def add_km(self, km):
#        """Mashinaga kmga yana qo'shish"""
#        if km>0:
#            self.__km += km
#        else:
#            return "Mashinani kmga kamaytirib bo'lmaydi"
#avto1 = Avto("KIA", 'k5000', 'qora', 2023, 48000)
#avto1.add_km(1500)
#print(avto1.get_km())

#from uuid import uuid4
#class Avto:
#    """Avtomobil klassi"""
#    __num_avto = 0
#    def __init__(self, make, model, rang, yil, narx, km = 0):
#        """Avtomobilning xususiyatlari"""
#        self.make = make
#        self.model = model
#        self.rang = rang
#        self.yil = yil
#        self.narx = narx
#        self.__km = km
#        self.__id = uuid4()
#        Avto.__num_avto += 1

#    @classmethod
#    def get_number_avto(cls):
#        return cls.__num_avto

#    def __repr__(self): #Obyektga __print__, __str__, yoki __repr__ metodlari yordamida obyekt haqida malumot olsak bo'ladi
#        """Obyekt haqida malumot"""
#        return f"Avto: {self.rang} {self.make}, {self.model}"

#    def __eq__(self, boshqa_avto):
#        """Tenglik"""
#        return self.narx == boshqa_avto.narx

#    def __lt__(self, boshqa_avto):
#        """Kichik"""
#        return self.narx<boshqa_avto.narx

#    def __le__(self, boshqa_avto):
#        """Kichik yoki teng"""
#        return self.narx<=boshqa_avto.narx

#avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
#avto2 = Avto("GM", "LAcetti", "Oq", 2020, 20000)
#avto3 = Avto("Toyota", "Carolla", "Silver", 2018, 45000)
#avto4 = Avto("Mazda", "6", "Qizil", 2015, 35000)
#avto5= Avto("VolksWagen", "Polo", "qora", 2015, 30000)
#avto6 = Avto("Honda", "Accord" , "Oq", 2017, 42000)
#avto7 = Avto("BMW", "X7", "Qora", 2015, 75000)


#class AvtoSalon:
#    """Avtosalon klassi"""
#    def __init__(self, name):
#        self.name = name
#        self.avtolar = []

#    def __repr__(self):
#        return f"{self.name} avtosaloni"

#    def add_avto(self, avto):
#        if isinstance(avto, Avto):
#            self.avtolar.append(avto)
#        else:
#            print("Avto obyektini kiriting")

#    def __len__(self):
#        return len(self.avtolar)

#    def __getitem__(self, index):
#        return self.avtolar[index]

#    def __setitem__(self, index, value):
#        if isinstance(value, Avto):
#            self.avtolar[index] = value

#    def add_avto(self, *qiymat):
#        for avto in qiymat:
#            if isinstance(avto, Avto):
#                self.avtolar.append(avto)
#            else:
#                print("Avto obyektni kiriting")

#    def __add__(self, qiymat):
#        if isinstance(qiymat, AvtoSalon):
#            yangi_salon = AvtoSalon(f"{self.name} {qiymat.name}")
#            yangi_salon.avtolar = self.avtolar + qiymat.avtolar
#            return yangi_salon
#        elif isinstance(qiymat, Avto):
#            self.add_avto(qiymat)
#        else:
#            print(f"Avtosalonga {type(qiymat)} qo'shib bo'lmaydi")

#    def __call__(self, *param):
#       if param:
#           for avto in param:
#               self.add_avto(avto)
#       else:
#           return [avto for avto in self.avtolar]

#salon1 = AvtoSalon("MaxAvto")
#for avto in [avto1, avto2, avto3]:
#    salon1.add_avto(avto)

#salon1[0] = avto4

#salon1 = AvtoSalon("MaxAvto")
#salon2 = AvtoSalon("Avto Lider")

#salon1.add_avto(avto1, avto2, avto3)
#salon2.add_avto(avto4, avto5, avto6)
#avto_new = Avto("Mercedes", "E200", "Silver", 2015, 80000)
#salon1(avto_new)
#print(salon1())

#salon3 = salon1 + salon2
#salon1 + avto7
#print(salon1[:])
#print(salon3)
#print(salon3[:])
#print(salon3)
#print(salon1())

#with open("pi.txt.txt") as fayl:
#    pi = fayl.read()
#print(pi)
#pi = pi.rstrip()
#pi = pi.replace('\n', '')
#pi = float(pi)
#print(pi)

#faylnomi = 'talabalar.txt'
#with open(faylnomi, 'w+') as fayl:
#    fayl.write("Hello World")

#faylnomi = 'talabalar.txt'
#ism = "Olimjon Xasanov"
#tyil = 2004
#with open(faylnomi, "w+") as fayl:
#    fayl.write(ism+'\n')
#    fayl.write(str(tyil)+'\n')
#with open(faylnomi, 'a') as fayl:
#    fayl.write('Alijon  Valiyev\n')
#    fayl.write('2000')

#import pickle
#talaba1 = {'ism':'hasan', 'familya':'husanov', 'tyil':2003, 'kurs':2}
#talaba2 = {"ism":"dilshod", 'familya':'axmadov', 'tyil':2004, 'kurs':2}
#with open('info', 'wb') as file:
#    pickle.dump(talaba1, file)
#    pickle.dump(talaba2, file)
#with open('info', 'rb') as file:
#    talaba1 = pickle.load(file)
#    talaba2 = pickle.load(file)
#print(talaba1)

#import pickle
#with open('pi_million_digits.txt') as file:
#    pi = file.read()
#pi = pi.rstrip()
#pi = pi.replace('\n', '')
#pi = pi.replace(' ', '')
#bdate = '2004'
#print(bdate in pi)
#pi = float(pi)
#with open('pi_float.txt', 'wb') as file:
#    pickle.dump(pi, file)

#while True:
#    book = input("Yaxshi ko'rgan kitobingizni kiriting (To'xtatish uchun Enter tugmasini bosing): ")
#    if not book:
#        break
#    with open('book.txt', 'a') as file:
#        file.write(book + "\n")

#import json
#bemor = {
#    "ism" : "Axmadov Dilshod",
#    "yosh" : 19,
#    "oila" : False,
#    "allergiya" : None,
#    "dorilar" : [
#        {"nomi" : "Analgin", "miqdori" : 0.5},
#        {"nomi" : "Panadol", "miqdori" : 1.2}
#    ]
#}
#bemor_json = json.dumps(bemor, indent = 4)

#with open('bemor.json', 'w') as file:
#    json.dump(bemor, file, indent=4)
#print(bemor)
#bemor = json.loads(bemor_json)
#file_name = "bemor.json"
#with open(file_name) as f:
#    bemor = json.load(f)
#print(type(bemor))


#DASTURNI TEKSHIRISH

#import datetime as dt
#hozir = dt.datetime.now()
#print(hozir)
#print(hozir.date())
#print(hozir.time())
#print(hozir.hour)
#print(hozir.minute)
#bugun = dt.date.today()
#print(f"Bugungi sana {bugun}")

#import calendar
#year = 2023
#month = 10
#day = calendar.month(year, month)
#print(day)

#bugun = dt.date.today()
#ramazon = dt.date(2024, 4, 20)
#farq = ramazon - bugun
#print(f"RAmazonga {farq.days} kun qoldi")

#vaqt = hozir.strftime("%H:%M:%S")
#print(f"Hozir vaqt: {vaqt}")
#sana  = hozir.strftime("%d-%m-%y")
#print(f"Bugun sana: {sana}")

#import math
#PI = math.pi
#print(PI)
#E = math.e
#print(f"e ning qiymati: {E}")
#print(math.radians(57))
#print(math.log10(10000000))
#print(math.ceil(7889.5686))
#print(math.floor(-12.9666))
#print(round(4469.79466446))
#x = 10
#print(math.sqrt(x))
#print(math.pow(x, 3))

#import re
#word1 = "temir"
#word2 = "tomir"
#word3 = "tulpor"
#andoza = "^t...r"
#print(re.match(andoza, word1))
#print(re.match(andoza, word2))
#print(re.match(andoza, word3))


#import calendar
#months = 12
#for month in range(1, months + 1):
#    year = 2023
#    day = calendar.month(year, month)
#    print(day)

#import re
#andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
#msg = "Yangi parolni kiriting"
#msg += '(kamida: 8 xona, 1 ta bosh va 1 ta kichik, '
#msg += '1 ta son va 1 ta maxsus belgi bo\'lishi kerak): '
#while True:
#   password = input(msg)
#    if re.match(andoza, password):
#        print("Maxfiy so'z qabul qilindi")
#        break
#    else:
#        print("Maxfiy so'z talabga javob bermadi")

#import datetime
#import re

#bugun = datetime.date.today()
#ikki_hafta_oldingi = bugun - datetime.timedelta(days=14)
#for i in range(1, 11):
#    sana = ikki_hafta_oldingi + datetime.timedelta(days=i)
#    print(sana)

#ramazon = datetime.date(2024, 4, 21)
#qurbon = datetime.date(2024, 8, 24)
#farq1 = ramazon - bugun
#farq2 = qurbon - bugun
#print(f"Ramazon hayitigacha {farq1.days} kun, Quurbon hayitigacha esa {farq2.days} kun qoldi")

#def kunlar_soni(birthday):
#    today = datetime.date.today()
#    age = today - birthday
#    yil = age.days//365
#    months = (age.days%365)//30
#    days = (age.days%365)%30
#    return yil, months, days
#birthday = datetime.date(2004, 11, 20)
#yil, month, days = kunlar_soni(birthday)
#print(f"Tug'ilgan kunimga {yil} yil, {month} oy va {days} kun o'tibdi")


#import re
#andoza = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
#message = "Telefon nomeringizni kiriting. "
#message += "Faqatgina o'zbekiston fuqarolari registratsiya qilishi mumkin"
#message += "Shuning uchun o'zbek raqamalaridan birini kiriting: "
#while True:
#    password = input(message)
#    if re.match(andoza, password):
#        print("Telefon raqam qabul qilindi. Siz O'zbekistondasiz")
#        break
#    else:
#        print("Xato teleofon raqam kiritdingiz. Iltimos O'zbekistondagi telefon raqamlardan birini kiriting")

#from googletrans import Translator
#tarjimon = Translator()
#matn_uz = "Python dunyodagi eng mashhur dasturlash tili"
#tarjima = tarjimon.translate(matn_uz)
#tarjima_ru = tarjimon.translate(matn_uz, dest="ru")
#tarjima_kz = tarjimon.translate(matn_uz, dest="kk")
#print(tarjima.text)
#print(tarjima_ru.text)
#print(tarjima_kz)

#import requests
#from pprint import pprint
#manzil = "https://kun.uz/news/main"
#r = requests.get(manzil)
#pprint(r.text)

#import requests
#from bs4 import BeautifulSoup
#sahifa = "https://www.instagram.com/axmadov_dilshod6929/"
#r = requests.get(sahifa)
#soup = BeautifulSoup(r.content, 'html.parser')
#images = soup.find_all('img', class_ = '_aagw')
#image_urls = [img['src'] for img in images]
#for i, url in enumerate(image_urls):
#    sahifa = requests.get(url)
#    with open(f'image_{i}.jpg', 'wb') as f:
#        f.write(sahifa.content)
#print(images)

#import requests
#from bs4 import BeautifulSoup
#from wordcloud import WordCloud
#import matplotlib.pyplot as plt
#sahifa = "https://kun.uz/news/main"
#r = requests.get(sahifa)
#soup = BeautifulSoup(r.text, 'html.parser')
#news = soup.find_all(class_="news-title")
#matn = ""
#for n in news:
#    matn += n.text
#stopwords = ['va', 'bo\'yicha', 'lekin', 'bor', 'ham', 'xil', 'yil']
#wordcloud = WordCloud(width = 1000, height = 1000,
#                      background_color = "white",
#                      stopwords = stopwords,
#                      min_font_size = 20).generate(matn)

#plt.figure(figsize=(8, 8), facecolor=None)
#plt.imshow(wordcloud)
#plt.axis("off")
#plt.tight_layout(pad=0)
#plt.show()

#import wx
#from googletrans import Translator
#tarjimon = Translator()
#class MyFrame(wx.Frame):
#    def __init__(self):
#        super().__init__(parent=None, title="O'zbek-Ingliz Lug'at")
#        panel = wx.Panel(self)
#        my_sizer = wx.BoxSizer(wx.VERTICAL)
#        self.text_ctrl = wx.TextCtrl(panel)
#        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
#        my_btn = wx.Button(panel, label = 'Tarjima')
#        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
#        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)

#        self.text_out = wx.TextCtrl(panel, style=wx.TE_READONLY)
#        my_sizer.Add(self.text_out, 0, wx.ALL | wx.EXPAND, 5)
#        panel.SetSizer(my_sizer)
#        self.Show()

#    def on_press(self, event):
#        value = self.text_ctrl.GetValue()
#        if not value:
#            self.text_out.SetValue("So'z kiritmadingiz")
#        else:
#            tarjima = tarjimon.translate(value, src='uz')
#            self.text_out.SetValue(tarjima.text.capitalize())

#if __name__ == '__main__':
#    app = wx.App()
#    frame = MyFrame
#    app.MainLoop()

#MyFrame()
#from pywebio.input import input, FLOAT
#from pywebio.output import put_text
#from math import pi
#def doira():
#    r = input("Doirani radiusini kiriting:", type=FLOAT)
#    yuza = pi*(r**2)
#    per = 2*pi*r
#    put_text(f"Doiraning yuzi {yuza},\nPerimetri esa {per} ga teng")
#doira()

# print("="*10, "\nWIUT\n", end="" "="*10)



























































































































