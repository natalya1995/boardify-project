from django.db import models 
from pytils.translit import slugify 
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField("Название локации", max_length=100)
    slug = models.SlugField(unique=True, blank=True, editable=False)
    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name) 
        super().save(*args, **kwargs) 
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField("Haзвaниe", max_length=100) 
    image = models.FileField("Фoтo", upload_to="images/categories/") 
    slug = models.SlugField(unique=True, blank=True, editable=False) 
    class Meta:
        verbose_name = "Категория" 
        verbose_name_plural = "Категории"
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name) 
        super().save(*args, **kwargs) 
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,verbose_name="Пользователь")
    phone=models.CharField("Телефон",max_length=13,unique=True,null=True,blank=True)
    avatar=models.ImageField("Аватар",upload_to="images/avatars/",null=True,blank=True)
    location=models.ForeignKey(Location,on_delete=models.CASCADE,verbose_name="Местоположение",null=True,blank=True)
    created_at=models.DateTimeField("Дата и время регистрации",auto_now_add=True)

    def __str__(self):
        return self.user.username

class Board(models.Model):
    userprofile=models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="Автор")
    title=models.CharField("Заголовок",max_length=150)
    image=models.ImageField("Фото",upload_to="images/boards/")
    description=models.TextField("Описание")
    price=models.IntegerField("Цена",default="")
    is_active_board=models.BooleanField("Активное объявление",default=False)
    location=models.ForeignKey(Location,on_delete=models.CASCADE,verbose_name="Местоположение",null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Категория",null=True)
    created_at=models.DateTimeField("Дата и время публикации",auto_now_add=True)

    class Meta:
        verbose_name="Доска"
        verbose_name_plural="Доски"
    
    def __str__(self):
        return self.title
    





    



          
