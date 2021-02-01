# this is a script which converts a text into a frequency dictionary
'''
my first python script
    @bogdan
'''
import sys, re, os

FileInput = open(sys.argv[1],'r')

DictionaryFrq = {}
for Line in FileInput:
    Line = re.sub('<.*?>', '', Line)
    Line = Line.lower()
    Line = Line.strip()
    ListOfWords = re.split('[ ,\.:;\!\(\)\"\[\]]+', Line)
    # sys.stdout.write( str( ListOfWords ) + '\n' )

    # { word1 : 4 , word2 : 4, word3 : 2 }
    for Word in ListOfWords:
        try:
            DictionaryFrq[Word] += 1
        except:
            DictionaryFrq[Word] = 1

# sys.stdout.write( str( DictionaryFrq ) + '\n' )
for Word, Frq in sorted( DictionaryFrq.items() , key=lambda x: x[1], reverse=True) :
    sys.stdout.write(Word + '\t' + str(Frq) + '\n')