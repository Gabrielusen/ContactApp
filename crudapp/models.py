from django.db import models


class Contact(models.Model):
    first_name = models.CharField('First name', max_length=255, blank=True, null=True)
    last_name = models.CharField('Last name', max_length=255, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField('Created At', auto_now_add=True)

    def __str__(self):
        full_name = f"{self.first_name} + {self.last_name}"
        return full_name
