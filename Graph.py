'''
Auteur: Malik Fleury
Date: 29.10.2018
Maj: 08.11.2018
'''

from City import *
from Path import *
from queue import *

class PriorityItem:
    ''' Classe spécifique à la queue de priorité afin de tester QUE la priorité et pas les données concernant la ville '''
    def __init__(self, priority, item):
        self.priority = priority
        self.item = item

    def get_item(self):
        return self.item

    def __eq__(self, other):
        return self.priority == other.priority

    def __lt__(self, other):
        return self.priority < other.priority

class Graph:
    ''' Graph des villes '''
    def __init__(self):
        self.cities = City.load_from_file("./Data/Positions.txt")
        self.paths = Path.load_from_file("./Data/Connections.txt", self.cities)

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

    def a_star(self,  city_src, city_dest, heuristic):
        ''' Algorithme A* '''
        # Queue prioritaire: la priorité est coût total pour le chemin actuel + heuristique
        frontier = PriorityQueue()
        frontier.put(PriorityItem(0, city_src));

        # Dictionnaire comportant les ville visitées auparavant
        came_from = {}
        came_from[city_src] = None

        # Dictionnaires gardant les coût totaux pour chaque chemin
        # Le coût augmente au fur et à mesure qu'on avance dans la recherche
        total_cost = {}
        total_cost[city_src] = 0

        while frontier:
            # Obtention d'un chemin qui est le meilleur pour le moment
            current = frontier.get().get_item()
            if current == city_dest:
                break;
            for path in current.paths_generator():
                # Obtention d'un voisin et calcule du nouveau coût
                neighbor = path.get_opposite_city(current)
                new_cost = total_cost[current] + path.get_cost()
                # Si le voisin n'existe pas dans le dictionnaire OU que le nouveau coût est plus bas
                # On ajoute le nouveau coût, on définit la priorité et on ajoute ce nouveau chemin
                if neighbor not in total_cost or new_cost < total_cost[neighbor]:
                    total_cost[neighbor] = new_cost
                    priority = new_cost + heuristic(current, city_dest)
                    frontier.put(PriorityItem(priority, neighbor))
                    came_from[neighbor] = current
        # Fin de la recherche, on reconstruit le chemin
        return self.reconstruct_way(came_from, city_src, city_dest)

    def get_city_from_name(self, name):
        return self.cities[name]
