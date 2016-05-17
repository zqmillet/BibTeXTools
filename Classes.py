from BibTeXParser import BibTeXParse
import os

class Literature:
    Type = ''
    Hash = ''
    PropertyList = {}

    def __init__(self, Type, Hash):
        self.Type = Type
        self.Hash = Hash
        self.PropertyList = {}

    def Print(self):
        print('Literature Type = {0}'.format(self.Type))
        print('Literature Hash = {0}'.format(self.Hash))
        for Name in self.PropertyList:
            print('{0} = {1}'.format(Name, self.PropertyList[Name]))

class DataBase:
    LiteratureList = []
    CommentList = []
    FileName = ''
    Encoding = ''

    def __init__(self):
        self.LiteratureList = []
        self.CommentList = []
        self.FileName = ''
        self.Encoding = ''

    def Load(self, FileName, Encoding = 'utf-8'):
        self.LiteratureList = []
        self.CommentList = []

        self.Encoding = Encoding
        if not os.path.isfile(FileName):
            return False

        self.FileName = FileName
        if not BibTeXParse(FileName, self.LiteratureList, self.CommentList, Encoding):
            self.LiteratureList.clear()
            self.CommentList.clear()
            return False

        return True


    def Save(self, FileName = '', Encoding = ''):
        if FileName == '':
            FileName = self.FileName

        if Encoding == '':
            Encoding = self.Encoding

        # Write the title of the BibTeX file
        BibTeXString = '% This file was created with BibTeXTools 0.10.\n'
        BibTeXString += '% Encoding: ' + Encoding + '\n\n'

        MaxNameLength = 0
        for Literature in self.LiteratureList:
            for Name in Literature.PropertyList:
                if len(Name) > MaxNameLength:
                    MaxNameLength = len(Name)


        for Literature in self.LiteratureList:
            LiteratureString = '@' + Literature.Type + '{' + Literature.Hash + ',\n'
            for Name in Literature.PropertyList:
                LiteratureString += '  ' + Name.ljust(MaxNameLength) + ' = {' + Literature.PropertyList[Name] + '},\n'
            LiteratureString = LiteratureString.rstrip(',\n') + '\n'
            LiteratureString += '}\n\n'
            BibTeXString += LiteratureString


        for Comment in self.CommentList:
            BibTeXString += '@comment{' + Comment + '}\n\n'

        BibTeXFile = open(FileName, 'w', encoding = Encoding)
        BibTeXFile.write(BibTeXString)
        BibTeXFile.close()
