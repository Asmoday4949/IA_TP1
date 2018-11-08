'''
Auteur: Malik Fleury
Date: 29.10.2018
Maj: 08.11.2018
'''
from Path import *
from City import *
from Graph import *
import sys
import math

#
#   Configs
bruteforce_mode = False
#
#

def heuristic_0(city_src, city_dest):
    ''' 0 '''
    return 0

def heuristic_1(city_src, city_dest):
    ''' Différence en X '''
    return abs(city_src.get_x() - city_dest.get_x())

def heuristic_2(city_src, city_dest):
    ''' Différence en Y '''
    return abs(city_src.get_y() - city_dest.get_y())

def heuristic_3(city_src, city_dest):
    ''' Vol d'oiseau '''
    return math.sqrt(abs(city_src.get_x() - city_dest.get_x())**2 + abs(city_src.get_y() - city_dest.get_y())**2)

def heuristic_4(city_src, city_dest):
    ''' Manhattan '''
    return abs(city_src.get_x() - city_dest.get_x()) + abs(city_src.get_y() - city_dest.get_y())

def ask_user_input():
    city_name_src = input("Source: ")
    city_name_dest = input("Destination: ")
    return city_name_src, city_name_dest

def show_way(title, way, nodes_counter):
    print(title + "\t", end='')
    print(' | Nodes counter: ' + str(nodes_counter) + "\t | \t", end='')
    for city in way:
        print(city, end='')
        if city != way[len(way)-1]:
            print(' --> ', end='')
    print()

def show_brute_force_a_star(graph):
    for city_name_src in graph.cities:
        print("-----------------------------------------------------------")
        for city_name_dest in graph.cities:
            show_result_all_heuristics(graph, city_name_src, city_name_dest)

def show_result_all_heuristics(graph, city_name_src, city_name_dest):
    city_src = graph.get_city_from_name(city_name_src)
    city_dest = graph.get_city_from_name(city_name_dest)

    way_h0, counter_0 = graph.a_star(city_src, city_dest, heuristic_0)
    way_h1, counter_1 = graph.a_star(city_src, city_dest, heuristic_1)
    way_h2, counter_2 = graph.a_star(city_src, city_dest, heuristic_2)
    way_h3, counter_3 = graph.a_star(city_src, city_dest, heuristic_3)
    way_h4, counter_4 = graph.a_star(city_src, city_dest, heuristic_4)
    show_way("Heuristic 0: ", way_h0, counter_0)
    show_way("Heuristic 1: ", way_h1, counter_1)
    show_way("Heuristic 2: ", way_h2, counter_2)
    show_way("Heuristic 3: ", way_h3, counter_3)
    show_way("Heuristic 4: ", way_h4, counter_4)

if __name__ == "__main__":
    graph = Graph()

    if bruteforce_mode:
        show_brute_force_a_star(graph)
    else:
        city_name_src, city_name_dest = ask_user_input()
        show_result_all_heuristics(graph, city_name_src, city_name_dest)
