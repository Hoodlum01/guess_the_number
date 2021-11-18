from tkinter import *
import random
from PIL import ImageTk, Image

def joc():

	global root
	root=Tk()
	
	root.iconbitmap('ico.ico')

	global nr_pc
	global sanse
	global input_jucator
	global confirmare_input_juc
	sanse=7
	input_jucator=Entry(root)
	confirmare_input_juc=Button(root)

	def butoane_final():
		Buton_restart=Button(root, text="Restart joc", command=restart)
		Buton_restart.pack()
		Buton_exit=Button(root, text="Iesire", command=root.destroy)
		Buton_exit.pack()

	def stop():
		input_jucator.config(state='disabled')
		confirmare_input_juc.config(state="disabled")

	def multiplu(nr_pc):
		multiplu=nr_pc*random.randint(1, 4)
		return multiplu

	def divizor(nr_pc):
		if nr_pc==1:
			divizor=1
		else:
			for i in range(2, nr_pc+1):
				if nr_pc%i==0:
					divizor=i
					return divizor

		return divizor

	def mic(nr_pc):
		mic=random.randint(nr_pc, 100)
		return mic

	def mare(nr_pc):
		mare=random.randint(1, nr_pc)
		return mare

	def afis():
		global sanse
		global nr_pc

		vf=StringVar()
		vf=input_jucator.get()
		if sanse==0:
			t1=Label(root, text="Din pacate ai ramas fara sanse, numarul era "+str(nr_pc), fg="red")
			t1.pack()
			stop()
			butoane_final()

		win_text="Ai castigat! Felicitari, chiar te pricepi!"

		if sanse == 6:
			if nr_pc!=vf:
				t2=Label(root, text="Gresit! Hint 2: Numarul este mai mare decat: "+str(mare(nr_pc))+ " (sanse ramase: "+str(sanse)+")")
				t2.pack()
				sanse=sanse-1			
			else:
				t2=Label(root, text=win_text, fg="green")
				t2.pack()
				stop()
				butoane_final()

		elif sanse == 5:
			if nr_pc!=vf:
				t3=Label(root, text="Gresit! Hint 3: Un divizor al numarului este: "+str(divizor(nr_pc))+ " (sanse ramase: "+str(sanse)+")")
				t3.pack()
				sanse=sanse-1			
			else:
				t3=Label(root, text=win_text, fg="green")
				t3.pack()
				stop()
				butoane_final()

		elif sanse == 4:
			if nr_pc!=vf:
				t4=Label(root, text="Gresit! Hint 4: Un multiplu al numarului este : "+str(multiplu(nr_pc))+ " (sanse ramase: "+str(sanse)+")")
				t4.pack()
				sanse=sanse-1
			else:
				t4=Label(root, text=win_text, fg="green")
				t4.pack()
				stop()
				butoane_final()

		elif sanse>0:
			if nr_pc!=vf:
				t5=Label(root, text="Gresit! (sanse ramase: "+str(sanse)+")")
				t5.pack()
				sanse=sanse-1
			else:
				t5=Label(root, text=win_text, fg="green")
				t5.pack()
				stop()
				butoane_final()


	def GotIt():
		global confirmare_input_juc
		Tabel1.destroy()
		ButtonGI.destroy()
		global sanse
		global nr_pc
		nr_pc=random.randint(1,100)
		Tabel2=Label(root, text="Care crezi ca e numarul?")
		Tabel2.pack()
		Tabel3=Label(root, text="Hint 1: Numarul e mai mic decat "+str(mic(nr_pc))+ " (sanse ramase: " + str(sanse)+ ")")
		sanse=sanse-1
		input_jucator.pack()
		confirmare_input_juc=Button(root, text="Verifica", command= afis)
		confirmare_input_juc.pack()
		Tabel3.pack()

	window=root
	window.title("Ghiceste numarul! - created by Hoodlum")
	window.geometry("600x300")

	Tabel1=Label(root, text="Hai noroc! Astazi o sa jucam un joc interesat! Uite cum sta treaba:\nEu o sa aleg un numar random intre 1 si 100 iar tu va trebui sa il ghicesti!\nAi 7 incercari, printre care si 4 indicii! Ramai fara incercari si pierzi jocul. Hai sa vedem ce poti:)")
	Tabel1.pack()

	ButtonGI=Button(root, text="Am inteles!", command=GotIt)
	ButtonGI.pack()

	root.mainloop()

def restart():
	root.destroy()
	joc()

joc()