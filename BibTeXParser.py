import ErrorMessage
import ParserState
import CharList
import Classes

def BibTeXParse(FileName, LiteratureList):
    BibTeXFile = open(FileName, 'r', encoding='utf-8')

    LiteratureType = ''
    LiteratureHash = ''

    SaveCharIndex = 0
    SaveLineIndex = 0
    CharIndex = 0
    OldChar = ''
    LineIndex = 1
    BraceNumber = 0

    State = ParserState.Idle

    LiteratureList.clear()

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
                State = ParserState.ReadType
                LiteratureType = ''
                LiteratureHash = ''
        elif State == ParserState.ReadType:
            if Char == '{':
                State = ParserState.ReadHash
                BraceNumber = 1
                LiteratureType = BibTeXString[SaveCharIndex + 1:CharIndex]
                SaveCharIndex = CharIndex
            elif Char in CharList.IllegalCharOfType:
                print(ErrorMessage.IllegalCharInType.format(LineIndex, Char))
                return False
            else:
                pass
        elif State == ParserState.ReadHash:
            if Char == ',':
                State = ParserState.ReadProperty
                SaveLineIndex = LineIndex
                LiteratureHash = BibTeXString[SaveCharIndex + 1:CharIndex]
                SaveCharIndex = CharIndex
            elif Char in CharList.IllegalCharOfHash:
                print(ErrorMessage.IllegalCharInHash.format(LineIndex, Char))
                return False
            pass
        else:  # State == ParserState.ReadProperty
            if Char == '{':
                BraceNumber += 1
            elif Char == '}':
                BraceNumber -= 1
                if BraceNumber == 0:
                    State = ParserState.Idle
                    PropertyString = BibTeXString[SaveCharIndex + 1:CharIndex]
                    Literature = Classes.Literature(LiteratureType, LiteratureHash)

                    if PropertyParse(PropertyString, Literature.PropertyList, SaveLineIndex):
                        LiteratureList.append(Literature)
                    else:
                        return False
            else:
                pass

        CharIndex += 1
        OldChar = Char

    if BraceNumber > 0:
        print(ErrorMessage.BracketNotClosed.format(SaveLineIndex, LiteratureHash))
        return False

    return True

def PropertyParse(PropertyString, PropertyList, LineIndex = 0):
    OldChar = ''
    SaveCharIndex = 0
    CharIndex = 0
    BracketNumber = 0
    State = ParserState.Idle
    Name = ''
    PropertyList.clear()

    for Char in PropertyString:
        # Count lines
        if Char == '\n':
            if OldChar != '\r':
                LineIndex += 1
        elif Char == '\r':
            LineIndex += 1
        else:
            pass

        # Parse property string
        if State == ParserState.Idle:
            if Char in CharList.EmptyChar:
                pass
            if Char in CharList.IllegalCharOfName:
                print(ErrorMessage.IllegalCharInName.format(LineIndex, Char))
                return False
            else:
                SaveCharIndex = CharIndex
                State = ParserState.ReadName
        elif State == ParserState.ReadName:
            if Char in CharList.IllegalCharOfName:
                print(ErrorMessage.IllegalCharInName.format(LineIndex, Char))
                return False
            elif Char == '=':
                State = ParserState.WhichMode
                Name = PropertyString[SaveCharIndex:CharIndex].strip()
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
            else:
                print(ErrorMessage.IllegalCharAfterEqualSign.format(LineIndex, Char))
                return False
        elif State == ParserState.BracketMode:
            if Char == '{':
                BracketNumber += 1
            elif Char == '}':
                BracketNumber -= 1
                if BracketNumber == 0:
                    PropertyList[Name] = PropertyString[SaveCharIndex + 1:CharIndex]
                    State = ParserState.WaitComma
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
                print(ErrorMessage.IllegalCharBetweenProperties.format(LineIndex, Char))
                return False
        else:
            pass

        OldChar = Char
        CharIndex += 1

    return True



