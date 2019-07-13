


class Parameters:

    def __init__(self, name=None, text=None, number_of_result=None, name_of_button=None, id=None):
        self.name = name
        self.text = text
        self.number_of_result = number_of_result
        self.name_of_button = name_of_button
        self.id = id

    def __repr__(self):
        return '%s:%s' % (self.name, self.text)
