# Settlers of Catan
# Vertex and Hextile class implementation

import collections
from hexLib import *

# Class to implement Catan board Hexagonal Tile
resource = collections.namedtuple("Resource", ["type", "num"])


class HexTile:
    """Class Definition for Catan Board Hexagonal Tile"""

    # Object Creation - specify the resource, num, center and neighbor list
    # Center is a point in axial coordinates q, r and neighborList is a list of hexTiles
    # hexIndex is a number from 0-18 specifying the Hex's position
    def __init__(self, hex_index, hex_resource, axial_coords, neighbor_list=None):
        self.hex = axial_hexagonal(axial_coords)  # Hex representation of this tile
        self.resource = hex_resource
        self.coord = axial_coords
        self.pixelCenter = None  # Pixel coordinates of hex as Point(x, y)
        self.index = hex_index
        self.neighborList = neighbor_list
        self.robber = False

    # Function to update hex neighbors
    def update_neighbors(self):
        return None

    # Function to Display Hex Info
    def display_hex_info(self):
        print('Index:{}; Hex:{}; Axial Coord:{}'.format(self.index, self.resource, self.coord))
        return None

    # Function to display Hex Neighbors
    def display_hex_neighbors(self):
        print('Neighbors:')
        for neighbor in self.neighborList:
            neighbor.displayHexInfo()

        return None


# Class definition of a Vertex
class Vertex:

    def __init__(self, pixel_coord, adj_hex_index, v_index):
        self.vertex_index = v_index  # Index to store vertex info
        self.pixel_coordinates = pixel_coord
        self.edge_list = []  # List to store adjacent Vertices
        self.adjacent_hex_list = [adj_hex_index]  # List to store indices of 3 adjacent hexes
        self.edge_state = [[None, False], [None, False], [None,
                                                          False]]  # Nested list to determine if a road is built on
        # edge, and player building road

        self.state = {'Player': None, 'Settlement': False, 'City': False}  # Vertex state
        self.port = False  # Add the corresponding port (BRICK, SHEEP, WHEAT, WOOD, ORE, 3:1) later
        self.is_colonised = False

        self.edge_length = 80  # Specify for hex size

    # Function to get a Vertex by its pixel coordinates
    def get_vertex_from_pixel(self, coords):
        if self.pixel_coordinates == coords:
            return self

    # Function to return if a vertex v1 is adjacent to another v2
    def is_adjacent(self, v1, v2):
        dist = ((v1.pixelCoordinates.x - v2.pixelCoordinates.x) ** 2 + (
                v1.pixelCoordinates.y - v2.pixelCoordinates.y) ** 2) ** 0.5
        if round(dist) == self.edge_length:
            return True

        return False

# Test Code testHex = hexTile(0, resource('Ore', 8), Point(2,3), [hexTile(2, resource('Wheat', 11), Point(5,6)),
# hexTile(3, resource('Brick', 11), Point(7,4))]) testHex.displayHexInfo() testHex.displayHexNeighbors()
