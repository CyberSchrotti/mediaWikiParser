Parser for MediaWiki Wikipedia xml dumps to get a link-graph and insights

### Resources from wikipedia

- Unpacked list of all articles titles e.g. https://dumps.wikimedia.org/dewiki/latest/ dewiki-latest-all-titles-in-ns0.gz 
- Unpacked wikipedia xml dumps e.g. https://dumps.wikimedia.org/dewiki/latest/ dewiki-latest-pages-articles1.xml-p1p297012.bz2

# Known issues  

Known issues with the link parser

## -- in link text
38500 0.06438965 Ungarischer Volksaufstand links:190 re:False ('Ungarisches Wappen#Geschichte', 'Kossuth-Wappenich hab das jetzt mal so verlinkt, das braucht doch keinen eigenen Artikel, oder?--[[Benutzer:Hannes2|Hannes2]] 17:13, 12. Jul 2005 (CEST)')
 52500 0.06452805 Lennep links:144 re:False ('Datei:Kölner Straße 82 (Remscheid-Lennep) (3).jpg', 'mini|Kreishaus Lennep (1889 erbaut)refInternetquelle urlhttp://www.baukunst-nrw.de/objekte/Kreishaus-Lennep-heute-Pestalozzi-Schule--1899.htm titelKreishaus Lennep (heute Pestalozzi-Schule) spracheen abruf2022-12-17ref – ehemals Sitz der Kreisverwaltung')
 74000 0.06474163 Lydien links:216 re:False ('Datei:Map of Lydia ancient times-de.svg', 'mini|hochkant=1.5|Ausdehnung des Herrschaftsgebietes Lydiens in der Mitte des 6.nbspJahrhunderts v.nbspChr. unter König Kroisos. <ref>{{Internetquelle | url=http://www.ancientanatolia.com/historical/lydian period.htm | titel=Lydian Period | titelerg=( 900 – 547 BCE.) | hrsg=Thracian Ltd | datum=2011-04-03 | abruf=2021-03-31 | sprache=en | offline=ja}}</ref> --- auskommentiert, da Quelle nicht in Archiv zu finden ist und mit Space korrigierter Pfad auf eine andere Adresse redirected wird  Die rote Grenzlinie zeigt eine leicht abweichende Fassung des rekonstruierten Grenzverlaufs.refInternetquelle  autorTore Kjeilen  urlhttp://i-cias.com/e.o/lydia.htm  titelLydia  hrsgLookLex Encyclopaedia  archiv-urlhttps://web.archive.org/web/20110829021634/http://i-cias.com/e.o/lydia.htm  archiv-datum2011-08-29  abruf2021-03-31  sprache ref')
 75500 0.06475530 Bad Zwischenahn links:269 re:False ('Datei:Muehle Bad Zwischenahn 3501.JPG', "mini|Kappenwindmühle im KurparkrefWebarchivurlhttp://www.xn--niederschsische-mhlenstrasse-cnc44e.de/index.php?id=424 wayback20160307022451 textNiedersächsische Mühlenstraße: ''Kappenwindmühle Bad Zwischenahn'' archiv-bot2023-06-13 06:36:14 InternetArchiveBot ref")
 95000 0.06495491 Cholin links:99 re:False ('Datei:Cl-.svg', 'x35px|Cl--Ion')
 100500 0.064100729 Samogitien links:102 re:False ('Datei:Litauen-regional.png', 'mini|400px|Kulturregionen des heutigen Litauen\ntablewidth100%tr----tdvaligntopalignleft\nFarblegende#e6fefeKleinlitauen')
100732 Oberlitauen links:22 re:False ('Image:Liet-etno-regionai.png', 'thumb|right|300px|divstyletext-align:centerKulturregionen des heutigen Litauendiv\n\ntablewidth100%tr----tdvaligntopalignleft\nFarblegende#e6fefeKleinlitauen')
 117000 0.064117237 Ethidiumbromid links:51 re:False ('Datei:Br-.svg', '28px|Struktur des Br--Ions')
 149500 0.064149714 Konferenz Europäischer Kirchen links:75 re:False ('Datei:WBofinger CEC 1964-25.jpg', 'mini|Konferenz Europäischer Kirchen --- Tagung 1964 --- Aussetzen der Teilnehmer aus der DDR und anderer Staaten des Warschauer Paktes in Beiboot vor Landung in Dänemark')
149714 Konferenz Europäischer Kirchen links:75 re:False ('Datei:WBofinger CEC 1964-36.jpg', 'mini|Konferenz Europäischer Kirchen --- Tagung 1964')
149714 Konferenz Europäischer Kirchen links:75 re:False ('Datei:WBofinger CEC 1964-27.jpg', 'mini|Konferenz Europäischer Kirchen --- Tagung 1964')
 155000 0.064155171

## [[ ]] in link text

[[DATEI:Emma Morano.jpg|mini|hochkant|[[Emma Morano]] im Alter von 30 Jahren]]

## link is url encoded:
####### NEW PAGE ####### Archimedisches Prinzip
|GAU%C3%9FSCHER_INTEGRALSATZ|Gau%C3%9Fscher_Integralsatz#Folgerungen|

## double whitespaces in link
#REDIRECT [[Extended Binary Coded Decimal  Interchange Code]]
