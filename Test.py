from BibTeXParser import BibTeXParse

FileName = 'References.bib'
LiteratureList = []
if BibTeXParse(FileName, LiteratureList):
    print(LiteratureList)
else:
    print('Error!')