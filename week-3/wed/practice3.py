class MySuperString:
    def __init__(self, mystr):
        self.mystr


    def space_to_underscore(self):
        underscorestring = ''
        for i in self.mystr:
            if i == ' ':
                underscorestring += '_'
            else:
               underscorestring += i
        return underscorestring
