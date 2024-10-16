from django.db import models
from pathlib import Path

class Category(models.Model):
    name = models.CharField(verbose_name='カテゴリー', max_length=50)
    
    class Meta:
        verbose_name = 'カテゴリー'
        verbose_name_plural = 'カテゴリー一覧'
        
    def __str__(self):
        return self.name

class Post(models.Model):  
    slug = models.SlugField(blank=True, editable=True, unique=True)
    date = models.DateField(verbose_name='投稿日')
    what_done = models.TextField(verbose_name='本日の作業内容')
    what_not_done = models.TextField(verbose_name='本日の課題', blank=True)
    what_learned = models.TextField(verbose_name='本日の取得スキル', blank=True)
    summary_image = models.ImageField(upload_to='study_summaries/', verbose_name='まとめノート', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='カテゴリー', related_name='posts', null=True, blank=True)

    
    class Meta:
        verbose_name = '勉強記録'
        verbose_name_plural = '勉強記録一覧'

    def __str__(self):
        return f'{self.slug} - {self.date} - {self.what_done}'
    
    def save(self, *args, **kwargs):
        # slugが空の場合はIDを使ってslugを生成
        if not self.slug:
            # 一度保存してIDを取得し、そのIDをslugに設定
            super().save(*args, **kwargs)
            self.slug = str(self.id)  # IDをslugに設定
            super().save(*args, **kwargs)  # もう一度保存してslugを更新
        else:
            super().save(*args, **kwargs)
            
    # ファイルに保存された画像を削除する
    def delete(self, *args, **kwargs):
        summary_image =self.summary_image
        super().delete(*args, **kwargs)
        if summary_image:
            Path(summary_image.path).unlink(missing_ok=True)

