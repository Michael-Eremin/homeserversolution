from django.db import models
from django.core.validators import URLValidator
from .datasite import get_list_data


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория', null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        """Outputs information about the 'category' by its 'name'."""
        return self.name


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
        """Outputs information about the 'news' by its 'title'."""
        return self.title


def save_data_to_base():
    """Saves the information received from web resources in the database."""
    data_list = get_list_data()
    for object in data_list:
        # Checks and saves if there is no such news in the database.
        if not NewsLink.objects.filter(title=object['title']).exists():
            data = NewsLink(**object)
            data.save()
            print(object['title'])
        

# WARNING. It is necessary to develop. Disconnect Save.
a = 0
if a == 1:
    save_data_to_base()
