class Mahasiswa:
    def __init__(self, name, age, adress):
        self.__name = name
        self.__age = age
        self.__adress = adress

    def showInfo(self):
        print(f"""INFO
Nama : {self.__name}
Umur : {self.__age}
Alamat: {self.__adress}
        """)
