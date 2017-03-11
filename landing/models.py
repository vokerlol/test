from django.db import  models

class Subscriber(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=128)

    def __str__(self):
        return "%s %s" %(self.email, self.name)

    class Meta:
        verbose_name="my_subs"
        verbose_name_plural="a lot of Subs"
