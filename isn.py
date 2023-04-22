import pygame
from pygame.locals import *
from tkinter import*
from math import*
from time import*
from tkinter import messagebox
from tkinter.simpledialog import askstring
p1=0
p2=0
p3=0
xy_h=150,50
xy_min=150,50

x, y, ang, a, b, res, flag, e, x2, y2, ang2, f, x3, y3, ang3 = 150., 30., pi, 150., 30., pi, 0, 0, 150., 30., pi, 0, 150., 30., pi

RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)


def main2():
	"""fonction principale"""
	import sys

	messagebox.showinfo("debut","Bonjour ! Vous serez face a differentes horloges, votre but est de lire la bonne heure, pour cela vous aurez 3 niveaux de difficulte afin de vous guider.\n Vous commencez au niveau 1.")
	p=0
	global p1
	while p != 1 :
		niveau1(niveau1)
		if p1 >= 5 :
			messagebox.showinfo("next1","Bravo, nous vous conseillons de passer au niveau suivant !")
			choix = int(askstring('next1', "Tapez 1 pour refaire ce niveau, 2 pour passer au niveau suivant, ou tout autre nombre pour quitter."))
			if choix == 1 :
				messagebox.showinfo("next1","Vous avez choisi de refaire le niveau 1.")
				p=p
			elif choix != 1 :
				if choix == 2 :
					messagebox.showinfo("next1","Vous avez choisi de passer au niveau 2.")
					p = p+1
				elif choix != 2 :
					messagebox.showerror("leave1","vous avez choisi de quitter.")
					sys.exit()
		elif p1 <= 4 :
			messagebox.askretrycancel("remake1","Vous devriez vous entrainer a ce niveau avant de passer au niveau suivant.")
			choix = int(askstring("remake1", "Tapez 1 pour refaire ce niveau avec une aide, ou tout autre nombre pour quitter."))
			if choix == 1 :
				messagebox.showinfo("remake1","Vous avez choisi de refaire le niveau 1. (aide : l'aiguille des heures est la plus petite, aidez vous des chiffres autout du cadran !)")
				p = p
			elif choix != 1 :
				messagebox.showerror("leave1","vous avez choisi de quitter.")
				sys.exit()

	while p != 2 :
		global p2
		niveau2(niveau2)
		if p2 >= 10 :
			messagebox.showinfo("next2","Bravo, nous vous conseillons de passer au niveau suivant !")
			choix = int(askstring("next2", "Tapez 1 pour refaire ce niveau, 2 pour passer au niveau suivant, ou tout autre nombre pour quitter."))
			if choix == 1 :
				messagebox.showinfo("next2","Vous avez choisi de refaire le niveau 1.")
				p=p
			elif choix != 1 :
				if choix == 2 :
					messagebox.showinfo("next2","Vous avez choisi de passer au niveau 3.")
					p = p+1
				elif choix != 2 :
					messagebox.showerror("leave2","vous avez choisi de quitter.")
					sys.exit()
		elif p2 <= 7 :
			messagebox.askretrycancel("remake2","Vous devriez vous entrainer a ce niveau avant de passer au niveau suivant.")
			choix = int(askstring("remake2", "Tapez 1 pour refaire ce niveau avec une aide, ou tout autre nombre pour quitter."))
			if choix == 1 :
				messagebox.showinfo("remake2","Vous avez choisi de refaire le niveau 2. (aide : l'aiguille des heures est la plus petite et celle des minutes la plus grande, aidez vous des chiffres autour du cadran !)")
				p = p
			elif choix != 1 :
				messagebox.showerror("leave2","vous avez choisi de quitter.")
				sys.exit()

	while p != 3 :
		global p3
		niveau3(niveau3)
		if p3 == 12 :
			messagebox.showinfo("done","Felicitation, vous avez tout reussi du premier coup, vous savez a present parfaitement lire l'heure !")
			choix = int(askstring("remake3", "Tapez 1 si vous souhaitez refaire ce niveau, ou tout autre nombre pour quitter."))
			if choix == 1 :
				messagebox.showinfo("remake3","Vous avez choisi de refaire le niveau 3.")
				p=p
			elif choix != 1 :
				messagebox.showerror("leave3","vous avez choisi de quitter.")
				sys.exit()


		elif p3 != 12 :
			if p3 > 9 :
				messagebox.showinfo("remake3","Felicitation, vous avez reussi tous les niveau ! Reesayez afin de tout reussir du premier coup.")
				choix = int(askstring("remake3", "Tapez 1 pour refaire ce niveau, ou tout autre nombre pour quitter."))
				if choix == 1 :
					messagebox.showinfo("remake3","Vous avez choisi de refaire le niveau 1.")
					p=p
				elif choix != 1 :
						messagebox.showerror("leave3","vous avez choisi de quitter.")
						sys.exit()
			elif p3 <= 9 :
				messagebox.askretrycancel("remake3","Vous devriez vous entrainer a ce niveau avant de passer au niveau suivant.")
				choix = int(askstring("remake3", "Tapez 1 pour refaire ce niveau, ou tout autre nombre pour quitter."))
				if choix == 1 :
					messagebox.showinfo("remake3","Vous avez choisi de refaire le niveau 3.")
					p = p
				elif choix != 1 :
					messagebox.showerror("leave3","vous avez choisi de quitter.")
					sys.exit()



