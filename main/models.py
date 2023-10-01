from django.db import models

class Case(models.Model):
    title = models.CharField("Название", max_length=255, default='')
    img = models.ImageField("Обложка", upload_to='case')
    titleForURL = models.CharField("Преобразование в URL", max_length=255, default='', blank=True)
    description = models.TextField("Наполнение", blank=True)

    def __str__(self):
        return self.title
    
class CaseBlock(models.Model):
    fk = models.ForeignKey(Case, on_delete = models.CASCADE)
    types = [
        (1, 'Текст'),
        (2, 'Одно изображение'),
        (3, 'Слайдер'),
    ]
    type = models.IntegerField("Тип", default=1, choices=types)
    img_1 = models.ImageField("Изображение 1", upload_to='caseBlocks', blank=True)
    img_2 = models.ImageField("Изображение 2", upload_to='caseBlocks', blank=True)
    img_3 = models.ImageField("Изображение 3", upload_to='caseBlocks', blank=True)
    img_4 = models.ImageField("Изображение 4", upload_to='caseBlocks', blank=True)
    img_5 = models.ImageField("Изображение 5", upload_to='caseBlocks', blank=True)
    text = models.TextField("Текст", blank=True)

    def __str__(self):
        return f'{"Блок " + str(self.fk)}'

class New(models.Model):
    title = models.CharField("Название Новости", max_length=255, default='')
    date = models.DateTimeField("Время поста", null=True)
    img_1 = models.ImageField("Изображение 1", upload_to='news', blank=True)
    img_2 = models.ImageField("Изображение 2", upload_to='news', blank=True)
    img_3 = models.ImageField("Изображение 3", upload_to='news', blank=True)
    img_4 = models.ImageField("Изображение 4", upload_to='news', blank=True)
    img_5 = models.ImageField("Изображение 5", upload_to='news', blank=True)
    text = models.TextField("Текст", blank=True)

    def __str__(self):
        return self.title