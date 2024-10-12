from django.db import models

class TopImageV(models.Model): #V de Videos
    title = models.CharField(max_length = 250, verbose_name = 'Titulo')
    image = models.ImageField(upload_to = 'images/', verbose_name = 'Imagem')
    description = models.TextField(verbose_name = 'Descrição') 
    
    def __str__(self):
        return f'{self.title} - {self.description}'
    
class Video(models.Model):
    type = models.CharField(max_length = 30, verbose_name = "Tipo")
    thumb = models.ImageField(upload_to = 'images/', verbose_name = 'Imagem')
    videoUrl = models.URLField(max_length = 255, verbose_name='URL do Vídeo')
    title = models.CharField(max_length = 50, verbose_name = 'Titulo')
    
    def __str__(self):
        return f'{self.title} - {self.type}'