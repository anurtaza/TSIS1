from dict_of_movies import movies

def check_to_above(movie_name):
    for movie in movies:
        if movie_name == movie['name'] and movie['imdb'] > 5.5:
            return True
        return False


def get_movies_above_imdb_score(movies):
    return [movie for movie in movies if check_to_above(movie)]


def get_movies_by_category(movies, category):
    return [movie for movie in movies if movie['category'] == category]

def calculate_average_imdb_score(movies):
    total_score = sum(movie['imdb'] for movie in movies)
    return total_score / len(movies)

def calculate_average(movies, category):
    category_movies = get_movies_by_category(movies, category)
    return calculate_average(category_movies)



movie_name = input("Enter the movie name: ")
is_above_5_5 = check_to_above(movie_name)
print(is_above_5_5)

average_score_romance = calculate_average(movies, "Romance")
print(f"Average IMDb score for Romance movies: {average_score_romance:.2f}")
