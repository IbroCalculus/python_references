from enum import Enum, auto


class State(str, Enum):                             # class State(str, Enum):    The values will be string, instead of integers, ie "1"
    PLAYING = auto()  # or PLAYING = 1
    PAUSED = auto()
    GAME_OVER = auto()


# ----------------------------------------------------
state = State.PLAYING
print(type(state.value))
if state == State.PLAYING:
    print("It is in playing state")

print(state.value)  # gets the value (ie 1 for PLAYING, 3 for GAME_OVER because of auto(). value count begins from 1 not zero)


# ================== EXAMPLE 2. ==================================

# Enum Definition
class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()


# Enum with explicit values
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5


# Accessing Enum members
print(Color.RED)  # Output: Color.RED
print(Weekday.WEDNESDAY)  # Output: Weekday.WEDNESDAY

# Enum iteration
for color in Color:
    print(color)

# Enum comparison
if Color.RED == Color.RED:
    print("Colors are equal")


# Enum with custom values
class Planet(Enum):
    MERCURY = (1, 4879)
    VENUS = (2, 12104)
    EARTH = (3, 12742)

    def __init__(self, order, diameter):
        self.order = order
        self.diameter = diameter


# Accessing custom values in Enums
earth = Planet.EARTH
print(f"Earth Order: {earth.order}, Diameter: {earth.diameter} km")
