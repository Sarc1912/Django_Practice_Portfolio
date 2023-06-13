from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

"""
to visualize image in admin panel, you must copy this code in url.py
from django.conf.urls.static import static
from django.conf import settings

    urlpatterns = [
        path('admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""

# Create your models here.

class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="portfolio/images/")
    url = URLField(blank=True)
    
    def __str__(self):
        return self.title