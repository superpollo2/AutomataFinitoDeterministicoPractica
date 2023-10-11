class Node:
    def __init__(self, _id, firstpos=None, lastpos=None, nullable=False, value=None, c1=None, c2=None):
        self._id = _id
        self.firstpos = firstpos
        self.lastpos = lastpos
        self.followpos = list()
        self.nullable = nullable
        self.value = value
        self.c1 = c1
        self.c2 = c2

    def __repr__(self):
        return f'''
    id: {self._id}
    value: {self.value}
    firstpos: {self.firstpos}
    lastpos: {self.lastpos}
    followpos: {self.followpos}
    nullabe: {self.nullable}
    '''
    #puede ser que no funcione