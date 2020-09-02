from django.db import models
from accounts.models import User
# Create your models here.

class Leave_data(models.Model):
    user = models.ForeignKey(User,to_field='id',on_delete=models.CASCADE,related_name='leave_application')
    
    start_date = models.DateField() 
    end_date = models.DateField()
    disc = models.TextField(max_length=100 ,default="",blank=False)

    is_approved = models.BooleanField(default=False)
    # emp_type = models.CharField(max_length=20, default="")


