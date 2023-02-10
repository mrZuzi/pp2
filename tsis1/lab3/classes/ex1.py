class myclass:
    def __init__(self):
        self.string=""
    def getString(self):
        self.string= input()
    def printString(self):
        print(self.string.upper())

str=myclass()
str.getString()
str.printString()