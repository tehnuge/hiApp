from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models


class Users(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Chats(models.Model):
	content = models.CharField(max_length=200)
	author = models.ForeignKey(User, related_name='chats_author')
	recipient = models.ForeignKey(User, related_name='chats_recipient')
	def __str__(self):
		return 'author: ' + self.author.name + ' recipient: ' + self.recipient.name


