import argparse
import Classes
import os
import sys

Parser = argparse.ArgumentParser()
Parser.add_argument('BibTeXFileName',
                    help='the file name of BibTeX database.')
Parser.add_argument('-d', '--delete',
                    nargs   = '*',
                    metavar = 'tag',
                    action  = Classes.ByOrder,
                    help    = 'delete tags of all entries in the database.')
Parser.add_argument('-f', '--fetch',
                    nargs   = '*',
                    metavar = 'tag',
                    action  = Classes.ByOrder,
                    help    = 'fetch tags of all entries in the database.')
Parser.add_argument('--clearempty',
                    nargs   = '*',
                    metavar = 'tag',
                    action  = Classes.ByOrder,
                    help    = 'clear the empty tags of all entries, if tag name list is empty, all empty tags in database will be deleted.')
Parser.add_argument('-r', '--rename',
                    nargs   = 2,
                    metavar = ('oldtagname', 'newtagname'),
                    action  = Classes.ByOrder,
                    help    = 'rename tags of all entries from oldtagname to newtagname.')
Parser.add_argument('-c', '--copy',
                    nargs   = 2,
                    metavar = ('tagname1', 'tagname2'),
                    action  = Classes.ByOrder,
                    help    = "copy the tagname1's content content tagname2.")
Parser.add_argument('--downloadfullpapers',
                    nargs   = 0,
                    action  = Classes.ByOrder,
                    help    = "download the full papers of each entry.")
Parser.add_argument('--fullpaper',
                    nargs   = 1,
                    metavar = 'directory',
                    help    = 'set the directory of downloaded full papers, if this option is not specified, the directory is current directory.')
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
Parser.add_argument('-e', '--encoding',
                    nargs   = 1,
                    metavar = 'encoding',
                    help    = 'set the encoding of the input file, if this option is not specified, the encoding is utf-8.')
Parser.add_argument('-v', '--version',
                    action  = 'version',
                    version = 'BibTeXTools 0.10.',
                    help    = 'show the version of BibTeXTools.')

Arguments = None
try:
    Arguments = Parser.parse_args(sys.argv[1:])
except:
    exit(1)
OrderedArgumentList = Arguments.OrderedArgumentList

Encoding = 'utf-8'
# Handle parameter '-e', '--encoding'.
if Arguments.encoding is not None:
    Encoding = Arguments.encoding

# Handle parameter 'BibTeXFileName'.
BibTeXFileName = Arguments.BibTeXFileName
if not os.path.isfile(BibTeXFileName):
    print('The file "{0}" does not exist.'.format(BibTeXFileName))
    exit(1)

BibTeXDataBase = Classes.DataBase()
if not BibTeXDataBase.Load(BibTeXFileName, Encoding):
    exit(1)

OutputFileName = BibTeXFileName
LogFileName = BibTeXFileName + '.log'

# Handle parameter '-o', '--output'.
if Arguments.output is not None:
    OutputFileName = Arguments.output[0]

# Handle parameter '--logfile'.
if Arguments.logfile is not None:
    LogFileName = Arguments.logfile

# Handle parameter '--fullpaper'.
FullPaperDirectory = '.\\'
if Arguments.fullpaper is not None:
    FullPaperDirectory = Arguments.fullpaper

# Handle the ordered arguments.
for Argument in OrderedArgumentList:
    if Argument[0] == 'delete':
        TagNameList = Argument[1]
        BibTeXDataBase.DeleteTags(TagNameList)
    elif Argument[0] == 'fetch':
        TagNameList = Argument[1]
        BibTeXDataBase.FetchTags(TagNameList)
    elif Argument[0] == 'rename':
        BibTeXDataBase.RenameTag(Argument[1][0], Argument[1][1])
    elif Argument[0] == 'copy':
        BibTeXDataBase.CopyTag(Argument[1][0], Argument[1][1])
    elif Argument[0] == 'clearempty':
        TagNameList = Argument[1]
        BibTeXDataBase.ClearEmptyTags(TagNameList)
    elif Argument[0] == 'downloadfullpapers':
        BibTeXDataBase.DownloadFullPaper(FullPaperDirectory)

BibTeXDataBase.Save(OutputFileName)

# Handle parameter '-l', '--log'.
SaveLogFile = Arguments.log
if SaveLogFile:
    LogFile = open(LogFileName, 'w', encoding='utf-8')
    for Commit in BibTeXDataBase.CommitList:
        LogFile.write(Commit + '\n')
    LogFile.close()