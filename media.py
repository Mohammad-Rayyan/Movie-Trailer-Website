class Movie(object):
	"""make a movie instance contain trailer,name,story,poster"""
	def __init__(self, name, story, poster, trailer):
		self.title = name
		self.trailer_youtube_url = trailer
		self.poster_image_url = poster
		self.storyline = story