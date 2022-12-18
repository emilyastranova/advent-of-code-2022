class Chamber(list):
    """ Chamber class """
    def __init__(self):
        super().__init__()

    def display_chamber(self):
        """ Display the chamber """
        # Grid of dots to represent the chamber
        grid = []
        # Hashes representing the rocks
        for rock in self:
            # Get the coordinates of the rock and rasterize it
            for x, y in rock.get_coordinates():
                # Add the rock to the grid
                grid.append((x, y))
        # Get the min and max y coordinates
        # X min is 0 and max is 7
        y_min = 0
        y_max = max([y for x, y in grid])
        print(f"Max height: {y_max+1}")
        # Display the chamber
        for y in range(y_min, y_max + 1):
            for x in range(0, 7):
                if (x, y) in grid:
                    print("#", end="")
                else:
                    print(".", end="")
            print()