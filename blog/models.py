from django.db import models
from django.core.urlresolvers import reverse
     
class Post(models.Model):
        title = models.CharField(max_length=255)
        slug = models.SlugField(unique=True, max_length=255)
        description = models.CharField(max_length=255)
        content = models.TextField()
        published = models.BooleanField(default=True)
        created = models.DateTimeField(auto_now_add=True)
        date_created = models.DateTimeField(auto_now_add=True)
        # date_modified = models.DateTimeField(auto_now=True)
        tags = models.CharField(max_length=255)
     
        def get_tag_list(self):
            return re.split(" ", self.tags)

        class Meta:
            ordering = ['-created']
        def __str__(self):
            return self.title

     
        def __unicode__(self):
            return u'%s' % self.title
     
        def get_absolute_url(self):
            return "/blog/%d/%02d/%s/" % (self.date_created.year,
                                      self.date_created.month,
                                      self.slug)

   
        


class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    text = models.TextField()
    post = models.ForeignKey(Post)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text