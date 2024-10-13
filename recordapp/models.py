from django.db import models


class Post(models.Model):  
    slug = models.SlugField(editable=False, unique=True)
    date = models.DateField(verbose_name='投稿日')
    what_done = models.TextField(verbose_name='本日の作業内容')
    what_not_done = models.TextField(verbose_name='本日の課題', blank=True)
    what_learned = models.TextField(verbose_name='本日の取得スキル', blank=True)
    summary_image = models.ImageField(upload_to='study_summaries/', verbose_name='まとめノート', blank=True, null=True)
    
    class Meta:
        verbose_name = '勉強記録'
        verbose_name_plural = '勉強記録一覧'

    def __str__(self):
        return f'{self.slug} - {self.date} - {self.what_done}'