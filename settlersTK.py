import random
from Tkinter import *
import math
import time

breves = {'s': 'settlement', 'c': 'city', 'k': 'knight', 'r': 'road'}
knight_types = {0: "weak (1)", 1: "strong (2)", 2: "mighty (3)"}
resources = ["wheat", "sheep", "wood", "brick", "ore"]
commodities = ["coin", "cloth", "paper"]
resources_commodities = ["wheat", "sheep", "wood", "brick", "ore", "coin", "cloth", "paper"]
color2tech = {"yellow": "cloth", "blue": "coin", "green": "paper"}
dice_frequencies = {2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:5, 9:4, 10:3, 11:2, 12:1}
piece_colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown']
resource2color = {"wheat": "yellow", "sheep": "green", "desert": "beige",
                  "wood": "dark green", "brick": "brown", "ore": "gray",
                  "paper": "dark green", "cloth": "green", "coin": "gray"}
WIDTH = 1000
HEIGHT = 800
HEX_RADIUS = 75
CORNER_RADIUS = 15
EMPTY_CORNER_COLOR = "white"
TOKEN_RADIUS = 15
TOKEN_COLOR = "beige"
TOKEN_TEXT_COLOR = "black"
ROBBER_COLOR = "black"
ROBBER_TEXT_COLOR = "dark gray"
ROBBER_RADIUS = 25
ROBBER_ALERT_COLOR = "pink"
ROBBER_ALERT_TEXT_COLOR = "black"
ROAD_WIDTH = 8
EMPTY_ROAD_COLOR = "white"
ROAD_ACTIVE_FILL = "pink"
CANVAS_BACKGROUND_COLOR = "black"
CARD_WIDTH = 50
CARD_HEIGHT = 70
PROGRESS_CARD_WIDTH = 100
PROGRESS_CARD_HEIGHT = 50
Y_ADJUST = HEX_RADIUS * math.sin(math.pi / 6)
X_ADJUST = HEX_RADIUS * math.cos(math.pi / 6)
WALL_RADIUS = 25
WALL_THICKNESS = 5
WALL_BACKGROUND_COLOR = "white"
METROPOLIS_RADIUS = 35
METROPOLIS_BORDER_WIDTH = 4
METROPOLIS_COLOR = "gold"
OUTLINE_WIDTH = 1
OUTLINE_COLOR = "white"
MERCHANT_WIDTH = 20
MERCHANT_HEIGHT = 40
MERCHANT_OFFSET = 30
HEX_CLICK_RADIUS = X_ADJUST
TOP_PADDING = 50
LEFT_PADDING = 50
BUTTON_WIDTH = 25
POP_UP_HEIGHT = 400
POP_UP_WIDTH = 400
INACTIVE_KNIGHT_COLOR = "white"
ACTIVE_KNIGHT_COLOR = "gold"
KNIGHT_ALERT_COLOR = "pink"
hex_coords = {2: (TOP_PADDING + 5 * HEX_RADIUS + 4 * Y_ADJUST, LEFT_PADDING + 3 * X_ADJUST),
              3: (TOP_PADDING + 5 * HEX_RADIUS + 4 * Y_ADJUST, LEFT_PADDING + 5 * X_ADJUST),
              4: (TOP_PADDING + 5 * HEX_RADIUS + 4 * Y_ADJUST, LEFT_PADDING + 7 * X_ADJUST),
              5: (TOP_PADDING + 4 * HEX_RADIUS + 3 * Y_ADJUST, LEFT_PADDING + 8 * X_ADJUST),
              6: (TOP_PADDING + 3 * HEX_RADIUS + 2 * Y_ADJUST, LEFT_PADDING + 9 * X_ADJUST),
              7: (TOP_PADDING + 2 * HEX_RADIUS + 1 * Y_ADJUST, LEFT_PADDING + 8 * X_ADJUST),
              8: (TOP_PADDING + 1 * HEX_RADIUS + 0 * Y_ADJUST, LEFT_PADDING + 7 * X_ADJUST),
              9: (TOP_PADDING + 1 * HEX_RADIUS + 0 * Y_ADJUST, LEFT_PADDING + 5 * X_ADJUST),
              10: (TOP_PADDING + 1 * HEX_RADIUS + 0 * Y_ADJUST, LEFT_PADDING + 3 * X_ADJUST),
              11: (TOP_PADDING + 2 * HEX_RADIUS + 1 * Y_ADJUST, LEFT_PADDING + 2 * X_ADJUST),
              0: (TOP_PADDING + 3 * HEX_RADIUS + 2 * Y_ADJUST, LEFT_PADDING + 1 * X_ADJUST),
              1: (TOP_PADDING + 4 * HEX_RADIUS + 3 * Y_ADJUST, LEFT_PADDING + 2 * X_ADJUST),
              13: (TOP_PADDING + 4 * HEX_RADIUS + 3 * Y_ADJUST, LEFT_PADDING + 4 * X_ADJUST),
              14: (TOP_PADDING + 4 * HEX_RADIUS + 3 * Y_ADJUST, LEFT_PADDING + 6 * X_ADJUST),
              15: (TOP_PADDING + 3 * HEX_RADIUS + 2 * Y_ADJUST, LEFT_PADDING + 7 * X_ADJUST),
              16: (TOP_PADDING + 2 * HEX_RADIUS + 1 * Y_ADJUST, LEFT_PADDING + 6 * X_ADJUST),
              17: (TOP_PADDING + 2 * HEX_RADIUS + 1 * Y_ADJUST, LEFT_PADDING + 4 * X_ADJUST),
              12: (TOP_PADDING + 3 * HEX_RADIUS + 2 * Y_ADJUST, LEFT_PADDING + 3 * X_ADJUST),
              18: (TOP_PADDING + 3 * HEX_RADIUS + 2 * Y_ADJUST, LEFT_PADDING + 5 * X_ADJUST)}

corner_coords = {0: (LEFT_PADDING + 0 * X_ADJUST, TOP_PADDING + 3 * HEX_RADIUS + 1 * Y_ADJUST),
                 1: (LEFT_PADDING + 0 * X_ADJUST, TOP_PADDING + 3 * HEX_RADIUS + 3 * Y_ADJUST),
                 2: (LEFT_PADDING + 1 * X_ADJUST, TOP_PADDING + 4 * HEX_RADIUS + 2 * Y_ADJUST),
                 3: (LEFT_PADDING + 1 * X_ADJUST, TOP_PADDING + 4 * HEX_RADIUS + 4 * Y_ADJUST),
                 4: (LEFT_PADDING + 2 * X_ADJUST, TOP_PADDING + 5 * HEX_RADIUS + 3 * Y_ADJUST),
                 5: (LEFT_PADDING + 2 * X_ADJUST, TOP_PADDING + 5 * HEX_RADIUS + 5 * Y_ADJUST),
                 6: (LEFT_PADDING + 3 * X_ADJUST, TOP_PADDING + 6 * HEX_RADIUS + 4 * Y_ADJUST),
                 7: (LEFT_PADDING + 4 * X_ADJUST, TOP_PADDING + 5 * HEX_RADIUS + 5 * Y_ADJUST),
                 8: (LEFT_PADDING + 5 * X_ADJUST, TOP_PADDING + 6 * HEX_RADIUS + 4 * Y_ADJUST),
                 9: (LEFT_PADDING + 6 * X_ADJUST, TOP_PADDING + 5 * HEX_RADIUS + 5 * Y_ADJUST),
                 10: (LEFT_PADDING + 7 * X_ADJUST, TOP_PADDING + 6 * HEX_RADIUS + 4 * Y_ADJUST),
                 11: (LEFT_PADDING + 8 * X_ADJUST, TOP_PADDING + 5 * HEX_RADIUS + 5 * Y_ADJUST),
                 12: (LEFT_PADDING + 8 * X_ADJUST, TOP_PADDING + 5 * HEX_RADIUS + 3 * Y_ADJUST),
                 13: (LEFT_PADDING + 9 * X_ADJUST, TOP_PADDING + 4 * HEX_RADIUS + 4 * Y_ADJUST),
                 14: (LEFT_PADDING + 9 * X_ADJUST, TOP_PADDING + 4 * HEX_RADIUS + 2 * Y_ADJUST),
                 15: (LEFT_PADDING + 10 * X_ADJUST, TOP_PADDING + 3 * HEX_RADIUS + 3 * Y_ADJUST),
                 16: (LEFT_PADDING + 10 * X_ADJUST, TOP_PADDING + 3 * HEX_RADIUS + 1 * Y_ADJUST),
                 17: (LEFT_PADDING + 9 * X_ADJUST, TOP_PADDING + 2 * HEX_RADIUS + 2 * Y_ADJUST),
                 18: (LEFT_PADDING + 9 * X_ADJUST, TOP_PADDING + 2 * HEX_RADIUS + 0 * Y_ADJUST),
                 19: (LEFT_PADDING + 8 * X_ADJUST, TOP_PADDING + 1 * HEX_RADIUS + 1 * Y_ADJUST),
                 20: (LEFT_PADDING + 8 * X_ADJUST, TOP_PADDING + 1 * HEX_RADIUS - 1 * Y_ADJUST),
                 21: (LEFT_PADDING + 7 * X_ADJUST, TOP_PADDING + 0 * HEX_RADIUS - 0 * Y_ADJUST),
                 22: (LEFT_PADDING + 6 * X_ADJUST, TOP_PADDING + 1 * HEX_RADIUS - 1 * Y_ADJUST),
                 23: (LEFT_PADDING + 5 * X_ADJUST, TOP_PADDING + 0 * HEX_RADIUS - 0 * Y_ADJUST),
                 24: (LEFT_PADDING + 4 * X_ADJUST, TOP_PADDING + 1 * HEX_RADIUS - 1 * Y_ADJUST),
                 25: (LEFT_PADDING + 3 * X_ADJUST, TOP_PADDING + 0 * HEX_RADIUS - 0 * Y_ADJUST),
                 26: (LEFT_PADDING + 2 * X_ADJUST, TOP_PADDING + 1 * HEX_RADIUS - 1 * Y_ADJUST),
                 27: (LEFT_PADDING + 2 * X_ADJUST, TOP_PADDING + 1 * HEX_RADIUS + 1 * Y_ADJUST),
                 28: (LEFT_PADDING + 1 * X_ADJUST, TOP_PADDING + 2 * HEX_RADIUS + 0 * Y_ADJUST),
                 29: (LEFT_PADDING + 1 * X_ADJUST, TOP_PADDING + 2 * HEX_RADIUS + 2 * Y_ADJUST),
                 30: (LEFT_PADDING + 2 * X_ADJUST, TOP_PADDING + 3 * HEX_RADIUS + 1 * Y_ADJUST),
                 31: (LEFT_PADDING + 2 * X_ADJUST, TOP_PADDING + 3 * HEX_RADIUS + 3 * Y_ADJUST),
                 32: (LEFT_PADDING + 3 * X_ADJUST, TOP_PADDING + 4 * HEX_RADIUS + 2 * Y_ADJUST),
                 33: (LEFT_PADDING + 3 * X_ADJUST, TOP_PADDING + 4 * HEX_RADIUS + 4 * Y_ADJUST),
                 34: (LEFT_PADDING + 4 * X_ADJUST, TOP_PADDING + 5 * HEX_RADIUS + 3 * Y_ADJUST),
                 35: (LEFT_PADDING + 5 * X_ADJUST, TOP_PADDING + 4 * HEX_RADIUS + 4 * Y_ADJUST),
                 36: (LEFT_PADDING + 6 * X_ADJUST, TOP_PADDING + 5 * HEX_RADIUS + 3 * Y_ADJUST),
                 37: (LEFT_PADDING + 7 * X_ADJUST, TOP_PADDING + 4 * HEX_RADIUS + 4 * Y_ADJUST),
                 38: (LEFT_PADDING + 7 * X_ADJUST, TOP_PADDING + 4 * HEX_RADIUS + 2 * Y_ADJUST),
                 39: (LEFT_PADDING + 8 * X_ADJUST, TOP_PADDING + 3 * HEX_RADIUS + 3 * Y_ADJUST),
                 40: (LEFT_PADDING + 8 * X_ADJUST, TOP_PADDING + 3 * HEX_RADIUS + 1 * Y_ADJUST),
                 41: (LEFT_PADDING + 7 * X_ADJUST, TOP_PADDING + 2 * HEX_RADIUS + 2 * Y_ADJUST),
                 42: (LEFT_PADDING + 7 * X_ADJUST, TOP_PADDING + 2 * HEX_RADIUS + 0 * Y_ADJUST),
                 43: (LEFT_PADDING + 6 * X_ADJUST, TOP_PADDING + 1 * HEX_RADIUS + 1 * Y_ADJUST),
                 44: (LEFT_PADDING + 5 * X_ADJUST, TOP_PADDING + 2 * HEX_RADIUS + 0 * Y_ADJUST),
                 45: (LEFT_PADDING + 4 * X_ADJUST, TOP_PADDING + 1 * HEX_RADIUS + 1 * Y_ADJUST),
                 46: (LEFT_PADDING + 3 * X_ADJUST, TOP_PADDING + 2 * HEX_RADIUS + 0 * Y_ADJUST),
                 47: (LEFT_PADDING + 3 * X_ADJUST, TOP_PADDING + 2 * HEX_RADIUS + 2 * Y_ADJUST),
                 48: (LEFT_PADDING + 4 * X_ADJUST, TOP_PADDING + 3 * HEX_RADIUS + 1 * Y_ADJUST),
                 49: (LEFT_PADDING + 4 * X_ADJUST, TOP_PADDING + 3 * HEX_RADIUS + 3 * Y_ADJUST),
                 50: (LEFT_PADDING + 5 * X_ADJUST, TOP_PADDING + 4 * HEX_RADIUS + 2 * Y_ADJUST),
                 51: (LEFT_PADDING + 6 * X_ADJUST, TOP_PADDING + 3 * HEX_RADIUS + 3 * Y_ADJUST),
                 52: (LEFT_PADDING + 6 * X_ADJUST, TOP_PADDING + 3 * HEX_RADIUS + 1 * Y_ADJUST),
                 53: (LEFT_PADDING + 5 * X_ADJUST, TOP_PADDING + 2 * HEX_RADIUS + 2 * Y_ADJUST)}

class Card():
    def __init__(self, index, resource, canvas):
        self.index = index
        self.resource = resource
        self.canvas = canvas

    def draw(self):
        self.canvas.create_rectangle(self.index * CARD_WIDTH + 5, HEIGHT - CARD_HEIGHT - 10,
                                     (self.index + 1) * CARD_WIDTH + 5, HEIGHT - 10, fill = resource2color[self.resource])
        if self.resource in ["coin", "paper", "cloth"]:
            self.canvas.create_rectangle(self.index * CARD_WIDTH + 15, HEIGHT - CARD_HEIGHT,
                                         (self.index + 1) * CARD_WIDTH - 5, HEIGHT - 20, fill = "white")

class Hex():
    def __init__(self, location, resource):
        self.location = location
        self.corners = []
        self.resource = resource
        self.number = None
        self.blocked = False
        self.merchant = None
        self.center = (hex_coords[location][1], hex_coords[location][0])
        self.color = resource2color[resource]
        self.token_color = TOKEN_COLOR

    def set_number(self, number):
        self.number = number

    def set_corners(self, corners):
        self.corners = corners

    def draw(self, canvas):
        n = (self.center[0], self.center[1] - HEX_RADIUS)
        ne = (self.center[0] + X_ADJUST, self.center[1] - Y_ADJUST)
        se = (self.center[0] + X_ADJUST, self.center[1] + Y_ADJUST)
        s = (self.center[0], self.center[1] + HEX_RADIUS)
        sw = (self.center[0] - X_ADJUST, self.center[1] + Y_ADJUST)
        nw = (self.center[0] - X_ADJUST, self.center[1] - Y_ADJUST)
        if self.blocked and self not in invent_hexes:
            fill_color = ROBBER_COLOR
            text_color = ROBBER_TEXT_COLOR
            radius = ROBBER_RADIUS
        else:
            fill_color = self.token_color
            text_color = TOKEN_TEXT_COLOR
            radius = TOKEN_RADIUS
        if status in ["move robber", "progress bishop"] and not self.blocked:
            fill_color = ROBBER_ALERT_COLOR
            text_color = ROBBER_ALERT_TEXT_COLOR
        canvas.create_polygon(n[0], n[1], ne[0], ne[1], se[0], se[1],
                              s[0], s[1], sw[0], sw[1], nw[0], nw[1],
                              fill = self.color)
        if self.number or self.blocked:
            canvas.create_oval(self.center[0] - radius, self.center[1] - radius,
                               self.center[0] + radius, self.center[1] + radius,
                               fill = fill_color)
        if self.number:
            canvas.create_text(self.center[0], self.center[1], text=str(self.number), fill = text_color)
        if self.merchant:
            canvas.create_polygon(self.center[0] - MERCHANT_OFFSET - MERCHANT_WIDTH / 2, self.center[1] + MERCHANT_HEIGHT / 2,
                                  self.center[0] - MERCHANT_OFFSET, self.center[1] - MERCHANT_HEIGHT / 2,
                                  self.center[0] - MERCHANT_OFFSET + MERCHANT_WIDTH / 2, self.center[1] + MERCHANT_HEIGHT / 2,
                                  fill = self.merchant, outline = OUTLINE_COLOR)
        

