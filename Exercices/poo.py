class Tabouret:

	# je suis dans mon plan
	# plan = class
	# un plan peut contenir des variables et des méthodes.
	# celles-ci seront spécifiques à notre classe / plan
	# et ne pourront pas être utilisées en dehors.

	# en orienté objet, on appelle les variables et fonctions différemment : 
	# variable => attribut
	# fonction => méthode
	# Fondamentalement, cela reste la même chose, la même manière de déclaration,
	# la différenciation des termes permet juste de savoir si l'on se situe
	# dans un contexte procédural ou objet.

	# déclaration du constructeur. Le constructeur est une méthode spéciale
	# qui s'exécute automatiquement à chaque création d'objet.
	# En orienté objet, Python présente la particularité de devoir, pour
	# chaque méthode (fonction), passer en premier paramètre "self"
	# le constructeur n'est pas obligatoire, il reste optionnel.
	def __init__(self, hauteur, nb_pieds, diametre, couleur):
		# le "self" permet à python d'identifier les attributs qui lui sont propre
		# donc qui sont DANS la classe, et qui ne proviennent pas de l'extérieur
		self.hauteur = hauteur
		self.nb_pieds = nb_pieds
		self.diametre = diametre
		self.couleur = couleur
		# je défini un nouvel attribut. Je lui affecte comme valeur
		# le résultat du calcul de la méthode "calcule_hauteur_pied()"
		# Effectuant ce calcul dans le constructeur (__init__()), alors
		# celui-ci sera effectué dès la création de l'objet
		self.hauteur_pied = self.calcule_hauteur_pied()

	def calcule_hauteur_pied(self):
		return self.hauteur * self.nb_pieds

	def calcule_poid_pied(self):
		return self.hauteur_pied * 30

if __name__ == "__main__":
	# création d'un objet "tabouret", et stockage de cet objet 
	# dans la variable "t"
	t = Tabouret(80, 4, 40, "bleu")
	# affichage des attributs de l'objet tabouret "t"
	print(t.hauteur)
	print(t.nb_pieds)
	print(t.diametre)
	print(t.couleur)
	# j'affiche l'attribut "hauteur_pied"
	print(t.hauteur_pied)
	# j'affiche le résultat du calcul de la méthode calcule_hauteur_pied()
	print(t.calcule_hauteur_pied())

	tabourets = [
		{
			"hauteur": 80,
			"nb_pieds": 4,
			"diametre": 40,
			"couleur": "bleu"
		}, {
			"hauteur": 90,
			"nb_pieds": 5,
			"diametre": 35,
			"couleur": "rouge"
		}, {
			"hauteur": 85,
			"nb_pieds": 6,
			"diametre": 45,
			"couleur": "vert"
		}
	]

	tabourets_objects = []

	for tab in tabourets:
		tabourets_objects.append( Tabouret(tab["hauteur"], tab["nb_pieds"], tab["diametre"], tab["couleur"]) )

	print(tabourets_objects)
