
class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.paths = []

    def __str__(self):
        return self.name

    def __hash__(self):
        return self.x + self.y + ord(self.name[0]) + ord(self.name[1])

    def add_path(self, newPath):
        self.paths.append(newPath)

    def add_paths(self, newPaths):
        for path in paths:
            self.addPath(path)

    def get_name(self):
        return self.name

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def paths_generator(self):
        for path in self.paths:
            yield path

    def get_neighbors(self):
        neighbors = []
        for path in self.paths:
            neighbors.append(path.get_city_dest())
        return neighbors

    @staticmethod
    def load_from_file(filename):
        cities = dict()
        file = open(filename, 'r')
        lines = file.readlines()
        for line in lines:
            data = line.split()
            cities[data[0]] = City(data[0], int(data[1]), int(data[2]))
        file.close()
        return cities
