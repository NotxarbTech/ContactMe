from django.db import models
import uuid

# Create your models here.
class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    @property
    def qr_code_url(self):
        if self.qr_code:
            return self.qr_code.url
        else:
            return ''
        
    @property
    def profile_pic_url(self):
        if self.profile_pic:
            return self.profile_pic.url
        else:
            return ''

    def __str__(self):
        return f"{self.name} - {self.phone_number} - {self.id}"