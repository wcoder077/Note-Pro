from django.db import models


from django.contrib.auth.models import User


class NoteData(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Sarlavha",
        default="Sarlovha ...",
        null=True,
        blank=True,
    )
    content = models.TextField(verbose_name="Ma'lumot")
    is_trashed = models.BooleanField(default=False, verbose_name="Korzina")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "notes"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.pk} - {self.title}"
