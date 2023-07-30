from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    start_date_time = models.DateTimeField(
        blank=False,
        validators=[
            MinValueValidator(timezone.now() + timezone.timedelta(days=1)),
            MaxValueValidator(timezone.now() + timezone.timedelta(days=1100))
        ]
    )
    end_date_time = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    website_link = models.URLField(max_length=250, blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cover_image = models.ImageField(
        upload_to='images/', default='../default_post_ed2doq',
        blank=True, null=True)

    def clean(self):
        if self.start_date_time and self.end_date_time:
            if self.end_date_time < self.start_date_time:
                raise ValidationError('End date and time must be after or equal to the start date and time.')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
