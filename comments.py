class Comments:
    def __init__(self, comment1, comment2):
        self.com1 = comment1
        self.com2 = comment2

    def begin(self):
        print ("### " + str(self.com1)  + "     ###")

    def end(self):
        print ("### " + str(self.com2)  + "   ###")

    pass