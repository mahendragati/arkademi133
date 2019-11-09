def array(kal):
konsonan=”BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnopqrstvwxyz”
vokal=”AIUEOaiueo”
jumlahvokal=””
jumlahkonsonan=””
for karakter in kal:
	if karakter in vokal:
		jumlahvokal+=karakter
	if karakter in konsonan:
		jumlahkonsonan+=karakter
	totalhuruf=jumlahvokal+jumlahkonsonan
print “banyaknya huruf vokal :”
print len(jumlahvokal)
print “banyaknya huruf konsonan :”
print len(jumlahkonsonan)
print “Setiap huruf dalam kalimat:”
print list(kal)

#program utama
kal=raw_input(“Masukkan kalimat :”)
array(kal)