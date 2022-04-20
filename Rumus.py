import os
import sys, math, time, datetime 
from time import sleep as jeda
from datetime import datetime as dt
from rich.table import Table as me
from rich.console import Console as sol
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as colom

# COLORS
x = '\33[m' # DEFAULT
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +

ct = dt.now()
n = ct.month
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:exit()
current = dt.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
tgl = ("%s %s %s"%(ha, op, ta))
tt= time.asctime() 
ticks = tt.split()
del ticks[0:3] 
del ticks [1:2]
punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
jam = ""
for char in ticks :
   if char not in punctuations:
       jam = jam + char
def loading():
        try:
                a = 33
                b = 0
                d = 1
                e = '%' 
                for c in range(a):
                        a -=1
                        b +=1
                        d +=3
                        sys.stdout.write("\r\033[93mMemuat [%s%s\033[93m] %s%s"%("\x1b[1;92m#\033[93m"*b,"\33[m-"*a,d,e)),;sys.stdout.flush()
                        time.sleep(0.1)
        except KeyboardInterrupt:
                sys.exit()
def loading1 () :
	loading() 
	print ('\r                                                   ') 
def jalan(sunade):
	for wibu in sunade +'\n' :
		sys.stdout.write(wibu)
		sys.stdout.flush()
		time.sleep(0.03)
copyright = 'Copyright © 2022'

_rjBasalamah_print_ = print
_rjBasalamah_input_ = input
_rjBasalamah_exit_ = exit
_rjBasalamah_blank_ =  (' ') 
_rjBasalamah_1_ = ['01','1']
_rjBasalamah_2_ = ['02','2']
_rjBasalamah_3_ = ['03','3']
_rjBasalamah_4_ = ['04','05']
_rjBasalamah_5_ = ['05','5']
_rjBasalamah_6_ = ['06','6']
_rjBasalamah_7_ = ['07','7']
_rjBasalamah_8_ = ['08','8'] 
_rjBasalamah_9_ = ['09','9']
_rjBasalamah_10_ = ['10']

_author_abdur_rouf_rjBasalamah_p_Konvers_suhu_fisika = ' 1. Dari Cecius \n 2. Dari suhu reamur \n 3. Dari suhu fahrenheit \n 4. Dari suhu kelvin' 

	

def _rjBasalamah_c_ () :
	os.system('clear') 
# BANNER
def banner():
	wel = '# WELCOME TO RJB \n %s'%(copyright)
	wel1 = mark(wel, style='red')
	wel2 = nel(wel1, style='red') 
	sol().print(wel2, style='on cyan')
	ise = '# 𝐑𝐎𝐔𝐅 𝐉𝐄𝐕𝐈𝐀𝐍 𝐁𝐀𝐒𝐀𝐋𝐀𝐌𝐀𝐇'
	fc = mark(ise, style='green')
	sol().print(fc, style='cyan' )
	kek = '# Jam ( %s ) Tanggal %s'%(jam,tgl) 
	kej = mark(kek, style='white') 
	sol().print(kej, style=' green') 
	io = ' Author\t : Abdur Rouf\n Github\t : Github.com/Rj-Basalamah \n No Wa\t : +6285755085745 ' 
	oi = nel(io, style='cyan')
	cetak(nel(oi, title='[INFO SCRIPT]', style='green' ))
def menu () :
	_rjBasalamah_c_ () 
	banner () 
	wel = '# MENU' 
	wel2 = mark(wel, style='cyan')
	sol().print(wel2) 
	tap = me()
	tap.add_column('NO', style='yellow', justify='center')
	tap.add_column('Rumus Pelajaran', style='yellow', justify='center')
	tap.add_column('Status', style='red', justify='center' ) 
	tap.add_row('[1]','Matematika', 'ON', style=' yellow')
	tap.add_row('[2]','Fisika', 'ON', style=' yellow')
	tap.add_row('[3]' ,'Kimia','OFF' )
	tap.add_row('[4]','Biologi', 'OFF' )
	tap.add_row('[5]','Lain-Lain', 'ON', style=' yellow')
	tap.add_row('[0]','Exit', 'Anda akan keluar', style='yellow' )
	sol().print(tap,style='green',justify='center')
	rjb = input(x+'['+p+'Menu'+x+'] Pilih : ')
	if rjb in _rjBasalamah_1_ :
		matematika () 
	elif rjb in _rjBasalamah_2_ :
		fisika () 
	elif rjb in _rjBasalamah_3_ : 
		menu_belum_tersedia() 
	elif rjb in _rjBasalamah_4_ :
		menu_belum_tersedia () 
	elif rjb in _rjBasalamah_5_ :
		rouf =' 1. Menghitung umur' 
		rouf_jevianz = nel(rouf, style='yellow')
		cetak(nel(rouf_jevianz, title='[Lainlain]', style='green' ))
		rjb = input(x+'['+p+'Lain-lain'+x+'] Pilih : ') 
		if rjb in _rjBasalamah_1_ :
			os.system('python umur.py')
		else:
			menu () 
	elif rjb in ['0','00']:
		os.system('exit') 
	else: 
		menu () 


def menu_belum_tersedia() :
	wel = '# OFF [menu belum tersedia] ' 
	wel2 = mark(wel, style='red')
	sol().print(wel2) 
def diketahui () :
	io = 'Gunakan titik sebagi koma (.) '
	oi = mark(io,style = 'white' )
	cetak(nel(oi, title='[Diketahui]', style='green' ))
def matematika () :
	_rjBasalamah_print_ (_rjBasalamah_blank_) 
	io =' 1. Rumus Kecepatan \n 2. Rumus Debit \n 3. Rumus Skala  \n 4. Rumus Keliling dan Luas Bangun Datar \n 5. Rumus Luas Permukaan dan Volume Bangun Ruang \n 6. Rumus Barisan dan Deret Aritmatika \n 7. Rumus Barisan dan Deret Geometri \n 8. Rumus Peluang' 
	oi = nel(io, style='yellow')
	cetak(nel(oi, title='[MATEMATIKA]', style='green' )) 
	rjb = input(x+'['+p+'Matematika'+x+'] Pilih : ') 
	if rjb in _rjBasalamah_1_ :
		kecepatan () 
	elif rjb in _rjBasalamah_2_ :
		debit () 
	elif rjb in _rjBasalamah_3_ : 
		skala () 
	elif rjb in _rjBasalamah_4_ :
		bangun_datar () 
	elif rjb in _rjBasalamah_5_ :
		bangun_ruang () 
	elif rjb in _rjBasalamah_6_ :
		aritmatika () 
	elif rjb in _rjBasalamah_7_:
		geometri () 
	elif rjb in _rjBasalamah_8_ :
		peluang () 
	else:
		matematika () 
	
def kecepatan () :
	print (' ') 
	oi = 'Rumus MTK yang satu ini digunakan dalam materi Matematika SD kelas 5.' 
	io = mark(oi, style='white') 
	cetak(nel(io, title='[Matematika Kecepatan]', style='green' ))
	io = '\t\t Jarak\n  1. Kecepatan = ▬▬▬▬▬\n\t\t Waktu \n  2. Jarak = Kecepatan x Waktu \n\t       Jarak\n  3. Waktu = ▬▬▬▬▬▬▬▬▬\n\t     Kecepatan' 
	oi = nel(io, style='cyan')
	cetak(nel(oi, title='[Rumus]', style='green' ))
	jh = input(x+'['+p+'Ditanya'+x+'] Pilih : ')
	if jh in ['1','01']:
		print (' ') 
		diketahui () 
		a = float(input('Jarak\t: ')) 
		b = float(input('Waktu\t: ') ) 
		hasil = a/b
		io = ' %s ÷ %s = %s' %(a, b, hasil) 
		oi = nel(io, style='yellow')
		loading() 
		print ('\r                                                   ') 
		cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
	elif jh in ['2']:
		print (' ') 
		diketahui () 
		a = float(input('Kecepatan\t: ')) 
		b = float(input('Waktu\t\t: ') ) 
		hasil = a*b
		io = ' %s ÷ %s = %s' %(a, b, hasil) 
		oi = nel(io, style='yellow')
		loading() 
		print ('\r                                                   ') 
		cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
	elif jh in ['3']:
		print (' ') 
		diketahui () 
		a = float(input('Waktu\t\t: ')) 
		b = float(input('Kecepatan\t: ') ) 
		hasil = a/b
		io = ' %s ÷ %s = %s' %(a, b, hasil) 
		oi = nel(io, style='yellow')
		loading() 
		print ('\r                                                   ') 
		cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
	else :
		kecepatan () 
		
def debit () :
	print (' ') 
	oi = 'Rumus MTK yang satu ini digunakan dalam materi Matematika SD kelas 5.' 
	io = mark(oi, style='white') 
	cetak(nel(io, title='[Matematika Kecepatan]', style='green' ))
	io = '\t     Volume\n  1. Debit = ▬▬▬▬▬▬\n\t     Waktu \n  2. Volume = Debit x Volume \n\t     Volume\n  3. Debit = ▬▬▬▬▬▬\n\t     Waktu ' 
	oi = nel(io, style='cyan')
	cetak(nel(oi, title='[Rumus]', style='green' ))
	jh = input(x+'['+p+'Ditanya'+x+'] Pilih : ')
	if jh in ['1','01']:
		print (' ') 
		diketahui () 
		a = float(input('Volume\t: ')) 
		b = float(input('Waktu\t: ') ) 
		hasil = a/b
		io = ' %s ÷ %s = %s' %(a, b, hasil) 
		oi = nel(io, style='yellow')
		loading() 
		print ('\r                                                   ') 
		cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
	elif jh in ['2']:
		print (' ') 
		diketahui () 
		a = float(input('Debit\t: ')) 
		b = float(input('Volume\t: ') ) 
		hasil = a*b
		io = ' %s ÷ %s = %s' %(a, b, hasil) 
		oi = nel(io, style='yellow')
		loading() 
		print ('\r                                                   ') 
		cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
	elif jh in ['3']:
		print (' ') 
		diketahui () 
		a = float(input('Volume\t: ')) 
		b = float(input('Waktu\t: ') ) 
		hasil = a/b
		io = ' %s ÷ %s = %s' %(a, b, hasil) 
		oi = nel(io, style='yellow')
		loading() 
		print ('\r                                                   ') 
		cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
	else :
		debit ()  

def skala () :
	print (' ') 
	oi = 'Rumus MTK yang satu ini digunakan dalam materi Matematika SD kelas 5.' 
	io = mark(oi, style='white') 
	cetak(nel(io, title='[Matematika Kecepatan]', style='green' ))
	io = '\t     Jarak pada peta\n  1. Skala = ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\t     Jarak Sebenarnya \n  2. Jarak pada peta = Skala x Jarak Sebenarnya \n\t\t\tJarak pada peta\n  3. Jarak Sebenarnya = ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\t\t\t     Skala' 
	oi = nel(io, style='cyan')
	cetak(nel(oi, title='[Rumus]', style='green' ))
	jh = input(x+'['+p+'Ditanya'+x+'] Pilih : ')
	if jh in ['1','01']:
		print (' ') 
		diketahui () 
		a = float(input('Jarak pada peta\t: ')) 
		b = float(input('Jarak senenarnya\t: ') ) 
		hasil = a/b
		io = ' %s ÷ %s = %s' %(a, b, hasil) 
		oi = nel(io, style='yellow')
		loading() 
		print ('\r                                                   ') 
		cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
	elif jh in ['2']:
		print (' ') 
		diketahui () 
		a = float(input('Skala\t\t: ')) 
		b = float(input('Jarak pada peta\t: ') ) 
		hasil = a*b
		io = ' %s ÷ %s = %s' %(a, b, hasil) 
		oi = nel(io, style='yellow')
		loading() 
		print ('\r                                                   ') 
		cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
	elif jh in ['3']:
		print (' ') 
		diketahui () 
		a = float(input('Jarak pada peta\t: ')) 
		b = float(input('Skala\t\t: ') ) 
		hasil = a/b
		io = ' %s ÷ %s = %s' %(a, b, hasil) 
		oi = nel(io, style='yellow')
		loading() 
		print ('\r                                                   ') 
		cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
	else :
		skala ()  
	 
