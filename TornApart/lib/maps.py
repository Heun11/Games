import json
from .entities import entity

# Maps and maps rendering
class MapLoader:
    def __init__(self, map_file_json, tiles=[], objects=[]):
        self.tiles = tiles
        self.objects = objects
        with open(map_file_json, "r") as f:
            self.map = json.load(f)

    def draw(self):
        # floor_0
        size = self.map["size"]
        f_0 = self.map["floor_0"]
        for i in range(size["x"]):
            for j in range(size["y"]):
                tile = f_0[j][i]
                self.tiles[tile].draw(i, j)

        # floor_1
        f_1 = self.map["floor_1"]
        for i in range(size["x"]):
            for j in range(size["y"]):
                object = f_1[j][i]
                self.objects[object].draw(i, j)


    def update(self):
        pass
