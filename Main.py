from Path import *
from City import *
from Graph import *
import math

def heuristic_0(city_src, city_dest):
    return 0

def heuristic_1(city_src, city_dest):
    '''  '''
    return abs(city_src.get_x() - city_dest.get_x())

def heuristic_2(city_src, city_dest):
    return math.abs(city_src.get_y() - city_dest.get_y())

def heuristic_3(city_src, city_dest):
    return math.sqrt(math.abs(city_src.get_x() - city_dest.get_x())**2 + math.abs(city_src.get_y() - city_dest.get_y())**2)

def heuristic_4(city_src, city_dest):
    return math.abs(city_src.get_x() - city_dest.get_x()) + math.abs(city_src.get_y() - city_dest.get_y())

if __name__ == "__main__":
    graph = Graph()
    graph.debug_show()

    # city_src = graph.get_city_from_name('Bern')
    # city_dest = graph.get_city_from_name('Rome')
    # result = graph.a_star(city_src, city_dest, heuristic_1)
    #
    # for city in result:
    #     print(city.get_name())
