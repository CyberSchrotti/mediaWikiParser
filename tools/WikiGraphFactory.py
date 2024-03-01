import networkit as nk
from . import PersistentManager as pm

def makeGraphNkit(adjacentListPath=""):
        
        print("load adjacence list ", adjacentListPath)
        adjacenceList = pm.loadParsedPages(adjacentListPath)

        g = nk.Graph(n=len(adjacenceList), directed=True, weighted=False)
        print("generate graph ...")
        for i, node in enumerate(adjacenceList):
            if len(pm.getLinksFromAdjaTuple(node)) > 0 and pm.getArticleFromAdjaTuple(node):
                for e in pm.getLinksFromAdjaTuple(node):
                    g.addEdge(pm.getArticleFromAdjaTuple(node), e, addMissing=True, checkMultiEdge=True)
                    
            if i % 10000 == 0:
                print(i, "/" , len(adjacenceList), end="\r")
        print(i, "/" , len(adjacenceList))
        print("generate done")
        return g