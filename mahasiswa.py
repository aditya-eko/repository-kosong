class Mahasiswa:
    universitas="universitas indonesia"


    def __init__(self,inputnama,inputnip,inpputsemester):
        self.nama=inputnama
        self.nip=inputnip
        self.semester=inpputsemester


    def belajar(self):
        print("saya sedang belajar")

    def ambildata(self):
        return self.nama

    def tambahnilai(self,up):
        return self.semester+up

    def remidi(self,up):
        total= (self.semester+up)/2
        return total




eko=Mahasiswa("eko agus aditya",8348949,7)
adit=Mahasiswa("adits aditya",8999,90)

print(eko.nama)
print(eko.ambildata())
a=eko.tambahnilai(8)
print(a)

remidi=eko.remidi(8)
print(remidi)