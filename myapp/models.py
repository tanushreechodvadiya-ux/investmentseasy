from django.db import models
from django.utils.safestring import mark_safe

from django.db import models

class ContactMessage(models.Model):
    cname = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cname
