


class Parameters:

    def __init__(self, name=None, text=None):
        self.name = name
        self.text = text

    def __repr__(self):
        return '%s:%s' % (self.name, self.text)
