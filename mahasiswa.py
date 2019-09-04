class Mahasiswa:
    pass


    def __init__(self,inputnama,inputnip,inpputsemester):
        self.nama=inputnama
        self.nip=inputnip
        self.semester=inpputsemester


    def belajar(self):
        print("saya sedang belajar")



eko=Mahasiswa("eko agus aditya",8348949,7)


print(eko.nama)