class Corner():
    def __init__(self, location):
        self.location = location
        self.edges = []
        self.occupier = None
        self.occ_type = ""
        self.port = ""
        self.value = 0
        self.hexes_touched = []
        self.center = corner_coords[location]

    def set_edges(self, edges):
        self.edges = edges

    def draw(self, canvas, mode):
        if not self.occ_type:
            if ((mode in ["place initial settlement", "place initial city"] and self.location in player.show_valid_locations('i', display=False))
                or (mode in ["place settlement"] and self.location in player.show_valid_locations('s', display=False))
                or ((mode in ["place knight"] or mode.startswith("progress place knight")) and self.location in player.show_valid_locations('b', display=False))):
                canvas.create_oval(self.center[0] - CORNER_RADIUS, self.center[1] - CORNER_RADIUS,
                                     self.center[0] + CORNER_RADIUS, self.center[1] + CORNER_RADIUS,
                                     fill = EMPTY_CORNER_COLOR)
        elif self.occ_type == "settlement":
            canvas.create_polygon(self.center[0], self.center[1] - CORNER_RADIUS,
                                  self.center[0] + CORNER_RADIUS, self.center[1],
                                  self.center[0] + CORNER_RADIUS, self.center[1] + CORNER_RADIUS,
                                  self.center[0] - CORNER_RADIUS, self.center[1] + CORNER_RADIUS,
                                  self.center[0] - CORNER_RADIUS, self.center[1],
                                  fill = self.occupier, width = OUTLINE_WIDTH, outline = OUTLINE_COLOR)
        elif self.occ_type == "city":
            city = [c for p in players for c in p.cities_built if c[0] == self.location][0]
            if city[2]:
                canvas.create_rectangle(self.center[0] - METROPOLIS_RADIUS, self.center[1] - METROPOLIS_RADIUS,
                                        self.center[0] + METROPOLIS_RADIUS, self.center[1] + METROPOLIS_RADIUS,
                                        fill = METROPOLIS_COLOR, width = METROPOLIS_BORDER_WIDTH, outline = resource2color[city[2]])
            if city[1]:
                canvas.create_rectangle(self.center[0] - WALL_RADIUS, self.center[1] - WALL_RADIUS,
                                        self.center[0] + WALL_RADIUS, self.center[1] + WALL_RADIUS,
                                        fill = self.occupier)
                canvas.create_rectangle(self.center[0] - WALL_RADIUS + WALL_THICKNESS, self.center[1] - WALL_RADIUS + WALL_THICKNESS,
                                        self.center[0] + WALL_RADIUS - WALL_THICKNESS, self.center[1] + WALL_RADIUS - WALL_THICKNESS,
                                        fill = WALL_BACKGROUND_COLOR)
            canvas.create_polygon(self.center[0] - CORNER_RADIUS / 4., self.center[1] - CORNER_RADIUS / 4.,
                                  self.center[0] - CORNER_RADIUS / 4., self.center[1] - CORNER_RADIUS,
                                  self.center[0] + CORNER_RADIUS, self.center[1] - CORNER_RADIUS,
                                  self.center[0] + CORNER_RADIUS, self.center[1] + CORNER_RADIUS,
                                  self.center[0] - CORNER_RADIUS, self.center[1] + CORNER_RADIUS,
                                  self.center[0] - CORNER_RADIUS, self.center[1] - CORNER_RADIUS / 4.,
                                  fill = self.occupier, width = OUTLINE_WIDTH, outline = OUTLINE_COLOR)
        elif self.occ_type == "knight":
            if status in ["upgrade knight", "activate knight", "move knight select"] and player.color == self.occupier:
                knight_color = KNIGHT_ALERT_COLOR
            else:
                knight_color = self.occupier
            knight = [k for p in players if p.color == self.occupier for k in p.knights_built if k[0] == self.location][0]
            level = knight[1]
            active = knight[2]
            if active: color = ACTIVE_KNIGHT_COLOR
            else: color = INACTIVE_KNIGHT_COLOR
            canvas.create_oval(self.center[0] - CORNER_RADIUS, self.center[1] - CORNER_RADIUS,
                               self.center[0] + CORNER_RADIUS, self.center[1] + CORNER_RADIUS,
                               fill = knight_color, outline = knight_color)
            canvas.create_oval(self.center[0] - CORNER_RADIUS + 2, self.center[1] - CORNER_RADIUS + 2,
                               self.center[0] + CORNER_RADIUS - 2, self.center[1] + CORNER_RADIUS - 2,
                               fill = color, outline = self.occupier)
            canvas.create_text(self.center[0], self.center[1], text = str(level + 1), fill = self.occupier)

class Edge():
    def __init__(self, location):
        self.location = location
        self.corners = []
        self.occupier = None

    def get_midpoint(self):
        corns = [c for c in corners if c.location in self.corners]
        A = corns[0].center
        B = corns[1].center
        return (A[0] + B[0]) / 2., (A[1] + B[1]) / 2.

    def draw(self, canvas, mode):
        corns = [c for c in corners if c.location in self.corners]
        A = corns[0].center
        B = corns[1].center
        if not self.occupier:
            if mode in ["place settlement road", "progress place road 1", "place road 2", "progress place road diplomat",
                        "place road"] and self.location in player.show_valid_locations('r', display=False):
                canvas.create_line(A[0], A[1], B[0], B[1], width = ROAD_WIDTH, fill = EMPTY_ROAD_COLOR, activefill = ROAD_ACTIVE_FILL)
            elif mode == "place city road" and self.location in player.show_valid_locations('rc', display=False):
                canvas.create_line(A[0], A[1], B[0], B[1], width = ROAD_WIDTH, fill = EMPTY_ROAD_COLOR, activefill = ROAD_ACTIVE_FILL)
        else:
            canvas.create_line(A[0], A[1], B[0], B[1], width = ROAD_WIDTH, fill = self.occupier)

class Player():
    def __init__(self, seat_number, color):
        self.color = color
        self.seat_number = seat_number
        self.resources = {"wheat":0, "sheep":0, "wood":0, "brick":0, "ore":0, "paper":4, "cloth":0, "coin":0}
        self.victory_points = 0
        self.settlements_remaining = 5
        self.cities_remaining = 4
        self.roads_remaining = 15
        self.walls_remaining = 3
        self.knights_remaining = [2,2,2]
        self.settlements_built = []
        self.cities_built = []
        self.roads_built = []
        self.knights_built = []
        self.walls_built = []
        self.corners_touched = set()
        self.technology = {"coin": 1, "paper": 4, "cloth": 1}
        self.technology_powers = {"coin": "You now have the ability to upgrade strong knights to mighty knights.",
                                  "paper": "You may select a resource of your choice when you don't gain any resources on a non-7 roll.",
                                  "cloth": "You may now trade commodities at the 2-for-1 rate."}
        self.progress_cards = []
        self.two_for_one = []
        self.three_for_one = False
        self.merchant = ""
        self.temp_two_for_one = []
        self.has_longest_road = False
        self.pop_up = None

    def build_settlement(self, corner_location, initial_placement=False):
        if not initial_placement and corner_location not in self.corners_touched:
            print "You must build along one of your roads"
        elif not self.settlements_remaining:
            print "You do not have any settlements left."
        elif not initial_placement and not all([self.resources["wood"], self.resources["wheat"],
                                                self.resources["sheep"], self.resources["brick"]]):
            print "You do not have the resources to buy a settlement"
            return
        else:
            for corner in corners:
                if corner.location == corner_location:
                    if corner.occupier:
                        print "This corner is already occupied by a " + corner.occupier + " " + corner.occ_type
                        return
                    else:
                        for edge in edges:
                            if corner.location in edge.corners:
                                for corner2 in corners:
                                    if corner2.location in edge.corners and corner2.location != corner.location:
                                        if corner2.occ_type in ["settlement", "city"]:
                                            print "You must build at least 2 corners away from all existing buildings."
                                            return
                        print "Building a settlement at " + str(corner_location)
                        if self.resources["wood"]: self.resources["wood"] -= 1
                        if self.resources["wheat"]: self.resources["wheat"] -= 1
                        if self.resources["sheep"]: self.resources["sheep"] -= 1
                        if self.resources["brick"]: self.resources["brick"] -= 1
                        self.settlements_remaining -= 1
                        self.settlements_built.append(corner_location)
                        self.corners_touched |= {corner_location}
                        self.victory_points += 1
                        if corner.port == "3:1":
                            print "You built on a port! You may now trade resources at the 3:1 rate."
                            self.three_for_one = True
                        elif corner.port:
                            print "You built on a port! You may now trade", corner.port, "at the 2:1 rate."
                            self.two_for_one.append(corner.port)
                        corner.occupier = self.color
                        corner.occ_type = "settlement"
                        overall_longest_road()
                        return "success"
            print "Invalid location."
            return

    def build_city(self, corner_location, special=""):
        if special == "initial":
            for corner in corners:
                if corner.location == corner_location:
                    if corner.occupier:
                        print "This corner is already occupied by a " + corner.occupier + " " + corner.occ_type
                        return
                    else:
                        for edge in edges:
                            if corner.location in edge.corners:
                                for corner2 in corners:
                                    if corner2.location in edge.corners and corner2.location != corner.location:
                                        if corner2.occ_type in ["settlement", "city"]:
                                            print "You must build at least 2 corners away from all existing buildings."
                                            return
                        print "Building a city at " + str(corner_location)
                        self.cities_remaining -= 1
                        self.cities_built.append([corner_location, 0, ''])
                        self.corners_touched |= {corner_location}
                        self.victory_points += 2
                        if corner.port == "3:1":
                            print "You built on a port! You may now trade resources at the 3:1 rate."
                            self.three_for_one = True
                        elif corner.port:
                            print "You built on a port! You may now trade", corner.port, "at the 2:1 rate."
                            self.two_for_one.append(corner.port)
                        corner.occupier = self.color
                        corner.occ_type = "city"
                        for hexe in hexes:
                            if corner.location in hexe.corners and hexe.resource != "desert":
                                self.resources[hexe.resource] += 1
                        return "success"
        elif (self.resources["ore"] < 3 or self.resources["wheat"] < 2) and special != "medicine":
            print "You don't have the resources to buy a city."
            return
        elif not self.cities_remaining:
            print "You don't have any cities left."
            return
        elif corner_location not in self.settlements_built:
            print "You can't build here because you don't have a settlement at this location."
            return
        else:
            print "Building a city at " + str(corner_location)
            if special == "medicine":
                self.resources["ore"] -= 2
                self.resources["wheat"] -= 1
            else:
                self.resources["ore"] -= 3
                self.resources["wheat"] -= 2
            self.cities_remaining -= 1
            self.cities_built.append([corner_location,0,''])
            self.settlements_built.remove(corner_location)
            self.settlements_remaining += 1
            self.victory_points += 1
            for corner in corners:
                if corner.location == corner_location:
                    corner.occ_type = "city"
            overall_longest_road()
            return "success"

    def upgrade_city_GUI(self, color, crane=0):
        global status
        if self.technology[color] == 6:
            status_label.config(text = color + " is maxed out at level 6.")
            print "You can't upgrade", color, "any further. It is maxed out at level 6."
            return
        if self.resources[color] + crane < self.technology[color]:
            status_label.config(text = "Not enough " + color + " to upgrade.")
            print "You don't have enough", color, "to upgrade. You need", self.technology[color] - crane
            return
        naked_cities = [c[0] for c in self.cities_built if not c[2]]
        if self.technology[color] == 4 and not naked_cities:
            status_label.config(text = "Need an un-metropolized city to upgrade.")
            print "You can't upgrade", color, "to a metropolis because you have no un-metropolized cities."
            return
        if not self.cities_built:
            status_label.config(text = "Can't upgrade without cities.")
            print "You can't upgrade because you don't have any cities."
            return
        self.resources[color] -= (self.technology[color] - crane)
        self.technology[color] += 1
        print color, "technology is now at level", self.technology[color]
        if self.technology[color] == 4:
            print self.technology_powers[color]
            if color == "cloth": self.two_for_one += ["coin", "paper", "cloth"]
        if self.technology[color] > 4: self.gain_metropolis(color)
        return "success"

    def upgrade_city(self, crane=0):
        # No longer needed
        if not self.cities_built:
            print "You can't perform an upgrade because you don't have any cities."
            return
        color = raw_input("What do you want to upgrade? (paper, coin, cloth) ")
        while color not in ["paper", "coin", "cloth"]:
            if not color: return
            print "Invalid entry. Please select one of the choices provided."
            color = raw_input("What do you want to upgrade? (paper, coin, cloth) ")
        if self.technology[color] == 6:
            print "You can't upgrade", color, "any further. It is maxed out at level 6."
            return
        if self.resources[color] + crane < self.technology[color]:
            print "You don't have enough", color, "to upgrade. You need", self.technology[color] - crane
            return
        naked_cities = [c[0] for c in self.cities_built if not c[2]]
        if self.technology[color] == 4 and not naked_cities:
            print "You can't upgrade", color, "to a metropolis because you have no un-metropolized cities."
            return
        self.resources[color] -= (self.technology[color] - crane)
        self.technology[color] += 1
        print color, "technology is now at level", self.technology[color]
        if self.technology[color] == 4:
            print self.technology_powers[color]
            if color == "cloth": self.two_for_one += ["coin", "paper", "cloth"]
        if self.technology[color] > 4: self.gain_metropolis(color)
        return "success"

    def gain_metropolis(self, col):
        # Needs tested
        global status
        max_color = max([1] + [player.technology[col] for player in players if player != self])
        if max_color >= self.technology[col]: return
        if [city for city in self.cities_built if city[2] == col]:
            print "you already have this metropolis"
            return
        loser = [p for p in players if p != self for c in p.cities_built if c[2] == col]
        if loser: loser[0].lose_metropolis(col)
        print self.color + ", you got the", col, "metropolis, which is worth 2 victory points!"
        status = "place metropolis=" + col
        status_label.config(text = "choose a city to metropolize")

        # Original non-GUI version:
##        print "Current city locations:", self.cities_built
##        location = raw_input("Where do you want to place the metropolis? " +
##                             str([city[0] for city in self.cities_built if not city[2]]) + " ")
##        while location not in [str(city[0]) for city in self.cities_built if not city[2]]:
##            print "Invalid entry. You must select one of the options provided."
##            location = raw_input("Where do you want to place the metropolis? " +
##                                 str([city[0] for city in self.cities_built if not city[2]]) + " ")
##        for city in self.cities_built:
##            if str(city[0]) == location:
##                city[2] = col
##        self.victory_points += 2

    def lose_metropolis(self, col):
        print self.color, "loses the", col, "metropolis. -2 victory points."
        for city in self.cities_built:
            if city[2] == col:
                city[2] = ""
                self.victory_points -= 2

    def build_road(self, edge_location, initial_placement=False):
        if not initial_placement and (not self.resources["brick"] or not self.resources["wood"]):
            print "You don't have the resources to build a road."
            return
        if not self.roads_remaining:
            print "You do not have any roads left."
            if status == "place road 2": return "road 2 placed"
            elif status == "progress place road diplomat": return "diplomat road placed"
            else: return
        else:
            for edge in edges:
                if edge.location == edge_location:
                    if edge.occupier:
                        print edge.occupier + " has already built a road here."
                        return
                    else:
                        for corner in edge.corners:
                            corner_object = [c for c in corners if c.location == corner][0]
                            if ((initial_placement in ["settlement", False] and corner in self.corners_touched and corner_object.occupier in [self.color, None])
                                or (initial_placement == "city" and corner in [city[0] for city in self.cities_built])):
                                print "Building a road at " + str(edge_location)
                                if not initial_placement: self.resources["wood"] -= 1
                                if not initial_placement: self.resources["brick"] -= 1
                                self.roads_remaining -= 1
                                self.roads_built.append(edge_location)
                                self.corners_touched |= set(edge.corners)
                                edge.occupier = self.color
                                overall_longest_road()
                                if status == "progress place road 1": return "road 1 placed"
                                elif status == "place road 2": return "road 2 placed"
                                elif status == "progress place road diplomat": return "diplomat road placed"
                                else: return "success"
            print "Invalid location: a new road must connect to your existing roads."
            return

    def remove_road(self, edge):
        print "remove road"
        global status
        open_roads = set()
        for p in players:
            open_roads |= p.get_open_roads()
        print edge.location, open_roads
        if edge in open_roads:
            print "yes"
            loser = [p for p in players if edge.location in p.roads_built][0]
            loser.roads_built.remove(edge.location)
            loser.roads_remaining += 1
            edge.occupier = None
            loser.set_corners_touched()
            overall_longest_road()
            if loser == self:
                status = "progress place road diplomat"
                status_label.config(text = player.color + ", place your road.")
            else:
                status = "player action"
                status_label.config(text = player.color + ", choose an action.")
                player.discard_progress_card("Diplomat")

##        self.roads_built.remove(location)
##        this_edge = [edge for edge in edges if edge.location == location][0]
##        this_edge.occupier = None
##        self.set_corners_touched()
##        overall_longest_road()
        

    def build_wall(self, location, special=False):
        if not self.walls_remaining:
            print "You don't have any walls left."
            return
        if special != "engineer" and self.resources["brick"] < 2:
            print "You don't have enough brick to build a wall."
            return
        if location not in [city[0] for city in self.cities_built if not city[1]]:
            print "Invalid location. Must be under a city that doesn't already have a wall."
            return
        for city in self.cities_built:
            if city[0] == location:
                print self.color, "is building a wall around the city at location", location
                if special != "engineer":
                    self.resources["brick"] -= 2
                city[1] = 1
                self.walls_remaining -= 1
                return "success"

    def build_knight(self, location, initial_state=[0,0,0], special=False):
        if not self.knights_remaining[0]:
            print "You don't have any level 1 knights left."
        elif (self.resources["sheep"] < 1 or self.resources["ore"] < 1) and not special:
            print "You don't have the resources to build a knight."
        elif location not in self.corners_touched:
            print "Invalid placement. Knight must touch one of your roads."
        else:
            corn = [corner for corner in corners if corner.location == location][0]
            if corn.occupier:
                print "This location is already occupied by a " + corn.occupier + " " + corn.occ_type
            else:
                if initial_state[1]: state = "active"
                else: state = "inactive"
                print self.color, "is building an", state, knight_types[initial_state[0]], "knight at location", location
                self.knights_remaining[initial_state[0]] -= 1
                self.knights_built.append([location] + initial_state)
                if not special:
                    self.resources["sheep"] -= 1
                    self.resources["ore"] -= 1
                corn.occupier = self.color
                corn.occ_type = "knight"
                overall_longest_road()
                return "success"

    def activate_knight(self, location):
        if not self.resources["wheat"]:
            print "You don't have any wheat to feed your knight."
        else:
            for knight in self.knights_built:
                if knight[0] == location:
                    if knight[2]:
                        print "This knight is already active"
                        return
                    else:
                        print "Activating", knight_types[knight[1]], "knight at location", location
                        self.resources["wheat"] -= 1
                        knight[2] = 1
                        knight[3] = 1
                        return "success"
            print "You don't have a knight at this location."

    def upgrade_knight(self, location, special=False):
        if (self.resources["sheep"] < 1 or self.resources["ore"] < 1) and not special:
            print "You don't have the resources to upgrade a knight."
            return
        for knight in self.knights_built:
            if knight[0] == location:
                if knight[1] == 2:
                    print "You already have a mighty knight at this location. Can't upgrade any further."
                    return
                elif knight[1] == 1:
                    if self.technology["coin"] < 4:
                        print "You can't upgrade to mighty knights until coin technology is at level 4."
                        return
                    if not self.knights_remaining[2]:
                        print "You don't have any mighty knights left."
                        return
                elif not self.knights_remaining[1]:
                    print "You don't have any strong knights left."
                    return
                print "Upgrading", knight_types[knight[1]], "knight to", knight_types[knight[1] + 1], "knight at", location
                if special != "smith":
                    self.resources["sheep"] -= 1
                    self.resources["ore"] -= 1
                self.knights_remaining[knight[1]] += 1
                knight[1] += 1
                self.knights_remaining[knight[1]] -= 1
                return "success"

    def move_knight_to(self, from_location, to_location, displaced=False):
        global status
        for p in players:
            print p.color, p.knights_built
        knight = [k for k in self.knights_built if k[0] == from_location][0]
        destinations = self.connected_unoccupied_corners(from_location, knight)
        if not destinations:
            if displaced:
                self.knights_built.remove(knight)
                self.knights_remaining[knight[1]] += 1
                status_label.config(text = self.color + " knight must be removed.")
            else:
                print "no places to move this knight"
                status_label.config(text = player.color + ", choose an action.")
            status = "player action"
        elif to_location in destinations:
            from_corner = [c for c in corners if c.location == from_location][0]
            if not displaced or displaced in [p.color for p in players]:
                from_corner.occupier = None
                from_corner.occ_type = ""
            else: status = "player action"
            to_corner = [c for c in corners if c.location == to_location][0]
            if to_corner.occupier:
                assert to_corner.occ_type == "knight" and to_corner.occupier != self.color
                status = "displace knight=" + str(to_location) + "=" + to_corner.occupier
            to_corner.occupier = self.color
            to_corner.occ_type = "knight"
            knight[0] = to_location
            if not displaced: knight[2] = 0
            overall_longest_road()
            if not status.startswith("displace knight"):
                status = "player action"
                status_label.config(text = player.color + ", choose an action.")
            if displaced in [p.color for p in players]: return "success"

    def move_knight_from(self, location, special=""):
        global status
        print "...in move_knight_from"
        for p in players:
            print p.color, p.knights_built
        if special: valid_locations = self.show_valid_locations('g')
        else: valid_locations = self.show_valid_locations('m')
        knight = [k for k in self.knights_built if k[0] == location]
        destinations = None
        if knight and ((knight[0][2] and not knight[0][3]) or special == "intrigue"):
            destinations = self.connected_unoccupied_corners(location, knight[0])
        if location in valid_locations:
            if not destinations:
                if not special:
                    status_label.config(text = "This knight cannot be moved.")
                    status = "player action"
                else:
                    status_label.config(text = "Knight must be removed.")
                    self.knights_built.remove(knight[0])
                    self.knights_remaining[knight[0][1]] += 1
                    corn = [c for c in corners if c.location == location][0]
                    corn.occupier = None
                    corn.occ_type = ""
                    status = "player action"
                    return "success"
            else:
                status = "move knight from=" + str(location) + "=" + self.color
                status_label.config(text = "Select a new location for this knight.")

