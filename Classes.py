class Literature:
    Type = ''
    Hash = ''
    PropertyList = {}

    def __init__(self, Type, Hash):
        self.Type = Type
        self.Hash = Hash

    def Print(self):
        print('Literature Type = {0}'.format(self.Type))
        print('Literature Hash = {0}'.format(self.Hash))
        for Name in self.PropertyList:
            print('{0} = {1}'.format(Name, self.PropertyList[Name]))
