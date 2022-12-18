class Rock:
    """ Class representing a rock """

    ROCK_TYPES = {
        "horizontal": {
            # Shape:
            # ####
            # Define the shape of the rock using 
            # offsets from the origin
            "shape": [
                (0, 0),
                (1, 0),
                (2, 0),
                (3, 0)
            ]
        },
        "plus": {
            # Shape:
            # .#.
            # ###
            # .#.
            "shape": [
                (1, 0),
                (0, 1),
                (1, 1),
                (2, 1),
                (1, 2)
            ]
        },
        "right_angle": {
            # Shape:
            # ..#
            # ..#
            # ###
            "shape": [
                (2, 0),
                (2, 1),
                (0, 2),
                (1, 2),
                (2, 2)
            ]
        },
        "vertical": {
            # Shape:
            # #
            # #
            # #
            # #
            "shape": [
                (0, 0),
                (0, 1),
                (0, 2),
                (0, 3)
            ]
        },
        "square": {
            # Shape:
            # ##
            # ##
            "shape": [
                (0, 0),
                (1, 0),
                (0, 1),
                (1, 1)
            ]
        },
    }

    def __init__(self, x, y, rock_type, falling=True):
        self.x = x # x coordinate of the rock origin
        self.y = y # y coordinate of the rock origin
        self.rock_type = rock_type # rock type
        self.falling = falling # is the rock falling?

    def __repr__(self):
        return f"Rock({self.x}, {self.y}, {self.rock_type})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
    
    def get_coordinates(self):
        """ Calcuilate and get the coordinates of the rock """
        # Calculate the coordinates of the rock
        #  using the rock type
        coords = []
        for offset in self.ROCK_TYPES[self.rock_type]["shape"]:
            coords.append((self.x + offset[0], self.y + offset[1]))
        return coords
    
    def freeze(self):
        """ Freeze the rock """
        self.falling = False