##        this_knight = [k for k in self.knights_built if k[0] == location][0]
##        destinations = self.connected_unoccupied_corners(location, this_knight)
##        choice = raw_input("Where do you want to move this knight? " + str(destinations) + " ")
##        while not choice.isdigit() or int(choice) not in destinations:
##            if not choice: return
##            print "Invalid entry. Please choose a location from the choices provided."
##            choice = raw_input("Where do you want to move this knight? " + str(destinations) + " ")
##        this_corner = [c for c in corners if c.location == location][0]
##        this_corner.occupier = None
##        this_corner.occ_type = ""
##        destination = [c for c in corners if c.location == choice][0]
##        if destination.occupier:
##            assert destination.occ_type == "knight" and destination.occupier != self.color
##            occupier = [p for p in players if p.color == destination.occupier][0]
##            occupier.displace_knight(choice)
##        assert not destination.occupier and not destination.occ_type
##        destination.occupier = self.color
##        destination.occ_type = "knight"
##        this_knight[0] = choice
##        this_knight[2] = 0
##        overall_longest_road()

    def drive_away_robber(self, location, valid_locations):
        assert location in valid_locations
        knight = [k for k in self.knights_built if k[0] == location]
        knight[2] = 0
        move_robber(self)

    def rob(self, hexe, special=False):
        global status
        touchers = [p for p in players if p.is_touching_hex(hexe) and p != self]
        if not touchers:
            status_label.config(text = "No opponents touching this hex")
        elif len(touchers) == 1:
            status_label.config(text = self.steal_random_resource(touchers[0]))
        elif special == "bishop":
            message = ""
            for (i,p) in enumerate(touchers):
                message += self.steal_random_resource(p)
                if i < len(touchers) - 1: message += "\n"
            self.discard_progress_card("Bishop")
            status_label.config(text = message)
        else:
            self.choose_player_to_rob(touchers)
        status = "player action"

    def steal_random_resource(self, other, set_label = False):
        card_list = other.card_list()
        if card_list:
            choice = random.choice(card_list)
            other.resources[choice] -= 1
            self.resources[choice] += 1
            message = self.color + " steals " + choice + " from " + other.color
        else:
            message = other.color + " has no resources to steal."
            status_label.config(text = other.color + " has no resources to steal.")
        if set_label: status_label.config(text = message)
        if self.pop_up: self.pop_up.destroy()
        return message

    def choose_player_to_rob(self, touchers):
        self.pop_up = Toplevel(root, height = POP_UP_HEIGHT, width = POP_UP_WIDTH)
        self.pop_up.title("choose a player to rob.")
        var = StringVar()
        for p in touchers:
            Radiobutton(self.pop_up, text = p.color + ' (' + str(len(p.card_list())) + ' cards)', variable = var, value = p.name,
                        command = lambda: self.steal_random_resource([p for p in players if p.name == var.get()][0], True)).pack()
            
##        Button(self.pop_up, text = "ROB SELECTED PLAYER", width = BUTTON_WIDTH, command = lambda: self.steal_random_resource(choice, True)).pack()
##        
##        var = StringVar()
##        for c in opponent_progress_cards:
##            Radiobutton(self.pop_up, text = c.name, variable = var, value = c.name, command = lambda: self.steal_progress_card(opponent, var.get())).pack()

    def displace_knight(self, location):
        # No longer needed
        print self.color + ", you must move the knight at location", location, "to a different spot."
        displaced_knight = [knight for knight in self.knights_built if knight[0] == location][0]
        possibilities = self.connected_unoccupied_corners(location, displaced_knight)
        this_corner = [corner for corner in corners if corner.location == location][0]
        this_corner.occupier = None
        this_corner.occ_type = ""
        if not possibilities:
            print "There are no unoccupied corners connected to this road, so you must destroy this knight."
            self.knights_built.remove(displaced_knight)
        else:
            choice = raw_input("Where do you want to move this knight to? " + str(possibilities) + " ")
            while not choice.isdigit() or int(choice) not in possibilities:
                print "Invalid entry. Please choose from the options provided."
                choice = raw_input("Where do you want to move this knight to? " + str(possibilities) + " ")
            print "Moving knight from", location, "to", choice
            displaced_knight[0] = int(choice)
            new_corner = [corner for corner in corners if corner.location == int(choice)][0]
            if new_corner.occupier and new_corner.occ_type == "knight" and new_corner.occupier != self.color:
                new_displacer = [p for p in players if p.color == new_corner.occupier][0]
                new_displacer.displace_knight(int(choice))
            new_corner.occupier = self.color
            new_corner.occ_type = "knight"
        overall_longest_road()
        

    def make_knights_actionable(self):
        for knight in self.knights_built:
            knight[3] = 0

    def desert_opponent(self, opponent_color):
        opponent = [p for p in players if p.color == opponent_color][0]
        opponent.choose_deserter()

    def choose_deserter(self):
        global status
        print self.color + " choose a knight to desert"
        status = self.color + " choose deserter"
        status_label.config(text = self.color + ", choose a knight to desert.")

        # Original non-GUI version
##        print self.color + "'s knights:", self.knights_built
##        choices = [knight[0] for knight in self.knights_built]
##        choice = raw_input(self.color + ", choose the knight you want to desert: " + str(choices))
##        while not choice.isdigit() or int(choice) not in choices:
##            print "Invalid entry. Please choose from the options provided."
##            choice = raw_input(self.color + ", choose the knight you want to desert: " + str(choices))
##        chosen_knight = [knight for knight in self.knights_built if knight[0] == int(choice)][0]
##        if chosen_knight[2]: state = "active"
##        else: state = "inactive"
##        print self.color, "is removing an", state, knight_types[chosen_knight[1]], "knight from location", int(choice)
##        self.knights_built.remove(chosen_knight)
##        for corner in corners:
##            if corner.location == int(choice):
##                corner.occupier = None
##                corner.occ_type = ""
##        overall_longest_road()
##        return chosen_knight[1:]

    def desert_knight_at_corner(self, corner, opponent):
        global status
        print "deserting knight at corner " + str(corner.location)
        deserted_knight = [k for k in self.knights_built if k[0] == corner.location][0]
        self.knights_built.remove(deserted_knight)
        self.knights_remaining[deserted_knight[1]] += 1
        corner.occupier = None
        corner.occ_type = ""
        if opponent.knights_remaining[k[1]]:
            status = "progress place knight " + str(k[1:])
            print status
            status_label.config(text = opponent.color + ", place your knight.")
        else:
            status = "player action"
            status_label.config(text = player.color + ", choose an action.")
        overall_longest_road()

    def display_status(self, detailed=False):
        if not detailed:
            print self.color + ":", self.victory_points
        elif detailed == "personal":
            output = "\npoints: " + str(self.victory_points) + "\tknights: " + str(len(self.knights_built)) + "(" + str(self.active_knights()) + ")"
            output += "\tcities: " + str(len([c for p in players for c in p.cities_built])) + "("
            output += str(sum([p.active_knights() for p in players])) + ")\tbarbs: " + str(barbs)
            print output
            print "technology:\t", self.technology
            print "progress:\t", [p.name for p in self.progress_cards]
            print len(self.card_list()), "cards:\t", self.card_list()
        else:
            print "\nname: ", self.color
            print "victory points: ", self.victory_points
            print "settlements: ", self.settlements_built
            print "cities: ", self.cities_built
            print "roads: ", self.roads_built
            print "knights: ", self.knights_built
            print "active: ", self.active_knights()
            print "barbarian distance: ", barbs
            if count_active_knights() >= count_cities():
                defender_list = get_defender_list()
                if self in defender_list:
                    if len(defender_list) == 1:
                        print "Catan is safe from the barbarians, and you have the largest army."
                    else:
                        print "Catan is safe from the barbarians, and you are tied for the largest army."
                else:
                    print "Catan is safe from the barbarians, but you do not have the largest army."
            else:
                loser_list = get_loser_list()
                if self in loser_list:
                    if self.cities_built:
                        print "You will lose a city when the barbarians attack! You need more active knights."
                    else:
                        print "Catan is in danger from the barbarians, but you have no unprotected cities to lose."
                else:
                    print "Catan is in danger from the barbarians, but you are protected."
            print "corners touched:", list(self.corners_touched)
            print "technology:", self.technology
            print "Hexes touched:", {resource: self.get_touching_hexes(resource) for resource in resources}
            #for resource in self.resources:
                #print resource, self.resources[resource]

    def show_valid_locations(self, build_code, intro="", display=True):
        valid_locations = []
        if build_code == 'i':
            valid_locations = set([corner.location for corner in corners if two_spaces_away(corner)])
        if build_code == 'b':
            valid_locations = set([corner.location for corner in corners if corner.location
                               in self.corners_touched and not corner.occupier])
        elif build_code == 'u':
            valid_locations = set([knight[0] for knight in self.knights_built if
                               (self.technology["coin"] > 3 and knight[1] < 2) or knight[1] < 1])
        elif build_code == 'a':
            valid_locations = set([knight[0] for knight in self.knights_built if not knight[2]])
        elif build_code == 'd':
            valid_locations = set([k[0] for hexe in hexes if hexe.blocked for corner in hexe.corners
                               for k in self.knights_built if k[0] == corner and k[2]])
        elif build_code == 'm':
            valid_locations = set([k[0] for k in self.knights_built if k[2] and
                                   self.connected_unoccupied_corners(k[0], k)])
        elif build_code == 'g':
            valid_locations = set([k[0] for k in self.knights_built])
        elif build_code == 's':
            valid_locations = set([corner.location for corner in corners if corner.location
                               in self.corners_touched and two_spaces_away(corner) and not corner.occupier])
        elif build_code == 'c':
            valid_locations = self.settlements_built
        elif build_code == 'r':
            valid_locations = set([edge.location for edge in edges if not edge.occupier
                                   for corner in edge.corners if corner in self.corners_touched
                                   for corn in corners if corn.occupier in [self.color, None] and corn.location == corner])
        elif build_code == 'rc':
            valid_locations = set([edge.location for edge in edges for corner in edge.corners
                                   if corner in [city[0] for city in self.cities_built]])
        elif build_code == 'w':
            valid_locations = set([city[0] for city in self.cities_built if not city[1]])
        if display:
            print intro, list(valid_locations)
        return valid_locations
                    

    def do(self, action, special=False):
        # No longer needed
        outcome = ''
        if action in ['s', 'c', 'r', 'k', 'w']:
            secondary = 'q'
            if action == 'k':
                while secondary and secondary not in ['b', 'a', 'u', 'm', 'd']:
                    secondary = raw_input("(b)uild, (a)ctivate, (u)pgrade, (m)ove, or (d)rive away robber? ")
                    if secondary not in ['b', 'a', 'u', 'm', 'd']:
                        print "Invalid entry. Choose 'b', 'a', 'u', 'm', 'd' or press Enter to escape. "
                    else:
                        print "Existing knights:", self.knights_built
                        valid_locations = self.show_valid_locations(secondary, "You can perform this action at locations")
            else: self.show_valid_locations(action, "You can perform this action at locations")
            location = raw_input("Where do you want to perform this action? ")
            if not location.isdigit(): return
            else: location = int(location)
            if action == 's': self.build_settlement(location)
            elif action == 'c': return self.build_city(location, special)
            elif action == 'r': self.build_road(location, special)
            elif action == 'w': return self.build_wall(location, special)
            elif secondary == 'b': self.build_knight(location)
            elif secondary == 'a': self.activate_knight(location)
            elif secondary == 'u': self.upgrade_knight(location)
            elif secondary == 'm': self.move_knight(location, valid_locations)
            elif secondary == 'd': self.drive_away_robber(location, valid_locations)
        elif action == 'b': self.bank_trade()
        elif action == 'o': self.offer_trade()
        elif action == 'u': return self.upgrade_city(special)
        elif action == 'p':
            secondary = 'q'
            if len(self.progress_cards) > 4:
                while secondary and secondary not in ['p', 'd']:
                    secondary = raw_input("(d)iscard or (p)lay a progress card? ")
            if secondary == 'p' or len(self.progress_cards) < 5:
                self.play_progress_card()
            else: self.discard_progress_card()
        elif action == 'v':
            self.display_status(True)
        elif action == "add":
            resource = raw_input("which resource? ")
            while resource not in self.resources:
                if not resource: return
                print "Invalid entry. Must be a resource in", self.resources.keys()
                resource = raw_input("which resource? ")
            amount = raw_input("how many? ")
            while not amount.isdigit():
                if not amount: return
                print "Invalid entry. Must be a positive integer."
                amount = raw_input("how many? ")
            self.resources[resource] += int(amount)

    def count_resources(self):
        return sum([self.resources[resource] for resource in self.resources])

    def hand_limit(self):
        return 7 + 2 * len([city for city in self.cities_built if city[1]])

    def give_wedding(self, opponent):
        self.pop_up = Toplevel(root, height = HEIGHT, width = WIDTH)
        self.pop_up.title("Wedding")
        Label(self.pop_up, text = self.color + ", give two cards to " + opponent.color).pack()
        #self.discard_canvas = Canvas(self.pop_up, height = HEIGHT, width = WIDTH)
        card_list = self.card_list()
        listbox = Listbox(self.pop_up, selectmode=MULTIPLE)
        listbox.pack()
        for c in card_list:
            listbox.insert(END, c)
            print c
        Button(self.pop_up, text = "GIVE SELECTED CARDS", width = BUTTON_WIDTH,
               command = lambda: self.give_wedding_cards(map(int, listbox.curselection()), opponent)).pack()

    def give_wedding_cards(self, list_of_cards, opponent, wedding = True):
        global status
        card_list = self.card_list()
        if (wedding and len(list_of_cards) < len(card_list) and len(list_of_cards) != 2) or len(list_of_cards) > 2:
            return
        for c in list_of_cards:
            self.resources[card_list[c]] -= 1
            opponent.resources[card_list[c]] += 1
        self.pop_up.destroy()
        redraw()
        self.pop_up = None
        players_remaining = [p for p in players if p.pop_up is not None]
        if not players_remaining:
            status = "player action"
            status_label.config(text = player.color + ", choose an action.")

    def discard(self, list_of_cards, saboteur = False):
        global status
        card_list = self.card_list()
        if len(card_list) / 2 != len(list_of_cards):
            return
        for c in list_of_cards:
            self.resources[card_list[c]] -= 1
        self.pop_up.destroy()
        self.pop_up = None
        players_remaining = [p for p in players if p.pop_up is not None]
        if not players_remaining:
            if barbs_have_attacked and not saboteur:
                status = "move robber"
                status_label.config(text = player.color + ", move the robber.")
                move_robber()
            else:
                status = "player action"
                status_label.config(text = player.color + ", choose an action.")
        redraw()

    def spy_opponent(self, opponent_color):
        opponent = [p for p in players if p.color == opponent_color][0]
        opponent_progress_cards = opponent.progress_cards
        if len(opponent_progress_cards) > 0:
            self.pop_up = Toplevel(root, height = HEIGHT, width = WIDTH)
            self.pop_up.title(opponent_color + "'s progress cards")
            Label(self.pop_up, text = self.color + ", choose a progress card to steal").pack()
