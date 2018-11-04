from City import *
from Path import *

class Graph:
    def __init__(self):
        self.cities = City.load_from_file("./Data/Positions.txt")
        self.paths = Path.load_from_file("./Data/Connections.txt", self.cities)

    def a_star_own_impl(self, city_src, city_dest, heuristic):
        cities_to_visit = [city_src]
        cities_visited = set()

        heuristic_values = dict()
        tot_heuristic_values = dict()

        while cities_to_visit:
            current_city = cities_to_visit.pop(1)

            if current_city == city_dest:
                return None
            else:
                for path in current_city.paths_generator():
                    opposite_city = path.get_opposite_city(city)
                    heuristic_values[opposite_city] = heuristic(current_city, opposite_city)
                    if opposite_city not in cities_to_visit and opposite_city not in cities_visited:
                        cities_to_visit.append(opposite_city)


    # def a_star_teacher_impl(self, city_src, city_dest, heuristic):
    #     frontier = [city_src]
    #     history = set()
    #
    #     while frontier:
    #         city = frontier.pop(0)
    #         if city == city_dest:
    #             print("end")
    #             return frontier
    #         else:
    #             print("loop")
    #             neighbors = city.get_neighbors()
    #             for neighbor in neighbors:
    #                 h_value = heuristic(city, neighbor)
    #                 neighbor.set_h_value(h_value)
    #                 if (neighbor not in frontier) and (neighbor not in history):
    #                     frontier.append(neighbor)
    #                 elif neighbor in frontier:
    #                     if h_value < neighbor.get_h_value():
    #                         neightbor.set_h_value(h_value)
    #         history.add(city)
    #     raise Exception("Solution not found")

    def get_city_from_name(self, name):
        return self.cities[name]

    def debug_show(self):
        for key, city in self.cities.items():
            print(city.get_name())
            for path in city.paths_generator():
                print("- ", path.get_opposite_city(city))
