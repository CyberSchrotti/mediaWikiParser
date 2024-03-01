import bz2
import tools.ParseMwXml as ParseMwXml
import tools.MwTextParser as MwTextParser
import tools.MwUtils as MwUtils
import tools.PersistentManager as PersistentManager
import time
import sys
#from memory_profiler import profile

NAMESPACES = {"Medium":-2 ,"Spezial":-1 ,"Page":0 ,"Diskussion":1 ,"Benutzer":2 ,"Benutzer Diskussion":3 ,"Wikipedia":4 ,"Wikipedia Diskussion":5 ,"Datei":6 ,"Datei Diskussion":7 ,"MediaWiki":8 ,"MediaWiki Diskussion":9 ,"Vorlage":10 ,"Vorlage Diskussion":11 ,"Hilfe":12 ,"Hilfe Diskussion":13 ,"Kategorie":14 ,"Kategorie Diskussion":15 ,"Portal":100 ,"Portal Diskussion":101 ,"Modul":828 ,"Modul Diskussion":829 ,"Gadget":2300 ,"Gadget Diskussion":2301 ,"Gadget-Definition":2302 ,"Gadget-Definition Diskussion":2303}


'''
https://dumps.wikimedia.org/backup-index.html
https://dumps.wikimedia.org/dewiki/latest/
https://mirror.accum.se/mirror/wikimedia.org/dumps/dewiki/
'''

        
    

def processBz2File(pathSource: str, pathAllTiles: str, pathOutput: str):
    pagecounter = 0
    parsedPages = []
    #articleIndex = readAllHeadingAll(pathAllTiles)
    articleIndex, _ = readAllHeadingNS0(pathAllTiles)

    with bz2.open(pathSource, 'rb') as file:
    
        for page, namespaces in ParseMwXml.iterPagesInXMLFile(file):
            pagecounter += 1
            namespace, title, id, text = ParseMwXml.extractContentFromXML(page, namespaces)

            if namespace == NAMESPACES["Page"]:
                links = MwTextParser.processText(text)
                mappedLinks = MwUtils.mapLinkListToIndexList(links, articleIndex)

                parsedPages.append((MwUtils.mapLinkNameToIndex(title, articleIndex),id,MwUtils.isPageRedirect(text), mappedLinks))           

            if pagecounter % 500 == 0:
                print( "\r", pagecounter, sys.getsizeof(parsedPages)/1000, end="")
                #PersistentManager.jsonDump(parsedPages, pathOutput)
                #parsedPages.clear()
       
    print(pagecounter)
    PersistentManager.saveParsedPages(parsedPages, pathOutput)   
    #PersistentManager.jsonDump(parsedPages, pathOutput) 



def readAllHeadingNS0(path):
    headingH2I = dict()
    headingI2H = list()

    with open(path, "r", encoding="utf-8") as f:         

        for index, line in enumerate(f):
            cleanedLine = line.strip().upper()            
            headingH2I[cleanedLine] = index
            headingI2H.append(cleanedLine)
            if index != headingH2I[headingI2H[index]]:
                print("Error parsing Heading File", index, cleanedLine, headingH2I[headingI2H[index]])
                exit(1)

    return headingH2I, headingI2H

def readAllHeadingNS0Pretty(path):
    headingH2I = dict()
    headingI2H = list()

    with open(path, "r", encoding="utf-8") as f:         

        for index, line in enumerate(f):
            cleanedLine = line.strip().replace("_", " ")          
            headingH2I[cleanedLine] = index
            headingI2H.append(cleanedLine)
            if index != headingH2I[headingI2H[index]]:
                print("Error parsing Heading File", index, cleanedLine, headingH2I[headingI2H[index]])
                exit(1)

    return headingH2I, headingI2H

