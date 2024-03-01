
import mwparserfromhell as mwpfh

SECTIONS_TO_IGNORE = ['Literatur', 'Weblinks','Einzelnachweise','Siehe auch','Quellen']
REF = "ref"
TEXT_TOKEN = 'text'

def handleRefTagClosing(toIt):
    isRef = False

    # got to end of tag
    for token in toIt:
        tokenType = type(token)
        if tokenType == mwpfh.parser.tokens.Text and token[TEXT_TOKEN] == REF:
            isRef = True
        elif tokenType == mwpfh.parser.tokens.TagCloseClose:
            return isRef
        elif tokenType == mwpfh.parser.tokens.TagCloseSelfclose:
            return isRef


def handleRefTag(toIt):
    # got to end of tag
    for token in toIt:
        tokenType = type(token)
        
        if tokenType == mwpfh.parser.tokens.TagCloseOpen:
            break
        elif tokenType == mwpfh.parser.tokens.TagCloseSelfclose:
            return
        
    # find end tag of ref    
    for token in toIt:
        tokenType = type(token)
        if tokenType == mwpfh.parser.tokens.TagOpenClose and handleRefTagClosing(toIt):
            return
        

def handleTagOpen(toIt):
    for token in toIt:
        tokenType = type(token)
        if tokenType == mwpfh.parser.tokens.Text and token[TEXT_TOKEN] == REF:
            handleRefTag(toIt)
            return
        elif tokenType == mwpfh.parser.tokens.TagCloseSelfclose:
            return
        elif tokenType == mwpfh.parser.tokens.TagCloseOpen:
            return


def handleComment(toIt):
    for token in toIt:
        tokenType = type(token)
        if tokenType == mwpfh.parser.tokens.CommentEnd :
            return


def handleHeading(toIt):
    reachedSectionsToOmmit = False
    for token in toIt:
        tokenType = type(token)
        if tokenType == mwpfh.parser.tokens.Text and token[TEXT_TOKEN].strip() in SECTIONS_TO_IGNORE:

            reachedSectionsToOmmit = True
        if tokenType == mwpfh.parser.tokens.HeadingEnd :
            return reachedSectionsToOmmit


def handleWikilink(toIt): # TODO handle nested links  e.g. [[foo| baro asd [[linkto]] bob bar]]
    link = [""]
    for token in toIt:
        tokenType = type(token)
        if tokenType == mwpfh.parser.tokens.Text:
            link[-1] += token[TEXT_TOKEN]
        elif tokenType == mwpfh.parser.tokens.WikilinkSeparator:
            link.append("")
        elif tokenType == mwpfh.parser.tokens.WikilinkClose:
            if len(link) == 1:
                return (link[0], "")
                #return WikiLink.WikiLink(link[0], link[0])
            else:
                return (link[0], link[1][:50])
                #return WikiLink.WikiLink(link[0], link[1])


def iterateTokens(tokens: list[mwpfh.parser.tokens]):

    wikilinks = list()
    toIt = iter(tokens)

    for token in toIt:
        tokenType = type(token)
        if tokenType == mwpfh.parser.tokens.TagOpenOpen:
            handleTagOpen(toIt)
        elif tokenType == mwpfh.parser.tokens.CommentStart:
            handleComment(toIt)
        elif tokenType == mwpfh.parser.tokens.HeadingStart and handleHeading(toIt):
            #reached Sections To Ommit 
            break
        elif tokenType == mwpfh.parser.tokens.WikilinkOpen:
            link = handleWikilink(toIt)
            wikilinks.append(link)

    return wikilinks   
        

def extractTokens(text: str):
    if not mwpfh.parser.use_c:
        print("CTokenizer not available!!")
        exit(1)
    tokens = mwpfh.parser.CTokenizer().tokenize(text, 0, True)
    return tokens 


def processText(text: str):
    tokenList = extractTokens(text)
    links = iterateTokens(tokenList)
    #if len(links) == 1:
    #    print(tokenList)
    #    print(text)
    #    exit()
    return links
