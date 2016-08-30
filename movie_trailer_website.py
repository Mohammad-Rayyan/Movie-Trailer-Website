import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story 3", "The toys are mistakenly delivered to a day-care center instead of the attic right before Andy leaves for college, and it's up to Woody to convince the other toys that they weren't abandoned and to return home."\
	, "http://ia.media-imdb.com/images/M/MV5BMTgxOTY4Mjc0MF5BMl5BanBnXkFtZTcwNTA4MDQyMw@@._V1_SY1000_CR0,0,707,1000_AL_.jpg"\
	, "https://www.youtube.com/watch?v=JcpWXaA2qeg")
Kevin_Can_Wait = media.Movie("Kevin Can Wait"\
	, "A newly retired police officer looks forward to spending more quality time with his wife and three kids only to discover he faces much tougher challenges at home than he ever did on the streets."\
	, "http://ia.media-imdb.com/images/M/MV5BMTc1MjkxNjY0Nl5BMl5BanBnXkFtZTgwMDc4MjU4OTE@._V1_.jpg"\
	, "https://www.youtube.com/watch?v=IGaIvCLm9pE")
Bull = media.Movie("Bull"\
	, "BULL stars Michael Weatherly as Dr. Jason Bull in a drama inspired by the early career of Dr. Phil McGraw, the founder of one of the most prolific trial consulting firms of all time."\
	, "http://ia.media-imdb.com/images/M/MV5BMTA5MzkwNzA5NDFeQTJeQWpwZ15BbWU4MDc1NzQ3Nzkx._V1_SY1000_CR0,0,674,1000_AL_.jpg"\
	, "https://www.youtube.com/watch?v=cmHeKAF6vwI")
Warcraft_The_Beginning = media.Movie("Warcraft: The Beginning"\
	, "As an Orc horde invades the planet Azeroth using a magic portal, a few human heroes and dissenting Orcs must attempt to stop the true evil behind this war"\
	, "http://ia.media-imdb.com/images/M/MV5BMjIwNTM0Mzc5MV5BMl5BanBnXkFtZTgwMDk5NDU1ODE@._V1_SY1000_CR0,0,631,1000_AL_.jpg"\
	, "https://www.youtube.com/watch?v=RhFMIRuHAL4")
movies = [toy_story, Kevin_Can_Wait, Bull, Warcraft_The_Beginning]
fresh_tomatoes.open_movies_page(movies)
