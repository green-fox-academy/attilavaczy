class MySuperString:
    def __init__(self, mystr):
        self.mystr = mystr

    def reverse(self):
        n = len(self.mystr)
        reversed = ''
        for i in range(n):
            print('i={}'.format(i))
            print(reversed)
            reversed = self.mystr[i] + reversed
        return reversed

#ver 2.

    def reverse(self):
        n = len(self.mystr)
        reversed = ''
        for i in range(n-1, -1, -1)
            reversed += self.mystr[i]
        return reversed

#ver 3.

    def reverse(self):
        reversed = ''
        for i in self.mystr
            reversed += i + reversed
        return reversed
