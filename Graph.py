from City import *
from Path import *

class Graph:
    def __init__(self):
        self.cities = City.load_from_file("./Data/Positions.txt")
        self.paths = Path.load_from_file("./Data/Connections.txt", self.cities)

    def compareHeuristic(h1, h2):
        if h1 < h2:
            return 1
        elif h1 == h2:
            return 0
        else:
            return -1

    def min(self, fScore):
        return min(fScore, key=fScore.get)

    def min_available(self, openList, fScore):
        h = fScore[openList[0]]
        k = openList[0]
        for value in openList:
            if h < fScore[value]:
                k = value
        return k

    def reconstruct_path(self, cameFrom, current):
        total_path = {current}
        while current in cameFrom.keys():
            current = cameFrom[current]
            total_path.add(current)
        return total_path

    def a_star_fr(self,  city_src, city_dest, heuristic):
        None

    def a_star_en(self, city_src, city_dest, heuristic):
        closedList = []
        openList = [city_src]

        cameFrom = dict()
        gScore = dict()
        fScore = dict()

        gScore[city_src] = 0
        fScore[city_src] = heuristic(city_src, city_dest)

        while openList:
            current = self.min_available(openList, fScore)
            if current == city_dest:
                return self.reconstruct_path(cameFrom, current)

            openList.remove(current)
            closedList.append(current)

            for neighbor in current.get_neighbors():
                if neighbor in closedList:
                    continue

                tentative_gScore = gScore[current] + self.paths[current.get_name() + "-" + neighbor.get_name()].get_cost()

                if neighbor not in openList:
                    openList.append(neighbor)
                elif tentative_gScore >= gScore[neighbor]:
                    continue

                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = gScore[neighbor] + heuristic(neighbor, city_dest)

    def get_city_from_name(self, name):
        return self.cities[name]

    def debug_show(self):
        for key, city in self.cities.items():
            print(city.get_name())
            for path in city.paths_generator():
                print("- ", path.get_opposite_city(city))
