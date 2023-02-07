class word:
    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

ans = word()
ans.getString()
ans.printString()