##            listbox = Listbox(self.pop_up, selectmode=MULTIPLE)
##            listbox.pack()
            var = StringVar()
            for c in opponent_progress_cards:
                Radiobutton(self.pop_up, text = c.name, variable = var, value = c.name, command = lambda: self.steal_progress_card(opponent, var.get())).pack()

    def steal_progress_card(self, opponent, card_name):
        global status
        print self.color + " is stealing a " + card_name + " card from " + opponent.color
        card = [p for p in opponent.progress_cards if p.name == card_name][0]
        opponent.progress_cards.remove(card)
        self.progress_cards.append(card)
        self.discard_progress_card("Spy")
        redraw()
        status_label.config(text = player.color + ", choose an action.")
        status = "player action"
        print type(self.pop_up)
        if self.pop_up is not None:
            print "self.pop_up is not None"
            self.pop_up.destroy()
            self.pop_up = None

    def harborize_opponent(self, opponent_color):
        global status
        opponent = [p for p in players if p.color == opponent_color][0]
        opponent_commodities = [c for c in opponent.card_list() if c in ["paper", "coin", "cloth"]]
        if not opponent_commodities:
            print opponent_color + " has no commodities."
            status_label.config(text = opponent_color + " has no commodities")
            status += "=" + opponent_color
            checked = status.split("=")[1:]
            if len(checked) >= len(players) - 1:
                self.discard_progress_card("Commercial Harbor")
                status = "player action"
                status_label.config(text = player.color + ", choose an action.")
            redraw()
        else:
            my_resources = [c for c in self.card_list() if c not in ["paper", "coin", "cloth"]]
            self.pop_up = Toplevel(root, height = HEIGHT, width = WIDTH)
            self.pop_up.title("Commercial Harbor")
            Label(self.pop_up, text = self.color + ", you must offer a resource to " + opponent_color).pack()
            var = StringVar()
            for c in my_resources:
                Radiobutton(self.pop_up, text = c, variable = var, value = c, command = lambda: self.harbor_give_resource(opponent, var.get())).pack()

    def harbor_give_resource(self, opponent, resource):
        print self.color + " is giving a " + resource + " to " + opponent.color
        self.resources[resource] -= 1
        opponent.resources[resource] += 1
        self.pop_up.destroy()
        redraw()
        self.pop_up = None
        opponent.harbor_choose_commodity(self)

    def harbor_choose_commodity(self, opponent):
        my_commodities = [c for c in self.card_list() if c in ["paper", "coin", "cloth"]]
        self.pop_up = Toplevel(root, height = HEIGHT, width = WIDTH)
        self.pop_up.title("Commercial Harbor")
        Label(self.pop_up, text = self.color + ", you must give a commodity to " + opponent.color).pack()
        var = StringVar()
        for c in my_commodities:
            Radiobutton(self.pop_up, text = c, variable = var, value = c, command = lambda: self.harbor_give_commodity(opponent, var.get())).pack()

    def harbor_give_commodity(self, opponent, commodity):
        global status
        print self.color + " is giving a " + commodity + " to " + opponent.color
        self.resources[commodity] -= 1
        opponent.resources[commodity] += 1
        self.pop_up.destroy()
        self.pop_up = None
        status += "=" + self.color
        checked = status.split("=")[1:]
        if len(checked) >= len(players) - 1:
            opponent.discard_progress_card("Commercial Harbor")
            status = "player action"
            status_label.config(text = player.color + ", choose an action.")
        redraw()

    def master_merchant(self, opponent_color):
        opponent = [p for p in players if p.color == opponent_color][0]
        opponent_cards = opponent.card_list()
        if not opponent_cards:
            status_label.config(text = opponent_color + " has no cards.")
            return
        self.pop_up = Toplevel(root, height = HEIGHT, width = WIDTH)
        self.pop_up.title("Master Merchant")
        Label(self.pop_up, text = self.color + ", take two cards from " + opponent_color).pack()
        listbox = Listbox(self.pop_up, selectmode=MULTIPLE)
        listbox.pack()
        for c in opponent_cards:
            listbox.insert(END, c)
        Button(self.pop_up, text = "STEAL SELECTED CARDS", width = BUTTON_WIDTH,
               command = lambda: self.master_merchant_steal(map(int, listbox.curselection()), opponent)).pack()

    def master_merchant_steal(self, list_of_cards, opponent):
        global status
        card_list = opponent.card_list()
        if (len(list_of_cards) < len(card_list) and len(list_of_cards) != 2) or len(list_of_cards) > 2:
            return
        for c in list_of_cards:
            self.resources[card_list[c]] += 1
            opponent.resources[card_list[c]] -= 1
        self.pop_up.destroy()
        redraw()
        self.pop_up = None
        status = "player action"
        status_label.config(text = player.color + ", choose an action.")
        self.discard_progress_card("Master Merchant")
        
    def merchant_fleet_choose(self):
        self.pop_up = Toplevel(root, height = HEIGHT, width = WIDTH)
        self.pop_up.title("Merchant Fleet")
        Label(self.pop_up, text = self.color + ", choose a resource or commodity\nto trade at the 2:1 rate this turn").pack()
        var = StringVar()
        for card in resources_commodities:
            Radiobutton(self.pop_up, text = card, variable = var, value = card, command = lambda: self.merchant_fleet_execute(var.get())).pack()

    def merchant_fleet_execute(self, resource):
        global status
        self.temp_two_for_one.append(resource)
        print self.color + " can now trade " + resource + " at the 2:1 rate for the rest of this turn."
        self.discard_progress_card("Merchant Fleet")
        self.pop_up.destroy()
        self.pop_up = None
        status = "player action"
        status_label.config(text = player.color + ", choose an action.")
        redraw()

    def monopoly_choose(self, type_of_monopoly):
        self.pop_up = Toplevel(root, height = HEIGHT, width = WIDTH)
        Label(self.pop_up, text = self.color + ", choose a " + type_of_monopoly + " to monopolize.").pack()
        if type_of_monopoly == "resource":
            self.pop_up.title("Resource Monopoly")
            choices = resources
            quantity = 2
        else:
            self.pop_up.title("Trade Monopoly")
            choices = commodities
            quantity = 1
        var = StringVar()
        for card in choices:
            Radiobutton(self.pop_up, text = card, variable = var, value = card, command = lambda: self.monopoly_execute(var.get(), quantity)).pack()

    def monopoly_execute(self, resource, quantity):
        global status
        opponents = [p for p in players if p is not self]
        for opp in opponents:
            for index in range(quantity):
                if opp.resources[resource] > 0:
                    opp.resources[resource] -= 1
                    self.resources[resource] += 1
                    redraw()
        if quantity == 2: self.discard_progress_card("Resource Monopoly")
        else: self.discard_progress_card("Trade Monopoly")
        if self.pop_up is not None:
            self.pop_up.destroy()
            self.pop_up = None
        status = "player action"
        status_label.config(text = player.color + ", choose an action.")
        redraw()

    def place_merchant(self, hexe):
        global status
        loser = [p for p in players if p.merchant]
        for hexagon in hexes:
            if hexagon.merchant: hexagon.merchant = None
        if loser:
            loser = loser[0]
            print loser.color, "loses the merchant and loses a victory point."
            loser.victory_points -= 1
            loser.merchant = ""
        print self.color + " is placing the merchant on " + hexe.resource + " and gains a victory point."
        self.merchant = hexe.resource
        self.victory_points += 1
        hexe.merchant = self.color
        self.discard_progress_card("Merchant")
        status = "player action"
        status_label.config(text = player.color + ", choose an action.")

    def discard_half(self, saboteur = False):
        status_label.config(text = "players must discard")
        discard_amount = self.count_resources() / 2
        if discard_amount > 0:
            self.pop_up = Toplevel(root, height = HEIGHT, width = WIDTH)
            self.pop_up.title("Pay The Robber")
            Label(self.pop_up, text = self.color + ", choose " + str(discard_amount) + " cards to discard").pack()
            #self.discard_canvas = Canvas(self.pop_up, height = HEIGHT, width = WIDTH)
            card_list = self.card_list()
            listbox = Listbox(self.pop_up, selectmode=MULTIPLE)
            listbox.pack()
            for c in card_list:
                listbox.insert(END, c)
                print c
            Button(self.pop_up, text = "DISCARD SELECTED CARDS", width = BUTTON_WIDTH,
                   command = lambda: self.discard(map(int, listbox.curselection()), saboteur)).pack()
               
##        for c in range(len(card_list)):
##            card = Card(c, card_list[c])
##            card.draw(self.discard_canvas)
##        print self.color + ", you must discard", discard_amount, "cards from your hand."
##        for n in range(discard_amount):
##            resource = raw_input(self.color + ", type a resource you wish to discard: " + str(self.card_list()) + " ")
##            while not resource in self.resources or not self.resources[resource]:
##                print "Sorry, but you don't have any " + resource + " to discard."
##                resource = raw_input(self.color + ", type a resource you wish to discard: " + str(self.card_list()) + " ")
##            self.resources[resource] -= 1

    def card_list(self):
        return [resource for resource in self.resources for n in range(self.resources[resource])]

    def active_knights(self):
        return sum([knight[1] + 1 for knight in self.knights_built if knight[2]])

    def is_defender(self):
        print "Congratulations, " + self.color + "! You get a victory point for defending Catan!"
        self.victory_points += 1

    def draw_progress_card(self, col, p):
        print self.color, "gets a", col, "progress card."
        if self.pop_up is not None:
            self.pop_up.destroy()
            self.pop_up = None
        card = progress[col].pop(0)
        self.progress_cards.append(card)
        if isinstance(card, VictoryPoint): card.execute(self)
        if len(self.progress_cards) > 4 and p: self.discard_progress_card_choose()

    def choose_progress_card(self, p):
        self.pop_up = Toplevel(root, height = HEIGHT, width = WIDTH)
        self.pop_up.title("Co-defender of Catan")
        Label(self.pop_up, text = self.color + ", which color progress card do you want?").pack()
        var = StringVar()
        choices = ["blue", "green", "yellow"]
        for color in choices:
            Radiobutton(self.pop_up, text = color, variable = var, value = color, command = lambda: self.draw_progress_card(var.get(), p)).pack()

        # Original non-GUI version:
##        choice = raw_input(self.color + ", what color progress card do you want? (blue, green, or yellow) ")
##        while choice not in ['blue', 'green', 'yellow']:
##            print "Invalid entry. Must be blue, green, or yellow."
##        card = progress[choice].pop(0)
##        self.progress_cards.append(card)
##        if isinstance(card, VictoryPoint): card.execute(self)
##        if len(self.progress_cards) > 4 and p: self.discard_progress_card()

    def play_progress_card(self):
        # No longer needed
        print "Your progress cards:", [(p.ID, p.name) for p in self.progress_cards]
        choice = raw_input("Enter the ID # of the progress card you wish to play. ")
        while not choice.isdigit() or choice not in [str(p.ID) for p in self.progress_cards]:
            if not choice: return
            print "Invalid Entry. Must be an ID number in your list of progress cards."
            choice = raw_input("Enter the ID # of the progress card you wish to discard. ")
        card = [p for p in self.progress_cards if str(p.ID) == choice][0]
        card.execute(self)

    def discard_progress_card_choose(self):
        print self.color + " has too many progress cards."
        self.pop_up = Toplevel(root, height = HEIGHT, width = WIDTH)
        self.pop_up.title("Discard Progress Card")
        Label(self.pop_up, text = self.color + ", select a progress card to discard").pack()
        var = StringVar()
        choices = [p.name for p in self.progress_cards]
        for card in choices:
            Radiobutton(self.pop_up, text = card, variable = var, value = card, command = lambda: self.discard_progress_card(var.get())).pack()
            
    def discard_progress_card(self, card):
        discarded_card = [p for p in self.progress_cards if p.name == card][0]
        progress[discarded_card.color].append(discarded_card)
        self.progress_cards = [p for p in self.progress_cards if p != discarded_card]
        if self.pop_up is not None:
            self.pop_up.destroy()
            self.pop_up = None

    def downgrade_city(self, location):
        # fixed for GUI
        global status, loser_list
        if location not in [city[0] for city in self.cities_built if not city[2]]:
            print "Invalid location. Must destroy a city that doesn't have a metropolis."
            return
        for city in self.cities_built:
            if city[0] == location:
                print self.color, "is destroying the city at location", location
                self.cities_built.remove(city)
                self.settlements_built.append(location)
                self.cities_remaining += 1
                self.settlements_remaining -= 1
                self.victory_points -= 1
                corner = [c for c in corners if c.location == location][0]
                corner.occ_type = "settlement"
                loser_list.remove(self)
                if loser_list:
                    status = "downgrade=" + loser_list[0].color
                    status_label.config(text = loser_list[0].color + ", click a city to downgrade.")
                else:
                    deactivate_knights()
                    settle_roll([dice[0], [None, dice[1][1]]])
                return "success"

        # Original non-GUI version:
##        choices = [city[0] for city in self.cities_built if not city[2]]
##        if choices:
##            choice = raw_input(self.color + ", choose a city to destroy: " + str(choices) + " ")
##            while not choice.isdigit() or int(choice) not in choices:
##                print "Invalid entry. Must choose from the options given."
##                choice = raw_input(self.color + ", choose a city to destroy: " + str(choices) + " ")
##            self.cities_built = [city for city in self.cities_built if city[0] != int(choice)]
##            corner = [c for c in corners if c.location == int(choice)][0]
##            corner.occ_type = "settlement"
##            self.settlements_built.append(int(choice))
##            self.victory_points -= 1

    def choose_resource(self):
        # fixed for GUI
        print self.color + ", choose a resource."
        self.pop_up = Toplevel(root, height = HEIGHT, width = WIDTH)
        self.pop_up.title("Aqueduct")
        Label(self.pop_up, text = self.color + ", select a resource").pack()
        var = StringVar()
        for card in resources:
            Radiobutton(self.pop_up, text = card, variable = var, value = card, command = lambda: self.choose_resource_execute(var.get())).pack()

        # Original non-GUI version:
##        choice = raw_input(self.color + ", select a free resource. (wheat, wood, sheep, ore, brick) ")
##        while choice not in ['wheat', 'wood', 'sheep', 'ore', 'brick']:
##            print "Invalid entry. Please choose from the options provided."
##            choice = raw_input(self.color + ", select a free resource. (wheat, wood, sheep, ore, brick) ")
##        self.resources[choice] += 1

    def choose_resource_execute(self, resource):
        print self.color + " chooses " + resource
        self.resources[resource] += 1
        if self.pop_up is not None:
            self.pop_up.destroy()
            self.pop_up = None
        redraw()

    def bank_trade(self):
        # Needs fixed for GUI
        giving = raw_input("which resource do you want to trade in? " + str(self.card_list()) + " ")
        if giving in self.two_for_one + [self.merchant] + self.temp_two_for_one: needed = 2
        elif self.three_for_one: needed = 3
        else: needed = 4
        while giving not in self.resources or self.resources[giving] < needed:
            if not giving: return
            print giving, "trades at the", needed, "for 1 rate. You don't have enough."
            giving = raw_input("which resource do you want to trade in? " + str(self.card_list()) + " ")
            if giving in self.two_for_one: needed = 2
            elif self.three_for_one: needed = 3
            else: needed = 4
        print giving, "trades at the", needed, "for 1 rate."
        getting = raw_input("which resource do you want in return? " + str([r for r in self.resources if r != giving]))
        while getting not in [r for r in self.resources if r != giving]:
            if not getting: return
            print "Invalid entry. You must choose from the options given."
            getting = raw_input("which resource do you want in return? " + str([r for r in self.resources if r != giving]))
        print "Trading in", needed, giving, "for 1", getting
        self.resources[giving] -= needed
        self.resources[getting] += 1

    def offer_trade(self):
        # Needs fixed for GUI
        choices = self.resources.keys()
        choice = raw_input(self.color + ", what resource do you want? " + str(choices) + " ")
        receiving = []
        if not choice: return
        while choice:
            while choice not in choices:
                if not choice:
                    choice = 'done'
                    break
                choice = raw_input(self.color + ", what other resource do you want? " + str(choices) + " ")
            if choice == 'done': break
            receiving.append(choice)
            choice = 'q'
        gives = self.card_list()
        give = raw_input(self.color + ", what are you willing to give? " + str(gives) + " ")
        giving = []
        if not give: return
        while give:
            while give not in gives:
                if not give:
                    give = 'done'
                    break
                give = raw_input(self.color + ", what else are you willing to give? " + str(gives) + " ")
            if give == 'done': break
            giving.append(give)
            gives.remove(give)
            give = 'q'
        opponents = [p.color for p in players if p != self]
        response = raw_input("If you wish to accept this trade or send a message, enter your name: " + str(opponents))
        outcome = False
        while not outcome:
            while response not in opponents:
                if not response:
                    print "Trade offer was rejected by all opponents"
                    return
                response = raw_input("If you wish to accept this trade or send a message, enter your name: " + str(opponents))
            responder = [p for p in players if p.color == response][0]
            outcome = responder.trade_response(self, giving, receiving)
            response = 'q'

    def trade_response(self, other, receiving, giving):
        # Needs fixed for GUI
        print other.color, "is offering", self.color, receiving, "for", giving
        print self.color + "'s resources:", self.card_list()
        response = raw_input(self.color + ", press 'y' to accept trade. Otherwise enter a response: ")
        if response == 'y':
            for resource in set(giving):
                if self.resources[resource] < giving.count(resource):
                    print self.color + ", you don't have enough", resource, "to make this trade."
                    return False
            print other.color, "is trading", receiving, "to", self.color, "for", giving
            for resource in receiving:
                self.resources[resource] += 1
                other.resources[resource] -= 1
            for resource in giving:
                self.resources[resource] -= 1
                other.resources[resource] += 1
            return True
        print self.color, "responds:", response
        return False
            

    def give_cards(self, amount, to_player, resource="", special=""):
        # Needs fixed for GUI
        if not resource:
            if special == "commodity":
                available = [c for c in self.card_list() if c in ["coin", "cloth", "paper"]]
            else: available = self.card_list()
            print self.color + "'s", special, "cards:", available
            for i in range(amount):
                if not available:
                    print self.color, "does not have any", special, "cards to give up."
                    return
                choice = raw_input(self.color + ", which " + special + " card do you want to give up? ")
                while choice not in available:
                    print "Invalid entry. Please enter a card from the list provided."
                    choice = raw_input(self.color + ", which " + special + " card do you want to give up? ")
                print self.color, "is giving a", special, "card to", to_player.color
                self.resources[choice] -= 1
                to_player.resources[choice] += 1
        elif self.resources[resource] < amount:
            print self.color + ", you don't have", amount, resource, "to give."
        else:
            print to_player.color, "gets", amount, resource, "from", self.color
            self.resources[resource] -= amount
            to_player.resources[resource] += amount

    def has_upgradeable_knights(self):
        upgradeable_knights = [k[0] for k in self.knights_built if k[1] < 1 or (k[1] < 2 and self.technology["coin"] > 3)]
        print upgradeable_knights
        return len(upgradeable_knights) > 0

    def is_touching_hex(self, hexe):
        hexes_touched = []
        corners_touched = self.settlements_built + [city[0] for city in self.cities_built]
        intersection = set(corners_touched) & set(hexe.corners)
        return len(intersection) > 0

    def get_touching_hexes(self, resource):
        hexes_touched = []
        corners_touched = self.settlements_built + [city[0] for city in self.cities_built]
        for hexe in hexes:
            if hexe.resource == resource:
                for corner in hexe.corners:
                    if corner in corners_touched:
                        hexes_touched.append(hexe)
        return len(set(hexes_touched))

    def get_resources_built_upon(self):
        corners_touched = self.settlements_built + [city[0] for city in self.cities_built]
        resources = set([hexe.resource for hexe in hexes for corner in hexe.corners if corner in corners_touched])
        return list(resources)

    def get_open_roads(self):
        corner_roads = [c for edge in edges if edge.occupier == self.color for c in edge.corners]
        open_roads = [e for e in edges if e.occupier == self.color for c in e.corners if corner_roads.count(c) == 1
                      for corner in corners if corner.location == c and not corner.occupier]
        return set(open_roads)

    def set_corners_touched(self):
        touched = self.settlements_built + [c[0] for c in self.cities_built] + [k[0] for k in self.knights_built]
        for e in edges:
            if e.occupier == self.color:
                for c in e.corners:
                    touched.append(c)
        self.corners_touched = set(touched)

    def connected_unoccupied_corners(self, location, knight):
        connected = self.get_connected_corners(location)
        connected_corners = [c for c in corners if c.location in connected]
        unoccupied = [c.location for c in connected_corners if (not c.occ_type or
                                                                (c.occ_type == "knight" and c.occupier != self.color and
                                                                 [k for p in players for k in p.knights_built if k[0] == c.location][0][1] < knight[1]))]
        return unoccupied

    def get_connected_corners(self, location, longest_road=False):
        connected = [location]
        visited = []
        found = True
        while found:
            found = False
            for edge in edges:
                if edge.occupier == self.color and edge not in visited:
                    if edge.corners[0] in connected and edge.corners[1] not in connected:
                        connected.append(edge.corners[1])
                        found = True
                        visited.append(edge)
                    elif edge.corners[1] in connected and edge.corners[0] not in connected:
                        connected.append(edge.corners[0])
                        found = True
                        visited.append(edge)
                    elif edge.corners[0] in connected and edge.corners[1] in connected:
                        visited.append(edge)
        if not longest_road: connected.remove(location)
        if not longest_road:
            print "Corners connected to location", location, "by", self.color + "'s roads:", str(connected)
            print "Roads used to connect these corners: ", [edge.location for edge in visited]
        if longest_road: return connected, visited
        else: return connected

    def longest_road1(self, detailed=False):
        my_edges = [edge for edge in edges if edge.occupier == self.color]
        paths = [set([edge]) for edge in my_edges]
        new_path = True
        while new_path:
            #print [[edge.location for edge in path] for path in paths]
            new_path = False
            updated_paths = []
            for path in paths:
                #print "checking path", [e.location for e in path]
                if len(path) == 1:
                    endpoints = [list(path)[0].corners[0], list(path)[0].corners[1]]
                else:
                    corner_list = [c for edge in path for c in edge.corners]
                    endpoints = [c for c in corner_list if corner_list.count(c) % 2 == 1]
                    if not endpoints: endpoints = corner_list
                    #start = [c for c in path[0].corners if c not in path[1].corners][0]
                    #finish = [c for c in path[-1].corners if c not in path[-2].corners][0]
                #print "endpoints:", endpoints
                unoccupied = [c.location for c in corners if c.location in endpoints and c.occupier in [None, self.color]]
                #print unoccupied
                for edge in my_edges:
                    #print "\tchecking edge", edge.location
                    #print "checking if edge", edge.location, "adds to path", [e.location for e in path]
                    #print [e.location for e in path], unoccupied, edge.corners, edge.location
                    for point in unoccupied:
                        if edge not in path and point in edge.corners:
                            newer_path = set([e for e in path] + [edge])
                            #print "\t\tyes"
                            if newer_path not in updated_paths:
                                #print "added", [e.location for e in newer_path], "to paths..."
                                updated_paths.append(newer_path)
                                new_path = True
                            #else: print [e.location for e in newer_path], "already exists in paths."
                        #else:
                            #print "\t\tno"
            if new_path: paths = [[edge for edge in path] for path in updated_paths]
        if detailed:
            print self.color
            for path in paths:
                print len(path), [edge.location for edge in path]
            print "longest road:", [edge.location for edge in max(paths, key=len)]
        return len(max(paths, key=len))

    def longest_road2(self, detailed):
        paths = []
        for start in self.corners_touched:
            connected, edge_list = self.get_connected_corners(start, True)
            for finish in connected:
                #print "checking from", start, "to", finish
                corners_visited = {start, finish}
                path = []
                added_corner = True
                while added_corner:
                    added_corner = False
                    for edge in edge_list:
                        found = False
                        #print "checking road at", edge.location
                        use_corners_visited = {c for c in corners_visited}
                        for corner in corners_visited:
                            #print "is", corner, "in", edge.corners, "?"
                            if corner in edge.corners and edge not in path:
                                path.append(edge)
                                for corn in edge.corners:
                                    has_knight = [c for c in corners if c.location == corn and c.occupier != self.color]
                                    if not has_knight:
                                        use_corners_visited |= set([corn])
                                        found = True
                    if found: added_corner = True
                if path not in paths: paths.append(path)
                print [edge.location for edge in path]
        if detailed:
            print "longest road:", [edge.location for edge in max(paths, key=len)], len(max(paths, key=len))
        return max(paths, key=len)

    def longest_road(self, detailed=False):
        # This one works:
        all_paths = []
        if len(self.roads_built) < 5: return len(self.roads_built)
        for start in self.corners_touched:
            connected, edge_list = self.get_connected_corners(start, True)
            path_queue = [[[], start]]
            max_path = []
            while path_queue:
                test_path = path_queue.pop(0)
                #if detailed: print "start:", start, "testing path", [e.location for e in test_path[0]], test_path[1]
                for edge in edge_list:
                    new_frontier = None
                    if edge not in test_path[0] and edge.corners[0] == test_path[1]:
                        new_frontier = edge.corners[1]
                    elif edge not in test_path[0] and edge.corners[1] == test_path[1]:
                        new_frontier = edge.corners[0]
                    if new_frontier is not None:
                        new_path = [test_path[0] + [edge], new_frontier]
                        corner = [c for c in corners if c.location == new_frontier][0]
                        #print corner.location, corner.occupier
                        if len(new_path[0]) > len(max_path):
                            max_path = [e for e in new_path[0]]
                            #print [e.location for e in new_path[0]], "is currently the longest road beginning at", start
                        if corner.occupier in [None, self.color]:
                            path_queue.append(new_path)
                            #print "adding path", [e.location for e in new_path[0]], "to the queue."
                        #else:
                            #print "path blocked by opponent."
            all_paths.append(max_path)
        longest = max(all_paths, key=len)
        if detailed: print "Longest Road:", len(longest), [e.location for e in longest]
        return len(longest)                       
                        
                    
        

