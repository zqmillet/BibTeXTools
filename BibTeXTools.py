import sys
import getopt
import Classes

def PrintUsage():
    print('Usage:')
    print('  BibTeXTools [options] BibTeXFileName.bib')
    print('  BibTeXTools BibTeXFileName.bib [options]')
    print('Options:')
    print('  -v, --version            : show the version.')
    print('  -h, --help               : show the usage.')
    print('  -o, --output=Name        : set the output file name.')
    print('  -d, --delete=TagNameList : delete tags whose name is in TagNameList of each entry.')
    print('  -l, --log=LogFileName    : save the log as LogFileName.')
    print('  --fetchurl               : fetch the Url tag of each literature;')

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
    Options, Arguments = getopt.getopt(ParameterList,
                                       'hvo:d:e:l:',
                                       ['help',
                                        'version',
                                        'fetchurl',
                                        'output=',
                                        'delete=',
                                        'encoding=',
                                        'log='])
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
SaveLogFile = False
LogFileName = ''

# Do something according to the arguments
DoneList = []
for Name, Value in Options:
    DoneList.append(Name)
    if Name.lower() in ['-h', '--help']:
        PrintUsage()
    elif Name.lower() in ['-v', '--version']:
        PrintVersion()
    elif Name.lower() in ['-o', '--output']:
        OutputFileName = Value
    elif Name.lower() in ['-e', '--encoding']:
        Encoding = Value
    elif Name.lower() in ['-l', '--log']:
        SaveLogFile = True
        LogFileName = Value
    else:
        DoneList.remove(Name)

if not BibTeXDataBase.Load(BibTeXFileName):
    exit()

for Name, Value in Options:
    if Name in DoneList:
        continue

    if Name.lower() in ['-d', '--delete']:
        NameList = Value.split(',')
        for Index in range(0, len(NameList)):
            NameList[Index] = NameList[Index].strip()
        BibTeXDataBase.DeleteTag(NameList)
    elif Name.lower() in ['--fetchurl']:
        BibTeXDataBase.FetchURL()
    else:
        PrintSyntaxError()
        PrintUsage()
        exit()

BibTeXDataBase.Save(OutputFileName)

if SaveLogFile:
    if LogFileName == '':
        print()
        exit()

    LogFile = open(LogFileName, 'w', encoding='utf-8')
    for Commit in BibTeXDataBase.CommitList:
        LogFile.write(Commit + '\n')
    LogFile.close()