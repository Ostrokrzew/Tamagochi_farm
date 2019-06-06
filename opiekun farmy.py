# Opiekun zwierzaka
# Wirtualny pupil, którym należy się opiekować

import random

class Critter(object):
	"""Wirtualny pupil"""
	count = 0

	def __init__(self, name, hunger = 0, boredom = 0):
		self.name = name
		self.hunger = random.randint(0,15)
		self.boredom = random.randint(0,15)
		Critter.count += 1

	def __str__(self):
		info = ('\nname = ' + str(self.name) + '\nhunger = ' + str(self.hunger) +\
		'\nboredom = ' + str(self.boredom) + '\nmood = ' + str(self.mood))
		return info

	def __pass_time(self):
		self.hunger += 1
		self.boredom += 1

	@property
	def mood(self):
		unhappiness = self.hunger + self.boredom
		if unhappiness < 5:
			m = "szczęśliwy"
		elif 5 <= unhappiness <= 10:
			m = "zadowolony"
		elif 11 <= unhappiness <= 15:
			m = "podenerwowany"
		else:
			m = "wściekły"
		return m

	def talk(self):
		print("Nazywam się", self.name, "i jestem", self.mood, "teraz.")
		self.__pass_time()

	def eat(self, food = 4):
		print("Mniam, mniam. Dziękuję.")
		self.hunger -= food
		if self.hunger < 0:
			self.hunger = 0
		if food == 2:
			self.__pass_time()
			self.hunger -= 0.5
			self.boredom -= 0.5
		if food == 4:
			self.__pass_time()
		if food == 6:
			self.__pass_time()
			self.hunger += 0.5
			self.boredom += 0.5

	def play(self, fun = 4):
		print("Hura!")
		self.boredom -= fun
		if self.boredom < 0:
			self.boredom = 0
		if fun == 2:
			self.__pass_time()
			self.hunger -= 0.5
			self.boredom -= 0.5
		if fun == 4:
			self.__pass_time()
		if fun == 6:
			self.__pass_time()
			self.hunger += 0.5
			self.boredom += 0.5

def eatFunc():
	choice = None  
	while choice != "0":
		print("""
		Czas karmienia:
	
		0 - cofnij
		1 - mała porcja karmy
		2 - zwykła porcja karmy
		3 - duża porcja karmy
		""")
	
		choice = input("Wybierasz: ")
		if choice == "0":
			print("Nie nakarmiłeś zwierząt.")

		elif choice == "1":
			return 2
		
		elif choice == "2":
			return 4

		elif choice == "3":
			return 6

		else:
			print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")

def playFunc():
	choice = None  
	while choice != "0":
		print("""
		Czas zabawy:
	
		0 - cofnij
		1 - krótki czas zabawy
		2 - średni czas zabawy
		3 - długi czas zabawy
		""")
	
		choice = input("Wybierasz: ")
		if choice == "0":
			print("Nie pobawiłeś się ze zwierzętami.")

		elif choice == "1":
			return 2
		
		elif choice == "2":
			return 4

		elif choice == "3":
			return 6

		else:
			print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")

def main():
	crit = list()
	response = None
	while response not in ('N','n'):
		response = input('Chcesz stworzyć zwierzaka? t/n: ').lower()
		if response == 't':
			crit_name = input('Jak chcesz nazwać swojego zwierzaka?: ').title()
			crit.append(Critter(crit_name))
			print()
		elif response == 'n':
			break
		else:
			print("\nNiestety,", response, "nie jest prawidłowym wyborem.\n")


	choice = None  
	while choice != "0":
		print \
		("""
		Opiekun zwierzaka
	
		0 - zakończ
		1 - słuchaj swoich zwierząt
		2 - nakarm swoje zwierzęta
		3 - pobaw się ze swoimi zwierzętami
		""")
	
		choice = input("Wybierasz: ")
		print()

		# wyjdź z pętli 
		if choice == "0":
			print("Do widzenia.")

		# słuchaj swojego zwierzaka
		elif choice == "1":
			for i in range(len(crit)):
				crit[i].talk()
		
		# nakarm swojego zwierzaka
		elif choice == "2":
			meal = eatFunc()
			for i in range(len(crit)):
				crit[i].eat(meal)

		# pobaw się ze swoim zwierzakiem
		elif choice == "3":
			fun = playFunc()
			for i in range(len(crit)):
				crit[i].play(fun)

		elif choice == 'info':
			print(f'Posiadasz zwierzęta w ilości {Critter.count} sztuk na swojej farmie.')
			for i in range(len(crit)):
				print(crit[i])

		# nieznany wybór 
		else:
			print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")

main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")