def two_spaces_away(corner):
    for edge in edges:
        if corner.location in edge.corners:
            for corner2 in corners:
                if corner2.location in edge.corners:
                    if corner2.occ_type in ["settlement", "city"]:
                        return False
    return True

# 19 hexes
hexes = []

# 54 corners
corners = []

# 72 edges
edges = []

# Dictionary {hex: corners}
hex_corners = {0:[0,1,2,29,30,31], 1:[2,3,4,31,32,33], 2:[4,5,6,7,33,34],
               3:[7,8,9,34,35,36], 4:[9,10,11,12,36,37], 5:[12,13,14,37,38,39],
               6:[14,15,16,17,39,40], 7:[17,18,19,40,41,42], 8:[19,20,21,22,42,43],
               9:[22,23,24,43,44,45], 10:[24,25,26,27,45,46], 11:[27,28,29,30,46,47],
               12:[30,31,32,47,48,49], 13:[32,33,34,35,49,50], 14:[35,36,37,38,50,51],
               15:[38,39,40,41,51,52], 16:[41,42,43,44,52,53], 17:[44,45,46,47,48,53],
               18:[48,49,50,51,52,53]}

# Dictionary {corner: edges}
corner_edges = {0:[30,1], 1:[1,2], 2:[2,3,31], 3:[3,4], 4:[4,5,32], 5:[5,6], 6:[6,7],
                7:[7,8,33], 8:[8,9], 9:[9,10,34], 10:[10,11], 11:[11,12], 12:[12,13,35],
                13:[13,14], 14:[14,15,36], 15:[15,16], 16:[16,17], 17:[17,18,37], 18:[18,19],
                19:[19,20,38], 20:[20,21], 21:[21,22], 22:[22,23,39], 23:[23,24], 24:[24,25,40],
                25:[25,26], 26:[26,27], 27:[27,28,41], 28:[28,29], 29:[29,30,42], 30:[42,43,60],
                31:[43,44,31], 32:[44,45,61], 33:[45,46,32], 34:[46,47,33], 35:[47,48,62],
                36:[48,49,34], 37:[49,50,35], 38:[50,51,63], 39:[51,52,36], 40:[52,53,37],
                41:[53,54,64], 42:[54,55,38], 43:[55,56,39], 44:[56,57,65], 45:[57,58,40],
                46:[58,59,41], 47:[59,60,66], 48:[66,67,0], 49:[67,68,61], 50:[68,69,62],
                51:[69,70,63], 52:[70,71,64], 53:[71,0,65]}

corner_ports = [(2,3), (5,6), (8,9), (12,13), (15,16), (18,19), (22,23), (25,26), (28,29)]
port_types = ["sheep", "wood", "wheat", "brick", "ore"] + 4 * ["3:1"]

# Green Progress Card classes:

class RoadBuilding():
    def __init__(self, ID):
        self.ID = ID
        self.color = "green"
        self.name = "Road Building"
        self.description = "Build 2 roads for free anywhere adjacent to your existing structures."
        
    def execute(self, player):
        # fixed for GUI
        global status
        status = "progress place road 1"
        status_label.config(text = player.color + ", place your first road.")

        # The old version for non_GUI
##        for i in range(2):
##            player.do('r', "settlement")
##        player.progress_cards.remove(self)
##        progress[self.color].append(self)

class Alchemist():
    def __init__(self, ID):
        self.ID = ID
        self.color = "green"
        self.name = "Alchemist"
        self.description = "Instead of rolling, choose the results of both numbered dice, then roll the event die as normal."
        self.pop_up = None
        
    def execute(self):
        # fixed for GUI
        global status, red, yellow
        status = "progress alchemist"
        self.pop_up = Toplevel()
        self.pop_up.title(player.color + ", choose the numbers you want to roll.")
        Label(self.pop_up, text = "Select the number on the red die.").pack(anchor = W)
        red = IntVar()
        Radiobutton(self.pop_up, text="1", variable=red, value=1).pack(anchor=W)
        Radiobutton(self.pop_up, text="2", variable=red, value=2).pack(anchor=W)
        Radiobutton(self.pop_up, text="3", variable=red, value=3).pack(anchor=W)
        Radiobutton(self.pop_up, text="4", variable=red, value=4).pack(anchor=W)
        Radiobutton(self.pop_up, text="5", variable=red, value=5).pack(anchor=W)
        Radiobutton(self.pop_up, text="6", variable=red, value=6).pack(anchor=W)
        Label(self.pop_up, text = "Select the number on the yellow die.").pack(anchor = W)
        yellow = IntVar()
        Radiobutton(self.pop_up, text="1", variable=yellow, value=1).pack(anchor=W)
        Radiobutton(self.pop_up, text="2", variable=yellow, value=2).pack(anchor=W)
        Radiobutton(self.pop_up, text="3", variable=yellow, value=3).pack(anchor=W)
        Radiobutton(self.pop_up, text="4", variable=yellow, value=4).pack(anchor=W)
        Radiobutton(self.pop_up, text="5", variable=yellow, value=5).pack(anchor=W)
        Radiobutton(self.pop_up, text="6", variable=yellow, value=6).pack(anchor=W)
        Button(self.pop_up, text = "ROLL SELECTED NUMBERS", width = BUTTON_WIDTH, command = lambda: roll_dice(red.get(), yellow.get())).pack()
        
        # Original verstion for non-GUI
##        print player.color, "is playing the Alchemist card."
##        red = raw_input(player.color + ", enter a value for the red die (the event number): ")
##        while not red.isdigit() or int(red) not in range(1,7):
##            if not red: return
##            print "Invalid entry. Must be an integer between 1 and 6."
##            red = raw_input(player.color + ", enter a value for the red die (the event number): ")
##        yellow = raw_input(player.color + ", enter a value for the yellow die: ")
##        while not yellow.isdigit() or int(yellow) not in range(1,7):
##            if not yellow: return
##            print "Invalid entry. Must be an integer between 1 and 6."
##            yellow = raw_input(player.color + ", enter a value for the yellow die: ")
##        player.progress_cards.remove(self)
##        progress[self.color].append(self)
##        return red, yellow
            

class Crane():
    def __init__(self, ID):
        self.ID = ID
        self.color = "green"
        self.name = "Crane"
        self.description = "A city upgrade costs one less commodity."
        
    def execute(self, player):
        # fixed for GUI
        global status
        if player.cities_built:
            status = "progress crane"
            status_label.config(text = "Click a technology to upgrade.")
        else:
            status = "player action"
            status_label.config(text = "Can't upgrade without cities.")

        # Original version for non-GUI:
##        print player.color, "is attempting to play the crane card."
##        outcome = player.do('u', 1)
##        if outcome == "success":
##            player.progress_cards.remove(self)
##            progress[self.color].append(self)

class Engineer():
    def __init__(self, ID):
        self.ID = ID
        self.color = "green"
        self.name = "Engineer"
        self.description = "Build one city wall for free."
        
    def execute(self, player):
        # fixed for GUI
        global status
        status = "progress engineer"
        status_label.config(text = player.color + ", place your wall.")

        # Originial version for non-GUI
##        print player.color, "is playing the Engineer card."
##        outcome = player.do('w', 'engineer')
##        if outcome == "success":
##            player.progress_cards.remove(self)
##            progress[self.color].append(self)

class Inventor():
    def __init__(self, ID):
        self.ID = ID
        self.color = "green"
        self.name = "Inventor"
        self.description = "Swap any 2 number tokens on the board. The numbers may not be 2, 6, 8, or 12."
        
    def execute(self, player):
        # fixed for GUI
        global status, invent_hexes
        status = "progress inventor"
        status_label.config(text = player.color + ", select which tokens to swap.")
        invent_hexes = []

        # Original non-GUI version
##        print player.color, "is playing the Inventor card."
##        choice1 = raw_input("Enter the number of one of the hexes whose token you wish to swap: (0 - 18) ")
##        hex_choice1 = [hexe for hexe in hexes if str(hexe.location) == choice1 and hexe.number in [3,4,5,9,10,11]]
##        while len(hex_choice1) != 1:
##            if not choice1: return
##            print "Invalid entry. Please select a hexagon with a number token that is 3,4,5,9,10, or 11."
##            choice1 = raw_input("Enter the number of one of the hexes whose token you wish to swap: (0 - 18) ")
##            hex_choice1 = [hexe for hexe in hexes if str(hexe.location) == choice1 and hexe.number in [3,4,5,9,10,11]]
##        choice2 = raw_input("Enter the number of the other hex whose token you wish to swap: (0 - 18) ")
##        hex_choice2 = [hexe for hexe in hexes if str(hexe.location) == choice2 and hexe.number in [3,4,5,9,10,11] and hexe != hex_choice1[0]]
##        while not hex_choice2:
##            if not choice2: return
##            print "Invalid entry. Please select a different hexagon with a number token that is 3,4,5,9,10, or 11."
##            choice2 = raw_input("Enter the number of the other hex whose token you wish to swap: (0 - 18) ")
##            hex_choice2 = [hexe for hexe in hexes if str(hexe.location) == choice2 and hexe.number in [3,4,5,9,10,11] and hexe != hex_choice1[0]]
##        hex_choice1[0].number, hex_choice2[0].number = hex_choice2[0].number, hex_choice1[0].number
##        player.progress_cards.remove(self)
##        progress[self.color].append(self)

class PlusTwo():
    def __init__(self, ID, resource):
        self.ID = ID
        self.color = "green"
        self.resource = resource
        if resource == "wheat": self.name = "Irrigation"
        else: self.name = "Mining"
        self.description = "Get 2 " + resource + " for each " + resource + " hex on which you have built a settlement or city."
        
    def execute(self, player):
        # works in both GUI and non-GUI
        print player.color, "is playing the", self.name, "card..."
        added_amount = 2 * player.get_touching_hexes(self.resource)
        print player.color, "gains", added_amount, self.resource
        player.resources[self.resource] += added_amount
        player.progress_cards.remove(self)
        progress[self.color].append(self)

class Medicine():
    def __init__(self, ID):
        self.ID = ID
        self.color = "green"
        self.name = "Medicine"
        self.description = "Build a city with 2 ore and 1 wheat."
        
    def execute(self, player):
        global status
        # fixed for GUI
        if player.resources["ore"] < 2 or player.resources["wheat"] < 1:
            print "You don't have the resources to play this card."
            return
        status = "progress medicine"
        status_label.config(text = player.color + ", choose a settlement to citify.")

        # Original non-GUI version.
##        outcome = player.do('c', 'medicine')
##        if outcome == "success":
##            player.progress_cards.remove(self)
##            progress[self.color].append(self)

class VictoryPoint():
    def __init__(self, ID, color):
        self.ID = ID
        self.color = color
        if color == "green": self.name = "Printer"
        else: self.name = "Constitution"
        self.description = "you got the " + self.name + "! It is played immediately for 1 free victory point!"
        
    def execute(self, player):
        # fixed for GUI
        print player.color + ", " + self.description
        if self.name == "Printer":
            barbs_message.config(text = player.color + " got the " + self.name + " victory point.")
        else:
            defend_message.config(text = player.color + " got the " + self.name + " victory point.")
        player.victory_points += 1
        player.progress_cards.remove(self)

class Smith():
    def __init__(self, ID):
        self.ID = ID
        self.color = "green"
        self.name = "Smith"
        self.description = "Upgrade 2 of your knights for free. Rules about mighty knights still apply."
        
    def execute(self, player):
        # fixed for GUI
        global status
        if player.has_upgradeable_knights():
            status = "progress smith"
            status_label.config(text = "Choose a knight to upgrade.")
        else:
            status_label.config(text = "No upgradeable knights.")

        # Original non-GUI version:
##        print player.color, "is playing the Smith card."
##        choices = [k[0] for k in player.knights_built if k[1] < 1 or (k[1] < 2 and player.technology["coin"] > 3)]
##        choice1 = raw_input("Select a knight you wish to upgrade: " + str(choices) + " ")
##        while not choice1.isdigit() or int(choice1) not in choices:
##            if not choice1: return
##            print "Invalid entry. Please choose from the options given."
##            choice1 = raw_input("Select a knight you wish to upgrade: " + str(choices) + " ")
##        outcome1 = player.upgrade_knight(int(choice1), "smith")
##        if outcome1 != "success": return
##        choices.remove(int(choice1))
##        if not choices: print "You do not have any more upgradeable knights."
##        else:
##            choice2 = raw_input("Select another knight you wish to upgrade: " + str(choices) + " ")
##            while not choice2.isdigit() or int(choice2) not in choices:
##                if not choice2:
##                    print "You have chosen not to upgrade the second knight."
##                    break
##                print "Invalid entry. Please choose from the options given."
##                choice2 = raw_input("Select a knight you wish to upgrade: " + str(choices) + " ")
##            if choice2: player.upgrade_knight(int(choice2), "smith")
##        player.progress_cards.remove(self)
##        progress[self.color].append(self)
        
    
# Blue Progress Card classes:

class Bishop():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Bishop"
        self.color = "blue"
        self.description = "Move the robber to any hex. Steal a card from each player occupying that hex."
        
    def execute(self, player):
        # fixed for GUI
        move_robber("bishop")

        # Original non-GUI version:
##        print player.color, "is playing the Bishop card."
##        move_robber("bishop")
##        player.progress_cards.remove(self)
##        progress[self.color].append(self)

class Deserter():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Deserter"
        self.color = "blue"
        self.description = "Choose an opponent. That player must remove one of his knights. You may then place a knight of equal strength."
        
    def execute(self, player):
        # fixed for GUI
        global status
        status = "progress deserter"
        status_label.config(text = "Click a knight of player to desert.")

        # Original non-GUI version
##        print player.color, "is playing the Deserter card."
##        choices = [p.color for p in players if p != player and p.knights_built]
##        if not choices:
##            print "None of your opponents has any knights to steal."
##            return
##        choice = raw_input(player.color + ", select a player to use the Deserter card against: " + str(choices) + " ")
##        while choice not in choices:
##            if not choice: return
##            print "Invalid entry. Please choose from the options given."
##            choice = raw_input(player.color + ", select a player to use the Deserter card against: " + str(choices) + " ")
##        deserter = [p for p in players if p.color == choice][0]
##        deserter_choice = deserter.choose_deserter()
##        if not player.knights_remaining[deserter_choice[0]]:
##            print player.color, "does not have any", knight_types[deserter_choice[0]], "remaining."
##        else:
##            print player.color + "'s existing knights:", player.knights_built
##            choices = list(player.show_valid_locations('b', "You can place this knight at locations"))
##            placement = raw_input(player.color + ", enter a location for this knight: " + str(choices) + " ")
##            while not placement.isdigit() or int(placement) not in choices:
##                if not placement:
##                    print player.color, "has elected to not place this knight."
##                else:
##                    print "Invalid entry. Please choose from the options provided."
##                    placement = raw_input(player.color + ", enter a location for this knight: " + str(choices) + " ")
##            player.build_knight(placement, deserter_choice, "deserter")
##        player.progress_cards.remove(self)
##        progress[self.color].append(self)
        

