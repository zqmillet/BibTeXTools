import PyPDF2 as pyPdf
import datetime
import Classes
import os
import shutil

Month = {'january': 1,
         'february': 2,
         'march': 3,
         'april': 4,
         'may': 5,
         'june': 6,
         'july': 7,
         'august': 8,
         'september': 9,
         'october': 10,
         'november': 11,
         'december': 12}

def String2Date(String):
    Index = 0
    mon = 1
    day = 1
    year = 1
    for c in String:
        if c in '0123456789':
            mon = Month[String[:Index]]
            break
        Index += 1

    String = String[Index:]
    day = int(String[:String.find(',')])
    String = String[String.find(',') + 1:]
    year = int(String)
    # print('day = {0}'.format(day))
    # print('mon = {0}'.format(mon))
    # print('year = {0}'.format(year))

    return datetime.datetime.strptime('{0}-{1}-{2}'.format(year, mon, day), '%Y-%m-%d')

def GetReviewTime(FilePath):
    try:
        PDF = pyPdf.PdfFileReader(open(FilePath, 'rb'))
    except:
        print('PDF file is damaged.')
        return -1

    PageString = PDF.getPage(0).extractText().replace('\n', '')

    ReceiveMark = 'manuscriptreceived'
    AcceptMark = 'accepted'
    PageString = PageString.lower()

    if not 'INVITEDPAPER'.lower() in PageString.lower() and not 'CONTRIBUTEDPAPER'.lower() in PageString.lower():
        return -4

    if ReceiveMark in PageString and AcceptMark in PageString.lower():
        try:
            Index = PageString.find(ReceiveMark) + len(ReceiveMark)
            PageString = PageString[Index:]

            Index = 0
            while True:
                if PageString[Index] in '0123456789':
                    break
                Index += 1
            mon = Month[PageString[:Index]]
            PageString = PageString[Index:]

            Index = 0
            while True:
                if not PageString[Index] in '0123456789':
                    break
                Index += 1
            day = PageString[:Index]
            PageString = PageString[Index + 1:]

            Index = 0
            while True:
                if not PageString[Index] in '0123456789':
                    break
                Index += 1
            year = PageString[:Index]
            PageString = PageString[Index:]

            ReceiveDate = datetime.datetime.strptime('{0}-{1}-{2}'.format(year, mon, day), '%Y-%m-%d')

            Index = PageString.find(AcceptMark) + len(AcceptMark)
            PageString = PageString[Index:]

            Index = 0
            while True:
                if PageString[Index] in '0123456789':
                    break
                Index += 1
            mon = Month[PageString[:Index]]
            PageString = PageString[Index:]

            Index = 0
            while True:
                if not PageString[Index] in '0123456789':
                    break
                Index += 1
            day = PageString[:Index]
            PageString = PageString[Index + 1:]

            Index = 0
            while True:
                if not PageString[Index] in '0123456789':
                    break
                Index += 1
            year = PageString[:Index]
            PageString = PageString[Index:]

            AcceptDate = datetime.datetime.strptime('{0}-{1}-{2}'.format(year, mon, day), '%Y-%m-%d')

            return (AcceptDate - ReceiveDate).days
        except:
            return -3

    return -2

# print('Review Time = {0} days.'.format(GetReviewTime('Test.pdf')))
DataBase = Classes.DataBase()
if not DataBase.Load('References.bib'):
    exit(1)

NewDataBase = Classes.DataBase()

Index = 0
String = ''
for Entry in DataBase.EntryList:
    Index += 1
    print('{0}/{1}'.format(Index, len(DataBase.EntryList)))

    if not 'file' in Entry.TagList:
        print('There is no file tag.')
        continue

    FileName = Entry.TagList['file'].split(':')
    FileName = FileName[0]

    if not os.path.isfile('References\\' + FileName):
        print('There is no file.')
        continue

    shutil.copy('References\\' + FileName, 'Temp\\' + FileName)

    # ReviewTime = GetReviewTime('References\\' + FileName)
    # if ReviewTime > 0:
    #     Entry.TagList['reviewtime'] = str(ReviewTime)
    #     NewDataBase.EntryList.append(Entry)
    #     shutil.copy('References\\' + FileName, 'PE\\' + FileName)
    #
    #     Pages = Entry.TagList['pages'].split('-')
    #     Pages = int(Pages[1]) - int(Pages[0])
    #
    #     String += '{0} {1} {2}\n'.format(Entry.CitationKey, ReviewTime, Pages)
    #
    # elif ReviewTime == -1:
    #     # del Entry.TagList['file']
    #     pass
    # elif ReviewTime == -2:
    #     print('There is no mark in {0}.'.format(Entry.CitationKey))
    #     pass
    # elif ReviewTime == -3:
    #     print('Syntax Error in {0}.'.format(Entry.CitationKey))
    #     pass
    # elif ReviewTime == -4:
    #     print('This is not invited paper.'.format(Entry.CitationKey))
    #     shutil.copy('References\\' + FileName, 'PE\\' + FileName)
    #     pass

# for Comment in DataBase.CommentList:
#     NewDataBase.CommentList.append(Comment)
#
# NewDataBase.Save('NewReferences.bib', 'utf-8')
# File = open('References.dat', 'w')
# File.write(String)
# File.close()










