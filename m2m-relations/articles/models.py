from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Тег'
        verbose_name = 'Тег'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    tags = models.ManyToManyField(Tag, through='Scope', related_name='articles', verbose_name='tag')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False, verbose_name='Основной')

    class Meta:
        verbose_name = 'Связь между статьей и тегом'
        verbose_name_plural = 'Связи между статьями и тегами'
        unique_together = ('article', 'tag')

    def __str__(self):
        return f'{self.article.title} - {self.tag.name} ({self.is_main})'
