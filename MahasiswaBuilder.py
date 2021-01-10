from Mahasiswa import Mahasiswa


class MahasiswaBuilder:
    def __init__(self):
        self.name = ""
        self.age = 0

    def setName(self, name):
        self.name = name
        return self

    def setAge(self, age):
        self.age = age
        return self

    def build(self):
        return Mahasiswa(self.name, self.age)

