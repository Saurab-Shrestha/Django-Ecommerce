from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File
# Create your models here.
# Category models
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to="category")

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

LABEL_CHOICES = (
    ('S', 'sale'),
    ('N', 'new'),
    ('P', 'promotion')
)

class Product(models.Model):
    category = models.ForeignKey(Category,related_name="products",on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description =models.TextField(blank=True,null=True)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="products",blank=True, null=True)
    thumbnail = models.ImageField(upload_to="products/thumbnails", blank=True, null=True)
    labels = models.CharField(choices=LABEL_CHOICES,max_length=1)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    """
        def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
            else:
                return 'https://via.placeholder.com/240x20x.jpg'

    def make_thumnail(self, image, size=(300,300)):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)

        thumb_io =BytesIO()
        img.save(thumb_io, "JPEG", qualtiy=85)

        thumbnail = File(thumb_io, name=image.name)
        return thumbnail
    """
