'''
Auteur: Malik Fleury
Date: 29.10.2018
Maj: 08.11.2018
'''

from City import *
from Path import *
import math

class Graph:
    ''' Graph des villes '''
    def __init__(self):
        self.cities = City.load_from_file("./Data/Positions.txt")
        self.paths = Path.load_from_file("./Data/Connections.txt", self.cities)

    def a_star(self, city_src, city_dest, heuristic):
        ''' A* basé sur le pseudo-code du wiki anglais '''
        nodes_counter = 0

        openSet = {city_src}
        closedSet = set()

        fScore = self.create_dict_big_value();
        fScore[city_src] = heuristic(city_src, city_dest)

        gScore = self.create_dict_big_value();
        gScore[city_src] = 0

        came_from = {}

        while openSet:
            current = self.get_node_min_fScore(fScore, openSet)

            # Si on a trouvé la destination, c'est la fin
            if current == city_dest:
                break

            # Enlève de la frontière l'élément courant et le met dans l'historique
            openSet.remove(current)
            closedSet.add(current)

            # Pour chaque chemin pour la ville courante
            for path in current.paths_generator():
                neighbor = path.get_opposite_city(current)  # Obtention du voisin
                cost = path.get_cost();                     # Obtention du coût
                # Si le voisin est déjà dans l'historique, on ne le prend pas en compte
                if neighbor in closedSet:
                    continue
                # Calcule du coût avec heuristique
                tentative_gScore  = gScore[current] + cost
                # Le voisin se trouve pas dans la frontière, on a un nouveau noeud non visité
                # Dans le cas où le coût est plus mauvais que le coût déjà existant => pas de meilleur chemin, on passe
                if not neighbor in openSet:
                    openSet.add(neighbor)
                elif tentative_gScore >= gScore[neighbor]:
                    continue

                ## On ajoute les informations du meilleur chemin du moment
                came_from[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = gScore[neighbor] + heuristic(neighbor, city_dest)
            nodes_counter = nodes_counter + 1
        # Retourne le chemin (reconstruction avant) et le nombre de noeud parcourus
        return self.reconstruct_way(came_from, city_src, city_dest), nodes_counter

    def create_dict_big_value(self):
        ''' Initialise le dictionnaire avec des valeurs infinies '''
        fScore = {}
        for city in self.cities.values():
            fScore[city] = math.inf;
        return fScore

    def get_node_min_fScore(self, fScore, openSet):
        ''' Retourne la ville qui a le score minimum '''
        city_min_fScore = None
        keys = fScore.keys()
        for city in openSet:
            if city in keys:
                if city_min_fScore == None:
                    city_min_fScore = city
                elif fScore[city_min_fScore] > fScore[city]:
                    city_min_fScore = city
        return city_min_fScore

    def reconstruct_way(self, came_from, city_src, city_dest):
        ''' Permet de reconstruire le chemin depuis la destination jusqu'a la source '''
        current_city = city_dest
        way = []
        # Retrouve le chemin inverse à l'aide de "came_from"
        while current_city != city_src:
            way.append(current_city)
            current_city = came_from[current_city]
        way.append(city_src)
        # Retourne la liste afin d'avoir les éléments dans le bon ordre
        way.reverse()
        return way

    def get_city_from_name(self, name):
        return self.cities[name]
