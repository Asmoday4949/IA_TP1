# IA_TP2

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

Oui. Le nombre de noeuds visités se retrouve réduit si on choisit une heurisitique de bonne qualité. Une bonne heuristique est la fonction qui va se rapprocher le plus possible du résultat réel.

### Pouvez-vous trouver des exemples où l'utilisation de différentes heuristiques donnes des résultats différents en termes de chemin trouvé ?

Oui, voici deux exemples où différentes heuristiques donnent des résultats différents :

![img1](./img1.jpg)

![img2](./img2.jpg)

On voit que cela concerne principalement l'heuristique 4 (distance de Manhattan). ...

### Dans un cas réel, quelle heuristique utiliseriez-vous ?

...
