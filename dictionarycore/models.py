from django.db import models



# Create your models here.


#Transalation table 
class translation(models.Model):
    word_twi = models.CharField(max_length=200,null=False, blank=False)
    word_english =  models.CharField(max_length=200,null=False, blank=False)
    other_words = models.TextField(null=True,blank=True)
    desc = models.TextField(null=True, blank=True) 
    date_modified = models.DateTimeField(auto_now=True)
    date_created =  models.DateTimeField(auto_now_add=True) 

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.word_english

