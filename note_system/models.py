from django.db import models
from django.urls import reverse

from accounts.models import User

from django.db import models
from django.db.models import Q


class Note(models.Model):
    theme = models.CharField(max_length=40, blank='False')
    text = models.TextField()
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes', null=True, verbose_name='username')
    is_public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('note', args=(self.id,))