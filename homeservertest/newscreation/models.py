from django.db import models
from django.core.validators import URLValidator
from django.urls import reverse
from .datasite import get_list_data

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория', null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

class NewsLink(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название новости')
    description = models.TextField(blank=True, verbose_name='Предисловие')
    img_link = models.TextField(validators=[URLValidator()], verbose_name='Представление')
    img_path = models.ImageField(upload_to="images", verbose_name='Картинка')
    content_link= models.TextField(validators=[URLValidator()], verbose_name='Содержание')
    date_published = models.DateField(auto_now_add=False, verbose_name='Дата публикации')
    date_added = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    source = models.CharField(max_length=255, verbose_name='Источник', null=True)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    
    
    def __str__(self):
         return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

def save_data_to_base():
    data_list = get_list_data()
    for object in data_list:
        if not NewsLink.objects.filter(title=object['title']).exists():
            data = NewsLink(**object)
            data.save()
            print(object['title'])
        

   


a = 0
if a == 1:
    save_data_to_base()



