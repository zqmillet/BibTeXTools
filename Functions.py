def GetFullDoiUrl(Doi):
    if Doi.lower().startswith('http://'):
        return Doi
    elif Doi.lower().startswith('https://'):
        return Doi
    else:
        return 'https://doi.org/' + Doi.strip('/')
