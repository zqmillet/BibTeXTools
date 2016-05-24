from html.parser import HTMLParser
import requests

class IEEEXplore(HTMLParser):
    ExistFullPaper = False
    FullPaperPath = ''

    def Parse(self, URL):
        if not 'ieeexplore.ieee.org' in URL.lower():
            return False

        ParameterList = URL[URL.index('?') + 1:].split('&')
        for Parameter in ParameterList:
            if Parameter.lower().startswith('arnumber'):
                ArticleNumber = Parameter[Parameter.index('=') + 1:]
                Address = 'http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=' + ArticleNumber
                break
            else:
                return False

        HTMLCode = requests.get(Address)
        self.feed(HTMLCode.text)
        return self.ExistFullPaper

    def handle_starttag(self, TagName, AttributeList):
        if TagName.lower() == 'frame':
            for Attribute in AttributeList:
                if Attribute[0].lower() == 'src':
                    if 'ieeexplore.ieee.org' in Attribute[1].lower():
                        self.ExistFullPaper = True
                        self.FullPaperPath = Attribute[1]
                        return

    def handle_endtag(self, TagName):
        pass

    def handle_data(self, Data):
        pass