class Diplomat():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Diplomat"
        self.color = "blue"
        self.description = "You may remove an open road. If it is your own road, you may place it somewhere else connected to you."
        
    def execute(self, player):
        # fixed for GUI
        global status
        status = "progress diplomat"
        status_label.config(text = "Select a road to remove.")

        # Original non-GUI version:
##        print player.color, "is playing the Diplomat card."
##        open_roads = set()
##        for p in players:
##            open_roads |= p.get_open_roads()
##        choice = raw_input(player.color + ", choose a road to remove: " + str(list(open_roads)))
##        while not choice.isdigit() or int(choice) not in open_roads:
##            if not choice: return
##            print "Invalid entry. Please choose from the options provided."
##            choice = raw_input(player.color + ", choose a road to remove: " + str(list(open_roads)))
##        if int(choice) in player.roads_built: add_on = True
##        else: add_on = False
##        for p in players:
##            if int(choice) in p.roads_built: p.remove_road(int(choice))
##        if add_on:
##            print player.color + ", since you removed your own road, you may place a new one."
##            player.do('r', 'settlement')
##        player.progress_cards.remove(self)
##        progress[self.color].append(self)

class Intrigue():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Intrigue"
        self.color = "blue"
        self.description = "You may displace an opponent's knight if it is touching your road."
        
    def execute(self, player):
        # fixed for GUI
        global status
        choices = [k[0] for p in players if p != player for k in p.knights_built if k[0] in player.corners_touched]
        if not choices:
            print "You can't play this card because there are no opponent knights touching any of your roads."
        else:
            status = "progress intrigue"
            status_label.config(text = "Click the knight you want to displace")

        # Original non-GUI version:
##        print player.color, "is playing the Intrigue card."
##        choices = [k[0] for p in players for k in p.knights_built if k[0] in player.corners_touched]
##        if not choices:
##            print "You can't play this card because there are no opponent knights touching any of your roads."
##            return
##        choice = raw_input(player.color + ", which knight would you like to displace? " + str(choices) + " ")
##        while not choice.isdigit() or int(choice) not in choices:
##            if not choice: return
##            print "Invalid entry. Please choose from the options provided."
##            choice = raw_input(player.color + ", which knight would you like to displace? " + str(choices) + " ")
##        displacer = [p for p in players for k in p.knights_built if k[0] == int(choice)][0]
##        displacer.displace_knight(int(choice))
##        player.progress_cards.remove(self)
##        progress[self.color].append(self)

class Saboteur():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Saboteur"
        self.color = "blue"
        self.description = "Each player who has as many or more victory points than you must discard half his hand."
        
    def execute(self, player):
        # fixed for GUI: def do_if_any(iterable, condition, do)
        found = False
        for p in players:
            if p.victory_points >= player.victory_points and p != player:
                found = True
                status = "discard"
                p.discard_half(True)
        if found: player.discard_progress_card("Saboteur")

        # Original non-GUI version:
##        print player.color, "is playing the Saboteur card."
##        losers = [p for p in players if p != player and p.victory_points >= player.victory_points]
##        if not losers:
##            print "You can't play this card because you have the most victory points."
##            return
##        for loser in losers:
##            loser.discard_half()
##        player.progress_cards.remove(self)
##        progress[self.color].append(self)

class Spy():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Spy"
        self.color = "blue"
        self.description = "Examine an opponent's hand of progress cards. You may choose one and add it to your hand."
        
    def execute(self, player):
        # fixed for GUI
        global status
        status = "progress spy"
        status_label.config(text = "Click a player's piece to spy them.")

        # Original non-GUI version:
##        print player.color, "is playing the Spy card."
##        choices = [p.color for p in players if p != player and p.progress_cards]
##        if not choices:
##            print "You can't play this card because none of your opponents has any progress cards to steal."
##            return
##        for p in players:
##            print p.color + "'s progress cards:", [prog.color for prog in p.progress_cards]
##        choice = raw_input(player.color + ", whose progress cards do you want to spy? " + str(choices) + " ")
##        while choice not in choices:
##            if not choice: return
##            print "Invalid entry. Please choose from the options provided."
##            choice = raw_input(player.color + ", whose progress cards do you want to spy? " + str(choices) + " ")
##        chosen_player = [p for p in players if p.color == choice][0]
##        print choice + "'s progress cards:", [(c.ID, c.name) for c in chosen_player.progress_cards]
##        card_choices = [c.ID for c in chosen_player.progress_cards]
##        card_choice = raw_input("Enter the ID of the card you wish to steal: " + str(card_choices) + " ")
##        while not card_choice.isdigit() or int(card_choice) not in card_choices:
##            print "Invalid entry. Please choose from the options provided."
##            card_choice = raw_input("Enter the ID of the card you wish to steal: " + str(card_choices) + " ")
##        stolen_card = [c for c in chosen_player.progress_cards if c.ID == int(card_choice)][0]
##        player.progress_cards.remove(self)
##        progress[self.color].append(self)
##        chosen_player.progress_cards.remove(stolen_card)
##        player.progress_cards.append(stolen_card)

class Warlord():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Warlord"
        self.color = "blue"
        self.description = "Activate all of your knights for free."
        
    def execute(self, player):
        # fixed for GUI
        print "Activating all of " + player.color + "'s knights."
        for knight in player.knights_built:
            knight[2] = 1
            knight[3] = 1
        player.progress_cards.remove(self)
        progress[self.color].append(self)

class Wedding():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Wedding"
        self.color = "blue"
        self.description = "Each player who has more victory points than you must give you two cards of his choice."
        
    def execute(self, player):
        # fixed for GUI:
        found = False
        for p in players:
            if p.victory_points > player.victory_points and p != player:
                found = True
                status = "wedding"
                status_label.config(text = player.color + " receives cards for wedding.")
                p.give_wedding(player)
        if found: player.discard_progress_card("Wedding")
        else: print "No one has more victory points than you."

        # Original non-GUI version:
##        print player.color, "is playing the Wedding card."
##        chosen_players = [p for p in players if p.victory_points > player.victory_points]
##        if not chosen_players:
##            print "You can't play this card because no one has more victory points than you."
##            return
##        for p in chosen_players:
##            print p.color, "must give 2 cards to", player.color
##            p.give_cards(2, player)
##        player.progress_cards.remove(self)
##        progress[self.color].append(self)

# Yellow Progress Card classes:

class CommercialHarbor():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Commercial Harbor"
        self.color = "yellow"
        self.description = "You may offer each player one resource in exchange for one commodity from his hand if he has any."
        
    def execute(self, player):
        # fixed for GUI
        global status
        choices = [c for c in player.card_list() if c not in ["coin", "paper", "cloth"]]
        if not choices:
            print player.color + ", you can't play the Commercial Harbor because you don't have any resources to give."
            return
        status_label.config(text = "choose an opponent to harborize")
        status = "progress harbor"

        # Original non-GUI version:
##        choices = [c for c in player.card_list() if c not in ["coin", "paper", "cloth"]]
##        if not choices:
##            print player.color + ", you can't play the Commercial Harbor because you don't have any resources to give."
##            return
##        print player.color, "is playing the Commercial Harbor."
##        opponents = [p for p in players if p != player]
##        opponent_colors = [p.color for p in players if p != player]
##        while choices and opponent_colors:
##            choice = raw_input("Choose an opponent to offer a resource to: " + str(opponent_colors))
##            while choice not in opponent_colors:
##                if not choice: choice = 'continue'
##                print "Invalid entry. Please choose from the options provided."
##                choice = raw_input("Choose an opponent to offer a resource to: " + str(opponent_colors))
##            if choice == 'continue': continue
##            chosen_player = [p for p in players if p.color == choice][0]
##            if chosen_player.resources["coin"] + chosen_player.resources["cloth"] + chosen_player.resources["paper"] == 0:
##                print chosen_player.color, "doesn't have any commodities to give."
##            else:
##                resource = raw_input("Choose a resource to offer " + chosen_player.color + ": " + str(choices) + " ")
##                while resource not in choices:
##                    print "Invalid entry. Please choose from the options provided."
##                    resource = raw_input("Choose a resource to offer " + chosen_player.color + ": " + str(choices) + " ")
##                chosen_player.resources[resource] += 1
##                chosen_player.give_cards(1, player, special="commodity")
##                choices.remove(resource)
##            opponent_colors.remove(choice)
##        player.progress_cards.remove(self)
##        progress[self.color].append(self)

class MasterMerchant():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Master Merchant"
        self.color = "yellow"
        self.description = "Choose a player who has more victory points than you. You may examine his hand of resources and commodities and take 2."
        
    def execute(self, player):
        # fixed for GUI
        global status
        choices = [p.color for p in players if p.victory_points > player.victory_points]
        if not choices:
            print "You can't play this card because no one has more victory points than you."
            return
        status_label.config(text = "choose an opponent to steal from")
        status = "progress master merchant"

        # Original non-GUI version:
##        print player.color, "is playing the Master Merchant card."
##        choices = [p.color for p in players if p.victory_points > player.victory_points]
##        if not choices:
##            print "You can't play this card because no one has more victory points than you."
##            return
##        print "card counts:", [(p.color, len(p.card_list())) for p in players]
##        choice = raw_input(player.color + ", choose a player to steal cards from: " + str(choices) + " ")
##        while choice not in choices:
##            if not choice: return
##            print "Invalid entry. Please choose from the options given."
##            choice = raw_input(player.color + ", choose a player to steal cards from: " + str(choices) + " ")
##        chosen_player = [p for p in players if p.color == choice][0]
##        for i in range(2):
##            if not chosen_player.card_list():
##                print chosen_player.color, "doesn't have any cards left."
##                break
##            card = raw_input("Choose a card from " + chosen_player.color + "'s hand: " + str(chosen_player.card_list()) + " ")
##            while card not in chosen_player.card_list():
##                print "Invalid entry. Please choose a card from the list provided."
##                card = raw_input("Choose a card from " + chosen_player.color + "'s hand: " + str(chosen_player.card_list()) + " ")
##            chosen_player.resources[card] -= 1
##            player.resources[card] += 1
##        player.progress_cards.remove(self)
##        progress[self.color].append(self)

class Merchant():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Merchant"
        self.color = "yellow"
        self.description = """Place the merchant on a hex adjacent to one of your settlements or cities.
You may trade that resource at the 2:1 rate for as long as you have the merchant. It is worth 1 victory point."""
        
    def execute(self, player):
        global status
        status = "progress merchant"
        status_label.config(text = "choose a hex to place merchant upon")

        #Original non-GUI version:
##        print player.color, "is playing the Merchant card."
##        loser = [p for p in players if p.merchant]
##        if loser:
##            loser = loser[0]
##            print loser.color, "loses the merchant and loses a victory point."
##            loser.victory_points -= 1
##            loser.merchant = ""
##        choices = player.get_resources_built_upon()
##        choice = raw_input(player.color + ", choose which hex to play the Merchant on: " + choices + " ")
##        while choice not in choices:
##            print "Invalid entry. Please choose from the options provided."
##            choice = raw_input(player.color + ", choose which hex to play the Merchant on: " + choices + " ")
##        print player.color, "places the Merchant on", choice, "and gains 1 victory point."
##        player.merchant = choice
##        player.victory_points += 1
##        player.progress_cards.remove(self)
##        progress[self.color].append(self)

class MerchantFleet():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Merchant Fleet"
        self.color = "yellow"
        self.description = "Choose any resource or commodity, which you may trade at the 2:1 rate for the rest of this turn."
        
    def execute(self, player):
        # fixed for GUI
        player.merchant_fleet_choose()

        # Original non-GUI version:
##        print player.color, "is playing the Merchant Fleet card."
##        choices = player.resources.keys()
##        choice = raw_input(player.color + ", which resource/commodity do you want to trade at the 2:1 rate? " + str(choices) + " ")
##        while choice not in choices:
##            if not choice: return
##            print "Invalid entry. Please choose from the options provided."
##            choice = raw_input(player.color + ", which resource/commodity do you want to trade at the 2:1 rate? " + str(choices) + " ")
##        player.temp_two_for_one.append(choice)
##        player.progress_cards.remove(self)
##        progress[self.color].append(self)

class ResourceMonopoly():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Resource Monopoly"
        self.color = "yellow"
        self.description = "Choose a resource. Each player must give you 2 of that resource if they have any."
        
    def execute(self, player):
        # fixed for GUI
        global status
        status = "progress monopoly resource"
        status_label.config(text = "choose a resource to monopolize.")
        player.monopoly_choose("resource")

        # Original non-GUI version:
##        print player.color, "is playing the Resource Monopoly card."
##        choice = raw_input(player.color + ", which resource do you wish to monopolize? " + str(resources) + " ")
##        while choice not in resources:
##            if not choice: return
##            print "Invalid entry. Please choose from the options provided."
##            choice = raw_input(player.color + ", which resource do you wish to monopolize? " + str(resources) + " ")
##        opponents = [p for p in players if p != player]
##        for p in opponents:
##            amount = min([2, p.resources[choice]])
##            p.resources[choice] -= amount
##            player.resources[choice] += amount
##            print player.color, "steals", amount, choice, "from", p.color
##        player.progress_cards.remove(self)
##        progress[self.color].append(self)

class TradeMonopoly():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Trade Monopoly"
        self.color = "yellow"
        self.description = "Choose a commodity. Each player must give you 1 of that commodity if they have it."
        
    def execute(self, player):
        # fixed for GUI
        global status
        status = "progress monopoly trade"
        status_label.config(text = "choose a commodity to monopolize.")
        player.monopoly_choose("commodity")

        # Original non-GUI version
##        print player.color, "is playing the Trade Monopoly card."
##        choice = raw_input(player.color + ", which commodity do you wish to monopolize? " + str(commodities) + " ")
##        while choice not in commodities:
##            if not choice: return
##            print "Invalid entry. Please choose from the options provided."
##            choice = raw_input(player.color + ", which commodity do you wish to monopolize? " + str(commodities) + " ")
##        opponents = [p for p in players if p != player]
##        for p in opponents:
##            amount = min([1, p.resources[choice]])
##            p.resources[choice] -= amount
##            player.resources[choice] += amount
##            print player.color, "steals", amount, choice, "from", p.color
##        player.progress_cards.remove(self)
##        progress[self.color].append(self)

progress = {"green": [Alchemist(0), Alchemist(1), RoadBuilding(2), RoadBuilding(3), Crane(4), Crane(5), Engineer(6),
                      Inventor(7), Inventor(8), PlusTwo(9, "wheat"), PlusTwo(10, "wheat"), Medicine(11), Medicine(12),
                      PlusTwo(13, "ore"), PlusTwo(14, "ore"), VictoryPoint(15, "green"), Smith(16), Smith(17)],
            "yellow": [TradeMonopoly(18), TradeMonopoly(19), CommercialHarbor(20), CommercialHarbor(21), MasterMerchant(22),
                       MasterMerchant(23), Merchant(24), Merchant(25), Merchant(26), Merchant(27), Merchant(28), Merchant(29),
                       MerchantFleet(30), MerchantFleet(31), ResourceMonopoly(32), ResourceMonopoly(33), ResourceMonopoly(34),
                       ResourceMonopoly(35)],
            "blue": [Bishop(36), Bishop(37), VictoryPoint(38, "blue"), Deserter(39), Deserter(40), Diplomat(41), Diplomat(42),
                     Intrigue(43), Intrigue(44), Saboteur(45), Saboteur(46), Spy(47), Spy(48), Spy(49),
                     Warlord(50), Warlord(51), Wedding(52), Wedding(53)]}

for color in progress:
    random.shuffle(progress[color])

def initialize_game_state():
    global turn, barbs, dice, barbs_have_attacked, player, status
    turn = 0
    barbs = 7
    dice = [0, [0, "black"]]
    barbs_have_attacked = False
    player = players[turn % len(players)]
    status = "place initial settlement"
    status_label.config(text = player.color + ", place your settlement.")
    redraw()

def initialize_board():
    global hexes, corners, edges
    print "Creating a new random board..."
    resources = ["wheat"] * 4 + ["sheep"] * 4 + ["wood"] * 4 + ["brick"] * 3 + ["ore"] * 3 + ["desert"]
    random.shuffle(resources)
    hexes = [Hex(n, resources.pop()) for n in range(19)]

    number_tiles = [5,2,6,3,8,10,9,12,11,4,8,10,9,4,5,6,3,11]
    for hexe in hexes:
        if hexe.resource != "desert":
            hexe.set_number(number_tiles.pop(0))
        hexe.set_corners(hex_corners[hexe.location])
                
    corners = [Corner(n) for n in range(54)]
    for corner in corners:
        corner.set_edges(corner_edges[corner.location])
        
    random.shuffle(port_types)
    for port in corner_ports:
        next_port = port_types.pop()
        for i in port:
            next_corner = [corner for corner in corners if corner.location == i][0]
            next_corner.port = next_port
        
    edges = [Edge(n) for n in range(72)]
    for edge in edges:
        for corner in corners:
            if edge.location in corner.edges:
                edge.corners.append(corner.location)
    initialize_game_state()

def set_corner_values():
    for corner in corners:
        value = 0
        hexes_touched = []
        for hexe in hexes:
            if corner.location in hexe.corners and hexe.resource != "desert":
                value += dice_frequencies[hexe.number]
                hexes_touched.append((hexe.resource, hexe.number))
        corner.value = value
        corner.hexes_touched = hexes_touched

def display_available_corners(canvas):
    for c in corners:
        c.draw(canvas, "available")
    
##    print "Corner values:"
##    for c in corners:
##        if two_spaces_away(c):
##            print str(c.location) + ":", c.value, c.hexes_touched, c.port

##initialize = Tk()
##
##def initialize_players():
##    # Needs fixed for GUI
##    print "initializing players..."
##    initialize.title("Cities and Knights of Catan")
##    Label(initialize, text = "Select the colors of the players").pack()
##    #self.discard_canvas = Canvas(self.pop_up, height = HEIGHT, width = WIDTH)
##    listbox = Listbox(initialize, selectmode=MULTIPLE)
##    listbox.pack()
##    for c in piece_colors:
##        listbox.insert(END, c)
##    Button(initialize, text = "START GAME", width = BUTTON_WIDTH,
##           command = lambda: self.initialize_players_execute(map(int, listbox.curselection()))).pack()

players = []

def initialize_players_execute(color_indices):
    global players
    for i in range(len(color_indices)):
        players.append(Player(i, piece_colors[color_indices[i]]))
    pop_up.destroy()
    initialize_board()

    # Original non-GUI version:
