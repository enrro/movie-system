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

with open('my file.txt', 'r') as f:
    json_data = json.load(f)
    user = User.from_json(json_data)
    print(user.json())
