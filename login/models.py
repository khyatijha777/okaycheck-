from django.db import models
class Login(models.Model):
    u_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=20)
    conatct_no = models.CharField(max_length=10)
    def __str__(self):
        return self.user_name
