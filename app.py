import os.path

from movie import Movie
from user import User
import json


# # loading and creating a user with movies
# user = User("Jose")
# my_movie = Movie("The Matrix", "Sci-Fi", True)
# user.movies.append(my_movie)
# user.add_movie("The interview", "comedy")
#
# # save to file as csv and load
# # user.save_to_file()
# # user = User.load_from_file("Jose.txt")
# # print(user.movies)
#
# # how to write json to file
# # print(user.json())
# # with open('my file.txt', 'w') as f:
# #     json.dump(user.json(), f)
# # how to load json file
# with open('my file.txt', 'r') as f:
#     json_data = json.load(f)
#     user = User.from_json(json_data)
#     print(user.json())
#

def menu():
    name = input("whats your name: ")
    filename = f"{name}.txt"
    if file_exists(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
    else:
        user = User(name)

    user_input = input("Enter 'a' to add a movie, 's' to see the list of movies,"
                       " 'w' to set a movie as watched, 'l' to see the list of watched movies 'f' to save"
                       " or 'q' to save and quit: ")

    while user_input != 'q':
        if user_input == 'a':
            movie_name = input("Enter a movie name: ")
            genre = input("Enmter a movie genre: ")
            user.add_movie(movie_name, genre)
        elif user_input == 's':
            for movie in user.movies:
                print(f"Name: {movie.name} Genre: {movie.genre} Watched: {movie.watched}")
        elif user_input == 'w':
            movie_name = input("enter the movie name to set as watched: ")
            user.set_watched(movie_name)
        elif user_input == 'd':
            movie_name = input("Enter the movie name to delete: ")
            user.delete_movie(movie_name)
        elif user_input == 'l':
            for movie in user.watched_movies():
                print(f"Name: {movie.name} Genre: {movie.genre} Watched: {movie.watched}")
        elif user_input == 'f':
            with open(filename, 'w') as f:
                json.dump(user.json(), f)
        user_input = input("Enter 'a' to add a movie, 's' to see the list of movies,"
                           " 'w' to set a movie as watched, 'l' to see the list of watched movies 'f' to save"
                           " or 'q' to save and quit")


def file_exists(file):
    return os.path.isfile(file)

menu()