def niveau1(premier):
	"""premier niveau"""

	messagebox.showinfo("lvl1","Dans ce premier niveau vous deverez lire l'aiguille des heure.")
	a1=0
	global p1
	while a1 <= 2 :
		a1=a1+1

		import random
		liste_heure = [1,2,3,4,5,6,7,8,9,10,11,12]
		heure = random.choice(liste_heure)
		minute = 0
		pygame.display.flip()
		horloge(heure, minute)
		horloge(heure, minute)

		#reponse_heure = int(input("Qu'indique l'aiguille des heures ?"))
		reponse_heure = int(askstring("heure1","Qu'indique l'aiguille des heures ?"))
		e1=1

		if reponse_heure == heure:
			messagebox.showinfo("Bonne reponse 1","Bonne reponse ! Vous avez trouve du 1er essai.")
			p1 = p1+2

		elif reponse_heure != heure :

			while reponse_heure != heure and e1 <= 2 :
				messagebox.showerror("mauvaise reponse 1","Mauvaie reponse, reessaye !")
				reponse_heure = int(askstring("heure1", "Qu'indique l'aiguille des heures ?"))
				e1=e1+1
			if reponse_heure == heure:
				messagebox.showinfo("bonne reponse 1","Bonne reponse !")
				p1 = p1+1

			elif e1==3:
				messagebox.showerror("mauvaise reponse 1","Vous n'avez pas trouve la bonne reponse. L'aiguille indiquait {} heure.".format(heure))

def niveau2(second):
	"""second niveau"""

	messagebox.showinfo("lvl2","Dans ce niveau vous deverez lire ce qu'indique l'aiguille des heures comme au niveau 1, ainsi que ce qu'indique l'aiguille des minutes.")
	a2=0
	global p2
	while a2 <= 2 :
		a2=a2+1

		import random
		liste_heure = [1,2,3,4,5,6,7,8,9,10,11,12]
		liste_minute = [0,5,10,15,20,25,30,35,40,45,50,55]
		heure = random.choice(liste_heure)
		minute = random.choice(liste_minute)
		horloge(heure, minute)
		horloge(heure, minute)


		reponse_heure = int(askstring("heure2", "Qu'indique l'aiguille des heures ?"))
		eh2=1

		if reponse_heure == heure:
			messagebox.showinfo("bonne reponse 2","Bonne reponse ! Vous avez trouve du 1er essai.")
			p2=p2+2

		elif reponse_heure != heure :

			while reponse_heure != heure and eh2 <= 2 :
				messagebox.showerror("mauvaise reponse 2","Mauvaie reponse, reessaye !")
				reponse_heure = int(askstring("heure2", "Qu'indique l'aiguille des heures ?"))
				eh2=eh2+1
			if reponse_heure == heure:
				messagebox.showinfo("bonne reponse 2","Bonne reponse !")
				p2=p2+1

			elif eh2==3:
				messagebox.showerror("mauvaise reponse 2","Vous n'avez pas trouve la bonne reponse. L'aiguille indiquait {} heure.".format(heure))

		reponse_minute = int(askstring("minute2", "Qu'indique l'aiguille des minutes ?"))
		em2=1

		if reponse_minute == minute :
			messagebox.showinfo("bonne reponse 2","Bonne reponse ! Vous avez trouve du 1er essai.")
			p2=p2+2

		elif reponse_minute != minute :

			while reponse_minute != minute and em2 <= 2 :
				messagebox.showerror("mauvaise reponse 2","Mauvaie reponse, reessaye !")
				reponse_minute = int(askstring("minute2", "Qu'indique l'aiguille des minutes ?"))
				em2=em2+1
			if reponse_minute == minute :
				messagebox.showinfo("bonne reponse 2","Bonne reponse !")
				p2=p2+1

			elif em2==3:
				messagebox.showerror("mauvaise reponse 2","Vous n'avez pas trouve la bonne reponse. L'aiguille indiquait {} heure.".format(minute))

