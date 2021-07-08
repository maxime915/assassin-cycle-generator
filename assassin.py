"assassin.py : generate a cycle for the assassin game"

import itertools
import random

ANIMALS = ["antilope", "chat", "furet", "lapin", "poulpe"]
COLORS = ["bleu", "jaune", "mauve", "rouge", "vert"]
FRUITS = ["abricot", "banane", "cerise", "fraise", "pomme"]

ACTIONS = ["la victime doit faire les lacets de l'assassin",
           "la victime doit perdre deux fois de suite à pierre-papier-ciseaux contre l'assassin",
           "la victime doit écrire un message sur le dos de l'assassin",
           "la victime doit danser avec l'assassin",
           "l'assassin doit faire parler la victime avec la voix de Batman",
           "l'assassin doit mettre un objet dans la poche de la victime sans qu'elle ne le sache",
           "l'assassin doit faire répéter la même phrase 3 fois de suite (au mot près)",
           "la victime doit finir une des phrases de l'assassin",
           "l'assassin doit faire jouer une scène culte à la victime",
           "la victime doit dire bonjour à 10 personnes différentes sur 1h",
           "l'assassin doit faire chanter baby shark à la victime",
           "l'assassin doit tricher à un jeu contre la vitime sans qu'elle ne le voie",
           "l'assassin doit se faire gifler par la victime",
           "l'assassin doit faire faire une roue à la victime",
           "l'assassin doit faire faire un poirier à la victime",
           "l'assassin doit faire boire un verre d'eau salée à la victime",
           "l'assassin doit lancer une course avec la victime",
           "l'assassin doit faire assoir la victime sur son lit",
           "l'assassin doit faire enlever ses chaussure à la victime (min 1h avant d'aller dormir)",
           "l'assassin doit échanger de chaussure avec la victime (au moins 2 mins)",
           "l'assassin doit faire faire 10 pompes à la victime",
           "l'assassin doit faire signer un papier à la victime",
           "l'assassin doit faire parler sa victime de foot",
           "l'assassin doit faire faire 10 petits bonhommes sans rire à la victime",
           "la victime doit offrir une fleur à l'assassin",
           "l'assassin et la victime doivent échanger de vêtement pendant au moins 5 mins",
           "la victime doit faire le sandwich de l'assassin",
           "la victime doit faire le lit de l'assassin",
           "l'assassin doit convaincre la victime de manger de l'herbe (sans paris, sans forcer, etc)",
           "l'assassin doit faire énoncer le théorème de Pythagore à sa victime",
           ]


def generate(limit : int = -1):
    """return a list of type (assassin, victime, action) where assassin and victim
        are both tuple from (ANIMALS, COLORS, FRUITS). The length of the list is
        limit if given and limit > 0, 125 otherwise."""

    # random list of all combination
    identifiers = list(itertools.product(ANIMALS, COLORS, FRUITS))
    random.shuffle(identifiers)

    # cap
    if limit > 0:
        identifiers = identifiers[:limit]

    # make cycle (assassin, victim, action)
    cycle = [(identifiers[i-1], identifiers[i], random.choice(ACTIONS))
             for i in range(1, len(identifiers))]
    cycle.append((identifiers[-1], identifiers[0], random.choice(ACTIONS)))

    return cycle


def main(length : int = 3):
    "print a textual representation of a cycle of given length (default 3)"
    for assassin, victime, action in generate(limit=length):
        print(f'{assassin = }')
        print(f'{victime  = }')
        print(f'{action   = }\n')


if __name__ == "__main__":
    import sys
    main(3 if len(sys.argv) < 2 else int(sys.argv[1]))
