from django.db import models
from datetime import *
from django.contrib.auth.models import User


class Album(models.Model):
  class Meta():
      db_table = "Album"
  def __str__(self):
        return self.title
  title = models.CharField("Название альбома", max_length=100)
  album_date = models.DateTimeField(default=datetime.now())
  album_user=models.ForeignKey(User)
  album_likes=models.IntegerField(default=0)
  slug = models.SlugField("Ссылка для альбома", max_length=100, unique=True)
  img = models.ImageField("Изображение альбома", upload_to='images',
	help_text='Желательно 250px на 250px')

  
    

class Photo(models.Model):
  class Meta():
      db_table ="Photo"
  def __str__(self):
        return self.title
  title = models.CharField("Название фотографии", max_length=100)
  photo_date = models.DateTimeField(default=datetime.now())
  photo_likes=models.IntegerField(default=0)
  album = models.ForeignKey(Album, verbose_name='Альбом')
  img = models.ImageField("Фото", upload_to='images')




class Comment(models.Model):
  class Meta():
      db_table="comment"
  def __str__(self):
        return self.comments_text
  comments_text=models.TextField("Текст Коментария")
  comments_date = models.DateTimeField(default=datetime.now())
  comments_photo = models.ForeignKey(Photo)
  comments_likes = models.IntegerField(default = 0 )
  comments_author=models.ForeignKey(User)


class Avatar(models.Model):
    def __str__(self):
        return self.avatar_user.username
    avatar=models.ImageField(u'avatar',upload_to='images')
    avatar_user=models.OneToOneField(User)
