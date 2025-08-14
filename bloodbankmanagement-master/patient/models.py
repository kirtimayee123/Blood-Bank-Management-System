from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/Patient/', null=True, blank=True)

    age = models.PositiveIntegerField()
    bloodgroup = models.CharField(max_length=10)
    disease = models.CharField(max_length=100)
    doctorname = models.CharField(max_length=50)

    address = models.CharField(max_length=40)

    # Validator to ensure the mobile number contains only 10 digits

    mobile = models.CharField(max_length=10,null=False,validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$',message="mobile number error")])


    @property
    def get_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def get_instance(self):
        return self

    def _str_(self):
        return self.user.first_name