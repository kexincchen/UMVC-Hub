from django.db import models
from django.utils import timezone
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

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
