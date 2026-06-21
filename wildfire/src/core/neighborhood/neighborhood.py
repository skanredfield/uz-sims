from grid import Grid


class Neighborhood:

    @classmethod
    def get_neighborhood(cls, _: Grid):
        pass

    def _append_if_not_none(cls, l: list, obj: object):
        if obj is not None:
            l.append(obj)
