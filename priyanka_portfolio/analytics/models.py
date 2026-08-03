import uuid

from django.db import models

class Visitor(models.Model):


    visitor_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True,
    )

    user_agent = models.TextField(
        blank=True,
    )

    browser = models.CharField(
        max_length=100,
        blank=True,
    )

    operating_system = models.CharField(
        max_length=100,
        blank=True,
    )

    device = models.CharField(
        max_length=50,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.browser} - {self.ip_address}"


class ResumeDownloadLog(models.Model):
    visitor = models.ForeignKey(
        Visitor,
        on_delete=models.CASCADE,
        related_name="resume_download_logs",
    )

    ip_address = models.GenericIPAddressField()

    downloaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-downloaded_at"]
        verbose_name = "Resume Download"
        verbose_name_plural = "Resume-Downloads"

    def __str__(self):
        return f"{self.ip_address} - {self.downloaded_at}"