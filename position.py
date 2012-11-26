from utils import bold


class Position(object):
    TYPES = {
        'black': bold('@'),
        'white': bold('O'),
        'empty': '.',
    }

    class PositionError(Exception):
        pass

    def __init__(self, type):
        if type not in self.TYPES:
            raise self.PositionError('Type \'{0}\' must be one of the following: {1}'.format(
                type,
                self.TYPES.keys(),
            ))
        self._type = type

    def __eq__(self, other):
        return self._type == other._type

    def __hash__(self):
        return hash(self._type)

    def __str__(self):
        return self.TYPES[self._type]

    def __repr__(self):
        return self._type.title()
