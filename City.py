'''
Auteur: Malik Fleury
Date: 29.10.2018
Maj: 08.11.2018
'''

class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.paths = []

    def __str__(self):
        ''' Retourne le nom de la ville '''
        return self.name

    def add_path(self, newPath):
        ''' Ajoute un chemin à la ville '''
        self.paths.append(newPath)

    def add_paths(self, newPaths):
        ''' Ajoute plusieurs chemins à la ville '''
        for path in paths:
            self.addPath(path)

    def get_name(self):
        ''' Permet d'obtenir le nom de la ville '''
        return self.name

    def get_x(self):
        ''' Permet d'obtenir la position en X '''
        return self.x

    def get_y(self):
        ''' Permet d'obtenir la position en Y '''
        return self.y

    def paths_generator(self):
        ''' Generateur permettant d'itérer sur les chemins connectés à la ville '''
        for path in self.paths:
            yield path

    def get_neighbors(self):
        ''' Permet d'obtenir les villes voisines '''
        neighbors = []
        for path in self.paths:
            neighbors.append(path.get_city_dest())
        return neighbors

    @staticmethod
    def load_from_file(filename):
        ''' Charge les villes dans un dictionnaire; les clés correspondent aux noms des villes, les valeurs sont les objets "City" correspondants'''
        cities = dict()
        file = open(filename, 'r')
        lines = file.readlines()
        for line in lines:
            data = line.split()
            cities[data[0]] = City(data[0], int(data[1]), int(data[2]))
        file.close()
        return cities
