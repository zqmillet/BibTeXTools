import sys
import getopt
import Classes

def PrintUsage():
    print('Usage:')
    print('  BibTeXTools [options] BibTeXFileName.bib')
    print('  BibTeXTools BibTeXFileName.bib [options]')
    print('Options:')
    print('  -v, --version         : show the version.')
    print('  -h, --help            : show the usage.')
    print('  -o, --output=Name     : set the output file name.')
    print('  -d, --delete=NameList : delete the property whose name is in NameList of each')
    print('                          literature.')
    print('  -l, --log=LogFile     : save the log.')

def PrintSyntaxError():
    print('Syntax Error!\n')

def PrintVersion():
    print('This is BibTeXTools v0.10.')

# Order the arguments
ParameterList = sys.argv[1:]
if len(ParameterList) == 0:
    PrintVersion()
    PrintUsage()
    exit()
elif ParameterList[0][0] != '-':
    ParameterList.append(ParameterList[0])
    del ParameterList[0]
else:
    pass

# Analyze the arguments
Options = {}
Arguments = []
try:
    Options, Arguments = getopt.getopt(ParameterList, 'ho:vd:e:', ['help', 'output=', 'version', 'delete=', 'encoding='])
except getopt.GetoptError:
    PrintSyntaxError()
    PrintUsage()
    exit()

# Obtain the BibTeXFileName
if len(Arguments) != 1:
    BibTeXFileName = ''
else:
    BibTeXFileName = Arguments[0]

OutputFileName = BibTeXFileName
BibTeXDataBase = Classes.DataBase()
Encoding = ''

# Do something according to the arguments
DoneList = []
for Name, Value in Options:
    if Name.lower() in ['-h', '--help']:
        PrintUsage()
        DoneList.append(Name)
    elif Name.lower() in ['-v', '--version']:
        PrintVersion()
        DoneList.append(Name)
    elif Name.lower() in ['-o', '--output']:
        OutputFileName = Value
        DoneList.append(Name)
    elif Name.lower in ['-e', '--encoding']:
        Encoding = Value
        DoneList.append(Name)

for Name, Value in Options:
    if Name in DoneList:
        continue

    if Name.lower() in ['-d', '--delete']:
        if not BibTeXDataBase.Load(BibTeXFileName):
            exit()

        NameList = Value.split(',')
        for Index in range(0, len(NameList)):
            NameList[Index] = NameList[Index].strip()
        BibTeXDataBase.DeleteProperty(NameList)
        BibTeXDataBase.Save(OutputFileName)
    else:
        PrintSyntaxError()
        PrintUsage()
        exit()
