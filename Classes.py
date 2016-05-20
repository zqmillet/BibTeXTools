from BibTeXParser import BibTeXParse
import os
import time
import requests

class Entry:
    Type = ''
    CitationKey = ''
    TagList = {}

    def __init__(self, Type, CitationKey):
        self.Type = Type
        self.CitationKey = CitationKey
        self.TagList = {}

    def Print(self):
        print('Entry Type = {0}'.format(self.Type))
        print('Entry Citation Key = {0}'.format(self.CitationKey))
        for TagName in self.TagList:
            print('{0} = {1}'.format(TagName, self.TagList[TagName]))


class DataBase:
    EntryList = []
    CommentList = []
    FileName = ''
    Encoding = ''
    CommitList = []

    def __init__(self):
        self.EntryList = []
        self.CommentList = []
        self.FileName = ''
        self.Encoding = ''
        self.CommitList = []

    def Load(self, FileName, Encoding = ''):
        self.EntryList = []
        self.CommentList = []
        self.FileName = FileName

        if Encoding == '':
            self.Encoding = 'utf-8'
        else:
            self.Encoding = Encoding

        if not os.path.isfile(self.FileName):
            print('The file "{0}" does not exist!'.format(self.FileName))
            return False

        self.FileName = FileName
        if not BibTeXParse(FileName, self.EntryList, self.CommentList, self.Encoding):
            self.EntryList.clear()
            self.CommentList.clear()
            return False

        self.Commit('Database {0} has been loaded.'.format(self.FileName))
        self.Commit('|-The encoding is {0}.'.format(self.Encoding))

        self.Commit('|-The number of entries in {0} is {1}.'.format(self.FileName, len(self.EntryList)))
        TypeList = {}
        for Entry in self.EntryList:
            if Entry.Type in TypeList:
                TypeList[Entry.Type] += 1
            else:
                TypeList[Entry.Type] = 1

        for Type in TypeList:
            self.Commit('  |-The number of {0}(s) is {1}'.format(Type, TypeList[Type]))

        return True

    def Save(self, FileName = '', Encoding = ''):
        if FileName == '':
            FileName = self.FileName

        if Encoding == '':
            Encoding = self.Encoding

        # Write the title of the BibTeX file
        DataBaseString = '% This file was created with BibTeXTools 0.10.\n'
        DataBaseString += '% Encoding: ' + Encoding + '\n\n'

        MaxTagNameLength = 0
        for Entry in self.EntryList:
            for TagName in Entry.TagList:
                if len(TagName) > MaxTagNameLength:
                    MaxTagNameLength = len(TagName)

        for Entry in self.EntryList:
            EntryString = '@' + Entry.Type + '{' + Entry.CitationKey + ',\n'
            for TagName in Entry.TagList:
                EntryString += '  ' + TagName.ljust(MaxTagNameLength) + ' = {' + Entry.TagList[TagName] + '},\n'
            EntryString = EntryString.rstrip(',\n') + '\n'
            EntryString += '}\n\n'
            DataBaseString += EntryString

        for Comment in self.CommentList:
            DataBaseString += '@comment{' + Comment + '}\n\n'

        BibTeXFile = open(FileName, 'w', encoding = Encoding)
        BibTeXFile.write(DataBaseString)
        BibTeXFile.close()

        self.Commit('The database has been saved as {0}.'.format(FileName))

    def Commit(self, CommitMessage):
        self.CommitList.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +
                         ': ' + CommitMessage)
        print(CommitMessage)

    def DeleteTag(self, TagNameList):
        self.Commit('Delete {0} properties from {1}.'.format('"' + '", "'.join(TagNameList) + '"', self.FileName))
        for Entry in self.EntryList:
            for TagName in TagNameList:
                TagName = TagName.lower()
                if TagName in Entry.TagList:
                    del Entry.TagList[TagName]
                    self.Commit('|-Delete "{0}" tag from {1} {2}.'.format(TagName.lower(), Entry.Type, Entry.CitationKey))

    def FetchURL(self):
        self.Commit('Fetch "url" tag for all entries.')
        TimeOut = 1
        for Entry in self.EntryList:
            if 'url' in Entry.TagList:
                self.Commit('|-There is already "url" tag in {0} {1}.'.format(Entry.Type, Entry.CitationKey))
            else:
                if 'doi' in Entry.TagList:
                    URL = GetFullDoiUrl(Entry.TagList['doi'])
                    while True:
                        try:
                            Request = requests.get(URL, timeout = TimeOut)
                            Entry.TagList['url'] = Request.url
                            break
                        except:
                            TimeOut += 1

                        if TimeOut > 10:
                            self.Commit('|-No response from {0}, try other servers.'.format('http://dx.doi.org/'))
                            TimeOut = 1
                            break
                    self.Commit('|-"url" tag has been added in {0} {1}.'.format(Entry.Type, Entry.CitationKey))
                else:
                    self.Commit('|-There is no "doi" tag in {0} {1}. Try Title tag.'.format(Entry.Type, Entry.CitationKey))

def GetFullDoiUrl(Doi):
    if Doi.lower().startswith('http://'):
        return Doi
    elif Doi.lower().startswith('https://'):
        return Doi
    else:
        return 'http://dx.doi.org/' + Doi.strip('/')