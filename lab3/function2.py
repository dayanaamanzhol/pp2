# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def is_above_5_5(movie):
    return movie['imdb'] > 5.5

def above_5_5(movies):
    filtered = []
    for movie in movies:
        if is_above_5_5(movie):
            filtered.append(movie)
    return filtered

def Сategory(movies, category):
    category_movies = []
    for movie in movies:
        if movie['category'] == category:
            category_movies.append(movie)
    return category_movies

def average(movies):
    total_score = 0
    for movie in movies:
        total_score += movie['imdb']
    return total_score / len(movies)

def averagec(movies, category):
    category_movies = Сategory(movies, category)
    return average(category_movies)


print(is_above_5_5({"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"}))  
print(above_5_5(movies))
print(Сategory(movies, "Romance"))
print(average(movies))
print(averagec(movies, "Romance"))
