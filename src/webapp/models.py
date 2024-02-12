from django.db import models
from django.utils import timezone
from django.contrib import admin
import datetime


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Report(models.Model):
    name = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=timezone.now)
    # tags = models.CharField(max_length=255)
    tags = models.ManyToManyField(
        Tag, related_name="reports"
    )  # access the set of reports from a Tag (e.g., some_tag.reports.all()).
    description = models.TextField()
    file = models.FileField(upload_to="reports", blank=True, null=True)

    def __str__(self):
        return self.name

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        """
        Only return True if the date is in the past
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
