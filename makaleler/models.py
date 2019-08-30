from django.db import models
from ckeditor.fields import RichTextField

class Makale(models.Model):

    title = models.CharField(max_length=50 ,verbose_name="başlık")
    content = RichTextField(verbose_name="içerik")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    article_media = models.FileField(blank=True,null=True,verbose_name="Medya Ekle")
    def __str__(self):
        return self.title

