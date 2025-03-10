from django.db import models

class Package(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Transit', 'In Transit'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    ]

    tracking_number = models.CharField(max_length=50, unique=True)
    sender = models.CharField(max_length=255)
    recipient = models.CharField(max_length=255)
    address = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)  # Soft Delete

    def __str__(self):
        return self.tracking_number
