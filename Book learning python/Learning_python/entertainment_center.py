import fresh_tomatoes
import media

toy_story = media.Movie("Toy story", "A story of a boy whose toys come to life",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print (toy_story.storyline)

avatar = media.Movie('Avatar', 'A marine on an alien planet',
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print (avatar.storyline)
# avatar.show_trailer()

avnegers = media.Movie('Avengers: Infinity War', 'Superheroes gather to fight a villian',
                       'https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg',
                       "https://www.youtube.com/watch?v=mmZqOKVvWrY")

thor = media.Movie('Thor', 'A story of a Superheroe Thor',
                   'https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg',
                   'https://www.youtube.com/watch?v=JOddp-nlNvQ')

the_hunger_games = media.Movie('The Hunger Games', 'A story of a novel',
                               'https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg',
                               'https://www.youtube.com/watch?v=mfmrPu43DF8')

deadpool = media.Movie('Deadpool', 'A story of a villian',
                       'https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg',
                       'https://www.youtube.com/watch?v=9vN6DHB6bJc')

movies = [toy_story, avatar, avnegers, thor, the_hunger_games, deadpool]
# fresh_tomatoes.open_movies_page
# print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
