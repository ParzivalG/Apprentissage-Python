import player
import cases

#créer une carte avec absis et ordonnée


class Map:
	def __init__(self, abscisse, ordonnee):
		self.abscisse = abscisse
		self.ordonnee = ordonnee


	#définir la limite de la carte 
	#en fonction de la position du personnage
	def limitemap(self, abspos, ordopos):

		if abspos > self.abscisse:
			print ("Vous ne pouvez pas allez par là!")
			return (abspos=10)

		elif ordopos > self.ordonnee:
			print ("Vous ne pouvez pas allez par là!")
			return (ordopos=10) 

		elif abspos < 1:
			print ("Vous ne pouvez pas allez par là!")
			return (abspos=1)

		elif ordopos < 1:
			print ("Vous ne pouvez pas allez par là!")
			return (ordopos=1) 
