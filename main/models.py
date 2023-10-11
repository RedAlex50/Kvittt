from django.db import models

def case_directory_path(Case ,filename):
    return 'cases/case_{0}/{1}'.format(Case.title, filename)

def case_obl_directory_path(Case ,filename):
    return 'cases/case_{0}/oblojka/{1}'.format(Case.title, filename)

class Case(models.Model):
    title = models.CharField("Название", max_length=255, default='')
    img = models.ImageField("Обложка", upload_to=case_obl_directory_path)
    titleForURL = models.CharField("Преобразование в URL", max_length=255, default='', blank=True)
    img_1 = models.ImageField("Изображение 1", upload_to=case_directory_path, blank=True)
    img_2 = models.ImageField("Изображение 2", upload_to=case_directory_path, blank=True)
    img_3 = models.ImageField("Изображение 3", upload_to=case_directory_path, blank=True)
    img_4 = models.ImageField("Изображение 4", upload_to=case_directory_path, blank=True)
    img_5 = models.ImageField("Изображение 5", upload_to=case_directory_path, blank=True)
    description = models.TextField("Наполнение", blank=True)

    def __str__(self):
        return self.title
    
class New(models.Model):
    title = models.CharField("Название Новости", max_length=255, default='')
    date = models.DateTimeField("Время поста", null=True, auto_now_add=True)
    img_1 = models.ImageField("Изображение 1", upload_to='news', blank=True)
    img_2 = models.ImageField("Изображение 2", upload_to='news', blank=True)
    img_3 = models.ImageField("Изображение 3", upload_to='news', blank=True)
    img_4 = models.ImageField("Изображение 4", upload_to='news', blank=True)
    img_5 = models.ImageField("Изображение 5", upload_to='news', blank=True)
    text = models.TextField("Текст", blank=True)

    def __str__(self):
        return self.title