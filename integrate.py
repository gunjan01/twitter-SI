import tweet11
import IMDB

movie=raw_input("enter movie name")
one=tweet11.twitterRating(movie)
two=IMDB.rating(movie)

two = float(two)/10
final = float(one+two)/2

print final


