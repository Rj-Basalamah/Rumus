import os
import datetime as dt
import datetime 
from time import sleep as timeout
from time import sleep as jeda
from time import sleep as timeout
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
import time
import sys
h = '\x1b[1;92m' # HIJAU +
u = '\033[95m' # UNGU
def jalanc(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush();jeda(0.05)
     
   
#BANER UMUR
def bnt() :
	print ('\n \33[37;1m ______            __   __  __                     \n /_  __/___  ____  / /  / / / /___ ___  __  _______ \n  / / / __ \/ __ \/ /  / / / / __  __ \/ / / / ___/ \n / / / /_/ / /_/ / /  / /_/ / / / / / / /_/ / /     \n/_/  \____/\____/_/   \____/_/ /_/ /_/\__ _/_/  ')   
                      
#MENHITUNG UMUR
def umur () :
	os.system('clear') ; bnt() 
	print (50*'\033[1;33m═','﹡')
	jalanc ('\n\33[31;1m﹡ \33[32;1mSilahkan masukkan tanggal lahir anda \33[31;1m⸙')
	tanggal = int(input('\33[32;1mTanggal \t :\033[1;33m '))  
	bulan = int(input('\33[32;1mBulan \t \t : \033[1;33m')) 
	tahun = int(input('\33[32;1mTahun \t \t :\033[1;33m ')) 
	n = bulan
	jevi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
	try:
		if n < 0 or n > 12:
			exit()
		nTemp = n - 1
	except ValueError:exit()
	op = jevi[nTemp]
	tgllahir = ("%s %s %s"%(tanggal, op, tahun))
	tl = dt.date(tahun,bulan, tanggal)
	hrumur = tl
	print ('\033[1;33m\n',4*'═','[\33[32;1mINFORMASI ANDA\033[1;33m]', 27*'═','\33[31;1m﹡') 
	jalanc (f'\n\33[32;1mTanggal lahir anda adalah {tgllahir} ') 
	hi = dt.date.today()
	umr = hi - tl
	umrthn = umr.days // 365
	umsw = ( umr.days % 365) // 30
	jmlumr = (umsw * 30) + (umrthn * 365)
	sisa_hari  = umr.days - jmlumr
	jalanc (f'Lahir di hari {tl:%A} ')  
	jalanc (f'Umur {umrthn} tahun, {umsw} bulan, {sisa_hari} hari' ) ; mulai() 
def mulai () :
	io = 'Enter untuk menjalankan script kembali' 
	oi = mark(io, style='white')
	cetak(nel(oi, style='green' ))
	rjb = input(u+'['+h+' ENTER '+u+']') 
	if rjb in ['1'] :
		os.system('python Rumus.py')
	else:
		os.system('python Rumus.py') 
	
umur()