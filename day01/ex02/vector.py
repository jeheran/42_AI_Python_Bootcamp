class Vector:

    def __init__(self, values):

        if isinstance(values, list):
            self.values = values
            self.size = len(values)
        if isinstance(values, int) and values > 0:
            self.values = list(map(float, range(0, values, 1)))
            self.size = len(self.values)
        if isinstance(values, int) and values < 0:
            self.values = list(map(float, range(0, values, -1)))
            self.size = len(self.values)
        if isinstance(values, tuple):
            self.values = list(map(float, range(values[0], values[1], 1)))
            self.size = len(self.values)

    def __add__(self, v2):
        res = []
        i = 0
        while i < self.size:
            res.append(self.values[i] + v2.values[i])
            i += 1
        return res
        


