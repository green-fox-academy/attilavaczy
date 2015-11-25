class MySuperString:
    def __init__(self, mystr):
        self.mystr = mystr

    def count(self, char):
        counter = 0
        for h in self.mystr:
            if (char == h):
                counter = counter + 1
        return counter