##    global players
##    number_of_players = input("\nHow many players are playing? ")
##    while number_of_players not in [1,2,3,4]:
##        print "you must enter 1,2,3 or 4"
##        number_of_players = input("\nHow many players are playing? ")
##    while number_of_players != len(players): players.pop()
##    for player in range(len(players)):
##        player_color = raw_input("\nWhat is the name of player " + str(player + 1) + "? ")
##        players[player] = Player(player, player_color)

def initial_placements():
    # No longer needed
    global players
    for player in players:
        display_available_corners()
        spot = input("\n" + player.color + ": Enter a location for your first settlement: ")
        while player.settlements_remaining == 5:
            while spot not in range(len(corners)):
                print "\nNot a valid placement. Must be an integer < 54 at least 2 spaces away from the nearest building."
                spot = input("\n" + player.color + ": Enter a location for your first settlement: ")
            player.build_settlement(spot, True)
            spot = 100
        player.show_valid_locations('r', "Place a road at one of the following locations:")
        road_spot = input("\n" + player.color + ": Where would you like to place your road? ")
        while player.roads_remaining == 15:
            while road_spot not in range(len(edges)):
                print "\nNot a valid placement. Must be an integer < 72 adjacent to your settlement."
                road_spot = input("\n" + player.color + ": Where would you like to place your road? ")
            player.build_road(road_spot, "settlement")
            road_spot = 100
    for player in players[::-1]:
        display_available_corners()
        spot = input("\n" + player.color + ": Enter a location for your first city: ")
        while player.cities_remaining == 4:
            while spot not in range(len(corners)):
                print "\nNot a valid placement. Must be an integer < 54 at least 2 spaces away from the nearest building."
                spot = input("\n" + player.color + ": Enter a location for your first city: ")
            player.build_city(spot, "initial")
            spot = 100
        player.show_valid_locations('rc', "Place a road at one of the following locations:")
        road_spot = input("\n" + player.color + ": Where would you like to place your road? ")
        while player.roads_remaining == 14:
            while road_spot not in range(len(edges)):
                print "\nNot a valid placement. Must be an integer < 72 adjacent to your city."
                road_spot = input("\n" + player.color + ": Where would you like to place your road? ")
            player.build_road(road_spot, "city")
            road_spot = 100

def dot_animation():
    # No longer needed
    if status == "roll":
        for i in range(10):
            display = [" "] * i + ["*"] + [" "] * (9 - i)
            str_display = ""
            for d in display:
                str_display += d
            outcome_label.config(text = str_display)
            time.sleep(0.1)
    roll_dice()

def destroy_alchemist_pop_up():
    card = [p for p in player.progress_cards if p.name == "Alchemist"][0]
    card.pop_up.destroy()

def roll_dice(red='', yellow=''):
    global status, turn, player, outcome_message
    if status in ["roll", "progress alchemist"]:
        if not red and not yellow:
            red1 = random.randrange(1,7)
            yellow1 = random.randrange(1,7)
        else:
            print "playing alchemist..."
            red1 = red
            yellow1 = yellow
            destroy_alchemist_pop_up()
            player.discard_progress_card("Alchemist")
        event = random.choice(["blue", "yellow", "green", "black", "black", "black"])
        dice[0] = red1 + yellow1
        dice[1] = [event, red1]
        status = "settle roll"
        outcome_message = "The roll is " + str(dice[0]) + ", with a " + event + " " + str(red1)
        outcome_label.config(text = outcome_message)
        roll_button.config(text = "END TURN")
        settle_roll(dice)
        redraw()
        return red1 + yellow1, [event, red1]
    elif status == "player action":
        #outcome_message = "Victory Points:"
        #for p in players:
        #    outcome_message += "\n" + p.color + ": " + str(p.victory_points)
        #outcome_label.config(text = outcome_message)
        if len(player.progress_cards) > 4:
            print player.color + " must discard or play a progress card before ending turn."
            status_label.config(text = "must play or discard a progress card.")
        else:
            turn += 1
            for p in players:
                p.make_knights_actionable()
            outcome_label.config(text = player.color + " is finished.")
            player = players[turn % len(players)]
            status_label.config(text = player.color + ", it is your turn.")
            barbs_message.config(text = "")
            defend_message.config(text = "")
            status = "roll"
            roll_button.config(text = "ROLL")
    update_score()
    redraw(True)

def settle_roll(dice):
    print dice
    global status
    total, event = dice[0], dice[1]
    if event[0] == "black":
        result = move_barbarians()
        if result == "waiting for cities to be destroyed": return
    else: distribute_progress_cards(event[0], event[1])
    if total == 7: evaluate_seven(player, barbs_have_attacked)
    else:
        distribute_resources(total)
        status = "player action"
        status_label.config(text = player.color + " choose an action.")
    update_score()
                        
    

def distribute_resources(total):
    global outcome_message
    gainers = []
    for hexe in hexes:
        if not hexe.blocked and hexe.number == total:
            for player in players:
                for settlement in player.settlements_built:
                    if settlement in hexe.corners:
                        print "\n", player.color, "gains 1", hexe.resource
                        outcome_message += "\n" + player.color + " gains 1 " + hexe.resource
                        player.resources[hexe.resource] += 1
                        gainers.append(player)
                for city in player.cities_built:
                    if city[0] in hexe.corners:
                        if hexe.resource != "desert": gainers.append(player)
                        if hexe.resource in ["wheat", "brick"]:
                            player.resources[hexe.resource] += 2
                            print "\n", player.color, "gains 2", hexe.resource
                            outcome_message += "\n" + player.color + " gains 2 " + hexe.resource
                        elif hexe.resource == "ore":
                            player.resources["ore"] += 1
                            player.resources["coin"] += 1
                            print "\n", player.color, "gains 1 ore and 1 coin."
                            outcome_message += "\n" + player.color + " gains 1 ore and 1 coin."
                        elif hexe.resource == "sheep":
                            player.resources["sheep"] += 1
                            player.resources["cloth"] += 1
                            print "\n", player.color, "gains 1 sheep and 1 cloth."
                            outcome_message += "\n" + player.color + " gains 1 sheep and 1 cloth."
                        elif hexe.resource == "wood":
                            player.resources["wood"] += 1
                            player.resources["paper"] += 1
                            print "\n", player.color, "gains 1 wood and 1 paper."
                            outcome_message += "\n" + player.color + " gains 1 wood and 1 paper."
    for player in players:
        if player.technology["paper"] > 3 and player not in gainers:
            player.choose_resource()
    outcome_label.config(text = outcome_message)

def integer_prompt(string):
    # No longer needed
    output = raw_input(string)
    while not output.isdigit():
        print "Invalid entry. You must enter an integer"
        output = raw_input(string + " ")
    return int(output)

def move_robber(special=False):
    global status
    if special == "bishop": status = "progress bishop"
    else: status = "move robber"
    status_label.config(text = player.color + ", place the robber.")
##    
##    blocked_hexe = [hexe for hexe in hexes if hexe.blocked]
##    if len(blocked_hexe): blocked_hexe = blocked_hexe[0]
##    else: blocked_hexe = None
##    location = integer_prompt(player.color + ", where would you like to place the robber? ")
##    while blocked_hexe and (location > 18 or location == blocked_hexe.location):
##        print "Invalid entry. The location must be a number < 19 not currently occupied by the robber."
##        location = integer_prompt(player.color + ", where would you like to place the robber? ")
##    new_hexe = [hexe for hexe in hexes if hexe.location == location][0]
##    if blocked_hexe: blocked_hexe.blocked = False
##    new_hexe.blocked = True
##    player_list = [corn.occupier for hexe in hexes if hexe.location == location for corner in hexe.corners
##                   for corn in corners if (corn.location == corner and corn.occ_type in ["settlement", "city"]
##                                           and corn.occupier != player.color)]
##    if player_list:
##        if special == "bishop":
##            print player.color + "'s bishop is stealing a resource from the following players:", player_list
##            robbee_players = [p for p in players if p.color in player_list]
##        else:
##            robbee = raw_input("Which player do you wish to steal from? " + str(player_list)) + " "
##            while robbee not in player_list:
##                print robbee + " does not occupy this location. Please choose a player from the list provided."
##                robbee = raw_input("Which player do you wish to steal from? " + str(player_list)) + " "
##            robbee_players = [p for p in players if p.color == robbee]
##        for robbee_player in robbee_players:
##            robbee_cards = robbee_player.card_list()
##            random.shuffle(robbee_cards)
##            if not len(robbee_cards):
##                print robbee + " does not have any cards for you to steal."
##            else:
##                stolen_card = robbee_cards.pop()
##                print "You stole a " + stolen_card + " from " + robbee_player.color + "."
##                player.resources[stolen_card] += 1
##                robbee_player.resources[stolen_card] -= 1
##    else:
##        print "None of your opponents occupy this hex."

def get_defender_list():
    active_max = max([player.active_knights() for player in players])
    defender_list = [players[(turn + i) % len(players)] for i in range(len(players))
                     if players[(turn + i) % len(players)].active_knights() == active_max]
    return defender_list

def get_loser_list():
    active_min = min([player.active_knights() for player in players])
    loser_list = [players[(turn + i) % len(players)] for i in range(len(players))
                  if players[(turn + i) % len(players)].active_knights() == active_min
                  and [city for city in players[(turn + i) % len(players)].cities_built if not city[2]]]
    return loser_list

def find_defender():
    defend_message.config(text = "You have defended Catan!")
    print "You have successfully defended Catan!"
    defender_list = get_defender_list()
    if len(defender_list) == 1:
        defender_list[0].is_defender()
        defend_message.config(text = defender_list[0].color + " is defender of Catan")
    else:
        defender_colors = [d.color for d in defender_list]
        defend_message.config(text = str(defender_colors) + " get a progress card")
        print "The following players get a progress card for having the largest army:", [player.color for player in defender_list]
        for p, player in enumerate(defender_list):
            player.choose_progress_card(p)

loser_list = []

def destroy_city():
    # fixed for GUI
    global loser_list, status
    print "Oh no! You do not have enough active knights to defend Catan!"
    loser_list = get_loser_list()
    if not loser_list:
        print "However, no one will lose a city because there are no un-metropolized cities."
        return
    print "The following players had the weakest army and must destroy a city:", [player.color for player in loser_list]
    status_label.config(text = loser_list[0].color + ", click a city to downgrade.")
    status = "downgrade=" + loser_list[0].color

##    for player in loser_list:
##        player.downgrade_city()

def deactivate_knights():
    for player in players:
        for knight in player.knights_built:
            knight[2] = 0

def count_cities():
    return sum([len(player.cities_built) for player in players])

def count_active_knights():
    return sum([player.active_knights() for player in players])

def move_barbarians():
    global barbs, barbs_have_attacked
    barbs -= 1
    if not barbs:
        barbs_message.config(text = "The barbarians are attacking!")
        print "The barbarians are attacking!"
        barbs_have_attacked = True
        barbs = 7
        if count_active_knights() >= count_cities():
            find_defender()
        else:
            destroy_city()
            return "waiting for cities to be destroyed"
        deactivate_knights()
    else:
        print "The barbarians are only", barbs, "spaces away!"

def evaluate_seven(player, barbs_have_attacked):
    global status
    found = False
    for p in players:
        if p.count_resources() > p.hand_limit():
            found = True
            status = "discard"
            p.discard_half()
    if not found:
        if barbs_have_attacked:
            print "no discard -- move the robber."
            status_label.config(text = "move the robber")
            status = "move robber"
            move_robber()
        else:
            status = "player action"
            status_label.config(text = player.color + ", choose an action.")
    

def query_progress_cards(player):
    # maybe no longer needed
    while len(player.progress_cards) > 4:
        print "You have too many progress cards:", [(p.ID, p.name) for p in player.progress_cards]
        choice = raw_input("(d)iscard or (p)lay a progress card? ")
        while choice not in ['d', 'p']:
            print "Invalid entry. Must enter 'd' or 'p'."
            choice = raw_input("(d)iscard or (p)lay a progress card? ")

def distribute_progress_cards(col, number):
    if col == None: return
    player_list = [players[(turn + i) % len(players)] for i in range(len(players))]
    for p, player in enumerate(player_list):
        if player.technology[color2tech[col]] > 1 and player.technology[color2tech[col]] >= number:
            player.draw_progress_card(col, p)

def try_alchemist():
    # No longer needed
    if status == "roll":
        for p in player.progress_cards:
            if p.name == "Alchemist":
                p.execute()
                break
    #if not red: print player.color + ", you do not have an Alchemist card. You must roll the dice."
    #return red, yellow

def overall_longest_road():
    road_lengths = [p.longest_road() for p in players]
    road_lengths2 = [r for r in road_lengths]
    if max(road_lengths) > 4:
        previous = [p for p in players if p.has_longest_road]
        toppers = [p for p in players if p.longest_road() == max(road_lengths)]
        if len(toppers) == 1:
            if toppers[0].has_longest_road == False:
                toppers[0].has_longest_road = True
                toppers[0].victory_points += 2
                if previous:
                    previous[0].has_longest_road = False
                    previous[0].victory_points -= 2
                    print toppers[0].color, "has taken the longest road from", previous[0].color, "with a length of", toppers[0].longest_road()
                else: print toppers[0].color, "has taken the longest road with a length of", toppers[0].longest_road()
            #else:
                #print toppers[0].color, "retains the longest road with a length of", toppers[0].longest_road()
        else:
            print [t.color for t in toppers], "are tied for the longest road with a length of", toppers[0].longest_road()
            if previous:
                if previous[0] in toppers:
                    print previous[0].color, "keeps the longest road card."
                else:
                    previous[0].has_longest_road = False
                    previous[0].victory_points -= 2
                    print previous[0].color, "loses the longest road card, which will be unclaimed until someone builds another road."

def road_test():
    global corners
    initialize_board()
    player = Player(0, "Brett")
    player.build_settlement(30, True)
    player.build_road(60, "settlement")
    player.resources["brick"] = 15
    player.resources["wood"] = 15
    assert player.longest_road(True) == 1
    player.build_road(42)
    assert player.longest_road(True) == 2
    player.build_road(43)
    assert player.longest_road(True) == 2
    player.build_city(40, "initial")
    player.build_road(52, "city")
    assert player.longest_road(True) == 2
    player.build_road(36)
    assert player.longest_road(True) == 2
    player.build_road(59)
    assert player.longest_road(True) == 3
    player.build_road(41)
    assert player.longest_road(True) == 4
    player.build_road(28)
    assert player.longest_road(True) == 5
    player.build_road(29)
    assert player.longest_road(True) == 7
    player.build_road(31)
    assert player.longest_road(True) == 8
    corn = [c for c in corners if c.location == 31][0]
    corn.occupier = "Matt"
    assert player.longest_road(True) == 7
    corn2 = [c for c in corners if c.location == 30][0]
    corn2.occupier = "Matt"
    assert player.longest_road(True) == 6

def main_game():
    # No longer needed
    global barbs, barbs_have_attacked, turn
    while True:
        turn += 1
        print "\nVictory Points:"
        for p in players:
            p.display_status()
        player = players[turn % len(players)]
        red, yellow = '', ''
        code = raw_input("\n" + player.color + ": press enter to roll the dice or 'a' to play Alchemist. ")
        if code == 'a':
            red, yellow = try_alchemist()
        total, event = roll_dice(red, yellow)
        if code == '7': total = 7
        print "\nthe roll is " + str(total) + " with a " + event[0] + " " + str(event[1])
        if event[0] == "black": move_barbarians()
        else: distribute_progress_cards(event[0], event[1])
        if total == 7: evaluate_seven(player, barbs_have_attacked)
        else: distribute_resources(total)
        action = "q"
        while action or len(player.progress_cards) > 4:
            if len(player.progress_cards) > 4:
                print "You must play or discard a progress card on this turn."
            player.display_status("personal")
            action = raw_input("\n" + player.color + """, what do you want to do?\n
(s)ettlement, (c)ity, (r)oad, (k)night, (w)all, (p)rogress card, (u)pgrade city,
(b)ank exchange, (o)ffer trade, (v)iew status """)
            player.do(action)
        player.make_knights_actionable()
        # TO DO: test full multiplayer game, trade with other players (should there be a 'confirm' option for the player offering the trade?),
        # GUI, computer AI

#road_test()

def draw_hexes(canvas):
    for hexe in hexes:
        hexe.draw(canvas)

def draw_corners(canvas, status):
    for c in corners:
        c.draw(canvas, status)

def draw_edges(canvas, status):
    for e in edges:
        e.draw(canvas, status)

def draw_cards():
    card_list = player.card_list()
    for c in range(len(card_list)):
        centerX = 5 + CARD_WIDTH / 2. + c * min([CARD_WIDTH, 0.5 * WIDTH / len(card_list)])
        canvas.create_rectangle(centerX - CARD_WIDTH / 2, HEIGHT - CARD_HEIGHT + 5,
                                     centerX + CARD_WIDTH / 2, HEIGHT - 10, fill = resource2color[card_list[c]])
        if card_list[c] in ["coin", "paper", "cloth"]:
            canvas.create_rectangle(centerX - CARD_WIDTH / 2 + 10, HEIGHT - CARD_HEIGHT + 15,
                                     centerX + CARD_WIDTH / 2 - 10, HEIGHT - 20, fill = "white")

def draw_progress():
    for p in range(len(player.progress_cards)):
        centerY = HEIGHT - 10 - PROGRESS_CARD_HEIGHT / 2. - p * PROGRESS_CARD_HEIGHT
        canvas.create_rectangle(0.8 * WIDTH - PROGRESS_CARD_WIDTH, centerY - PROGRESS_CARD_HEIGHT / 2.,
                                0.8 * WIDTH - 5, centerY + PROGRESS_CARD_HEIGHT / 2., fill = player.progress_cards[p].color)
        canvas.create_rectangle(0.8 * WIDTH - PROGRESS_CARD_WIDTH + 5, centerY - PROGRESS_CARD_HEIGHT / 2. + 5,
                                0.8 * WIDTH - 10, centerY + PROGRESS_CARD_HEIGHT / 2. - 5, fill = "white")
        name = ""
        name_list = player.progress_cards[p].name.split()
        for n in name_list:
            name += n + "\n"
        canvas.create_text(0.8 * WIDTH - PROGRESS_CARD_WIDTH / 2., centerY + 5, text = name)
        

def update_upgrade_buttons():
    cloth_button.config(text = "UPGRADE CLOTH (" + str(player.technology["cloth"]) + ")")
    paper_button.config(text = "UPGRADE PAPER (" + str(player.technology["paper"]) + ")")
    coin_button.config(text = "UPGRADE COIN (" + str(player.technology["coin"]) + ")")

def redraw(between_turns = False):
    canvas.delete("all")
    draw_hexes(canvas)
    draw_edges(canvas, status)
    draw_corners(canvas, status)
    draw_cards()
    draw_progress()
    if status != "roll":
        alchemist_button.config(state = DISABLED)
        for button in action_buttons:
            button.config(state = NORMAL)
    else:
        for button in action_buttons:
            button.config(state = DISABLED)
        if "Alchemist" not in [p.name for p in player.progress_cards]:
            alchemist_button.config(state = DISABLED)
        else:
            alchemist_button.config(state = NORMAL)
    console_frame.config(background = player.color)
    update_upgrade_buttons()

