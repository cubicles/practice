class savingprivatejack:
    def __init__(self, publicvar):
        self.privatetest = publicvar * 10
        self.privatejack = 'spielberg'
        self.publictest = publicvar * 2
        #__privatetest = publicvar * 10

    def privateduties(self):
        return self.privatetest

jack = savingprivatejack(4)
print(jack.publictest)
print(jack.privatejack)
# print(jack.__privatetest)
print(jack.privateduties())
