class calculator:
    def add(self, *args):
        return sum(args)
    

c = calculator()
print(c.add(1, 2))
print(c.add(1, 2, 3))
print(c.add(1, 2, 3, 4))