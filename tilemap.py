import json

class visualTilemap:
    def __init__(self, width, height, default_tile=0):
        """
        Creates a tilemap of given width and height, filled with the default_tile value.
        """
        self.width = width
        self.height = height
        self.tiles = [[default_tile for _ in range(width)] for _ in range(height)]

    def set_tile(self, x, y, tile_type):
        """Sets a specific tile in the tilemap."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.tiles[y][x] = tile_type
        else:
            raise ValueError("Tile position out of bounds")

    def get_tile(self, x, y):
        """Returns the tile type at a specific position."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[y][x]
        else:
            raise LookupError("Lookup tile position does not exist")

    def save(self, filename="tilemap.json"):
        """Saves the tilemap to a JSON file."""
        with open(filename, "w") as f:
            json.dump({"width": self.width, "height": self.height, "tiles": self.tiles}, f, indent=4)

    @classmethod
    def load(cls, filename="tilemap.json"):
        """Loads a tilemap from a JSON file."""
        with open(filename, "r") as f:
            data = json.load(f)
        tilemap = cls(data["width"], data["height"])
        tilemap.tiles = data["tiles"]
        return tilemap

class speedTilemap:
    def __init__(self, width, height, deafultMovementSpeed):
        """
        Creates a tilemap of given width and height, filled with the default_tile value.
        """
        self.width = width
        self.height = height
        self.tiles = [[deafultMovementSpeed for _ in range(width)] for _ in range(height)]

    def set_tile(self, x, y, tile_type):
        """Sets a specific tile in the tilemap."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.tiles[y][x] = tile_type
        else:
            raise ValueError("Tile position out of bounds")

    def get_tile(self, x, y):
        """Returns the tile type at a specific position."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[y][x]
        else:
            raise LookupError("Tile position does not exist")

    def save(self, filename="speedTilemap.json"):
        """Saves the tilemap to a JSON file."""
        with open(filename, "w") as f:
            json.dump({"width": self.width, "height": self.height, "tiles": self.tiles}, f, indent=4)

    @classmethod
    def load(cls, filename="speedTilemap.json"):
        """Loads a tilemap from a JSON file."""
        with open(filename, "r") as f:
            data = json.load(f)
        tilemap = cls(data["width"], data["height"])
        tilemap.tiles = data["tiles"]
        return tilemap
