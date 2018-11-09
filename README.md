# IA_TP2

Auteur: Malik Fleury
Date: 29.10.2018
Maj: 09.11.2018

## Description

Dans le cadre du cours d'intelligence d'artificelle, il nous est demandé d'implémenter l'algorithme A* afin de trouver le chemin le plus court entre 2 villes.
Pour cela, nous devons utiliser les 5 heuristiques suivantes:

- h0(n) = 0
- h1(n) = "la distance entre n et B sur l'axe des x"
- h2(n) = "la distance entre n et B sur l'axe des y"
- h3(n) = "la distance à vol d'oiseau entre n et B"
- h4(n) = "la distance de Manhattan entre n et B"

## How to ...

Pour lancer le script, il suffit d'utiliser python 3.6 avec le script Main.py passé en paramètre:

```
python Main.py
```

Le programme peut fonctionner en deux modes:

1. Mode normal (Par défaut): l'utilisateur doit entrer deux villes; la ville source (de départ) et la ville de destination (d'arrivée). L'affichage comporte les 5 heuristiques et l'ordre de visite de chaque ville.
2. Mode bruteforce: le programme affiche tous les chemins possibles avec les 5 heuristiques. Pour choisir ce mode, il faut modifier la variable "bruteforce_mode" à "True" qui se trouve en haut du fichier "Main.py".

## Questions

### L'utilisation des différentes heuristiques a-t-elle une influence sur l'efficacité de la recherche (en terme de nombre de noeuds visités) ?

Oui. Le nombre de noeuds visités se retrouve réduit si on choisit une heurisitique de bonne qualité. Une bonne heuristique est la fonction qui va se rapprocher le plus possible du résultat réel (g(n)).

### Pouvez-vous trouver des exemples où l'utilisation de différentes heuristiques donnes des résultats différents en termes de chemin trouvé ?

Oui, voici deux exemples où différentes heuristiques donnent des résultats différents :

![img1](./img1.jpg)

![img2](./img2.jpg)

On voit que cela concerne principalement l'heuristique 4 (distance de Manhattan). Cela est dûe au fait que cette heuristique n'est pas admissible. En effet, les résultats obtenus peuvent être supérieures à g(n) ce qui peut engendrer de mauvaises estimations.

### Dans un cas réel, quelle heuristique utiliseriez-vous ?

L'heuristique à vol d'oiseau me semble la meilleure pour une estimation plus correcte. En effet, cette heuristique est admissible et les valeurs obtenues avec celle-ci seront toujours comprise en dessous ou égale à h(n).

Les autres heuristiques me semblent peu ou pas cohérentes pour les éléments suivants:

- 0: cette heuristique peut fonctionner (admissible), mais elle n'est pas top car elle ne permet pas de définir un meilleur chemin dans le cas où nos g(n) sont égaux pour deux ou plusieurs chemins d'une ville
- Différence en X: cette heuristique est admissible, cependant elle ne permet pas de représenté réellement la réalité en prenant en compte uniquement la différence en X
- Différence en Y: cette heuristique est également rejetée pour la même raison que la différence en X
- Manhattan: cette heuristique n'est tout simplement pas admissible, car le résultat peut être supérieure à g(n)

## Liens utiles

[A* Algorithme - Wikipedia EN](https://en.wikipedia.org/wiki/A*_search_algorithm)