def niveau3(troisieme):
	"""troisieme niveau"""

	messagebox.showinfo("lvl3","Dans ce niveau vous deverez lire l'heure sans aide !")
	a3=0
	global p3
	while a3 <= 2 :
		a3=a3+1

		import random
		liste_heure = [1,2,3,4,5,6,7,8,9,10,11,12]
		liste_minute = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]
		heure = random.choice(liste_heure)
		minute = random.choice(liste_minute)
		horloge(heure, minute)
		horloge(heure, minute)


		reponse_heure = int(askstring("heure3", "Qu'indique l'aiguille des heures ?"))
		eh3=1

		if reponse_heure == heure:
			messagebox.showinfo("bonne reponse 3","Bonne reponse ! Vous avez trouve du 1er essai.")
			p3=p3+2

		elif reponse_heure != heure :

			while reponse_heure != heure and eh3 <= 2 :
				messagebox.showerror("mauvaise reponse 3","Mauvaie reponse, reessaye !")
				reponse_heure = int(askstring("heure3", "Qu'indique l'aiguille des heures ?"))
				eh3=eh3+1
			if reponse_heure == heure:
				messagebox.showinfo("bonne reponse 3","Bonne reponse !")
				p3=p3+1

			elif eh3==3:
				messagebox.showerror("mauvaise reponse 3","Vous n'avez pas trouve la bonne reponse. L'aiguille indiquait {} heure.".format(heure))

		reponse_minute = int(askstring("minute3", "Qu'indique l'aiguille des minutes ?"))
		em3=1

		if reponse_minute == minute :
			messagebox.showinfo("bonne reponse3","Bonne reponse ! Vous avez trouve du 1er essai.")
			p3=p3+2

		elif reponse_minute != minute :

			while reponse_minute != minute and em3 <= 2 :
				messagebox.showerror("mauvaise reponse 3","Mauvaie reponse, reessaye !")
				reponse_minute = int(askstring("minute3", "Qu'indique l'aiguille des minutes ?"))
				em3=em3+1
			if reponse_minute == minute :
				messagebox.showinfo("bonne reponse 3","Bonne reponse !")
				p3=p3+1

			elif em2==3:
				messagebox.showerror("mauvais reponse 3","Vous n'avez pas trouve la bonne reponse. L'aiguille indiquait {} heure.".format(minute))



def horloge(heures, mins):
	#Création du cadran et des aiguilles
	fenetre2 = pygame.display.set_mode((1200, 800))
	fenetre2.blit(fond, (0,0))
	pygame.display.flip()
	for a in range(0, 360):
		pygame.draw.line( fond ,WHITE , [600, 400],[600+(220*cos(radians(a))), 400+(220*sin(radians(a)))] ,7)
	for a in range(0, 360, 6):
		pygame.draw.line( fond ,GREY , [600+(210*cos(radians(a))), 400+(210*sin(radians(a)))],[600+(220*cos(radians(a))), 400+(220*sin(radians(a)))] ,3)
	for a in range(0, 360, 30):
		pygame.draw.line( fond ,BLACK , [600+(205*cos(radians(a))), 400+(205*sin(radians(a)))],[600+(220*cos(radians(a))), 400+(220*sin(radians(a)))] ,4)
	pygame.draw.circle( fond, BLACK, [600, 400], 225, 5)
	pygame.draw.line( fond , BLUE, [600, 400],[600+(180*cos(radians(mins)*6-pi/2)), 400+(180*sin(radians(mins)*6-pi/2))],5)
	pygame.draw.line(fond, RED, [600, 400], [600+(100*cos(radians(heures)*30-pi/2)), 400+(100*sin(radians(heures)*30-pi/2))],5)
	pygame.draw.circle( fond, BLACK, [600, 400], 7, 5)
	pygame.display.flip()


pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((1200, 800))

#Chargement et collage du fond
ecran = pygame.image.load("ecran.png").convert()
fond = pygame.image.load("fond.png").convert()
fenetre.blit(ecran, (0,0))

#Chargement et collage du personnage
rectangle = pygame.image.load("rectangle.jpg").convert()
fenetre.blit(rectangle, (200,300))

titre = pygame.image.load("titre.png").convert_alpha()
fenetre.blit(titre, (200,100))
#Rafraîchissement de l'écran
pygame.display.flip()

#Lecture d'une musique
pygame.mixer.music.load("Digital_Memories.wav")
pygame.mixer.music.play(loops=-1, start=0.0)

heure = 12
minute = 0

#BOUCLE INFINIE
continuer = 1

while continuer:
	#Fermer la fenêtre
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0	
		#Ouverture d'une nouvelle fenêtre pour lancer le jeu		
		mx, my = pygame.mouse.get_pos()
		if 200 < mx < 1000 and 300 < my < 500:
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1 :
					fenetre2 = pygame.display.set_mode((1200, 800))
					fenetre2.blit(fond, (0,0))
					pygame.display.flip()
					if event.type == QUIT:
						continuer = 0
					#Fonction principale
					horloge(heure, minute)
					main2()
					fenetre2.mainloop()
					


