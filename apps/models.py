from django.db import models
from datetime import datetime  

#footer
class Contact(models.Model):
    phoneNumber = models.CharField(max_length = 15, verbose_name = 'Número do telefone')
    email = models.EmailField('Email')
    address = models.CharField(max_length = 255, verbose_name = 'Endereço')
    instagram = models.URLField(max_length = 255, verbose_name = 'Instagram')
    facebook = models.URLField(max_length = 255, verbose_name ='Facebook')
    youtube = models.URLField(max_length = 255, verbose_name = 'Youtube')
    
    def __str__(self):
        return f'{self.phoneNumber} - {self.email}'
    
class Information(models.Model):
    randomUrl1 = models.URLField(max_length = 255, verbose_name ='URL qualquer')
    randomUrl2 = models.URLField(max_length = 255, verbose_name ='URL qualquer')
    randomUrl3 = models.URLField(max_length = 255, verbose_name ='URL qualquer')
    whoAreWe = models.URLField(max_length = 255, verbose_name = 'Quem somos')
    
    def __str__(self):
        return f'{self.whoAreWe} - {self.randomURL1} - {self.randomURL2} - {self.randomURL3}'


#Home
#add top
class Tools(models.Model):
    image = models.ImageField(upload_to = 'images/', verbose_name = 'Imagem')
    title = models.CharField(max_length = 50, verbose_name = 'Titulo')
    description = models.TextField(verbose_name = 'Descrição')
    
    def __str__(self):
        return f'{self.title} - {self.description}'
    
class Team(models.Model):
    image = models.ImageField(upload_to = 'images/', verbose_name = 'Imagem')
    name = models.CharField(max_length = 25, verbose_name = 'Nome')
    profession = models.CharField(max_length = 150, verbose_name = 'Titulo')
    
    def __str__(self):
        return f'{self.name} - {self.profession}'
    
    
#Videos
class TopImageV(models.Model): #V de Videos
    title = models.CharField(max_length = 250, verbose_name = 'Titulo')
    image = models.ImageField(upload_to = 'images/', verbose_name = 'Imagem')
    description = models.TextField(verbose_name = 'Descrição') 
    
    def __str__(self):
        return f'{self.title} - {self.description}'
    
class Videos(models.Model):
    tip = models.CharField(max_length = 30, verbose_name = "Tipo")
    thumb = models.ImageField(upload_to = 'images/', verbose_name = 'Imagem')
    videoUrl = models.URLField(max_length = 255, verbose_name='URL do Vídeo')
    title = models.CharField(max_length = 50, verbose_name = 'Titulo')
    
    def __str__(self):
        return f'{self.title} - {self.tip}'
 
    
#Pais e profs   
class TopDesc(models.Model):
    title = models.CharField(max_length = 250, verbose_name = 'Titulo')
    description = models.TextField(verbose_name = 'Descrição')
    
    def __str__(self):
        return f'{self.title} - {self.description}'
    
class DrawingAndCardAndKnow(models.Model):
    image = models.ImageField(upload_to = 'images/', verbose_name = 'Imagem')
    file = models.FileField(upload_to = 'downloads/', blank=True, null=True, verbose_name = 'Arquivo para Download')
    tip = models.CharField(max_length = 30, verbose_name = "Tipo")
    description = models.TextField(verbose_name = 'Descrição')#mudar
    
    def __str__(self):
        return f'{self.tip} - {self.description}'
    
#Fórum
class TopImageF(models.Model): #F de Fórum
    title = models.CharField(max_length = 250, verbose_name = 'Titulo')
    image = models.ImageField(upload_to = 'images/', verbose_name = 'Imagem')
    description = models.TextField(verbose_name = 'Descrição') 
    
    def __str__(self):
        return f'{self.title} - {self.description}'
    
class Post(models.Model):
    title = models.CharField(max_length = 200, verbose_name = 'Título')
    userName = models.CharField(max_length = 100, verbose_name = 'Nome de Usuário')
    date = models.DateTimeField(auto_now_add = True, verbose_name = 'Data')
    description = models.TextField(verbose_name = 'Descrição')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name = 'comentarios', on_delete = models.CASCADE)  # Relaciona o comentário ao post
    userNameComment = models.CharField(max_length = 100, verbose_name = 'Autor')  # Nome do autor do comentário
    commentDesc = models.TextField(verbose_name = 'Descrição') 
    date = models.DateTimeField(auto_now_add = True, verbose_name = 'Data') 

    def __str__(self):
        return f'{self.userNameComment}: {self.commentDesc[:30]}'
    
class PopularTopic(models.Model):
    title = models.CharField(max_length = 50, verbose_name = 'Título')
    subject = models.TextField(verbose_name = 'Descrição')
    quantityComments = models.IntegerField(default=0, verbose_name='Quantidade de Comentários')
    date = models.DateTimeField(auto_now_add = True, verbose_name = 'Data')
    
    def __str__(self):
        return self.title