tabouret = [
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

# print(tabouret)

# je veux calculer la longueur totale de tuyau qu'il faut pour pouvoir faire les 
# pieds par rapport à la hauteur
for tab in tabouret:
	hauteur = tab["hauteur"] * tab["nb_pieds"]
	print(tab, hauteur)