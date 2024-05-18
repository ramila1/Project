from django.db import models
from model_app.models import CustomUser
from django.utils import timezone

class Blog(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE,related_name='blog_post')
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def str(self):
        return self.title

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()
    
    def hard_delete(self):
        self.delete()




