from django.db import models


class AboutMe(models.Model):
    name = models.CharField('ФИО', max_length=20)
    profession = models.CharField('Профессия', max_length=20)
    about_me = models.TextField('О себе')
    hobby = models.TextField('Хобби')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'О себе'
        verbose_name_plural = 'О себе'
