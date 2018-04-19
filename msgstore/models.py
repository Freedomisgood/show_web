from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class msg(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    # name = models.CharField(max_length=20)
    text = models.TextField(null=False)
    ddate = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-ddate',]

    def __str__(self):
        return self.text

class information(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    data = models.DateField(verbose_name='出生年月')
    sexy = models.CharField(max_length=4)
    love = models.CharField(max_length=20)

    def __str__(self):
        return self.love
