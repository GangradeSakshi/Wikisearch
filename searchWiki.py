import wikipedia

def searchQuery(query):
    #query = raw_input("What do you want to search today")
    searchResult = wikipedia.summary(query, sentences=1)   
    return searchResult
 

"""def searchQuery():
    query = raw_input("What do you want to search today")
    searchResult = wikipedia.summary(query, sentences=1)   
    print searchResult"""

#searchQuery()