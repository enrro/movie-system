from movie import Movie
from user import User


# user = User("Jose")
# my_movie = Movie("The Matrix", "Sci-Fi", True)
# print(user)
# user.movies.append(my_movie)
# user.add_movie("The interview", "comedy")
# print(user.watched_movies())
#
# user.save_to_file()

user = User.load_from_file("Jose.txt")
print(user.movies)
# with open('my_file.txt', 'w') as f:
#     f.write('hello world')
