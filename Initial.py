HOME="/home/honeysweetpotato";
import os
import pickle
class FromTo:
	def __init__(self,frm,to,day):
		self.frm=frm;
		self.to=to;
		self.refresh_day=day;
def Settime():
	from_time=int(raw_input("Jam mulai dihitung (contoh : 3.30 -> input 330) : \n"))
	to_time=int(raw_input("Jam ditutup penggunaan waktunya (sistemnya sama dengan sebelumnya) : \n"))
	day=int(raw_input("Hari perhitungan di reset : \n"))
	fp=open(HOME+"/.usage/Freetime","w");
	freetime=FromTo(from_time,to_time,day)
	os.system("bash Resetcron "+str(day));	
	pickle.dump(freetime,fp)
	fp.close()
Settime();
