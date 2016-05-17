import Classes

FileName = 'References.bib'
BibTeXDataBase = Classes.DataBase()
if not BibTeXDataBase.Load(FileName):
    exit()

print('DataBase has been loaded!')
BibTeXDataBase.Save('Test.bib')
