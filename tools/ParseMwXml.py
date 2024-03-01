import xml.etree.ElementTree as ET



def extractContentFromXML(elem, myNamespace):
    ns = elem.find("a:ns", myNamespace)
    title = elem.find("a:title", myNamespace)
    id = elem.find("a:id", myNamespace)
    revision = elem.find("a:revision", myNamespace)
    text = revision.find("a:text", myNamespace)
        
    return int(ns.text), title.text, int(id.text), text.text

    

def iterPagesInXMLFile(inputFile):
    context = ET.iterparse(inputFile, events=("end", "start-ns"))

    namespaces = dict()
    for event, elem in context:
        if event == "start-ns":
            if not elem[0]: # prefix is empty
                namespaces["a"] = elem[1] # assign uri to default namespace
            else:
                namespaces[elem[0]] = elem[1]

        if event == "end" and elem.tag == ET.QName(namespaces['a'], "page") :

            yield elem, namespaces
            elem.clear()

    #context.clear()