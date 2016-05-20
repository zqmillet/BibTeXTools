import ErrorMessage
import ParserState
import CharList
import Classes

def BibTeXParse(FileName, EntryList, CommentList, Encoding = 'utf-8'):
    BibTeXFile = open(FileName, 'r', encoding = Encoding)

    EntryType = ''
    EntryCitationKey = ''

    SaveCharIndex = 0
    SaveLineIndex = 0
    CharIndex = 0
    OldChar = ''
    LineIndex = 1
    BraceNumber = 0

    State = ParserState.Idle

    EntryList.clear()
    CommentList.clear()

    BibTeXString = BibTeXFile.read()
    BibTeXFile.close()
    for Char in BibTeXString:
        # Count lines
        if Char == '\n':
            if OldChar != '\r':
                LineIndex += 1
        elif Char == '\r':
            LineIndex += 1
        else:
            pass

        # Parse BibTeX
        if State == ParserState.Idle:
            if Char == '@':
                SaveCharIndex = CharIndex
                State = ParserState.ReadEntryType
                EntryType = ''
                EntryCitationKey = ''
        elif State == ParserState.ReadEntryType:
            if Char == '{':
                EntryType = BibTeXString[SaveCharIndex + 1:CharIndex]
                SaveCharIndex = CharIndex
                BraceNumber = 1
                if EntryType.lower() == 'comment':
                    State = ParserState.ReadComment
                else:
                    State = ParserState.ReadEntryCitationKey
            elif Char in CharList.IllegalCharOfEntryType:
                print(ErrorMessage.IllegalCharInEntryType.format(LineIndex, Char))
                return False
            else:
                pass
        elif State == ParserState.ReadEntryCitationKey:
            if Char == ',':
                State = ParserState.ReadTagList
                SaveLineIndex = LineIndex
                EntryCitationKey = BibTeXString[SaveCharIndex + 1:CharIndex]
                SaveCharIndex = CharIndex
            elif Char in CharList.IllegalCharOfEntryCitationKey:
                print(ErrorMessage.IllegalCharInEntryCitationKey.format(LineIndex, Char))
                return False
            pass
        elif State == ParserState.ReadComment:
            if Char == '{':
                BraceNumber += 1
            elif Char == '}':
                BraceNumber -= 1
                if BraceNumber == 0:
                    CommentList.append(BibTeXString[SaveCharIndex + 1:CharIndex])
                    State = ParserState.Idle
        else:  # State == ParserState.ReadTagList
            if Char == '{':
                BraceNumber += 1
            elif Char == '}':
                BraceNumber -= 1
                if BraceNumber == 0:
                    State = ParserState.Idle
                    TagListString = BibTeXString[SaveCharIndex + 1:CharIndex]
                    Entry = Classes.Entry(EntryType, EntryCitationKey)

                    if TagListParse(TagListString, Entry.TagList, SaveLineIndex):
                        EntryList.append(Entry)
                    else:
                        return False
            else:
                pass

        CharIndex += 1
        OldChar = Char

    if BraceNumber > 0:
        print(ErrorMessage.BracketNotClosed.format(SaveLineIndex, EntryCitationKey))
        return False

    return True

def TagListParse(TagListString, TagList, LineIndex = 0):
    OldChar = ''
    SaveCharIndex = 0
    CharIndex = 0
    BracketNumber = 0
    State = ParserState.Idle
    TagName = ''
    TagList.clear()

    for Char in TagListString:
        # Count lines
        if Char == '\n':
            if OldChar != '\r':
                LineIndex += 1
        elif Char == '\r':
            LineIndex += 1
        else:
            pass

        # Parse TagListString
        if State == ParserState.Idle:
            if Char in CharList.EmptyChar:
                pass
            if Char in CharList.IllegalCharOfTagName:
                print(ErrorMessage.IllegalCharInTagName.format(LineIndex, Char))
                return False
            else:
                SaveCharIndex = CharIndex
                State = ParserState.ReadTagName
        elif State == ParserState.ReadTagName:
            if Char in CharList.IllegalCharOfTagName:
                print(ErrorMessage.IllegalCharInTagName.format(LineIndex, Char))
                return False
            elif Char == '=':
                State = ParserState.WhichMode
                TagName = TagListString[SaveCharIndex:CharIndex].strip().lower()
                SaveCharIndex = CharIndex
            else:
                pass
        elif State == ParserState.WhichMode:
            if Char in CharList.EmptyChar:
                pass
            elif Char == '{':
                BracketNumber = 1
                State = ParserState.BracketMode
                SaveCharIndex = CharIndex
            elif Char == '"':
                State = ParserState.QuotationMode
                SaveCharIndex = CharIndex
            else:
                State = ParserState.NoneMode
                SaveCharIndex = CharIndex
        elif State == ParserState.BracketMode:
            if Char == '{':
                BracketNumber += 1
            elif Char == '}':
                BracketNumber -= 1
                if BracketNumber == 0:
                    TagList[TagName] = TagListString[SaveCharIndex + 1:CharIndex]
                    State = ParserState.WaitComma
            else:
                pass
        elif State == ParserState.NoneMode:
            if Char == ',':
                TagList[TagName] = TagListString[SaveCharIndex:CharIndex]
                State = ParserState.Idle
            else:
                pass
        elif State == ParserState.QuotationMode:
            pass
        elif State == ParserState.WaitComma:
            if Char == ',':
                State = ParserState.Idle
            elif Char in CharList.EmptyChar:
                pass
            else:
                print(ErrorMessage.IllegalCharBetweenTags.format(LineIndex, Char))
                return False
        else:
            pass

        OldChar = Char
        CharIndex += 1

    if State == ParserState.NoneMode:
        TagList[TagName] = TagListString[SaveCharIndex:CharIndex]

    return True



