import argparse
import sys

class ByOrder(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not 'OrderedArgumentList' in namespace:
            setattr(namespace, 'OrderedArgumentList', [])
        previous = namespace.OrderedArgumentList
        previous.append((self.dest, values))
        setattr(namespace, 'OrderedArgumentList', previous)

Parser = argparse.ArgumentParser()
Parser.add_argument('BibTeXFileName',
                    help='the file name of BibTeX database.')
Parser.add_argument('-d', '--delete',
                    nargs   = '*',
                    metavar = 'tag',
                    action  = ByOrder,
                    help    = 'delete tags of all entries in the database.')
Parser.add_argument('-f', '--fetch',
                    nargs   = '*',
                    metavar = 'tag',
                    action  = ByOrder,
                    help    = 'fetch tags of all entries in the database.')
Parser.add_argument('-o', '--output',
                    nargs   = 1,
                    metavar = 'file name',
                    help    = 'set the name of the output file, if this option is not specified, the database will be overwrited.')
Parser.add_argument('-l', '--log',
                    action  = 'store_true',
                    help    = 'save log file.')
Parser.add_argument('--logfile',
                    nargs   = 1,
                    metavar = 'file name',
                    help    = 'set the name of the output file, if this option is not specified, the name of log file will be BibTeXFileName.log.')
Parser.add_argument('-v', '--version',
                    action  = 'version',
                    version = 'BibTeXTools 0.10.',
                    help    = 'show the version of BibTeXTools.')

Parameters = 'BibTeXFileName.bib -f url --delete Title title'.split()

try:
    Parser.parse_args(['-h'])
except:
    exit(1)

Arguments = Parser.parse_args(Parameters)
OrderedArgumentList = Arguments.OrderedArgumentList
SaveLogFile = Arguments.log

print(OrderedArgumentList)

for Name in OrderedArgumentList:
    print(Name[1])


# ArgumentList = Arguments.positionals
# pass
#     .__dict__
# BibTeXFileName = Arguments.BibTeXFileName
# OutputFileName = BibTeXFileName
# SaveLogFile = False
# LogFileName = ''
#
# for Name in ArgumentList:
#     if Name in ['d', 'delete']:
#         print('delete')
#         print(ArgumentList[Name])
#     elif Name in ['f', 'fetch']:
#         print('fetch')
#         print(ArgumentList[Name])
#     elif Name in ['o', 'output']:
#         print('output')
#         OutputFileName = ArgumentList[Name]
#         print(ArgumentList[Name])
#     elif Name in ['l', 'logfile']:
#         SaveLogFile = True
#         if ArgumentList[Name] is not None:
#             LogFileName = ArgumentList[Name]
#         else:
#             LogFileName = BibTeXFileName + '.log'
#         print('logfile')
#         print(LogFileName)
# ref: http://python.usyiyi.cn/python_278/library/argparse.html