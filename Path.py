
class Path:
    def __init__(self, city_src, city_dest, cost):
        self.city_src = city_src
        self.city_dest = city_dest
        self.cost = cost

    def __str__(self):
        return self.city_src.get_name() + "-" + self.city_dest.get_name()

    def __hash__(self):
        return self.cost + ord(city_src[0]) + ord(city_dest[0])

    def get_city_src(self):
        return self.city_src

    def get_city_dest(self):
        return self.city_dest

    def get_cost(self):
        return self.cost

    def get_opposite_city(self, city):
        if city == self.city_src:
            return self.city_dest
        elif city == self.city_dest:
            return self.city_src
        else:
            raise Exception("Error")

    @staticmethod
    def load_from_file(filename, cities):
        paths = dict()
        file = open(filename, 'r')
        lines = file.readlines()
        for line in lines:
            data = line.split()
            city_src, city_dest, cost = cities[data[0]], cities[data[1]], data[2]
            path1 = Path(city_src, city_dest, cost)
            city_src.add_path(path1)
            city_dest.add_path(path1)
            paths[city_src.get_name() + '-' + city_dest.get_name()] = path1
            paths[city_dest.get_name() + '-' + city_src.get_name()] = path1
        file.close()
        return paths
