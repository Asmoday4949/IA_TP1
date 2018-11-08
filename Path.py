'''
Auteur: Malik Fleury
Date: 29.10.2018
Maj: 08.11.2018
'''

class Path:
    def __init__(self, city_src, city_dest, cost):
        self.city_src = city_src
        self.city_dest = city_dest
        self.cost = cost

    def __str__(self):
        ''' Retourne une string sous la forme "villeSrc-VilleDst" '''
        return self.city_src.get_name() + "-" + self.city_dest.get_name()

    def get_city_src(self):
        ''' Obtient la source (ville à gauche dans le fichier texte) '''
        return self.city_src

    def get_city_dest(self):
        ''' Obtient la destination (ville à droite dans le fichier texte) '''
        return self.city_dest

    def get_cost(self):
        ''' Coût du chemin '''
        return self.cost

    def get_opposite_city(self, city):
        ''' Retourne la ville opposée par rapport à celle passée en paramètre '''
        if city == self.city_src:
            return self.city_dest
        elif city == self.city_dest:
            return self.city_src
        else:
            raise Exception("Error: the city passed as parameter doesn't match")

    @staticmethod
    def load_from_file(filename, cities):
        ''' Charge les chemins; les clés est une string sous la forme "villeSrc-VilleDst", les valeurs sont les objets "Path" correspondants '''
        paths = dict()
        file = open(filename, 'r')
        lines = file.readlines()
        for line in lines:
            data = line.split()
            city_src, city_dest, cost = cities[data[0]], cities[data[1]], int(data[2])
            path1 = Path(city_src, city_dest, cost)
            city_src.add_path(path1)
            city_dest.add_path(path1)
            paths[city_src.get_name() + '-' + city_dest.get_name()] = path1
            paths[city_dest.get_name() + '-' + city_src.get_name()] = path1
        file.close()
        return paths
