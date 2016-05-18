import os,sys
import getopt

def PrintUsage():
    PrintVersion()
    print('\nUsage:')
    print('  BibTeXTools [options] BibTeXFileName.bib')
    print('  BibTeXTools BibTeXFileName.bib [options]')
    print('Options:')
    print('  -v, --version : show the version.')
    print('  -h, --help    : show the usage.')
    print('  -o, --output  : set the output file name.')

def PrintSyntaxError():
    print('Syntax Error!\n')

def PrintVersion():
    print('This is BibTeXTools v0.10.')

# Order the arguments
ParameterList = sys.argv[1:]
if len(ParameterList) == 0:
    PrintUsage()
    exit()
elif ParameterList[0][0] != '-':
    ParameterList.append(ParameterList[0])
    del ParameterList[0]
else:
    pass

# Analyze the arguments
try:
    opts, args = getopt.getopt(ParameterList, 'ho:v', ['help', 'output=', 'version'])
except getopt.GetoptError:
    PrintSyntaxError()
    PrintUsage()
    exit()

# If there is no required argument, exit
if len(args) != 1:
    BibTeXFileName = ''
else:
    # Obtain the BibTeXFileName
    BibTeXFileName = args[0]

# Do something according to the arguments
for name, value in opts:
    if name in ['-h', '--help']:
        PrintUsage()
    elif name in ['-v', '--version']:
        PrintVersion()
