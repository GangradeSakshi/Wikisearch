import wikipedia

def searchQuery():
    query = raw_input("What do you want to search today")
    print wikipedia.summary(query, sentences=2)   
        
searchQuery()



