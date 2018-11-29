from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
    # Blog Post
    author = models.ForeignKey('auth.User') # Ovo nije dobar nacin jer je superuser povezan sa kreatorom textova
                                            # resenje treba da bude drugacije, da svaki registrovani moze to
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approve_comments=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk }) # kad se napravi post redirektuje na ovu stranicu

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments') # each comment connected with blog application post
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approve_comments = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.post