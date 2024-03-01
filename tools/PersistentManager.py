
import pickle
import json

def saveParsedPages(parsedPages, path):
    print("save parsed pages", path)
    with open(path, "wb") as f:
        pickle.dump(parsedPages, f)

def loadParsedPages(path):
    with open(path, "rb") as f:
        return pickle.load(f)
    
def saveGraph(parsedPages, path):
    with open(path, "wb") as f:
        pickle.dump(parsedPages, f)

def loadGraph(path):
    with open(path, "rb") as f:
        return pickle.load(f)

def jsonDump(wikipages: list, path):
    with open(path, 'a') as f:
        for w in wikipages:
            json.dump(w, f)#, indent=0)
            f.write("\n")

def makeAdjacenclistTuple(article, id, isredirect, links):
    return (article, id, isredirect, links)

def getArticleFromAdjaTuple(adjacenceTuple):
    return adjacenceTuple[0]

def getIdFromAdjaTuple(adjacenceTuple):
    return adjacenceTuple[1]

def getRidirectFromAdjaTuple(adjacenceTuple):
    return adjacenceTuple[2]

def getLinksFromAdjaTuple(adjacenceTuple):
    return adjacenceTuple[3]

def mergeAdjacenclistPickels(pickelFiles :list, outputFile :str):

    
    merged = []

    for fname in pickelFiles:
        print("load: " , fname)
        merged.extend(loadParsedPages(fname))

    saveParsedPages(merged, outputFile)