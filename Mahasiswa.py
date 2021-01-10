class Mahasiswa:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def showInfo(self):
        print(f"""INFO
Nama : {self.__name}
Umur : {self.__age}
        """)
