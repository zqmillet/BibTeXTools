import Classes

FileName = 'References.bib'
BibTeXDataBase = Classes.DataBase(FileName)
if BibTeXDataBase.HasNoError:
    print('DataBase has been loaded!')

BibTeXDataBase.Save('Test.bib')