def bangun_datar () :
	print (' ') 
	oi = 'Rumus MTK yang satu ini digunakan dalam materi Matematika sekolah SMP. ' 
	io = mark(oi, style='white') 
	cetak(nel(io, title='[Matematika Bangun Datar]', style='green' ))
	io = ' [1] Keliling\t[2] Luas' 
	oi = nel(io, style='yellow')
	cetak(nel(oi, title='[Rumus]', style='green' ))
	rjb = input(x+'['+p+'Rumus'+x+'] Pilih : ')
	if rjb in ['1'] :
		print (' ') 
		io = ' 1. Persegi \n 2. Persegi panjang \n 3. Jajar genjang \n 4. Segitiga \n 5. Belah ketupat \n 6. Layang-Layang \n 7. Trapesium \n 8. Lingkaran' 
		oi = nel(io, style='yellow')
		cetak(nel(oi, title='[Rumus Keliling]', style='green' ))
		rjb = input(x+'['+p+'Rumus Keliling'+x+'] Pilih : ')
		if rjb in ['1']:
			print (' ') 
			io = ' 1. K = 4 x s \n 2. s = K ÷ 4' 
			oi = nel(io, style='cyan')
			pi = ' K : Keliling \n s : sisi'
			po = nel(pi, style='white')
			cetak(nel(oi, title='[Rumus]', style='green' ))
			cetak(nel(po,title='[Keterangan]' , style='green' )) 
			rjb = input(x+'['+p+'Rumus'+x+'] Pilih : ')
			if rjb in ['1']:
				print (' ') 
				diketahui () 
				a = float(input('Sisi (s)\t : ')) 
				hasil = a*4
				io = ' %s x 4 = %s' %(a,hasil) 
				oi = nel(io, style='yellow')
				loading() 
				print ('\r                                                   ') 
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('Keliling (K)\t : ')) 
				hasil = a*4
				io = ' %s ÷ 4 = %s' %(a,hasil) 
				oi = nel(io, style='yellow')
				loading() 
				print ('\r                                                   ') 
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
			else:
				bangun_datar () 
		elif rjb in ['2' ]:
			print (' ') 
			io = ' 1. K = 2( p + l) \n 2. l = ( K ÷ 2 ) - p \n p = ( K ÷ 2 ) - l' 
			oi = nel(io, style='cyan')
			cetak(nel(oi, title='[Rumus]', style='green' ))
			pi = ' K : Keliling \n p : panjang \n l : lebar' 
			po = nel(pi, style='white')
			cetak(nel(po, title='[Keterangan] ', style='green' ))
			rjb = input(x+'['+p+'Rumus'+x+'] Pilih : ')
			if rjb in ['1']:
				print (' ') 
				diketahui () 
				a = float(input('Panjamg (p) \t : ')) 
				b = float(input('Labar (l) \t : ')) 
				hasil = 2*(a+b)
				io = ' 2 x ( %s + %s ) = %s' %(a, b,hasil) 
				oi = nel(io, style='yellow')
				loading() 
				print ('\r                                                   ') 
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('Keliling (K) \t : ')) 
				b = float(input('Labar (l) \t : ')) 
				hasil = (a/2)-b
				io = ' ( %s ÷ 2 ) - %s = %s' %(a, b,hasil) 
				oi = nel(io, style='yellow')
				loading() 
				print ('\r                                                   ') 
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['3']:
				print (' ') 
				diketahui () 
				a = float(input('Keliling (K) \t : ')) 
				b = float(input('panjang (p) \t : ')) 
				hasil = (a/2)-b
				io = ' ( %s ÷ 2 ) - %s = %s' %(a, b,hasil) 
				oi = nel(io, style='yellow')
				loading() 
				print ('\r                                                   ') 
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			else : 
				bangun_datar () 
		if rjb in ['3']:
			print (' ') 
			io = ' 1. K = a + b + c + d \n 2. a = K - ( b + c + d ) \n 3. b = K - ( a + c + d ) \n 4. c = K - ( a + b + d ) \n 5. d = K - ( a + b + c )' 
			oi = nel(io, style='cyan')
			cetak(nel(oi, title='[Rumus]', style='green' ))
			pi = ' K : Keliling \n a : sisi(a)\n b : sisi(b)  \n c : siss(c) \n d : sisi(d) ' 
			po = nel(pi, style='white')
			cetak(nel(po, title = '[Keterangan]' , style='green' ))
			rjb = input(x+'['+p+'Rumus'+x+'] Pilih : ')
			if rjb in ['1']:
				print (' ') 
				diketahui () 
				a = float(input('Sisi (a)\t : ')) 
				b = float(input('Sisi (b)\t : ')) 
				c = float(input('Sisi (c)\t : ')) 
				d = float(input('Sisi (d)\t : ')) 
				hasil = a+b+c+d
				io = ' %s + %s + %s + %s= %s' %(a, b, c, d,hasil) 
				oi = nel(io, style='yellow')
				loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('Keliling (K)\t : ')) 
				b = float(input('Sisi (b)\t : ')) 
				c = float(input('Sisi (c)\t : ')) 
				d = float(input('Sisi (d)\t : ')) 
				hasil = a-(b+c+d) 
				io = ' %s - ( %s + %s + %s ) = %s' %(a, b, c, d,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['3']:
				print (' ') 
				diketahui () 
				a = float(input('Keliling (K)\t : ')) 
				b = float(input('Sisi (a)\t : ')) 
				c = float(input('Sisi (c)\t : ')) 
				d = float(input('Sisi (d)\t : ')) 
				hasil = a-(b+c+d) 
				io = ' %s - ( %s + %s + %s ) = %s' %(a, b, c, d,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['4']:
				print (' ') 
				diketahui () 
				a = float(input('Keliling (K)\t : ')) 
				b = float(input('Sisi (a)\t : ')) 
				c = float(input('Sisi (b)\t : ')) 
				d = float(input('Sisi (d)\t : ')) 
				hasil = a-(b+c+d) 
				io = ' %s - ( %s + %s + %s ) = %s' %(a, b, c, d,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['5']:
				print (' ') 
				diketahui () 
				a = float(input('Keliling (K)\t : ')) 
				b = float(input('Sisi (a)\t : ')) 
				c = float(input('Sisi (b)\t : ')) 
				d = float(input('Sisi (c)\t : ')) 
				hasil = a-(b+c+d) 
				io = ' %s - ( %s + %s + %s ) = %s' %(a, b, c, d,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			else:
				bangun_datar () 
		if rjb in ['4']:
			print (' ') 
			io = ' 1. K = a + b + c + d \n 2. a = K - ( b + c ) \n 3. b = K - ( a + c ) \n 4. c = K - ( a + b )' 
			oi = nel(io, style='cyan')
			cetak(nel(oi, title='[Rumus]', style='green' ))
			pi = ' K : Keliling \n a : sisi(a)\n b : sisi(b)  \n c : siss(c) \n d : sisi(d) ' 
			po = nel(pi, style='white')
			cetak(nel(po, title = '[Keterangan]' , style='green' ))
			rjb = input(x+'['+p+'Rumus'+x+'] Pilih : ')
			if rjb in ['1']:
				print (' ') 
				diketahui () 
				a = float(input('Sisi (a)\t : ')) 
				b = float(input('Sisi (b)\t : ')) 
				c = float(input('Sisi (c)\t : ')) 
				hasil = a+b+c+d
				io = ' %s + %s + %s = %s' %(a, b, c,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('Keliling (K)\t : ')) 
				b = float(input('Sisi (b)\t : ')) 
				c = float(input('Sisi (c)\t : ')) 
				hasil = a-(b+c) 
				io = ' %s - ( %s + %s ) = %s' %(a, b, c,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['3']:
				print (' ') 
				diketahui () 
				a = float(input('Keliling (K)\t : ')) 
				b = float(input('Sisi (a)\t : ')) 
				c = float(input('Sisi (c)\t : ')) 
				hasil = a-(b+c+d) 
				io = ' %s - ( %s + %s ) = %s' %(a, b, c,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['4']:
				print (' ') 
				diketahui () 
				a = float(input('Keliling (K)\t : ')) 
				b = float(input('Sisi (a)\t : ')) 
				c = float(input('Sisi (b)\t : ')) 
				hasil = a-(b+c+d) 
				io = ' %s - ( %s + %s ) = %s' %(a, b, c,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			else:
				bangun_datar () 
		if rjb in ['5']:
			print (' ') 
			io = ' 1. K = a + b + c + d \n 2. a = K - ( b + c + d ) \n 3. b = K - ( a + c + d ) \n 4. c = K - ( a + b + d ) \n 5. d = K - ( a + b + c )' 
			oi = nel(io, style='cyan')
			cetak(nel(oi, title='[Rumus]', style='green' ))
			pi = ' K : Keliling \n a : sisi(a)\n b : sisi(b)  \n c : siss(c) \n d : sisi(d) ' 
			po = nel(pi, style='white')
			cetak(nel(po, title = '[Keterangan]' , style='green' ))
			rjb = input(x+'['+p+'Rumus'+x+'] Pilih : ')
			if rjb in ['1']:
				print (' ') 
				diketahui () 
				a = float(input('Sisi (a)\t : ')) 
				b = float(input('Sisi (b)\t : ')) 
				c = float(input('Sisi (c)\t : ')) 
				d = float(input('Sisi (d)\t : ')) 
				hasil = a+b+c+d
				io = ' %s + %s + %s + %s= %s' %(a, b, c, d,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('Keliling (K)\t : ')) 
				b = float(input('Sisi (b)\t : ')) 
				c = float(input('Sisi (c)\t : ')) 
				d = float(input('Sisi (d)\t : ')) 
				hasil = a-(b+c+d) 
				io = ' %s - ( %s + %s + %s ) = %s' %(a, b, c, d,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['3']:
				print (' ') 
				diketahui () 
				a = float(input('Keliling (K)\t : ')) 
				b = float(input('Sisi (a)\t : ')) 
				c = float(input('Sisi (c)\t : ')) 
				d = float(input('Sisi (d)\t : ')) 
				hasil = a-(b+c+d) 
				io = ' %s - ( %s + %s + %s ) = %s' %(a, b, c, d,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['4']:
				print (' ') 
				diketahui () 
				a = float(input('Keliling (K)\t : ')) 
				b = float(input('Sisi (a)\t : ')) 
				c = float(input('Sisi (b)\t : ')) 
				d = float(input('Sisi (d)\t : ')) 
				hasil = a-(b+c+d) 
				io = ' %s - ( %s + %s + %s ) = %s' %(a, b, c, d,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['5']:
				print (' ') 
				diketahui () 
				a = float(input('Keliling (K)\t : ')) 
				b = float(input('Sisi (a)\t : ')) 
				c = float(input('Sisi (b)\t : ')) 
				d = float(input('Sisi (c)\t : ')) 
				hasil = a-(b+c+d) 
				io = ' %s - ( %s + %s + %s ) = %s' %(a, b, c, d,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			else:
				bangun_datar () 
		if rjb in ['6' ]:
			print (' ') 
			io = ' 1. K = a + b + c + d \n 2. a = K - ( b + c + d ) \n 3. b = K - ( a + c + d ) \n 4. c = K - ( a + b + d ) \n 5. d = K - ( a + b + c )' 
			oi = nel(io, style='cyan')
			cetak(nel(oi, title='[Rumus]', style='green' ))
			pi = ' K : Keliling \n a : sisi(a)\n b : sisi(b)  \n c : siss(c) \n d : sisi(d) ' 
			po = nel(pi, style='white')
			cetak(nel(po, title = '[Keterangan]' , style='green' ))
			rjb = input(x+'['+p+'Rumus'+x+'] Pilih : ')
			if rjb in ['1']:
				print (' ') 
				diketahui () 
				a = float(input('Sisi (a)\t : ')) 
				b = float(input('Sisi (b)\t : ')) 
				c = float(input('Sisi (c)\t : ')) 
				d = float(input('Sisi (d)\t : ')) 
				hasil = a+b+c+d
				io = ' %s + %s + %s + %s= %s' %(a, b, c, d,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('Keliling (K)\t : ')) 
				b = float(input('Sisi (b)\t : ')) 
				c = float(input('Sisi (c)\t : ')) 
				d = float(input('Sisi (d)\t : ')) 
				hasil = a-(b+c+d) 
				io = ' %s - ( %s + %s + %s ) = %s' %(a, b, c, d,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['3']:
				print (' ') 
				diketahui () 
				a = float(input('Keliling (K)\t : ')) 
				b = float(input('Sisi (a)\t : ')) 
				c = float(input('Sisi (c)\t : ')) 
				d = float(input('Sisi (d)\t : ')) 
				hasil = a-(b+c+d) 
				io = ' %s - ( %s + %s + %s ) = %s' %(a, b, c, d,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['4']:
				print (' ') 
				diketahui () 
				a = float(input('Keliling (K)\t : ')) 
				b = float(input('Sisi (a)\t : ')) 
				c = float(input('Sisi (b)\t : ')) 
				d = float(input('Sisi (d)\t : ')) 
				hasil = a-(b+c+d) 
				io = ' %s - ( %s + %s + %s ) = %s' %(a, b, c, d,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['5']:
				print (' ') 
				diketahui () 
				a = float(input('Keliling (K)\t : ')) 
				b = float(input('Sisi (a)\t : ')) 
				c = float(input('Sisi (b)\t : ')) 
				d = float(input('Sisi (c)\t : ')) 
				hasil = a-(b+c+d) 
				io = ' %s - ( %s + %s + %s ) = %s' %(a, b, c, d,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			else:
				bangun_datar () 
		if rjb in ['7']:
			print (' ') 
			io = ' 1. K = a + b + c + d \n 2. a = K - ( b + c + d ) \n 3. b = K - ( a + c + d ) \n 4. c = K - ( a + b + d ) \n 5. d = K - ( a + b + c )' 
			oi = nel(io, style='cyan')
			cetak(nel(oi, title='[Rumus]', style='green' ))
			pi = ' K : Keliling \n a : sisi(a)\n b : sisi(b)  \n c : siss(c) \n d : sisi(d) ' 
			po = nel(pi, style='white')
			cetak(nel(po, title = '[Keterangan]' , style='green' ))
			rjb = input(x+'['+p+'Rumus'+x+'] Pilih : ')
			if rjb in ['1']:
				print (' ') 
				diketahui () 
				a = float(input('Sisi (a)\t : ')) 
				b = float(input('Sisi (b)\t : ')) 
				c = float(input('Sisi (c)\t : ')) 
				d = float(input('Sisi (d)\t : ')) 
				hasil = a+b+c+d
				io = ' %s + %s + %s + %s= %s' %(a, b, c, d,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('Keliling (K)\t : ')) 
				b = float(input('Sisi (b)\t : ')) 
				c = float(input('Sisi (c)\t : ')) 
				d = float(input('Sisi (d)\t : ')) 
				hasil = a-(b+c+d) 
				io = ' %s - ( %s + %s + %s ) = %s' %(a, b, c, d,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['3']:
				print (' ') 
				diketahui () 
				a = float(input('Keliling (K)\t : ')) 
				b = float(input('Sisi (a)\t : ')) 
				c = float(input('Sisi (c)\t : ')) 
				d = float(input('Sisi (d)\t : ')) 
				hasil = a-(b+c+d) 
				io = ' %s - ( %s + %s + %s ) = %s' %(a, b, c, d,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['4']:
				print (' ') 
				diketahui () 
				a = float(input('Keliling (K)\t : ')) 
				b = float(input('Sisi (a)\t : ')) 
				c = float(input('Sisi (b)\t : ')) 
				d = float(input('Sisi (d)\t : ')) 
				hasil = a-(b+c+d) 
				io = ' %s - ( %s + %s + %s ) = %s' %(a, b, c, d,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['5']:
				print (' ') 
				diketahui () 
				a = float(input('Keliling (K)\t : ')) 
				b = float(input('Sisi (a)\t : ')) 
				c = float(input('Sisi (b)\t : ')) 
				d = float(input('Sisi (c)\t : ')) 
				hasil = a-(b+c+d) 
				io = ' %s - ( %s + %s + %s ) = %s' %(a, b, c, d,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			else:
				bidang_datar () 
		if rjb in ['8']:
			print (' ') 
			io = ' 1. K = 2 x π x r \n 2. K = π x d\n 3. r = D ÷ 2' 
			oi = nel(io, style='cyan')
			cetak(nel(oi, title='[Rumus]', style='green' ))
			pi = ' K : Keliling \n π : ²²/7 / 3.14\n r : jari-jari \n D : diameter' 
			po = nel(pi, style='white')
			cetak(nel(po, title = '[Keterangan]' , style='green' ))
			rjb = input(x+'['+p+'Rumus'+x+'] Pilih : ')
			if rjb in ['1']:
				print (' ') 
				diketahui () 
				a = float(input('Jari jari (r)\t : ')) 
				hasil = (22/7)*2*a
				io = ' 3,14 x 2 x %s = %s' %(a, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('Diameter (d)\t : ')) 
				hasil = (22/7)*a
				io = ' 3,14 x %s = %s' %(a, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['3']:
				print (' ') 
				diketahui () 
				a = float(input('Diameter(r)\t : ')) 
				hasil = a/2
				io = ' %s ÷ 2 = %s' %(a, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			else:
				bangun_datar () 
		else:
			bangun_datar() ; os.system('1\n' )
	if rjb in ['2'] :
		print (' ') 
		io = ' 1. Persegi \n 2. Persegi panjang \n 3. Jajar genjang \n 4. Segitiga \n 5. Belah ketupat \n 6. Layang-Layang \n 7. Trapesium \n 8. Lingkaran' 
		oi = nel(io, style='yellow')
		cetak(nel(oi, title='[Rumus Luas]', style='green' ))
		rjb = input(x+'['+p+'Rumus Luas'+x+'] Pilih : ')
		if rjb in ['1']:
			print (' ') 
			io = ' 1. L = s x 2\n 2. s = L ÷ 2' 
			oi = nel(io, style='cyan')
			pi = ' L : Luas \n p : Panjang \n l : Lebar'
			po = nel(pi, style='white') ; loading1 ()
			cetak(nel(oi, title='[Rumus]', style='green' ))
			cetak(nel(po,title='[Keterangan]' , style='green' )) 
			rjb = input(x+'['+p+'Rumus'+x+'] Pilih : ')
			if rjb in  ['1']:
				print (' ') 
				diketahui () 
				a = float(input('Sisi ()\t : ')) 
				hasil = a*2
				io = ' %s x 2 = %s' %(a, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('Luas (L)\t : ')) 
				hasil = a/b
				io = ' %s ÷ 2 = %s' %(a,hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			else :
				bangun_datar () 
		elif rjb in ['2']:
			print (' ') 
			io = ' 1. L = p x l\n 2. p = L ÷ l \n l = L ÷ p' 
			oi = nel(io, style='cyan')
			pi = ' L : Luas \n p : Panjang \n l : Lebar'
			po = nel(pi, style='white')
			cetak(nel(oi, title='[Rumus]', style='green' ))
			cetak(nel(po,title='[Keterangan]' , style='green' )) 
			rjb = input(x+'['+p+'Rumus'+x+'] Pilih : ')
			if rjb in ['1']:
				print (' ') 
				diketahui () 
				a = float(input('Panjang (p)\t : ')) 
				b = float(input('Lebar (l)\t : ')) 
				hasil = a*b
				io = ' %s x %s = %s' %(a,b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('Luas (L)\t : ')) 
				b = float(input('Lebar (l)\t : ')) 
				hasil = a/b
				io = ' %s ÷ %s = %s' %(a,b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['3']:
				print (' ') 
				diketahui () 
				a = float(input('Luas (L)\t : ')) 
				b = float(input('Panjang (p)\t : ')) 
				hasil = a/b
				io = ' %s ÷ %s = %s' %(a,b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			else:
				bangun_datar () 
		elif rjb in ['3']:
			print (' ') 
			io = ' 1. L = a x t\n 2. a = L ÷ t\n 3. t = L ÷ a' 
			oi = nel(io, style='cyan')
			pi = ' L : Luas \n a : Alas \n t : Tinggi' 
			po = nel(pi, style='white')
			cetak(nel(oi, title='[Rumus]', style='green' ))
			cetak(nel(po,title='[Keterangan]' , style='green' )) 
			rjb = input(x+'['+p+'Rumus'+x+'] Pilih : ')
			if rjb in ['1']:
				print (' ') 
				diketahui () 
				a = float(input('Alas (a)\t : ')) 
				b = float(input('tinggi (t)\t : ')) 
				hasil = a*b
				io = ' %s x %s = %s' %(a,b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('Luas (L)\t : ')) 
				b = float(input('TInggi (t)\t : ')) 
				hasil = a/b
				io = ' %s ÷ %s = %s' %(a,b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['3']:
				print (' ') 
				diketahui () 
				a = float(input('Luas (L)\t : ')) 
				b = float(input('Alas (a)\t : ')) 
				hasil = a/b
				io = ' %s ÷ %s = %s' %(a,b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			else:
				bangun_datar () 
		elif rjb in ['5' ]:
			print (' ') 
			io = ' 1. L = ½ d1 x d2\n 2. d1 = 2 ( L ÷ d2 ) \n 3. d2 = 2 ( L ÷ d1 ) '
			oi = nel(io, style='cyan')
			pi = ' L : Luas \n d1 : Diameter 1 \n d2 : Diameter 2'
			po = nel(pi, style='white')
			cetak(nel(oi, title='[Rumus]', style='green' ))
			cetak(nel(po,title='[Keterangan]' , style='green' )) 
			rjb = input(x+'['+p+'Rumus'+x+'] Pilih : ')
			if rjb in ['1']:
				print (' ') 
				diketahui () 
				a = float(input('Diameter 1 (d1)\t : ')) 
				b = float(input('Diameter 2 (d2)\t : ')) 
				hasil = (1/2)*a*b
				io = ' ½ x %s x %s = %s' %(a,b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('Luas (L)\t : ')) 
				b = float(input('Diameter 2 (d2)\t : ')) 
				hasil = (a/b)*2
				io = ' ( %s ÷ %s ) x 2 = %s' %(a,b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['3']:
				print (' ') 
				diketahui () 
				a = float(input('Luas (L)\t : ')) 
				b = float(input('Diameter 1 (d1)\t : ')) 
				hasil = (a/b)*2
				io = ' ( %s ÷ %s ) x 2 = %s' %(a,b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			else:
				bangun_datar () 
		elif rjb in ['4' ]:
			print (' ') 
			io = ' 1. L = ½ a x t\n 2. a = 2 ( L ÷ t ) \n 3. t = 2 ( L ÷ a ) '
			oi = nel(io, style='cyan')
			pi = ' L : Luas \n a : Alas \n t : Tinggi' 
			po = nel(pi, style='white')
			cetak(nel(oi, title='[Rumus]', style='green' ))
			cetak(nel(po,title='[Keterangan]' , style='green' )) 
			rjb = input(x+'['+p+'Rumus'+x+'] Pilih : ')
			if rjb in ['1']:
				print (' ') 
				diketahui () 
				a = float(input('Alas (a)\t : ')) 
				b = float(input('tinggi (t)\t : ')) 
				hasil = (1/2)*a*b
				io = ' ½ x %s x %s = %s' %(a,b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('Luas (L)\t : ')) 
				b = float(input('TInggi (t)\t : ')) 
				hasil = (a/b)*2
				io = ' ( %s ÷ %s ) x 2 = %s' %(a,b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['3']:
				print (' ') 
				diketahui () 
				a = float(input('Luas (L)\t : ')) 
				b = float(input('Alas (a)\t : ')) 
				hasil = (a/b)*2
				io = ' ( %s ÷ %s ) x 2 = %s' %(a,b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			else:
				bangun_datar () 
		elif rjb in ['6' ]:
			print (' ') 
			io = ' 1. L = ½ d1 x d2\n 2. d1 = 2 ( L ÷ d2 ) \n 3. d2 = 2 ( L ÷ d1 ) '
			oi = nel(io, style='cyan')
			pi = ' L : Luas \n p : Panjang \n l : Lebar'
			po = nel(pi, style='white')
			cetak(nel(oi, title='[Rumus]', style='green' ))
			cetak(nel(po,title='[Keterangan]' , style='green' )) 
			rjb = input(x+'['+p+'Rumus'+x+'] Pilih : ')
			if rjb in ['1']:
				print (' ') 
				diketahui () 
				a = float(input('Diameter 1 (d1)\t : ')) 
				b = float(input('Diameter 2 (d2)\t : ')) 
				hasil = (1/2)*a*b
				io = ' ½ x %s x %s = %s' %(a,b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('Luas (L)\t : ')) 
				b = float(input('Diameter 2 (d2)\t : ')) 
				hasil = (a/b)*2
				io = ' ( %s ÷ %s ) x 2 = %s' %(a,b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['3']:
				print (' ') 
				diketahui () 
				a = float(input('Luas (L)\t : ')) 
				b = float(input('Diameter 1 (d1)\t : ')) 
				hasil = (a/b)*2
				io = ' ( %s ÷ %s ) x 2 = %s' %(a,b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			else :
				bangun_datar () 
		elif rjb in ['7']:
			print (' ') 
			io = ' 1. L = ½ x ( a + b) x t\n 2. a = 2 ( L ÷ t ) - b \n 3. b = 2 ( L ÷ t ) -  a \n 4. t = 2 ( L ÷ ( a + b ) ) '
			oi = nel(io, style='cyan')
			pi = ' L : Luas \n a : Sisi (a) \n b : Sisi (b) \n t : Tinggi' 
			po = nel(pi, style='white')
			cetak(nel(oi, title='[Rumus]', style='green' ))
			cetak(nel(po,title='[Keterangan]' , style='green' )) 
			rjb = input(x+'['+p+'Rumus'+x+'] Pilih : ')
			if rjb in ['1']:
				print (' ') 
				diketahui () 
				a = float(input('Sisi (a)\t : ')) 
				b = float(input('Sisi (b)\t : ')) 
				c = float(input('tinggi (t)\t : ')) 
				hasil = (1/2)*(a+b)*c
				io = ' ½ x %s x %s = %s' %(a,b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('Luas (L)\t : ')) 
				b = float(input('Sisi (b)\t : ')) 
				c = float(input('tinggi (t)\t : ')) 
				hasil = 2*(a/c)-b
				io = ' 2 x ( %s + %s ) - %s= %s' %(a,c, b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['3']:
				print (' ') 
				diketahui () 
				a = float(input('Luas (L)\t : ')) 
				b = float(input('Sisi (a)\t : ')) 
				c = float(input('tinggi (t)\t : ')) 
				hasil = 2*(a/c) - b
				io = ' 2 x ( %s ÷ %s ) - %s = %s' %(a,c, b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['4']:
				print (' ') 
				diketahui () 
				a = float(input('Luas (L)\t : ')) 
				b = float(input('Sisi (a)\t : ')) 
				c = float(input('sisi (b)\t : ')) 
				hasil = 2*(a/(b+c))
				io = ' ( %s ÷ %s ) x 2 = %s' %(a,b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			else :
				bangun_datar () 
		if rjb in ['8']:
			print (' ') 
			io = ' 1. L = π x r x r \n 2. r = D ÷ 2' 
			oi = nel(io, style='cyan')
			cetak(nel(oi, title='[Rumus]', style='green' ))
			pi = ' K : Keliling \n π : ²²/7 / 3.14\n r : jari-jari \n D : diameter' 
			po = nel(pi, style='white')
			cetak(nel(po, title = '[Keterangan]' , style='green' ))
			rjb = input(x+'['+p+'Rumus'+x+'] Pilih : ')
			if rjb in ['1']:
				print (' ') 
				diketahui () 
				a = float(input('Jari jari (r)\t : ')) 
				hasil = (22/7)*a*a
				io = ' 3,14 x %s x %s = %s' %(a, a, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('Diameter(r)\t : ')) 
				hasil = a/2
				io = ' %s ÷ 2 = %s' %(a, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			else:
				bangun_datar ()  
		else :
			bangun_datar ();os.system('2')
	else:
		bangun_datar() 
def bangun_ruang () :
	print (' ') 
	oi = 'Rumus MTK yang satu ini digunakan dalam materi Matematika sekolah SMP. ' 
	io = mark(oi, style='white') 
	cetak(nel(io, title='[Matematika Bangun Ruang]', style='green' ))
	io = ' [1] Luas Permukaan\t[2] Volume' 
	oi = nel(io, style='yellow')
	cetak(nel(oi, title='[Rumus]', style='green' ))
	rjb = input(x+'['+p+'Rumus'+x+'] Pilih : ')
	if rjb in ['1'] :
		print (' ') 
		io = ' 1. Kubus \n 2. Balok \n 3. Limas Segi (3-6)\n 4. Prisma Segi (3,5,6,8) \n 5. Silinder (Tabung) \n 6. Kerucut \n 7. Bola' 
		oi = nel(io, style='yellow')
		cetak(nel(oi, title='[Rumus Luas Permukaan]', style='green' ))
		rjb = input(x+'['+p+'Rumus Luas Permukaan'+x+'] Pilih : ') 
		if rjb in ['1']:
			print (' ') 
			io = ' L = 6 x R²' 
			oi = nel(io, style='cyan')
			pi = ' L : Luas Permukaan \n R : Rusuk'
			po = nel(pi, style='white') ; loading1 ()
			cetak(nel(oi, title='[Rumus]', style='green' ))
			cetak(nel(po,title='[Keterangan]' , style='green' )) 
			print (' ') 
			diketahui () 
			a = float(input('Rusuk\t : ')) 
			hasil = 6*a*a
			io = ' 6 x %s² = %s' %(a, hasil) 
			oi = nel(io, style='yellow') ; loading1 ()
			cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
		elif  rjb in ['2' ]:
			print (' ') 
			io = ' L = 2( p + l + l + t + t + p ) ' 
			oi = nel(io, style='cyan')
			pi = ' L : Luas Permukaan \n p : Panjang \n l : Lebar \n t : Tinggi'
			po = nel(pi, style='white')
			cetak(nel(oi, title='[Rumus Balok]', style='green' ))
			cetak(nel(po,title='[Keterangan]' , style='green' )) 
			print (' ') 
			diketahui () 
			a = float(input('Panjang\t : ')) 
			b = float(input('Lebar\t : ')) 
			c = float(input('Tinggi\t : ')) 
			hasil = 2*(a+b+b+c+c+a) 
			io = ' 2 x ( %s + %s + %s + %s + %s + %s = %s' %(a, b, b, c, c, a, hasil) 
			oi = nel(io, style='yellow') ; loading1 ()
			cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
		elif  rjb in ['3' ]:
			print (' ') 
			io = ' 1. Segitiga = ( ½ x a x t ) + ( 3 x luas sisi tegak )\n 2. Segiempat =  ( s x s ) + ( 4 x luas sisi tegak ) \n 3. Segilima = ( 1,72 x s x s ) + ( 5 x luas sisi tegak ) \n 4. Segienam = ( 2,598 x s x s ) + ( 6 x Luas sisi tegak )' 
			oi = nel(io, style='cyan')
			pi = ' L : Luas Permukaan \n a : Alas \n s : sisi \n t : Tinggi\n Luas sisi tegak => (menggunakan perhitungan phytagoras)'
			po = nel(pi, style='white')
			cetak(nel(oi, title='[Rumus Limas]', style='green' ))
			cetak(nel(po,title='[Keterangan]' , style='green' ))  
			rjb = input(x+'['+p+'Luas Permukaan Limas'+x+'] Pilih : ') 
			if rjb in ['1']:
				print (' ') 
				diketahui () 
				a = float(input('\rAlas\t\t : ')) 
				b = float(input('\rTinggi\t\t : ')) 
				rjs = input('\rIsi otomatis Luas sisi tegak y/t : ') 
				if rjs in ['y', 'Y'] :
					akar = ((a/2)**2)+(b**2)
					xyd = math.sqrt(akar)
					lts = (a/2)*xyd
					jalan('\rLuas sisi tega\t : ' +str(lts))
					c = lts
					hasil = ((1/2)*a*a)+(3*c)
					io = '( ½ x %s x %s ) + ( 3 x %s ) = %s' %(a, a, c, hasil) 
					oi = nel(io, style='yellow') ; loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
				elif rjs in ['t', 'T'] :
					c = float(input('\rLuas sisi tegak\t : ')) 
					hasil = ((1/2)*a*a)+(3*c)
					io = '( ½ x %s x %s ) + ( 3 x %s ) = %s' %(a, a, c, hasil) 
					oi = nel(io, style='yellow') ; loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
				else :
					c = float(input('\rLuas sisi tegak\t : ')) 
					hasil = ((1/2)*a*a)+(3*c)
					io = '( ½ x %s x %s ) + ( 3 x %s ) = %s' %(a, a, c, hasil) 
					oi = nel(io, style='yellow') ; loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('sisi\t\t : ')) 
				b = float(input('\rTinggi\t\t : ')) 
				rjs = input('\rIsi otomatis Luas sisi tegak y/t : ') 
				if rjs in ['y', 'Y'] :
					akar = ((a/2)**2)+(b**2)
					xyd = math.sqrt(akar)
					lts = (a/2)*xyd
					jalan('\rLuas sisi tega\t : ' +str(lts))
					c = lts
					hasil = (a*a)+(4*c)
					io = '( %s x %s ) + ( 4 x %s ) = %s' %(a, a, c, hasil) 
					oi = nel(io, style='yellow') ; loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
				elif rjs in ['t', 'T'] :
					c = float(input('\rLuas sisi tegak\t : ')) 
					hasil = (a*a)+(4*c)
					io = '( %s x %s ) + ( 4 x %s ) = %s' %(a, a, c, hasil) 
					oi = nel(io, style='yellow') ; loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
				else :
					c = float(input('\rLuas sisi tegak\t : ')) 
					hasil = (a*a)+(4*c)
					io = '( %s x %s ) + ( 4 x %s ) = %s' %(a, a, c, hasil) 
					oi = nel(io, style='yellow') ; loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
			elif rjb in ['3']:
				print (' ') 
				diketahui () 
				a = float(input('sisi\t\t : ')) 
				b = float(input('\rTinggi\t\t : ')) 
				rjs = input('\rIsi otomatis Luas sisi tegak y/t : ') 
				if rjs in ['y', 'Y'] :
					akar = ((a/2)**2)+(b**2)
					xyd = math.sqrt(akar)
					lts = (a/2)*xyd
					jalan('\rLuas sisi tega\t : ' +str(lts))
					c = lts
					hasil = (1.72*a*a)+(5*c)
					io = '( 1,72 %s x %s ) + ( 5 x %s ) = %s' %(a, a, c, hasil) 
					oi = nel(io, style='yellow') ; loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
				elif rjs in ['t', 'T'] :
					c = float(input('\rLuas sisi tegak\t : ')) 
					hasil = (1.72*a*a)+(5*c)
					io = '( 1,72 %s x %s ) + ( 5 x %s ) = %s' %(a, a, c, hasil) 
					oi = nel(io, style='yellow') ; loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
				else :
					c = float(input('\rLuas sisi tegak\t : ')) 
					hasil = (1.72*a*a)+(5*c)
					io = '( 1,72 %s x %s ) + ( 5 x %s ) = %s' %(a, a, c, hasil) 
					oi = nel(io, style='yellow') ; loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
			elif rjb in ['4' ]:
				print (' ') 
				diketahui () 
				a = float(input('sisi\t\t : ')) 
				b = float(input('\rTinggi\t\t : ')) 
				rjs = input('\rIsi otomatis Luas sisi tegak y/t : ') 
				if rjs in ['y', 'Y'] :
					akar = ((a/2)**2)+(b**2)
					xyd = math.sqrt(akar)
					lts = (a/2)*xyd
					jalan('\rLuas sisi tega\t : ' +str(lts))
					c = lts
					hasil = (2.598*a*a)+(6*c)
					io = '( %s x %s ) + ( 6 x %s ) = %s' %(a, a, c, hasil) 
					oi = nel(io, style='yellow') ; loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
				elif rjs in ['t', 'T'] :
					c = float(input('\rLuas sisi tegak\t : ')) 
					hasil = (2.598*a*a)+(6*c)
					io = '( %s x %s ) + ( 6 x %s ) = %s' %(a, a, c, hasil) 
					oi = nel(io, style='yellow') ; loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
				else :
					c = float(input('\rLuas sisi tegak\t : ')) 
					hasil = (2.598*a*a)+(6*c)
					io = '( %s x %s ) + ( 6 x %s ) = %s' %(a, a, c, hasil) 
					oi = nel(io, style='yellow') ; loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
			else:
				bangun_ruang () 
		elif  rjb in ['4']:
			print (' ') 
			io = ' 1. Segitiga = ( 2 x a ) + ( Keliling alas x t )\n 2. Segilima =  ( 2 x ( 1,72 x s x s ) ) + ( Keliling alas x t ) \n 3. Segienam = ( 2 x( 2,598 x s x s ) + ( Keliling alas x t ) \n 4. Segidelapan = ( 2 x ( ⅔ x s x s ) + ( Keliling alas x t )' 
			oi = nel(io, style='cyan')
			pi = ' L : Luas Permukaan \n a : Alas \n s : sisi \n t : Tinggi\n Panjang keliling alas=> ( dapat menggunakan hitungan otomatis)'
			po = nel(pi, style='white')
			cetak(nel(oi, title='[Rumus Prisma]', style='green' ))
			cetak(nel(po,title='[Keterangan]' , style='green' ))  
			rjb = input(x+'['+p+'Luas Permukaan Prisma'+x+'] Pilih : ') 
			if rjb in ['1']:
				print (' ') 
				diketahui () 
				a = float(input('\rAlas\t\t : ')) 
				b = float(input('\rTinggi\t\t : ')) 
				rjs = input('\rIsi otomatis Keliling alas y/t : ') 
				if rjs in ['y', 'Y'] :
					alas = a*4
					jalan('\rKeliling alas\t : ' +str(alas))
					c = alas
					hasil = (2*a)+(b*c)
					io = '( 2 x %s ) + ( %s x %s ) = %s' %(a, c, b, hasil) 
					oi = nel(io, style='yellow') ; loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
				elif rjs in ['t', 'T'] :
					c = float(input('\rKeliling alas\t : ')) 
					hasil = (2*a)+(b*c)
					io = '( 2 x %s ) + ( %s x %s ) = %s' %(a, c, b, hasil) 
					oi = nel(io, style='yellow') ; loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
				else :
					c = float(input('\rKeliling alas\t : ')) 
					hasil = (2*a)+(b*c)
					io = '( 2 x %s ) + ( %s x %s ) = %s' %(a, c, b, hasil) 
					oi = nel(io, style='yellow') ; loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('\rSisi (s) \t\t : ')) 
				b = float(input('\rTinggi\t\t : ')) 
				rjs = input('\rIsi otomatis Keliling alas y/t : ') 
				if rjs in ['y', 'Y'] :
					alas = a*5
					jalan('\rKeliling alas\t : ' +str(alas))
					c = alas
					hasil = (2*(1.72*a*a))+(b*c)
					io = ' ( 2 x ( 1,72 x %s x %s ) ) + ( %s x %s ) = %s' %(a, a, c, b, hasil) 
					oi = nel(io, style='yellow')
					loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
				elif rjs in ['t', 'T'] :
					c = float(input('\rLuas sisi tegak\t : ')) 
					hasil = (2*(1.72*a*a))+(b*c)
					io = ' ( 2 x ( 1,72 x %s x %s ) ) + ( %s x %s ) = %s' %(a, a, c, b, hasil) 
					oi = nel(io, style='yellow')
					loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
				else :
					c = float(input('\rLuas sisi tegak\t : ')) 
					hasil = (2*(1.72*a*a))+(b*c)
					io = ' ( 2 x ( 1,72 x %s x %s ) ) + ( %s x %s ) = %s' %(a, a, c, b, hasil) 
					oi = nel(io, style='yellow')
					loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
			elif rjb in ['3']:
				print (' ') 
				diketahui () 
				a = float(input('\rSisi (s) \t\t : ')) 
				b = float(input('\rTinggi\t\t : ')) 
				rjs = input('\rIsi otomatis Keliling alas y/t : ') 
				if rjs in ['y', 'Y'] :
					alas = a*6
					jalan('\rKeliling alas\t : ' +str(alas))
					c = alas
					hasil = (2*(2.598*a*a))+(b*c)
					io = ' ( 2 x ( 2,598 x %s x %s ) ) + ( %s x %s ) = %s' %(a, a, c, b, hasil) 
					oi = nel(io, style='yellow')
					loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
				elif rjs in ['t', 'T'] :
					c = float(input('\rLuas sisi tegak\t : ')) 
					hasil = (2*(2.598*a*a))+(b*c)
					io = ' ( 2 x ( 2,598 x %s x %s ) ) + ( %s x %s ) = %s' %(a, a, c, b, hasil) 
					oi = nel(io, style='yellow')
					loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
				else :
					c = float(input('\rLuas sisi tegak\t : ')) 
					hasil = (2*(2.598*a*a))+(b*c)
					io = ' ( 2 x ( 2,598 x %s x %s ) ) + ( %s x %s ) = %s' %(a, a, c, b, hasil) 
					oi = nel(io, style='yellow')
					loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
			elif rjb in ['4']:
				print (' ') 
				diketahui () 
				a = float(input('\rSisi (s) \t\t : ')) 
				b = float(input('\rTinggi\t\t : ')) 
				rjs = input('\rIsi otomatis Keliling alas y/t : ') 
				if rjs in ['y', 'Y'] :
					alas = a*8
					jalan('\rKeliling alas\t : ' +str(alas))
					c = alas
					hasil = (2*((2/3)*a*a))+(b*c)
					io = ' ( 2 x ( ⅔ x %s x %s ) ) + ( %s x %s ) = %s' %(a, a, c, b, hasil) 
					oi = nel(io, style='yellow')
					loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
				elif rjs in ['t', 'T'] :
					c = float(input('\rLuas sisi tegak\t : ')) 
					hasil = (2*((2/3)*a*a))+(b*c)
					io = ' ( 2 x ( ⅔ x %s x %s ) ) + ( %s x %s ) = %s' %(a, a, c, b, hasil) 
					oi = nel(io, style='yellow')
					loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
				else :
					c = float(input('\rLuas sisi tegak\t : ')) 
					hasil = (2*((2/3)*a*a))+(b*c)
					io = ' ( 2 x ( ⅔ x %s x %s ) ) + ( %s x %s ) = %s' %(a, a, c, b, hasil) 
					oi = nel(io, style='yellow')
					loading1 ()
					cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			else :
				bangun_ruang () 
		elif  rjb in ['5' ]:
			print (' ') 
			io = ' 1. Ls = 2 x π x r x t \n 2. Lp = 2 x π r² + ( 2 x π x r x t )' 
			oi = nel(io, style='cyan')
			pi = ' Lp : Luas Permukaan \n Ls Luas Selimut \n r : Jari jari \n t : Tinggi \n π : 22/7 / 3,14'
			po = nel(pi, style='white')
			cetak(nel(oi, title='[Rumus Tabung]', style='green' ))
			cetak(nel(po,title='[Keterangan]' , style='green' )) 
			rjb = input(x+'['+p+'Luas Permukaan Tabung'+x+'] Pilih : ') 
			if rjb in ['1']:
				print (' ') 
				diketahui () 
				a = float(input('Jari-jari\t : ')) 
				b = float(input('Tinggi\t : ')) 
				hasil = 2*(22/7)*a*b
				io = ' 2 x 22/7 x %s x %s = %s' %(a, b, hasil) 
				oi = nel(io, style='yellow')
				loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('Jari-jari\t : ')) 
				b = float(input('Tinggi\t : ')) 
				hasil = (2*(22/7)*(a**2)) + (2*(22/7)*a*b) 
				io = ' 2 x 22/7 x %s² + ( 2 x 22/7 x%s x %s ) = %s' %(a, a, b, hasil) 
				oi = nel(io, style='yellow')
				loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			else :
				bangun_ruang () 
		elif  rjb in ['6' ]:
			print (' ') 
			io = ' 1. Ls = π x r x s\n 2. Lp = π x r x s + ( π x r²)' 
			oi = nel(io, style='cyan')
			pi = ' Lp : Luas Permukaan \n Ls Luas Selimut \n r : Jari jari \n t : Tinggi \n π : 22/7 / 3,14 \n s : Daris pelukis' 
			po = nel(pi, style='white')
			cetak(nel(oi, title='[Rumus Kerucut]', style='green' ))
			cetak(nel(po,title='[Keterangan]' , style='green' )) 
			rjb = input(x+'['+p+'Luas Permukaan Kerucut'+x+'] Pilih : ') 
			if rjb in ['1']:
				print (' ') 
				diketahui () 
				a = float(input('Jari-jari\t\t : ')) 
				b = float(input('Tinggi\t\t\t : '))
				c = float(input('Garis Pelukis (s)\t : '))
				hasil = (22/7)*a*c
				io = ' 22/7 x %s x %s = %s' %(a, c, hasil) 
				oi = nel(io, style='yellow')
				loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green',)) ; mulai () 
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('Jari-jari\t\t : ')) 
				b = float(input('Tinggi\t\t\t : '))
				c = float(input('Garis Pelukis (s)\t : '))
				hasil = ((22/7)*a*c) +((22/7)*(a**2))
				io = ' ( 22/7 x %s x %s ) + ( 22/7 x %s² ) = %s' %(a, c, hasil) 
				oi = nel(io, style='yellow')
				loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green',)) ; mulai () 
			else:
				bangun_ruang () 
		elif  rjb in ['7' ]:
			print (' ') 
			io = ' Lp = 4( π x r²)' 
			oi = nel(io, style='cyan')
			pi = ' Lp : Luas Permukaan \n r : Jari jari \n π : 22/7 / 3,14' 
			po = nel(pi, style='white')
			cetak(nel(oi, title='[Rumus Bola]', style='green' ))
			cetak(nel(po,title='[Keterangan]' , style='green' ))  
			a = float(input('Jari-jari\t\t : ')) 
			hasil = 4*(22/7)*(a**2)
			io = ' 4 x ( 22/7 x %s² ) = %s' %(a, hasil) 
			oi = nel(io, style='yellow')
			loading1 ()
			cetak(nel(oi, title='[Jawaban]', style='green',)) ; mulai ()
		else:
			bangun_ruang () 
	elif rjb in ['2'] :
		print (' ') 
		io = ' 1. Kubus \n 2. Balok \n 3. Limas Segi (3-6)\n 4. Prisma Segi (3,5,6,8) \n 5. Silinder (Tabung) \n 6. Kerucut \n 7. Bola' 
		oi = nel(io, style='yellow')
		cetak(nel(oi, title='[Rumus Volume]', style='green' ))
		rjb = input(x+'['+p+'Rumus Volume'+x+'] Pilih : ') 
		if rjb in ['1']:
			print (' ') 
			io = ' V =   R³' 
			oi = nel(io, style='cyan')
			pi = ' L : Luas Permukaan \n R : Rusuk'
			po = nel(pi, style='white') 
			cetak(nel(oi, title='[Rumus]', style='green' ))
			cetak(nel(po,title='[Keterangan]' , style='green' )) 
			print (' ') 
			diketahui () 
			a = float(input('Rusuk\t : ')) 
			hasil = a**3
			io = ' %s³ = %s' %(a, hasil) 
			oi = nel(io, style='yellow') ; loading1 ()
			cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
		elif rjb in ['2']:
			print (' ') 
			io = ' 1. V = p x l x t \n 2. p = v ÷ ( l x t ) \n 3. l = V ÷ ( p x t) \n 4. t = V ÷ ( p x l )' 
			oi = nel(io, style='cyan')
			pi = ' V : Volume \n p : Panjang \n l : Lebar \n t : Tinggi' 
			po = nel(pi, style='white')
			cetak(nel(oi, title='[Rumus]', style='green' ))
			cetak(nel(po,title='[Keterangan]' , style='green' )) 
			rjb = input(x+'['+p+'Rumus Volume'+x+'] Pilih : ') 
			if rjb in ['1']:
				print (' ') 
				diketahui () 
				a = float(input('Panjang\t : ')) 
				b = float(input('Lebar\t : ')) 
				c = float(input('Tinggi\t : ')) 
				hasil = a*b*c
				io = ' %s x %s x %s = %s' %(a, b, c, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('Voulme\t : ')) 
				b = float(input('Panjang\t : ')) 
				c = float(input('Tinggi\t : ')) 
				hasil = a*b*c
				io = ' %s ÷ ( %s x %s ) = %s' %(a, b, c, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['3']:
				print (' ') 
				diketahui () 
				a = float(input('Voulme\t : ')) 
				b = float(input('Panjang\t : ')) 
				c = float(input('Lebar\t : ')) 
				hasil = a*b*c
				io = ' %s ÷ ( %s x %s ) = %s' %(a, b, c, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('Voulme\t : ')) 
				b = float(input('Panjamg\t : ')) 
				c = float(input('Lebar\t : ')) 
				hasil = a*b*c
				io = ' %s ÷ ( %s x %s ) = %s' %(a, b, c, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			else:
				bangun_ruang () 
		elif  rjb in ['3' ]:
			print (' ') 
			io = ' 1. Segitiga = ⅓ ( ½ x a x t ) x t\n 2. Segiempat =  ⅓ x ( s x s ) x t\n 3. Segilima = ⅓ x ( 1,72 x s x s ) x t\n 4. Segienam =  ⅓ x ( 2,598 x s x s ) x t' 
			oi = nel(io, style='cyan')
			pi = ' V = Volume \n a : Alas \n s : sisi \n t : Tinggi' 
			po = nel(pi, style='white')
			cetak(nel(oi, title='[Rumus Limas]', style='green' ))
			cetak(nel(po,title='[Keterangan]' , style='green' ))  
			rjb = input(x+'['+p+'Volum Limas'+x+'] Pilih : ') 
			if rjb in ['1']:
				print (' ') 
				diketahui () 
				a = float(input('\rAlas\t\t : ')) 
				b = float(input('\rTinggi\t\t : ')) 
				hasil = ((1/3)*(1/2)*a*a)*b
				io = ' ⅓ x ( ½ x %s x %s ) x %s = %s' %(a, a,c, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('sisi\t\t : ')) 
				b = float(input('\rTinggi\t\t : ')) 
				hasil = (a*a)*b
				io = '( %s x %s ) x %s  = %s' %(a, a, b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
			elif rjb in ['3']:
				print (' ') 
				diketahui () 
				a = float(input('sisi\t\t : ')) 
				b = float(input('\rTinggi\t\t : ')) 
				hasil = (1/3)*(1.72*a*a)*b
				io = ' ⅓ x ( 1,72 %s x %s ) x %s  = %s' %(a, a, b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
			elif rjb in ['4' ]:
				print (' ') 
				diketahui () 
				a = float(input('sisi\t\t : ')) 
				b = float(input('\rTinggi\t\t : ')) 
				hasil = (1/3)*(2.598*a*a)*b
				io = ' ⅓ x ( %s x %s ) x %s = %s' %(a, a, b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
			else:
				bangun_ruang () 
		elif  rjb in ['4']:
			print (' ') 
			io = ' 1. Segitiga = ( ½ x a x t ) x t \n 2. Segilima = ( 1,72 x s x s ) x t \n 3. Segienam = ( 2,598 x s x s ) x t \n 4. Segidelapan = ( ⅔ x s x s ) x t' 
			oi = nel(io, style='cyan')
			pi = ' V : Volume \n a : Alas \n s : sisi \n t : Tinggi'
			po = nel(pi, style='white')
			cetak(nel(oi, title='[Rumus Prisma]', style='green' ))
			cetak(nel(po,title='[Keterangan]' , style='green' ))  
			rjb = input(x+'['+p+'Volume Prisma'+x+'] Pilih : ') 
			if rjb in ['1']:
				print (' ') 
				diketahui () 
				a = float(input('\rAlas\t\t : ')) 
				b = float(input('\rTinggi\t\t : ')) 
				hasil = ((1/2)*a)*b
				io = '( ½ x %s x %s ) x %s = %s' %(a, c, b, hasil) 
				oi = nel(io, style='yellow') ; loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
			elif rjb in ['2']:
				print (' ') 
				diketahui () 
				a = float(input('\rSisi (s) \t\t : ')) 
				b = float(input('\rTinggi\t\t : ')) 
				hasil = (1.72*a*a)*b
				io = ' ( 1,72 x %s x %s ) x %s = %s' %(a, a, b, hasil) 
				oi = nel(io, style='yellow')
				loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
			elif rjb in ['3']:
				print (' ') 
				diketahui () 
				a = float(input('\rSisi (s) \t\t : ')) 
				b = float(input('\rTinggi\t\t : ')) 
				hasil = (2.598*a*a)*b
				io = ' ( 2,598 x %s x %s ) x %s = %s' %(a, a, b, hasil) 
				oi = nel(io, style='yellow')
				loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
			elif rjb in ['4']:
				print (' ') 
				diketahui () 
				a = float(input('\rSisi (s) \t\t : ')) 
				b = float(input('\rTinggi\t\t : ')) 
				hasil = ((2/3)*a*a)*b
				io = ' ( 2 x ( ⅔ x %s x %s ) ) + ( %s x %s ) = %s' %(a, a,b, hasil) 
				oi = nel(io, style='yellow') ;loading1 ()
				cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
			else :
				bangun_ruang () 
		elif  rjb in ['5' ]:
			print (' ') 
			io = ' V = π x r² x t ' 
			oi = nel(io, style='cyan')
			pi = ' V : Volume \n r : Jari jari \n t : Tinggi \n π : 22/7 / 3,14'
			po = nel(pi, style='white')
			cetak(nel(oi, title='[Rumus Tabung]', style='green' ))
			cetak(nel(po,title='[Keterangan]' , style='green' )) 
			print (' ') 
			diketahui () 
			a = float(input('Jari-jari\t\t : ')) 
			b = float(input('Tinggi\t\t\t : '))
			hasil = (22/7)*(a**2)*b
			io = '  22/7 x %s² x %s = %s' %(a, b, hasil) 
			oi = nel(io, style='yellow')
			loading1 ()
			cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
		elif  rjb in ['6' ]:
			print (' ') 
			io = ' V =  ⅓ π x r² x t' 
			oi = nel(io, style='cyan')
			pi = ' V : Volume \n r : Jari jari \n t : Tinggi \n π : 22/7 / 3,14' 
			po = nel(pi, style='white')
			cetak(nel(oi, title='[Rumus Kerucut]', style='green' ))
			cetak(nel(po,title='[Keterangan]' , style='green' ))
			print (' ') 
			diketahui () 
			a = float(input('Jari-jari\t\t : ')) 
			b = float(input('Tinggi\t\t\t : '))
			hasil = (1/3)*(22/7)*a*b
			io = ' ⅓ x 22/7 x %s² x %s = %s' %(a, b, hasil) 
			oi = nel(io, style='yellow')
			loading1 ()
			cetak(nel(oi, title='[Jawaban]', style='green',)) ; mulai ()  
		elif  rjb in ['7' ]:
			print (' ') 
			io = ' Lp = 4( π x r²)' 
			oi = nel(io, style='cyan')
			pi = ' Lp : Luas Permukaan \n r : Jari jari \n π : 22/7 / 3,14' 
			po = nel(pi, style='white')
			cetak(nel(oi, title='[Rumus Bola]', style='green' ))
			cetak(nel(po,title='[Keterangan]' , style='green' ))  
			a = float(input('Jari-jari\t\t : ')) 
			hasil = (4/3)*(22/7)*(a**2)
			io = ' ⁴/³ x ( 22/7 x %s² ) = %s' %(a, hasil) 
			oi = nel(io, style='yellow')
			loading1 ()
			cetak(nel(oi, title='[Jawaban]', style='green',)) ; mulai ()
		else:
			bangun_ruang () 
def aritmatika () :
	print (' ') 
	oi = 'Rumus MTK yang satu ini digunakan dalam materi Matematika sekolah SMP. ' 
	io = mark(oi, style='white') 
	cetak(nel(io, title='[Baris Deret Aritmatika]', style='green' ))
	io = ' 1. Uₙ = a + ( n - 1) b \n 2. Sₙ = ½ n ( 2a x ( n - 1 ) x b)\n 3. Sₙ = ½n x (a + Uₙ )' 
	oi = nel(io, style='cyan')
	cetak(nel(oi, title='[Rumus]', style='green' ))
	pi = ' a : suku pertama \n b : beda atau selisih antar suku \n n : banyaknya suku\n Uₙ :suku ke-n \n Sn : jumlah suku pertama sampai suku ke-n' 
	po = nel(pi, style='white')
	cetak(nel(po,title='[Keterangan]' , style='green' ))
	rjb = input(x+'['+p+'Volume Prisma'+x+'] Pilih : ') 
	if rjb in ['1']:
		print (' ') 
		diketahui () 
		a = float(input('Suku pertama (a)\t : ')) 
		b = float(input('Selisih anatar suku (b)\t : ')) 
		c = float(input('Banyakknya suku (n)\t : ')) 
		hasil = a+(c-1)*b
		io = ' %s + ( %s - 1 ) x %s = %s' %(a, c, b, hasil) 
		oi = nel(io, style='yellow') ; loading1 ()
		cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
	elif rjb in ['2']:
		print (' ') 
		diketahui () 
		a = float(input('Suku pertama (a)\t : ')) 
		b = float(input('Selisih anatar suku (b)\t : ')) 
		c = float(input('Banyakknya suku (n)\t : ')) 
		hasil = (1/2)*c*(2*a(c-1)*b)
		io = ' ½ x %s( 2 x %s x ( %s - 1 ) x %s ) = %s' %(c, a, c, b, hasil) 
		oi = nel(io, style='yellow') ; loading1 ()
		cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
	elif rjb in ['3']:
		print (' ') 
		diketahui () 
		a = float(input('Suku pertama (a)\t : ')) 
		b = float(input('Selisih anatar suku (b)\t : ')) 
		c = float(input('Banyakknya suku (n)\t : ')) 
		hasil = a+(c-1)*b
		io = ' %s + ( %s - 1 ) x %s = %s' %(a, c, b, hasil) 
		oi = nel(io, style='yellow') ; loading1 ()
		cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
	else:
		aritmatika () 
def geometri () :
	print (' ') 
	oi = 'Rumus MTK yang satu ini digunakan dalam materi Matematika sekolah SMP. ' 
	io = mark(oi, style='white') 
	cetak(nel(io, title='[Baris Deret Geometri]', style='green' ))
	io = ' 1. Uₙ = arⁿ⁻¹ \n 2. Sₙ = a( 1 - rⁿ ) ÷ ( 1 - r ), 𝒋𝒊𝒌𝒂 r > 1\n 3. Sₙ = a x ( rⁿ -  1 ) ÷ ( r - 1 ), 𝒋𝒊𝒌𝒂 r <1' 
	oi = nel(io, style='cyan')
	cetak(nel(oi, title='[Rumus]', style='green' ))
	pi = ' a : suku pertama \n b : beda atau selisih antar suku \n n : banyaknya suku\n Uₙ :suku ke-n \n Sn : jumlah suku pertama sampai suku ke-n' 
	po = nel(pi, style='white')
	cetak(nel(po,title='[Keterangan]' , style='green' ))
	rjb = input(x+'['+p+'Volume Prisma'+x+'] Pilih : ') 
	if rjb in ['1']:
		print (' ') 
		diketahui () 
		a = float(input('Suku pertama (a)\t : ')) 
		b = float(input('Rasio anatar suku (r)\t : ')) 
		c = float(input('Banyakknya suku (n)\t : ')) 
		hasil = a*(b**c) 
		io = ' %s' %( hasil) 
		oi = nel(io, style='yellow') ; loading1 ()
		cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
	elif rjb in ['2']:
		print (' ') 
		diketahui () 
		a = float(input('Suku pertama (a)\t : ')) 
		b = float(input('Rasio antar suku (r)\t : ')) 
		c = float(input('Banyakknya suku (n)\t : ')) 
		hasil = (a*(1-(b**c)))/(1-b)
		io = ' %s' %(hasil) 
		oi = nel(io, style='yellow') ; loading1 ()
		cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
	elif rjb in ['3']:
		print (' ') 
		diketahui () 
		a = float(input('Suku pertama (a)\t : ')) 
		b = float(input('Rasio antar suku (r)\t : ')) 
		c = float(input('Banyakknya suku (n)\t : ')) 
		hasil = (a*((b**c) -1))/(b-1)
		io = ' %s' %( hasil) 
		oi = nel(io, style='yellow') ; loading1 ()
		cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
	else:
		geometri ()  
 
def peluang () :
	print (' ') 
	oi = 'Rumus MTK yang satu ini digunakan dalam materi Matematika sekolah SMP. ' 
	io = mark(oi, style='white') 
	cetak(nel(io, title='[Peluang]', style='green' ))
	io = ' 1. Peluang suatu kejadian \n 2. Peluang gabungan dua kejadian\n 3. Peluang kejadian saling lepas \n 4. Peluang kejadjan saling bebas \n 5. Peluang kejadian bersyarat' 
	oi = nel(io, style='yellow')
	cetak(nel(oi, title='[Macam-macam Peluang]', style='green' ))
	rjb = input(x+'['+p+'Peluang'+x+'] Pilih : ') 
	if rjb in ['1']:
		print (' ') 
		io = ' P(A) = n(A) ÷ n(S)' 
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='[Rumus]', style='green' ))
		pi = ' P(A) : peluang dari kejadian A\n n(A) : banyak anggota A \n n(S) = banyak anggota ruang sampel' 
		po = nel(pi, style='white')
		cetak(nel(po,title='[Keterangan]' , style='green' ))
		diketahui () 
		a = float(input('Banyak anggota A\t : ')) 
		b = float(input('Banyak anggota ruang sample\t : ')) 
		hasil = a/b
		io = ' %s ÷ %s = %s' %( a, b, hasil) 
		oi = nel(io, style='yellow') ; loading1 ()
		cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
	elif rjb in ['2']:
		print (' ') 
		io = ' P(A∪B)=P(A)+P(B)-P(A∩B)' 
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='[Rumus]', style='green' ))
		pi = 'Jika diketahui A dan B merupakan dua kejadian yang berbeda, sehingga peluang kejadian A∪B dapat dihitung menggunakan rumus di atas' 
		po = nel(pi, style='white')
		cetak(nel(po,title='[Keterangan]' , style='green' ))
		diketahui () 
		a = float(input('Peluang A\t : ')) 
		b = float(input('Peluang B\t : ')) 
		c = float(input('Peluang A∩B\t : ')) 
		hasil = a+b-c
		io = ' %s + %s-  %s = %s' %( a, b, c, hasil) 
		oi = nel(io, style='yellow') ; loading1 ()
		cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
	elif rjb in ['3']:
		print (' ') 
		io = ' P(A∪B)=P(A) x P(B)' 
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='[Rumus]', style='green' ))
		pi = 'Dua kejadian dikatakan saling lepas jika kedua kejadian tersebut tidak mungkin terjadi bersama-sama sehingga PA∩B=0, yang dirumuskan di atas' 
		po = nel(pi, style='white')
		cetak(nel(po,title='[Keterangan]' , style='green' ))
		diketahui () 
		a = float(input('Peluang A\t : ')) 
		b = float(input('Peluang B\t : ')) 
		hasil = a*b
		io = ' %s x %s = %s' %( a, b, hasil) 
		oi = nel(io, style='yellow') ; loading1 ()
		cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()
	elif rjb in ['4']:
		print (' ') 
		io = ' P(A∩B)=P(A) x P(B)' 
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='[Rumus]', style='green' ))
		pi = 'Dua kejadian dikatakan saling bebas jika terjadinya kejadian A tidak mempengaruhi terjadinya kejadian B  begitu juga sebaliknya, yang dirumuskan sebagai di atas' 
		po = nel(pi, style='white')
		cetak(nel(po,title='[Keterangan]' , style='green' ))
		diketahui () 
		a = float(input('Peluang A\t : ')) 
		b = float(input('Peluang B\t : ')) 
		hasil = a*b
		io = ' %s x %s = %s' %( a, b, hasil) 
		oi = nel(io, style='yellow') ; loading1 ()
		cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai () 
	elif rjb in ['5']:
		print (' ') 
		io = ' P(A|B = P(A∩B) ÷ P(B), dimana, P(B) ≠0'
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='[Rumus]', style='green' ))
		pi = 'Peluang terjadinya kejadian A dengan syarat kejadian B telah terjadi dapat dihitung menggunakan rumus di atas' 
		po = nel(pi, style='white')
		cetak(nel(po,title='[Keterangan]' , style='green' ))
		diketahui () 
		a = float(input('Peluang (A∩B)\t : ')) 
		b = float(input('Peluang B\t : ')) 
		hasil = a/b
		io = ' %s ÷ %s = %s' %( a, b, hasil) 
		oi = nel(io, style='yellow') ; loading1 ()
		cetak(nel(oi, title='[Jawaban]', style='green' )) ; mulai ()  
	
def fisika () :
	_rjBasalamah_print_ (_rjBasalamah_blank_) 
	io =' 1. Rumus Massa Jenis\n 2. Rumus Gaya \n 3. Rumus Frekuensi\n 4. Rumus Periode\n 5. Cepat Rambat Gelombang\n 6. Rumus Energi Potensial \n 7. Rumus Energi Kinetik\n 8. Rumus Energi Mekanik\n 9. Rumus Rangkaian Listrik \n 10. Konvers sekala suhu ' 
	oi = nel(io, style='yellow')
	cetak(nel(oi, title='[FISIKA]', style='green' )) 
	rjb = input(x+'['+p+'Fisika'+x+'] Pilih : ') 
	if rjb in _rjBasalamah_1_ :
		_rjBasalamah_print_ (_rjBasalamah_blank_) 
		rouf = 'Lambang Fisika dari massa jenis adalah “ρ” (dibaca: rho). Menurut sistem Satuan Internasional (SI), satuan massa jenis adalah kg/m3 atau kg.m³\n 1. ρ = m÷v \n 2. m = ρ x v \n 3. v =  m ÷ ρ' 
		rouf_jevianz = nel(rouf, style='cyan')
		cetak(nel(rouf_jevianz, title='[Rumus]', style='green' ))
		rj = ' ρ = massa jenis (kg/m³).\n m = massa (kg).\n v = volume (m³).' 
		rjs = nel(rj, style='white')
		cetak(nel(rjs,title='[Keterangan]' , style='green' ))
		rjb = _rjBasalamah_input_(x+'['+p+'Massa jenis'+x+'] Pilih : ') 
		if rjb in _rjBasalamah_1_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('Massa\t : ')) 
			b = float(_rjBasalamah_input_('Volume \t : ')) 
			hasil = a/b
			rouf = ' %s ÷ %s = %s' %( a, b, hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai () 
		elif rjb in _rjBasalamah_2_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('Massa jenis\t : ')) 
			b = float(_rjBasalamah_input_('Volume \t : ')) 
			hasil = a*b
			rouf = ' %s x %s = %s' %( a, b, hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai () 
		elif rjb in _rjBasalamah_3_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('Volume\t : ')) 
			b = float(_rjBasalamah_input_('Masssa jenis\t : ')) 
			hasil = a/b
			rouf = ' %s ÷ %s = %s' %( a, b, hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai () 
		else:
			fisika () 
	elif rjb in _rjBasalamah_2_ :
		_rjBasalamah_print_ (_rjBasalamah_blank_) 
		rouf = 'Satuan gaya menurut SI adalah Newton (N). Simbol rumus Fisika untuk gaya yaitu F. Lalu, bagaimana cara mencari f? Berikut rumus yang bisa Sobat RJB pakai:\n 1. F = m x a \n 2. m = F ÷ a \n 3. a = F ÷ m' 
		rouf_jevianz = nel(rouf, style='cyan')
		cetak(nel(rouf_jevianz, title='[Rumus]', style='green' ))
		rj = ' F : gaya (Newton atau kg.m/s²). \n m = massa benda (kg).\n a : percepatan (m/s²). ' 
		rjs = nel(rj, style='white')
		cetak(nel(rjs,title='[Keterangan]' , style='green' ))
		rjb = _rjBasalamah_input_(x+'['+p+'Gaya'+x+'] Pilih : ') 
		if rjb in _rjBasalamah_1_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('Massa benda\t : ')) 
			b = float(_rjBasalamah_input_('Percepatan\t : ')) 
			hasil = a*b
			rouf = ' %s x %s = %s' %( a, b, hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai () 
		elif rjb in _rjBasalamah_2_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('Gaya\t\t : ')) 
			b = float(_rjBasalamah_input_('Massa benda\t : ')) 
			hasil = a/b
			rouf = ' %s ÷ %s = %s' %( a, b, hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai () 
		elif rjb in _rjBasalamah_3_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('Gaya\t\t : ')) 
			b = float(_rjBasalamah_input_('Percepatan\t : ')) 
			hasil = a/b
			rouf = ' %s ÷ %s = %s' %( a, b, hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai () 
		else:
			fisika () 
	elif rjb in _rjBasalamah_3_ : 
		_rjBasalamah_print_ (_rjBasalamah_blank_) 
		rouf = 'Rumus yang pertama digunakan untuk mencari frekuensi dari suatu getaran atau gelombang dengan mengetahui jumlah getaran dan waktunya terlebih dahulu. \n f = n ÷ t' 
		rouf_jevianz = nel(rouf, style='cyan')
		cetak(nel(rouf_jevianz, title='[Rumus 1 ]', style='green' ))
		rj = ' f : Frekuensi (Hz) \n n : Jumlah getaran\n t : Waktu yang dibutuhkan untuk melakukan getaran (s) ' 
		rjs = nel(rj, style='white')
		cetak(nel(rjs,title='[Keterangan]' , style='green' ))
		rouf = 'Rumus ini digunakan ketika kecepatan dan panjang gelombangnya diketahui.\n f = v ÷ 𝜆' 
		rouf_jevianz = nel(rouf, style='cyan')
		cetak(nel(rouf_jevianz, title='[Rumus 2 ]', style='green' ))
		rj = ' f : Frekuensi (Hz) \n v : kecepatan gelombang (m/s)\n 𝜆 : panjang gelombang (m)' 
		rjs = nel(rj, style='white')
		cetak(nel(rjs,title='[Keterangan]' , style='green' ))
		rouf = 'Frekuensi memang erat kaitannya dengan periode. Ketika nilai periode diketahui, elo bisa mencari frekuensi dengan menggunakan rumus ini\n f = 1 ÷ T' 
		rouf_jevianz = nel(rouf, style='cyan')
		cetak(nel(rouf_jevianz, title='[Rumus 3 ]', style='green' ))
		rj = ' f : Frekuensi (Hz) \n T : Periode (s) ' 
		rjs = nel(rj, style='white')
		cetak(nel(rjs,title='[Keterangan]' , style='green' ))
		rjb = _rjBasalamah_input_(x+'['+p+'Frekuensi'+x+'] Pilih : ') 
		if rjb in _rjBasalamah_1_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('n\t : ')) 
			b = float(_rjBasalamah_input_('t\t : ')) 
			hasil = a/b
			rouf = ' %s ÷ %s = %s' %( a, b, hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai () 
		elif rjb in _rjBasalamah_2_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('v\t : ')) 
			b = float(_rjBasalamah_input_('𝜆\t : ')) 
			hasil = a/b
			rouf = ' %s ÷ %s = %s' %( a, b, hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai () 
		elif rjb in _rjBasalamah_3_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('T\t : ')) 
			hasil = 1/a
			rouf = ' 1 ÷ %s = %s' %( a,hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai () 
		else:
			fisika () 
	elif rjb in _rjBasalamah_4_ :
		_rjBasalamah_print_ (_rjBasalamah_blank_) 
		rouf = 'Rumus ini bisa kamu gunakan untuk mencari periode dari jumlah getaran dan waktu.\n T = t ÷ n' 
		rouf_jevianz = nel(rouf, style='cyan')
		cetak(nel(rouf_jevianz, title='[Rumus 1 ]', style='green' ))
		rj = 'T : Periode (s)\n t : Waktu yang dibutuhkan untuk melakukan getaran (s)\n n : Jumlah getaran ' 
		rjs = nel(rj, style='white')
		cetak(nel(rjs,title='[Keterangan]' , style='green' ))
		rouf = 'Rumus yang kedua bisa digunakan ketika frekuensinya diketahui. Maka, kamu bisa menghitung periode getaran atau gelombang dengan mudah menggunakan rumus ini.\n T = 1 ÷ F' 
		rouf_jevianz = nel(rouf, style='cyan')
		cetak(nel(rouf_jevianz, title='[Rumus 2 ]', style='green' ))
		rj = ' T : Periode (s) /n F : Frekuensi (Hz) ' 
		rjs = nel(rj, style='white')
		cetak(nel(rjs,title='[Keterangan]' , style='green' ))
		rouf = 'Kamu bisa menggunakan rumus periode ini ketika kecepatan gelombang dan panjang gelombang diketahui.\n T = v x 𝜆' 
		rouf_jevianz = nel(rouf, style='cyan')
		cetak(nel(rouf_jevianz, title='[Rumus 3 ]', style='green' ))
		rj = ' T : Periode (s) \n v : kecepatan gelombang (m/s)\n 𝜆 : panjang gelombang (m) ' 
		rjs = nel(rj, style='white')
		cetak(nel(rjs,title='[Keterangan]' , style='green' ))
		rjb = _rjBasalamah_input_(x+'['+p+'Periode'+x+'] Pilih : ') 
		if rjb in _rjBasalamah_1_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('t\t : ')) 
			b = float(_rjBasalamah_input_('n\t : ')) 
			hasil = a/b
			rouf = ' %s ÷ %s = %s' %( a, b, hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai () 
		elif rjb in _rjBasalamah_2_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('F\t : ')) 
			hasil = 1/a
			rouf = ' 1 ÷ %s = %s' %( a,hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai () 
		elif rjb in _rjBasalamah_3_ :
			diketahui () 
			a = float(_rjBasalamah_input_('v\t : ')) 
			b = float(_rjBasalamah_input_('𝜆\t : ')) 
			hasil = a*b
			rouf = ' %s x %s = %s' %( a,b, hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai () 
		else:
			fisika () 
	elif rjb in _rjBasalamah_5_ :
		_rjBasalamah_print_ (_rjBasalamah_blank_) 
		rouf = 'Cepat rambat gelombang adalah jarak yang ditempuh oleh gelombang setiap detik. Satuannya adalah m/s dan dilambangkan dengan huruf “v”.\n\n Rumusnya adalah sebagai berikut:\n 1. v = s ÷ t\n 2. v = 𝜆 x f\n 3. v = 𝜆 ÷ T' 
		rouf_jevianz = nel(rouf, style='cyan')
		cetak(nel(rouf_jevianz, title='[Rumus]', style='green' ))
		rj = ' v : cepat rambat gelombang (m/s)\n s : jarak (m)\n t : waktu (s)\n 𝜆 : panjang gelombang (m)\n f : frekuensi (Hz)\n T : periode (s) ' 
		rjs = nel(rj, style='white')
		cetak(nel(rjs,title='[Keterangan]' , style='green' ))
		rjb = _rjBasalamah_input_(x+'['+p+'Cepat Rambat Gelombanh'+x+'] Pilih : ') 
		if rjb in _rjBasalamah_1_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('s\t : ')) 
			b = float(_rjBasalamah_input_('t\t : ')) 
			hasil = a/b
			rouf = ' %s ÷ %s = %s' %( a, b, hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai () 
		elif rjb in _rjBasalamah_2_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('𝜆\t : ')) 
			b = float(_rjBasalamah_input_('t\t : ')) 
			hasil = a*b
			rouf = ' %s x %s = %s' %( a,b, hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai () 
		elif rjb in _rjBasalamah_3_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('𝜆\t : ')) 
			b = float(_rjBasalamah_input_('t\t : ')) 
			hasil = a*b
			rouf = ' %s x %s = %s' %( a,b, hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai () 
		else:
			fisika () 
	elif rjb in _rjBasalamah_6_ :
		_rjBasalamah_print_ (_rjBasalamah_blank_) 
		rouf = ' 1. Ep = m x g x h \n 2. m = Ep ÷ ( g x h ) \n  3. g = Ep ÷ ( m x h ) 4. h = Ep ÷ ( m x g ) ' 
		rouf_jevianz = nel(rouf, style='cyan')
		cetak(nel(rouf_jevianz, title='[Rumus]', style='green' ))
		rj = ' Ep : energi potensial (Joule)\n m : massa benda (kg)\n g : gravitasi bumi (m/s2)\n h : ketinggian suatu benda (m)' 
		rjs = nel(rj, style='white')
		cetak(nel(rjs,title='[Keterangan]' , style='green' ))
		rjb = _rjBasalamah_input_(x+'['+p+'Energi potrnsial'+x+'] Pilih : ') 
		if rjb in _rjBasalamah_1_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('m\t : ')) 
			b = float(_rjBasalamah_input_('g\t : ')) 
			c = float(_rjBasalamah_input_('h\t : '))  
			hasil = a*b*c
			rouf = ' %s x %s x %s = %s' %( a, b, c, hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai ()
		elif rjb in _rjBasalamah_2_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('Ep\t : ')) 
			b = float(_rjBasalamah_input_('g\t : ')) 
			c = float(_rjBasalamah_input_('h\t : '))  
			hasil = a/(b*c)
			rouf = ' %s ÷ ( %s x %s ) = %s' %( a, b, c, hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai () 
		elif rjb in _rjBasalamah_3_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('Ep\t : ')) 
			b = float(_rjBasalamah_input_('m\t : ')) 
			c = float(_rjBasalamah_input_('h\t : '))  
			hasil = a/(b*c)
			rouf = ' %s ÷ ( %s x %s ) = %s' %( a, b, c, hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai () 
		elif rjb in _rjBasalamah_4_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('Ep\t : ')) 
			b = float(_rjBasalamah_input_('m\t : ')) 
			c = float(_rjBasalamah_input_('g\t : '))  
			hasil = a/(b*c)
			rouf = ' %s ÷ ( %s x %s ) = %s' %( a, b, c, hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai () 
		else:
			fisika () 
	elif rjb in _rjBasalamah_7_:
		_rjBasalamah_print_ (_rjBasalamah_blank_) 
		rouf = ' 1. Ek = ½ m x v² \n 2. m =  Ek ÷ ( ½ x v²\n  3. v = √ Ek ÷ ( ½ x m ) ' 
		rouf_jevianz = nel(rouf, style='cyan')
		cetak(nel(rouf_jevianz, title='[Rumus]', style='green' ))
		rj = ' Ep : energi potensial (Joule)\n m : massa benda (kg)\n g : gravitasi bumi (m/s2)\n h : ketinggian suatu benda (m)' 
		rjs = nel(rj, style='white')
		cetak(nel(rjs,title='[Keterangan]' , style='green' ))
		rjb = _rjBasalamah_input_(x+'['+p+'Energi kinetik'+x+'] Pilih : ') 
		if rjb in _rjBasalamah_1_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('m\t : ')) 
			b = float(_rjBasalamah_input_('v\t : ')) 
			hasil = (1/2)*a*(b**2)
			rouf = ' ½ x %s x %s² = %s' %( a, b, hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai ()
		elif rjb in _rjBasalamah_2_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('Ek\t : ')) 
			b = float(_rjBasalamah_input_('v\t : ')) 
			hasil = a/((1/2)*(b**2))
			rouf = ' %s ÷ ( %s x %s² ) = %s' %( a, b, c, hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai ()
		elif rjb in _rjBasalamah_3_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('Ek\t : ')) 
			b = float(_rjBasalamah_input_('m\t : ')) 
			akar = a/((1/2)*b)
			hasil = math.sqrt(akar)
			rouf = ' √ %s ÷ ( %s x %s ) = %s' %( a, b, c, hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai ()
		else :
			fisika() 
	elif rjb in _rjBasalamah_8_ :
		_rjBasalamah_print_ (_rjBasalamah_blank_) 
		rouf = ' Em = Ep + Ek ' 
		rouf_jevianz = nel(rouf, style='cyan')
		cetak(nel(rouf_jevianz, title='[Rumus]', style='green' ))
		rj = ' Em : Energi mekanik\n Ep : Energi potensial \n Ek = Energi kinetik' 
		rjs = nel(rj, style='white')
		cetak(nel(rjs,title='[Keterangan]' , style='green' ))
		diketahui () 
		a = float(_rjBasalamah_input_('Ep\t : ')) 
		b = float(_rjBasalamah_input_('Ek\t : ')) 
		hasil = a*b
		rouf = ' %s + %s = %s' %( a,b, hasil) 
		rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
		cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai () 
	elif rjb in _rjBasalamah_9_ :
		_rjBasalamah_print_ (_rjBasalamah_blank_) 
		rouf = ' 1. Hukum Ohm\n 2. Hukum Kirchoff \n 3. Hambatan Pengganti ' 
		rouf_jevianz = nel(rouf, style='yellow' )
		cetak(nel(rouf_jevianz, title='[Rumus]', style='green' ))
		rjb = _rjBasalamah_input_(x+'['+p+'Rangkaian Listrik'+x+'] Pilih : ') 
		if rjb in _rjBasalamah_1_ :
			rouf = 'Hukum Ohm berbunyi: “Besar arus listrik (I) yang mengalir melalui sebuah penghantar akan berbanding lurus dengan tegangan/beda potensial (V) yang diterapkan kepadanya dan berbanding terbalik dengan hambatannya R“. \n 1. V = I x R \n 2. I = V ÷ R \n 3. R = V ÷ I' 
			rouf_jevianz = nel(rouf, style='cyan')
			cetak(nel(rouf_jevianz, title='[Rumus]', style='green' ))
			rj = ' V : tegangan listrik (Volt) \n I : kuat arus (Ampere) \n R : hambatan (Ω atau Ohm)' 
			rjs = nel(rj, style='white')
			cetak(nel(rjs,title='[Keterangan]' , style='green' ))
			rjb = _rjBasalamah_input_(x+'['+p+'Energi kinetik'+x+'] Pilih : ') 
			if rjb in _rjBasalamah_1_ :
				_rjBasalamah_print_ (_rjBasalamah_blank_) 
				diketahui () 
				a = float(_rjBasalamah_input_('I\t : ')) 
				b = float(_rjBasalamah_input_('R\t : ')) 
				hasil = a*b
				rouf = '%s x %s² = %s' %( a, b, hasil) 
				rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
				cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai ()
			if rjb in _rjBasalamah_2_ :
				_rjBasalamah_print_ (_rjBasalamah_blank_) 
				diketahui () 
				a = float(_rjBasalamah_input_('V\t : ')) 
				b = float(_rjBasalamah_input_('R\t : ')) 
				hasil = a/b
				rouf = '%s ÷ %s² = %s' %( a, b, hasil) 
				rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
				cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai ()
			if rjb in _rjBasalamah_3_ :
				_rjBasalamah_print_ (_rjBasalamah_blank_) 
				rouf = 'Hukum Ohm berbunyi: “Besar arus listrik (I) yang mengalir melalui sebuah penghantar akan berbanding lurus dengan tegangan/beda potensial (V) yang diterapkan kepadanya dan berbanding terbalik dengan hambatannya R“. \n 1. V = I x R \n 2. I = V ÷ R \n 3. R = V ÷ I' 
				rouf_jevianz = nel(rouf, style='cyan')
				cetak(nel(rouf_jevianz, title='[Rumus]', style='green' ))
				rj = ' V : tegangan listrik (Volt) \n I : kuat arus (Ampere) \n R : hambatan (Ω atau Ohm)' 
				rjs = nel(rj, style='white')
				cetak(nel(rjs,title='[Keterangan]' , style='green' ))
				diketahui () 
				a = float(_rjBasalamah_input_('V\t : ')) 
				b = float(_rjBasalamah_input_('I\t : ')) 
				hasil = a/b
				rouf = '%s ÷ %s² = %s' %( a, b, hasil) 
				rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
				cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai ()
			else:
				fisika() 
		elif rjb in _rjBasalamah_2_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			rouf = 'Hukum Kirchoff berbunyi: “Jumlah kuat arus yang masuk ke suatu titik cabang sama dengan jumlah kuat arus yang keluar dari titik cabang tersebut”.\n 𝝨 I masuk = 𝝨 I keluar' 
			rouf_jevianz = nel(rouf, style='cyan')
			cetak(nel(rouf_jevianz, title='[Rumus]', style='green' ))
			rj = ' I : kuat arus (Ampere)' 
			rjs = nel(rj, style='white')
			cetak(nel(rjs,title='[Keterangan]' , style='green' ))
			diketahui () 
			a = float(_rjBasalamah_input_('I\t : ')) 
			hasil = a
			rouf = '%s = %s' %( a, hasil) 
			rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
			cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai ()
		elif rjb in _rjBasalamah_3_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			rouf = 'Hambatan pengganti adalah besarnya hambatan setara dengan total hambatan yang dihasilkan dari suatu rangkaian listrik.\n 1. Rangkaian Seri R = R1 + R2 + R3 + … \n 2. Rangkaian Pararel 1/R = 1/R1 + 1/R2 + 1/R3 + …' 
			rouf_jevianz = nel(rouf, style='cyan')
			cetak(nel(rouf_jevianz, title='[Rumus]', style='green' ))
			rj = ' R : hambatan (Ω atau Ohm)' 
			rjs = nel(rj, style='white')
			cetak(nel(rjs,title='[Keterangan]' , style='green' ))
			rjb = _rjBasalamah_input_(x+'['+p+'Pengganti hambatan'+x+'] Pilih : ') 
			if rjb in _rjBasalamah_1_ :
				_rjBasalamah_print_ (_rjBasalamah_blank_) 
				try :
					rjbs= int(_rjBasalamah_input_(x+'['+p+'Jumlah hambatan Seri (R) '+x+'] : ')) 
				except ValueError:
					pesan = '# INPUT YANG ANDA MASUKKAN BUKAN ANGKA'
					pesan2 = mark(pesan, style='red')
					sol().print(pesan2);jeda(1)
					fisika()
				if rjbs<1 or rjbs>100:
					pesan = '# OUT OF RANGE MEN'
					pesan2 = mark(pesan, style='red')
					sol().print(pesan2)
					fisika() 
				r_ham = []
				penjumlahan = [] 
				penjumlahani = [] 
				bsm = 0
				diketahui () 
				for met in range(rjbs):
					bsm+=1
					kl = float(_rjBasalamah_input_('R'+str(bsm)+' : ')) 
					r_ham.append(kl) 
				hasil_rangkaian_seri = sum(r_ham)
				rangkaian_seri = (len(r_ham)) 
				if rangkaian_seri in ['2'] :
					nama1 = r_ham.rsplit("," )[0]
					nama2 = r_ham,rsplit(",") [1]
					penjumlahani.append(nama1+' + '+nama2) 
				for tt in r_ham:
					rjmlh = format(tt)
					penjumlahan.append(format(tt))
				rouf = 'Jumlah hambatan seri adalah %s' %(hasil_rangkaian_seri) 
				rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
				cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai ()
			elif rjb in _rjBasalamah_2_ :
				menu_belum_tersedia () 
			else:
				fisika () 
	elif rjb in _rjBasalamah_10_ :
		_rjBasalamah_print_ (_rjBasalamah_blank_) 
		rouf = _author_abdur_rouf_rjBasalamah_p_Konvers_suhu_fisika
		rouf_jevianz = nel(rouf, style='yellow') ; 
		cetak(nel(rouf_jevianz, title='[Konvers Suhu]', style='green' ))
		rjb = _rjBasalamah_input_(x+'['+p+'Energi kinetik'+x+'] Pilih : ') 
		if rjb in _rjBasalamah_1_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('Suhu Celcius\t : ')) 
			reamur = (4/5)*a
			faren = (9/5)*a+32
			kelvin = a+273
			rouf = ' 1. Suhu reamur dari celcius adalah %s\n 2. Suhu fahrenheit dari celcius adalah %s\n 3. Suhu kelvin dari celcius adalah %s' %(reamur,faren, kelvin) 
			jawaban (rouf) 
		if rjb in _rjBasalamah_2_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('Suhu reamur\t : ')) 
			celsius = (5/4)*a
			faren = (9/4)*a+32
			kelvin = (5/4)*a+273
			rouf = ' 1. Suhu celcius dari reamur adalah %s\n 2. Suhu fahrenheit dari reamur adalah %s\n 3. Suhu kelvin dari reamur adalah %s' %(celcius,faren, kelvin) 
			jawaban (rouf) 
		if rjb in _rjBasalamah_3_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('Suhu fahrenheit\t : ')) 
			celsius = (5/9)*(a-32)
			reamur = (4/9)*(a-32)
			kelvin = ((5/9)*(a-32))+273
			rouf = ' 1. Suhu celcius dari farenheit adalah %s\n 2. Suhu reamur dari farenheit adalah %s\n 3. Suhu kelvin dari fahrenheit adalah %s' %(celcius,reamur, kelvin) 
			jawaban (rouf) 
		if rjb in _rjBasalamah_3_ :
			_rjBasalamah_print_ (_rjBasalamah_blank_) 
			diketahui () 
			a = float(_rjBasalamah_input_('Suhu kelvin\t : ')) 
			celsius = a-273
			reamur = (4/5)-273
			faren = ((9/5)*(a-273))+32 
			rouf = ' 1. Suhu celcius dari kelvin adalah %s\n 2. Suhu reamur dari kelvin adalah %s\n 3. Suhu  fahrenheit dari kelvin adalah %s' %(celcius,reamur,faren) 
			jawaban (rouf) 
			
	else:
		fisika ()  
		
		

def jawaban (rouf) :
	rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
	cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' )) ; mulai ()
def pertama (rouf) :
	rouf_jevianz = nel(rouf, style='yellow') ; loading1 ()
	cetak(nel(rouf_jevianz, title='[Jawaban]', style='green' ))
def login(name,password):
    sukses = False
    sandi = False
    file = open("logindatabase.txt","r")
    for i in file:
         a,b = i.split(",")
         b = b.strip()
         if(a==name and b==password):
             sukses = True
             break
    file.close()
    file = open("logindatabase.txt","r")
    for j in file:
         a,b = j.split(",")
         b = b.strip()
         if(a==name and b!=password):
         	print ('\r\n\t Keterangan Sandi salah') 
    file.close()
    if(sukses):
        io = 'Berhasil masuk, Anda akan di arahkan ke menu' 
        oi = mark(io, style='white') ; loading1 ()
        cetak(nel(oi, style='cyan'));jeda(2);menu()
    else:
        io = 'Anda belum terdaftar, Silahlan mendaftar dulu' 
        oi = mark(io, style='white') ; loading1 ()
        cetak(nel(oi, style='red'));jeda(2), os.system('python Rumus.py')  
    if(sandi) :
    	print ('sandi salah') 
def register(name,password):
    file = open("logindatabase.txt","a")
    file.write("\n"+name+","+password)
def access(option):
    global name
    if(option=="1"):
        wel = '# MASUKKAN EMAIL & SANDI' 
        wel2 = mark(wel, style='cyan')
        sol().print(wel2)
        name = input("Email\t: ")
        password = input("Sandi\t: ")
        login(name,password)
    elif(option=="2"):
        wel = '# MASUKKAN EMAIL & SANDI BARU UNTUK MENDAFTAR' 
        wel2 = mark(wel, style='cyan')
        sol().print(wel2)
        name = input("Email\t: ")
        password = input("Sandi\t: ")
        register(name,password)
        io = 'Berhasil mendaftar, Silahkan masuk sekarang' 
        oi = mark(io, style='white') ; loading1 ()
        cetak(nel(oi, style='green'));jeda(3), os.system('python Rumus.py')
    else :
    	os.system('python Rumus.py')
        
def begin():
    global option
    os.system ('clear') 
    wel = '# WELCOME TO RJB \n Copyright © 2022'
    wel1 = mark(wel, style='red')
    wel2 = nel(wel1, style='red') 
    sol().print(wel2, style='on cyan') 
    wel = '# HALAMAN LOGIN' 
    wel2 = mark(wel, style='cyan')
    sol().print(wel2)
    io =  ' 1. Masuk \n 2. Mendaftar\n' 
    oi = nel(io, style='cyan')
    cetak(nel(oi, title='[MENU]', style='green' ))
    io ='[white]Jika anda belum mendaftar. Silahkan pilih no[green] 2 [white]untuk mendaftar' 
    cetak(nel(io, style='cyan')) 
    #cetak(nel(oi, style='cyan')) 
    option = input("Pilih : ")
    if(option!="1" and option!="2"):
    	begin()
        

def mulai () :
	io = 'Enter untuk menjalankan script kembali' 
	oi = mark(io, style='white')
	cetak(nel(oi, style='green' ))
	rjb = input(u+'['+h+' ENTER '+u+']') 
	if rjb in _rjBasalamah_1_ :
		(menu) 
	else:
		menu () 
			
	
begin()
access(option) 
