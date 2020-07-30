from django.db import models
from django.contrib.auth.models import User

#Entry Class for each of the set reviews
class Entry(models.Model):
	#5 fields per post
	title  	= models.CharField(max_length=120)
	text 	= models.TextField()
	date 	= models.DateTimeField(auto_now_add=True)
	author 	= models.ForeignKey(User, on_delete=models.CASCADE)
	# 0 - 32767 pieces. Largest LEGO is 7541
	num_pieces 	= models.PositiveSmallIntegerField()

	class Meta:
		verbose_name_plural = "Entries"
		
	def __str__(self):
		return '{0}, {1}'.format(self.title, self.author)