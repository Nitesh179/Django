from django.db import models
 

# Create your models here.

class Sentiment(models.Model):
    sentiment_Data:models.JSONField()

