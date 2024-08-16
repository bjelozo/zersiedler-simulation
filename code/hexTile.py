# Zersiedler
# Vertex and Hextile class implementation

import collections
from hexLib import *

# Define namedtuple for zoning types
Zone = collections.namedtuple("Zone", ["type", "description"])


class HexTile:
    """ Class for a hexagonal field in the game, representing different zoning areas """

    # Object Creation - specify the resource, num, center and neighbor list
    # Center is a point in axial coordinates q, r and neighborList is a list of hexTiles
    # hexIndex is a number from 0-18 specifying the Hex's position
    def __init__(self, hex_index, zone, axial_coords, neighbor_list=None):
        self.hex = axial_hexagonal(axial_coords)  # Hex representation of this tile
        self.zone = zone # The zoning type of this tile
        self.coord = axial_coords
        self.pixelCenter = None  # Pixel coordinates of hex as Point(x, y)
        self.index = hex_index
        self.neighborList = neighbor_list
        self.robber = False

    # Method to update hex neighbors
    def update_neighbors(self):
        return None

    # Method to Display Hex Info
    def display_hex_info(self):
        print(f'Index: {self.index}; Zone: {self.zone.type}; Description: {self.zone.description}')
        return None

    # Method to display Hex Neighbors
    def display_hex_neighbors(self):
        print('Neighbors:')
        for neighbor in self.neighborList:
            neighbor.display_hex_info()

        return None

    # Method to change zone
    def change_zone(self, new_zone):
        """ Change the zoning type of this hex field """
        self.zone = new_zone
        print(f'Zone changed to: {new_zone.type} with description: {new_zone.description}')

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

    # Method to get a Vertex by its pixel coordinates
    def get_vertex_from_pixel(self, coords):
        if self.pixel_coordinates == coords:
            return self

    # Method to return if a vertex v1 is adjacent to another v2
    def is_adjacent(self, v1, v2):
        dist = ((v1.pixel_coordinates.x - v2.pixel_coordinates.x) ** 2 + (v1.pixel_coordinates.y - v2.pixel_coordinates.y) ** 2) ** 0.5
        return round(dist) == self.edge_length

