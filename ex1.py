class Aeraport: 
    def __init__(self , a_nomi , a_yili , a_shaxri , s_nomi):
        self.a_nomi = a_nomi
        self.a_yili = a_yili
        self.a_shaxri = a_shaxri
        self.s_nomi = s_nomi
    def __str__(self):
        return f"""
Aeraport nomi : {self.a_nomi}
Aeraport ochilgan yil : {self.a_yili}
Aeraport ochilgan shaxar : {self.a_shaxri}
        """
    def info(self):
        print("Samalyot nomi :" , self.s_nomi)
Aaeraport = [input("Aeraport nomi : ") , input("Ochilgan shaxri : ") , input("Ochilgan yili : ")]
while 1:
    print("""
[1] Aeraport haqida malumot
[2] Samalyotlar haqida
[3] Chiqish
    """)
    samalyot = ["Boing 477" , "AvgoRide 455" , "SatdatioTekki" , "ZekkerNation"]
    tanla = int(input("Tanlang : "))
    if tanla == 1:
        a1 = Aeraport(Aaeraport[0] , Aaeraport[2] , Aaeraport[1] , samalyot[0])
        print(a1)
    elif tanla == 2:
        for i in samalyot:
            s1 = Aeraport(Aaeraport[0] , Aaeraport[2] , Aaeraport[1] , i)
            s1.info()
    elif tanla == 3:
        print("Xayr salomat buling !!!")
        exit()
    else:
        print("Notugri tanlov !!!")