def readAllHeadingAll(path):
    headings = dict()
    with open(path, "r", encoding="utf-8") as f:         

        for index, line in enumerate(f):
            cleanedLine = line.split("\t")[1]
            cleanedLine = cleanedLine.strip().split("_",1)[-1]
            print(line.strip(),"|",cleanedLine, "|", sep="")
            headings[cleanedLine] = index
    return headings

#@profile
def processXMLFile(pathSource: str, pathAllTiles: str, pathOutput: str):
    pagecounter = 0
    parsedPages = []
    #articleIndex = readAllHeadingAll(pathAllTiles)
    articleIndex, _ = readAllHeadingNS0(pathAllTiles)
    
    for page, namespaces in ParseMwXml.iterPagesInXMLFile(pathSource):
        pagecounter += 1
        namespace, title, id, text = ParseMwXml.extractContentFromXML(page, namespaces)

        if namespace == NAMESPACES["Page"]:
            links = MwTextParser.processText(text)
            mappedLinks = MwUtils.mapLinkListToIndexList(links, articleIndex)

            parsedPages.append((MwUtils.mapLinkNameToIndex(title, articleIndex),id,MwUtils.isPageRedirect(text), mappedLinks))           

        if pagecounter % 500 == 0:
            print( "\r", pagecounter, sys.getsizeof(parsedPages)/1000, end="")
            #PersistentManager.jsonDump(parsedPages, pathOutput)
            #parsedPages.clear()
       
    print(pagecounter)
    PersistentManager.saveParsedPages(parsedPages, pathOutput)   
    #PersistentManager.jsonDump(parsedPages, pathOutput)   

def articleIndex2Name(path: str, articleNos):
    _, mapping = readAllHeadingNS0Pretty(path)

    for i in articleNos:
        print(i, mapping[i])

def selectionParsing(files: dict, workingdir: str):

    print("Select files:" , files.keys())
    selection = input()
    file = ""
    if selection in files:
        file = files[selection]
        print("selected " ,  selection, file)
    else:
        print("invalid selection: " + selection)
        exit(1)
    

    sourceFile = workingdir + file + "/" + file

    output = workingdir + "parsedPages/" + "articles"+ selection + ".pkl"

    return sourceFile, output

def getIndexFromNames(allTitlesPath, aNames):
    mapp , _ = readAllHeadingNS0Pretty(allTitlesPath)
    for name in aNames:
        print(name, mapp.get(name, "Not Found"))

def main():

    files = {"4_2":"dewiki-latest-pages-articles4.xml-p4876258p6115464",
             "5_1":"dewiki-latest-pages-articles5.xml-p6115465p7615464",
             "5_2":"dewiki-latest-pages-articles5.xml-p7615465p9115464",
             "5_3":"dewiki-latest-pages-articles5.xml-p9115465p9261244",
             "6_1":"dewiki-latest-pages-articles6.xml-p9261245p10761244",
             "6_2":"dewiki-latest-pages-articles6.xml-p10761245p12261244",
             "6_3":"dewiki-latest-pages-articles6.xml-p12261245p12978619"
            }
    workingdir = "____________"
    allTitles = workingdir + "dewiki-latest-all-titles-in-ns0/dewiki-latest-all-titles-in-ns0"
    
    #sourceFile, output = selectionParsing(files, workingdir)


    
    #articles = [871556, 331135, 330764, 1424674, 25977, 301571, 885681, 885288, 4461413, 4573620, 2025864, 2050174, 383524]
    #articles = [871556, 331135, 330764, 2843760, 20512, 1229907, 383524]
    articles = [1923038, 320536, 438794, 1219076, 4334757, 2539597]
    #processBz2File(sourceFile, allTitles, output)
    #processXMLFile(sourceFile, allTitles, output)
    articleIndex2Name(allTitles, articles)
    #getIndexFromNames(allTitles, ["Lindentunnel", "Illarramendi"])
    

if __name__ == "__main__" :
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print("\nDie Zeitdauer beträgt:", duration, "Sekunden")