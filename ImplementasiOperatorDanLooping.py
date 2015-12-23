print "Implementasi Looping dan Operator pada python"
print "masukkan jumlah mahasiswa uang akan diinput"
i = 0
nama = []
nim = []
nilaiUTS = []
nilaiUAS = []
total = []
banyak = input("Banyak Mahasiswa")
for i in range (banyak):
	a = raw_input ("Nama :")
	nama.append(a)
	b = raw_input ("nim :")
	nim.append(b)
	c = input ("nilaiUTS :")
	nilaiUTS.append(c)
	d = input ("nilaiUAS :")
	nilaiUAS.append(d)
	e = (c + d) / 2
	total.append(e);
	print "---------------"
	
for i in range (banyak):
	print "nama:", nama[i]
	print "nim:", nim[i]
	print "nilaiUTS:", nilaiUTS[i]
	print "nilaiUAS:", nilaiUAS[i]
	print "total:", total[i]