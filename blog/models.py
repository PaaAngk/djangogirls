from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Сomments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.SmallIntegerField(null=True)
    parent = models.BooleanField(default=True)
    levels = models.SmallIntegerField(null=True)
    author = models.CharField(max_length=50, help_text="Enter author")
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.author
        #        return '%s, %s' % (self.author, self.first_name)

    def comment_as_list(self):
        mylist = []
        if self.comment == "null":
            return mylist
        if len(self.comment) > 0:
            return list(map(int, self.comment.split()))
        return mylist

    def get_comment(self):
        return map(int, self.comment.split())

class SubСomments(models.Model):
    comment = models.ForeignKey(Сomments, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.author
        #        return '%s, %s' % (self.author, self.firsl

