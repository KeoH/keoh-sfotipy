from django.db import models

continents = [
	('EU','Europe'),
	('SA','South America'),
	('NA','North America'),
	('CA', 'Central America'),
	('AS','Asia'),
	('AS','Australia'),
	('OC','Oceania'),
	('AF','Africa'),
]

class Country(models.Model):

	name = models.CharField(max_length=50)
	continent = models.CharField(max_length=2, choices=continents, blank=True)

	def __unicode__(self):
		return self.name

	def get_continent(self):
		for i in continents:
			if self.continent == i[0]:
				return i[1]
		

	class Meta:
		verbose_name_plural="Countries"

class Artist(models.Model):

	first_name	= models.CharField(max_length=255)
	last_name 	= models.CharField(max_length=255, blank=True)

	biography	= models.TextField(blank=True)
	country		= models.ForeignKey(Country, blank=True)

	profile_image = models.ImageField(upload_to='artist/',blank=True)

	is_group	= models.BooleanField(default=False)

	def fullname(self):
		return self.first_name +' '+ self.last_name

	def get_profile_image(self):
		if(self.profile_image):
			return self.profile_image.url
		else:
			return ""
	def group_or_artist(self):
		if self.is_group == True:
			return "Group"
		else:
			return "Artist"

	def __unicode__(self):
		return self.fullname()
	
	fullname.short_description = "Full name of de artist or group"		
	group_or_artist.short_description = "Group or Artist"
	group_or_artist.admin_order_field = "is_group"

class JamendoArtist(models.Model):

	name = models.CharField(max_length=255)
	artist_jamendo_id = models.PositiveIntegerField(default=1)
	website = models.URLField()
	joindate = models.DateField()
	image = models.URLField()