def rescore():
    global outcome_message
    outcome_label.config(text = outcome_message)
    roll_button.config(text = "ROLL")
    if "Alchemist" in [prog.name for prog in player.progress_cards]:
        alchemist_button = Button(score_frame, "ALCHEMIST", command = alchemist)
        alchemist_button.pack
    display_roll = Label(score_frame, text = player.color + ", rolls " + str(dice[0]) + " with a " + dice[1][0]
                         + str(dice[1][1]) + ".")
    display_roll.pack(side = TOP)
    score_text = [Label(score_frame, text = p.color + ": " + str(p.victory_points)).pack(side = TOP) for p in players]
    

#initialize_players()
#initialize_board()
#set_corner_values()
cards = [p for p in progress["green"] if p.name == "Alchemist"] + [p for p in progress["yellow"] if p.name == "Trade Monopoly"]
print [p.name for p in cards]
##players[0].progress_cards.append(cards[0])
##players[0].progress_cards.append(progress["blue"].pop(0))
##players[0].progress_cards.append(progress["green"].pop(0))
##players[0].progress_cards.append(progress["green"].pop(0))
##players[1].progress_cards.append(cards[1])
##players[1].progress_cards.append(progress["green"].pop(0))
##players[1].progress_cards.append(progress["blue"].pop(0))
##players[1].progress_cards.append(progress["green"].pop(0))


def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def nearest_corner(x, y):
    for c in corners:
        if distance([x,y], c.center) <= CORNER_RADIUS:
            return c

def nearest_edge(x, y):
    for e in edges:
        midpoint = e.get_midpoint()
        if distance([x,y], midpoint) < HEX_RADIUS / 3.0:
            return e

def nearest_hex(x, y):
    for h in hexes:
        if distance([x,y], h.center) <= HEX_RADIUS:
            print "found hex"
            return h
        
def play_nearest_progress_card(x, y):
    for i in range(len(player.progress_cards)):
        if (y > HEIGHT - 10 - (i + 1) * PROGRESS_CARD_HEIGHT and y < HEIGHT - 10 - i * PROGRESS_CARD_HEIGHT and
            len(player.progress_cards) > i and player.progress_cards[i].name != "Alchemist"):
            player.progress_cards[i].execute(player)
            return

def update_score():
    score_message = "Victory Points:"
    for p in players:
        score_message += "\n" + p.color + ": " + str(p.victory_points)
    score_message += "\nbarbs: " + str(barbs)
    score_label.config(text = score_message)

invent_hexes = []

def mouse_click(event):
    global status, player, turn, score_message, invent_hexes
    print "clicked at", event.x, event.y
    print status
    if event.x > 693 and event.y > 530:
        if status == "player action":
            play_nearest_progress_card(event.x, event.y)
        elif status.startswith("progress"):
            if status.startswith("progress smith 0"): player.discard_progress_card("Smith")
            elif status.startswith("progress place knight"): player.discard_progress_card("Deserter")
            elif status == "progress place road diplomat": player.discard_progress_card("Diplomat")
            elif status.startswith("progress harbor="): player.discard_progress_card("Commercial Harbor")
            status = "player action"
            status_label.config(text = player.color + ", choose an action.")
            for hexe in invent_hexes:
                hexe.token_color = TOKEN_COLOR
            if player.pop_up is not None:
                player.pop_up.destroy()
                player.pop_up = None
    elif status in ["place initial settlement", "place initial city"]:
        c = nearest_corner(event.x, event.y)
        if c:
            if status == "place initial settlement":
                outcome = player.build_settlement(c.location, True)
            else: outcome = player.build_city(c.location, "initial")
            if outcome == "success":
                status_label.config(text = player.color + ", place your road.")
                if status == "place initial settlement":
                    status = "place settlement road"
                else:
                    status = "place city road"
                redraw()
    elif status in ["place settlement road", "place city road", "progress place road 1", "place road 2",
                    "progress diplomat", "progress place road diplomat"]:
        e = nearest_edge(event.x, event.y)
        if e:
            if status in ["place settlement road", "progress place road 1", "place road 2", "progress place road diplomat"]:
                outcome = player.build_road(e.location, "settlement")
            elif status == "progress diplomat":
                outcome = player.remove_road(e)
            else:
                outcome = player.build_road(e.location, "city")
            if outcome == "success":
                turn += 1
                if turn < len(players):
                    player = players[turn % len(players)]
                    status = "place initial settlement"
                    status_label.config(text = player.color + ", place your first settlement.")
                elif turn < 2 * len(players):
                    player = players[2 * len(players) - 1 - turn]
                    status = "place initial city"
                    status_label.config(text = player.color + ", place your first city.")
                else:
                    player = players[turn % len(players)]
                    status = "roll"
                    status_label.config(text = player.color + ", it is your roll.")
            elif outcome == "road 1 placed":
                status = "place road 2"
                status_label.config(text = player.color + ", place your second road.")
            elif outcome == "road 2 placed":
                status = "player action"
                status_label.config(text = player.color + ", select an action.")
                player.discard_progress_card("Road Building")
            elif outcome == "diplomat road placed":
                status = "player action"
                status_label.config(text = player.color + ", select an action.")
                player.discard_progress_card("Diplomat")
            redraw()
                            
    elif (status in ["place settlement", "place city", "place knight", "upgrade knight", "activate knight", "move knight select", "place wall",
                    "progress medicine", "progress engineer", "progress deserter", "progress intrigue", "progress spy", "progress master merchant"]
          or status.endswith("choose deserter") or status.startswith("progress place knight") or status.startswith("move knight from")
          or status.startswith("displace knight") or status.startswith("progress harbor") or status.startswith("place metropolis")
          or status.startswith("downgrade")):
        c = nearest_corner(event.x, event.y)
        if c:
            print "looking at corner", c.location
            outcome = ""
            if status == "place settlement": outcome = player.build_settlement(c.location)
            elif status == "place city": outcome = player.build_city(c.location)
            elif status == "progress medicine":
                outcome = player.build_city(c.location, "medicine")
                if outcome == "success": player.discard_progress_card("Medicine")
            elif status == "place wall": outcome = player.build_wall(c.location)
            elif status == "progress engineer":
                outcome = player.build_wall(c.location, "engineer")
                if outcome == "success": player.discard_progress_card("Engineer")
            elif status == "place knight": outcome = player.build_knight(c.location)
            elif status == "upgrade knight": outcome = player.upgrade_knight(c.location)
            elif status == "activate knight": outcome = player.activate_knight(c.location)
            elif status == "move knight select": outcome = player.move_knight_from(c.location)
            elif status.startswith("move knight from"):
                from_location = int(status.split("=")[1])
                special = status.split("=")[2]
                if special:
                    mover = [p for p in players if p.color == special][0]
                    outcome = mover.move_knight_to(from_location, c.location, special)
                    if outcome == "success":
                        player.discard_progress_card("Intrigue")
                else:
                    player.move_knight_to(from_location, c.location)
            elif status.startswith("displace knight"):
                status_list = status.split("=")
                from_location = int(status_list[1])
                mover = [p for p in players if p.color == status_list[2]][0]
                mover.move_knight_to(from_location, c.location, True)
            elif status == "progress spy" and c.occ_type and c.occupier != player.color:
                print player.color + " is spying " + c.occupier + "'s progress cards."
                outcome = player.spy_opponent(c.occupier)
            elif status.startswith("progress harbor"):
                if "=" in status: checked = status.split("=")[1:]
                else: checked = [None]
                print "checked:", checked
                if c.occ_type and c.occupier != player.color and c.occupier not in checked:
                    print player.color + " is harborizing " + c.occupier
                    outcome = player.harborize_opponent(c.occupier)
            elif status == "progress master merchant":
                choices = [p.color for p in players if p.victory_points > player.victory_points]
                if c.occ_type and c.occupier in choices:
                    print player.color + " is using the Master Merchant on " + c.occupier
                    outcome = player.master_merchant(c.occupier)
            elif status.startswith("place metropolis"):
                print "checking if", c.location, "is valid placement"
                metro_color = status.split("=")[-1]
                city_choice = [city for city in player.cities_built if not city[2] and city[0] == c.location]
                if city_choice:
                    print "placing metropolis at " + str(c.location)
                    city_choice[0][2] = metro_color
                    player.victory_points += 2
                    outcome = "success"
                else:
                    print "invalid placement"
                    status_label.config(text = "Invalid placement.")
            elif status.startswith("downgrade"):
                player_color = status.split("=")[1]
                downgrader = [p for p in players if p.color == player_color][0]
                downgrader.downgrade_city(c.location)
            elif status == "progress deserter" and c.occ_type == "knight" and c.occupier != player.color:
                print player.color + " is deserting " + c.occupier
                outcome = player.desert_opponent(c.occupier)
            elif status.endswith("choose deserter") and c.occ_type == "knight" and status.startswith(c.occupier):
                [p for p in players if p.color == c.occupier][0].desert_knight_at_corner(c, player)
            elif status.startswith("progress place knight"):
                initial_state = status.split("[")[-1][:-1].split(", ")
                print initial_state
                initial_state = [int(s) for s in initial_state]
                outcome = player.build_knight(c.location, initial_state, "deserter")
                if outcome == "success": player.discard_progress_card("Deserter")
            elif status == "progress intrigue":
                choices = [k[0] for p in players if p != player for k in p.knights_built if k[0] in player.corners_touched]
                if c.location in choices:
                    print "moving knight at location " + str(c.location)
                    mover = [p for p in players if p.color == c.occupier][0]
                    outcome = mover.move_knight_from(c.location, "intrigue")
                    if outcome == "success": player.discard_progress_card("Intrigue")
            if outcome == "success":
                status_label.config(text = player.color + ", choose an action.")
                status = "player action"
            redraw()
    elif status.startswith("progress smith"):
        c = nearest_corner(event.x, event.y)
        if c:
            if status == "progress smith":
                outcome = player.upgrade_knight(c.location, "smith")
                if outcome == "success":
                    if player.has_upgradeable_knights():
                        status = "progress smith 0" + str(c.location)
                    else:
                        player.discard_progress_card("Smith")
                        status = "player action"
                        status_label.config(text = player.color + ", choose an action.")
                else:
                    status = "player action"
                    status_label.config(text = "Invalid location. Choose an action.")
            elif int(status[-2:]) != c.location:
                outcome = player.upgrade_knight(c.location, "smith")
                if outcome == "success":
                    status = "player action"
                    status_label.config(text = player.color + ", choose an action.")
                    player.discard_progress_card("Smith")
                else:
                    status_label.config(text = "click progress card area to end smith.")
    elif status == "place road":
        e = nearest_edge(event.x, event.y)
        if e:
            outcome = player.build_road(e.location)
            status_label.config(text = player.color + ", choose an action.")
            status = "player action"
            redraw()
    elif status in ["progress inventor", "move robber", "progress bishop", "progress merchant"]:
        hexe = nearest_hex(event.x, event.y)
        if status == "progress inventor" and hexe:
            if hexe.number in [3,4,5,9,10,11] and hexe not in invent_hexes:
                hexe.token_color = "orange"
                invent_hexes.append(hexe)
                if len(invent_hexes) == 2:
                    invent_hexes[0].number, invent_hexes[1].number = invent_hexes[1].number, invent_hexes[0].number
                    invent_hexes[0].token_color = invent_hexes[1].token_color = TOKEN_COLOR
                    player.discard_progress_card("Inventor")
                    invent_hexes = []
                    status = "player action"
                    status_label.config(text = player.color + ", choose an action.")
        elif status in ["move robber", "progress bishop"] and hexe:
            old_hex = [h for h in hexes if h.blocked]
            if old_hex: old_hex = old_hex[0]
            if old_hex != hexe:
                hexe.blocked = True
                if old_hex: old_hex.blocked = False
                redraw()
                if status == "progress bishop": player.rob(hexe, "bishop")
                else: player.rob(hexe)
        elif status == "progress merchant" and hexe:
            print "hex: ", hexe.location, hexe.resource
            if player.is_touching_hex(hexe):
                player.place_merchant(hexe)
            else:
                status_label.config(text = "you aren't touching this hex")
        redraw()
        
    redraw()
    update_score()

def build(thing):
    global status
    if status in ["place settlement", "place city", "place road", "place wall", "build knight", "activate knight",
                  "upgrade knight", "move knight select"]:
        status = "player action"
        status_label.config(text = player.color + ", choose an action.")
    elif status == "player action":
        if thing == "settlement":
            status = "place settlement"
            status_label.config(text = player.color + ", place your settlement.")
        elif thing == "city":
            status = "place city"
            status_label.config(text = player.color + ", choose a settlement to citify.")
        elif thing == "road":
            status = "place road"
            status_label.config(text = player.color + ", place your road.")
        elif thing == "wall":
            status = "place wall"
            status_label.config(text = player.color + ", choose a city to wallify.")
        elif thing == "build knight":
            if player.knights_remaining[0]:
                status = "place knight"
                status_label.config(text = player.color + ", place your knight.")
            else:
                status = "player action"
                status_label.config(text = "You need to upgrade first")
        elif thing == "upgrade knight":
            status = "upgrade knight"
            status_label.config(text = player.color + ", choose a knight to upgrade.")
        elif thing == "activate knight":
            status = "activate knight"
            status_label.config(text = player.color + ", choose a knight to activate.")
        elif thing == "move knight":
            status = "move knight select"
            status_label.config(text = player.color + ", choose a knight to move.")
    redraw()

def upgrade(commodity, crane=0):
    global status
    if status in ["progress crane", "player action"]:
        if status == "progress crane": crane = 1
        outcome = player.upgrade_city_GUI(commodity, crane)
        if outcome == "success":
            if crane: player.discard_progress_card("Crane")
            if not status.startswith("place metropolis"):
                status = "player action"
        else: status = "player action"
    redraw()
    update_score()

root = Tk()
##top_frame = Frame(root, height = HEIGHT, width = WIDTH)
##top_frame.pack(side = TOP, expand = True, fill = BOTH)
##bottom_frame = Frame(root)
##bottom_frame.pack(side = BOTTOM, expand = True, fill = BOTH)
##card_frame = Frame(bottom_frame)
##card_frame.pack(side = LEFT, expand = True, fill = BOTH)
##card_canvas = Canvas(card_frame)
##card_canvas.pack(side = LEFT)
canvas_frame = Frame(root, height = HEIGHT, width = WIDTH)
canvas_frame.pack(side = LEFT, expand = True, fill = Y)
console_frame = Frame(root)
console_frame.pack(expand = True, fill = Y)
score_frame = Frame(console_frame)
score_frame.pack(side = TOP, expand = True, fill = X)
player_frame = Frame(console_frame)
player_frame.pack(side = TOP, expand = True, fill = X)

settle_button = Button(player_frame, text = "BUILD SETTLEMENT", command = lambda: build("settlement"), width = BUTTON_WIDTH)
settle_button.pack(side = TOP)
city_button = Button(player_frame, text = "BUILD CITY", command = lambda: build("city"), width = BUTTON_WIDTH)
city_button.pack(side = TOP)
road_button = Button(player_frame, text = "BUILD ROAD", command = lambda: build("road"), width = BUTTON_WIDTH)
road_button.pack(side = TOP)
wall_button = Button(player_frame, text = "BUILD WALL", command = lambda: build("wall"), width = BUTTON_WIDTH)
wall_button.pack(side = TOP)

knight_frame = Frame(console_frame)
knight_frame.pack(side = TOP, expand = True, fill = X)

knight_build_button = Button(knight_frame, text = "BUILD KNIGHT", command = lambda: build("build knight"), width = BUTTON_WIDTH)
knight_build_button.pack(side = TOP)
knight_activate_button = Button(knight_frame, text = "ACTIVATE KNIGHT", command = lambda: build("activate knight"), width = BUTTON_WIDTH)
knight_activate_button.pack(side = TOP)
knight_upgrade_button = Button(knight_frame, text = "UPGRADE KNIGHT", command = lambda: build("upgrade knight"), width = BUTTON_WIDTH)
knight_upgrade_button.pack(side = TOP)
knight_move_button = Button(knight_frame, text = "MOVE KNIGHT", command = lambda: build("move knight"), width = BUTTON_WIDTH)
knight_move_button.pack(side = TOP)

upgrade_frame = Frame(console_frame)
upgrade_frame.pack(side = TOP, expand = True, fill = X)

cloth_button = Button(upgrade_frame, text = "UPGRADE CLOTH (1)", command = lambda: upgrade("cloth"), width = BUTTON_WIDTH)
cloth_button.pack(side = TOP)
coin_button = Button(upgrade_frame, text = "UPGRADE COIN (1)", command = lambda: upgrade("coin"), width = BUTTON_WIDTH)
coin_button.pack(side = TOP)
paper_button = Button(upgrade_frame, text = "UPGRADE PAPER (1)", command = lambda: upgrade("paper"), width = BUTTON_WIDTH)
paper_button.pack(side = TOP)

score_message = ""
score_label = Label(score_frame, text = score_message)
score_label.pack(side = TOP)
outcome_message = ""
outcome_label = Label(score_frame, text = outcome_message)
outcome_label.pack(side = TOP)
#status_message = player.color + ", place your first settlement."
status_label = Label(score_frame, text = "choose players", fg = "dark red")
status_label.pack(side = TOP)
roll_button = Button(score_frame, text = "ROLL", command = roll_dice, width = BUTTON_WIDTH)
roll_button.pack(side = TOP)
alchemist_button = Button(score_frame, text = "PLAY ALCHEMIST", command = try_alchemist, width = BUTTON_WIDTH)
alchemist_button.pack(side = TOP)
barbs_message = Label(score_frame, text = "")
barbs_message.pack(side = TOP)
defend_message = Label(score_frame, text = "")
defend_message.pack()
canvas = Canvas(canvas_frame, height = HEIGHT, width = 0.8 * WIDTH, bg = CANVAS_BACKGROUND_COLOR)
canvas.bind("<ButtonRelease-1>", mouse_click)
canvas.pack()
action_buttons = [settle_button, city_button, road_button, wall_button, cloth_button, coin_button, paper_button,
                  knight_build_button, knight_upgrade_button, knight_activate_button, knight_move_button]

status = "initialize players"

pop_up = Toplevel(root, height = 600, width = 800)
pop_up.title("Initialize Players")
Label(pop_up, text = "Select the colors of the players.").pack()
listbox = Listbox(pop_up, selectmode=MULTIPLE)
listbox.pack()
for c in piece_colors:
    listbox.insert(END, c)
Button(pop_up, text = "START GAME", width = BUTTON_WIDTH,
       command = lambda: initialize_players_execute(map(int, listbox.curselection()))).pack()

#status = "place initial settlement"

#redraw()

root.mainloop()

#initial_placements()
#main_game()

## For enhanced testing purposes:
#  game is initialized with paper technology at level 4 (Aqueduct) for all players, and 4 progress cards for each player.
#  REMEMBER TO RESET THESE TO DEFAULT VALUES BEFORE PLAYING A REAL GAME!

## TO DO: drive away robber, trading, display ports, learn how to use images in Tkinter
# fix Corner.draw() method to display available corners to move/displace a knight.

# Search these tags:
# Needs fixed for GUI
# No longer needed
