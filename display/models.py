from django.db import models

# Create your models here.

# Location model to enable us choose location


class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.save()


# iterable tuple to use as choices of category field


ORDER_CHOICES = (
    ('11', 'Vegetation'),
    ('12', 'Trees'),
    ('13', 'Nature'),
    ('14', 'Abstract'),
    ('15', 'Painting'),
    ('16', 'Animals'),
    ('17', 'Illustrations'),
    ('18', 'Flowers'),
    ('19', 'Business'),
    ('20', 'Industries'),
    ('21', 'Cats'),
    ('22', 'Car'),
    ('23', 'People'),
    ('24', 'Travel'),
)


class Category(models.Model):
    name = models.CharField(max_length=30)
    category_choices = models.CharField(max_length=10, choices=ORDER_CHOICES)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_catgory(self):
        self.save()


# renaming class Images to Photos due to error in terminal;


class Image(models.Model):
    image_name = models.CharField(max_length=20)
    image_description = models.CharField(max_length=30)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    image = models.ImageField(upload_to='photos/', null="True", blank="True")

    # __str__ will return string representation of the image model
    # __str__ will enable us view our returned queries

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_category(cls, search_term):
        display = cls.objects.filter(category__name__icontains=search_term)
        return display

    # @classmethod
    # def location(cls):
    #     display = cls.objects.filter(location__name__icontains=cls)
    #     return display
    @classmethod
    def filter_by_location(cls):
        display = cls.objects.filter(
            location__name__icontains='Sili')
        return display

    class Meta:
        ordering = ['image_name']
