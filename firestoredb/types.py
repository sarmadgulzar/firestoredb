class Array:
    pass


class Boolean:
    pass


class GeoPoint:
    pass


class Map:
    pass


class Null:
    pass


class Number:
    pass


class Reference:
    pass


class String:
    def __init__(self, value):
        if isinstance(value, str):
            self.value = value
        else:
            raise TypeError("Value must be a string")


class Timestamp:
    pass
