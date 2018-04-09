import operator 
import pandas as pd
from imdb import IMDb
#--------------Helper functions----------------------------------------
def addMovie(movieID):
    return 

def getmovieTitle(movieID):
    title = ia.get_movie(movieID)
    return title

def jaccard_similiar_with_strings(a,b):
    if isinstance(a, list): a = set(a)
    if isinstance(b, list): b = set(b)
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

# Based on 'Weighted Jaccard.'
# Weighted Jaccard definition is:
# J(A,B)= ∑i min(ai,bi) / ∑i max(ai,bi)
# 
# my distance formula:
# distace = weighted(a,b) = (occurences of b in c) / (c.total_values)
# where c is a weighted dictionary that shows how many times each genre appears in the selections
# where a is a list of the list of genres
# where b is a list of genres of the compared to movie
# so the result will be between 0.0 - 1.0
def weighted_jaccard_similarity(a,b):
    # in this case, 'a' is all the selections that the user has made so far
    # build the weighted dictionary:
    c = {'total': 0}
    for el in a:
        for genre in el:
            #print(genre)
            if genre in c: c[genre] += 1
            else: c[genre] = 1
            c['total'] += 1
    
    numerator = 0
    denomenator = c['total']
    for genre in b:
        if genre in c:
            numerator += c[genre]
    return numerator / denomenator

# looks at the entire data set ('data')
# and returns the k nearest neighbors based on the distance metric
# 'target' is the movie that we are comparing to
# returns the index of the k movies that are closest
def getNeighbors(data, target, k):
    distances = []
    for x in range(len(data)):
        dist = jaccard_similiar_with_strings(target, data[x])
        distances.append((x, data[x], dist))
    distances.sort(key=operator.itemgetter(2), reverse=True)  # sort based on the distance
#    print("\nThe raw distance information sorted:")
#    print(distances)
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

ia = IMDb()
df = pd.read_csv("movies.csv")


selection = ['Toy Story','Jumanji']

X=df['genres'].tolist()
titles=df['title'].tolist()
#print('typeof titles', type(titles))
#target=[toy_story]

result = getNeighbors(X,selection,k=10)
print('results', result)
#print("\n\nThe movie that is closest to Toy Story is:")
#print(titles[result[0]])

#print('type of df',df['title'].tolist())

#result = getNeighbors(X,toy_story,k=5)
#print("\n\nThe 5 closest movies that are closest to Toy Story are (in order):")
for i in result:
    print(titles[result[i]])






#df[df['title'].str.contains('Jumanji')== True]
#print(df[df['title'].str.contains('toy story'.title())== True])
#cont = True
#selected = []
#prevSelected = []
#
#while cont == True:
#    print("Please choose an option: Using the numbers")
#    print("0: Add movie. ex 2 112233")
#    print("1: Show the selected terms")
#    print("2: show the recommended movies")
#    print("3: clear the search")
#    print("4: quit")
#    
#    chosen = input()
#    chosen = chosen.split(' ')
#    option = chosen[0]
#    if chosen[0] == 0:
#        variable = chosen[1]
#    
#    if option == '4': #quit number
#        cont = False
#    
#    elif option == '0': #put code here to add movie
#        addMovie()
#        continue
#    
#    elif option == '1':#show Selected terms
#        continue
#    
#    elif option == '2':#show the recommended movies
#        continue
#    
#    elif option == '3':#show the previous selected selected
#        continue
#    
#    else:
#        print("please enter a valid choice")
#        continue
#    
    
    









#def jaccard_similiar_with_strings(a,b):
#    if isinstance(a, list): a = set(a)
#    if isinstance(b, list): b = set(b)
#    c = a.intersection(b)
#    return float(len(c)) / (len(a) + len(b) - len(c))
#
## looks at the entire data set ('data')
## and returns the k nearest neighbors based on the distance metric
## 'target' is the movie that we are comparing to
## returns the index of the k movies that are closest
#def getNeighbors(data, target, k):
#    distances = []
#    for x in range(len(data)):
#        dist = jaccard_similiar_with_strings(target, data[x])
#        distances.append((x, data[x], dist))
#    distances.sort(key=operator.itemgetter(2), reverse=True)  # sort based on the distance
#    print("\nThe raw distance information sorted:")
#    print(distances)
#    neighbors = []
#    for x in range(k):
#        neighbors.append(distances[x][0])
#    return neighbors
#
#toy_story = ['Adventure','Animation','Children','Comedy','Fantasy'] #toy story
#princess_bride = ['Action','Adventure','Comedy','Fantasy','Romance'] #princess bride
#aliens = ['Action','Adventure','Horror','Sci-Fi'] #Aliens
#once_upon = ['Crime','Drama'] #once upon a time in america
#die_hard_2 = ['Action','Adventure','Thriller'] #die hard 2
#
#print("Example Jaccard Similarity distances:")
#print(jaccard_similiar_with_strings(toy_story,princess_bride))
#print(jaccard_similiar_with_strings(toy_story, aliens))
#print(jaccard_similiar_with_strings(princess_bride, aliens))
#
#X=[toy_story,princess_bride,aliens,once_upon,die_hard_2]
#titles=['Toy Story','Princess Bride', 'Aliens','Once Upon a Time in America','Die Hard 2']
#
#target=[toy_story] 
#
#result = getNeighbors(X,toy_story,k=1)
#print("\n\nThe movie that is closest to Toy Story is:")
#print(titles[result[0]])
#
#result = getNeighbors(X,toy_story,k=5)
#print("\n\nThe 5 closest movies that are closest to Toy Story are (in order):")
#for i in result:
#    print(titles[result[i]])


































