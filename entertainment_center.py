import media
import fresh_tomatoes

# Blade Runner movie: title, storyline, poster image and trailer
blade_runner = media.Movie(
    "Blade Runner",
    ("TA blade runner must pursue and try to terminate four replicants "
     "who stole a ship in space and have returned to Earth to find their "
     "creator."),
    ("https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzMzJhZTEtOWM4NS"
     "00MTdhLTg0YjgtMjM4MDRkZjUwZDBlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR"
     "0,0,182,268_AL_.jpg"),
    "https://www.youtube.com/watch?v=eogpIG53Cis")

# Willow movie: title, storyline, poster image and trailer
willow = media.Movie(
    "Willow",
    ("Willow follows a reluctant dwarf must play a critical role in "
     "protecting a special baby from an evil queen."),
    ("https://images-na.ssl-images-amazon.com/images/M/MV5BZWIyMTA2M2ItOGI5MC"
     "00OTY0LWFmZTItN2NkOWQ0MGQ5NDkyL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_"
     "UX182_CR0,0,182,268_AL_.jpg"),
    "https://www.youtube.com/watch?v=uzn2izehkno")

# There Will Be Blood movie: title, storyline, poster image and trailer
there_will_be_blood = media.Movie(
    "There Will Be Blood",
    ("There Will Be Blood is a story of family, religion, hatred, oil and "
     "madness, focusing on a turn-of-the-century prospector in the early days "
     "of the business."),
    ("https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxODQ4MDU5NV5BMl5"
     "BanBnXkFtZTcwMDU4MjU1MQ@@._V1_.jpg"),
    "https://www.youtube.com/watch?v=0FIm5ATyAY0")

# The Grand Butapest Hotel movie: title, storyline, poster image and trailer
the_grand_butapest_hotel = media.Movie(
    "The Grand Butapest Hotel",
    ("The Grand Butapest Hotel is a film about the adventures of Gustave H, a "
     "legendary concierge at a famous hotel from the fictional Republic of "
     "Zubrowka between the first and second World Wars, and Zero Moustafa, a "
     "lobby boy who becomes his most trusted friend."),
    ("https://images-na.ssl-images-amazon.com/images/M/MV5BMzM5NjUxOTEyMl5BMl5"
     "BanBnXkFtZTgwNjEyMDM0MDE@._V1_SY1000_SX675_AL_.jpg"),
    "https://www.youtube.com/watch?v=zru-1DbbcsA")

# Terminator movie: title, storyline, poster image and trailer
terminator = media.Movie(
    "Terminator",
    ("Terminator is a humanoid cyborg is sent from 2029 to 1984 to "
     "assassinate a waitress, whose unborn son will lead humanity in a war "
     "against the machines"),
    ("https://images-na.ssl-images-amazon.com/images/M/MV5BODE1MDczNTUxOV5BM"
     "l5BanBnXkFtZTcwMTA0NDQyNA@@._V1_UX182_CR0,0,182,268_AL_.jpg"),
    "https://www.youtube.com/watch?v=c4Jo8QoOTQ4")

# Hot Tub Time Machine movie: title, storyline, poster image and trailer
hot_tub_time_machine = media.Movie(
    "Hot Tub Time Machine",
    ("Hot Tub Time Machine is a film about a malfunctioning time machine at "
     "a ski resort takes a man back to 1986 with his two friends and nephew"),
    ("https://images-na.ssl-images-amazon.com/images/M/MV5BMTQwMjExODA4Ml5BMl"
     "5BanBnXkFtZTcwNTYwMDYxMw@@._V1_UX182_CR0,0,182,268_AL_.jpg"),
    "https://www.youtube.com/watch?v=50qJvOmjTxU")

movies = [blade_runner, willow, there_will_be_blood, the_grand_butapest_hotel,
          terminator, hot_tub_time_machine]

fresh_tomatoes.open_movies_page(movies)
