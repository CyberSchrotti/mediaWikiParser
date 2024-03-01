# import WikiLink

REDIRECT_FLAGS = ["#WEITERLEITUNG", "#REDIRECT"]
NAMESPACES = {"Medium":-2 ,"Spezial":-1 ,"Page":0 ,"Diskussion":1 ,"Benutzer":2 ,"Benutzer Diskussion":3 ,"Wikipedia":4 ,"Wikipedia Diskussion":5 ,"Datei":6 ,"Datei Diskussion":7 ,"MediaWiki":8 ,"MediaWiki Diskussion":9 ,"Vorlage":10 ,"Vorlage Diskussion":11 ,"Hilfe":12 ,"Hilfe Diskussion":13 ,"Kategorie":14 ,"Kategorie Diskussion":15 ,"Portal":100 ,"Portal Diskussion":101 ,"Modul":828 ,"Modul Diskussion":829 ,"Gadget":2300 ,"Gadget Diskussion":2301 ,"Gadget-Definition":2302 ,"Gadget-Definition Diskussion":2303}
NO_ARTICLE_LINK =['DATEI:', ":DATEI", "FILE:", ":FILE", "#",  ":KATEGORIE", "BILD:", "KATEGORIE:", "DOI:"]#['KATEGORIE:', 'WIKIPEDIA:', 'PORTAL:' , 'HILFE:',  ,'VORLAGE:', 'MEDIAWIKI:',  'MODUL:']
HTML_ANCHOR = "#"

def isPageRedirect(text: str):
    return any(flag in text.upper() for flag in REDIRECT_FLAGS)


# def _filterTitle_(link: str):
#     return not any(link.startswith(t) for t in NO_ARTICLE_LINK)

# def _filterTitleWikiLink_(link: WikiLink.WikiLink):
#     return _filterTitle_(link.article)

# def filterLinks(links: [WikiLink.WikiLink]):
#     return list(filter(_filterTitleWikiLink_, links))

def linkRemoveAnchor(link: str):
    return link.split(HTML_ANCHOR)[0]

def mapLinkNameToIndex(link: str, mapping: dict):
    cleanLink = linkRemoveAnchor(link)
    cleanLink = cleanLink.strip()
    cleanLink = cleanLink.replace(" ", "_")
    cleanLink = cleanLink.upper()
    index = mapping.get(cleanLink)
    #if not index and _filterTitle_(cleanLink) and _filterTitle_(link):
    #    print("|",cleanLink,"|", link,"|" , sep="")
    return index

def mapLinkListToIndexList(linkList: list, mapping: dict):
    mappedList = set()
    for l in linkList:
        index = mapLinkNameToIndex(l[0], mapping)
        if index != None:
            mappedList.add(index)
    return list(mappedList)

