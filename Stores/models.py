from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, unique=True)

    def __unicode__ (self):
        return self.name

class Store(models.Model):

    name = models.CharField(max_length=50, null=False)
    # store name

    category = models.ManyToManyField(Category)
    # category ( meal / alcohol)
    locationX = models.FloatField(null=False, default=0.0, blank=True)
    locationY = models.FloatField(null=False, default=0.0, blank=True)
    # location (GPS)
    address = models.CharField(max_length=150, null=False)
    # address
    phone = models.CharField(max_length=25, null=False)
    # phone
    main_image = models.ImageField(upload_to="main_image", null=True, blank=True)
    # image
    open_at = models.PositiveSmallIntegerField(null=True, blank=True)
    # business hour from
    close_at = models.PositiveSmallIntegerField(null=True, blank=True)
    # business hour to
    max_seats = models.IntegerField(null=False, default=0)
    # max capacity
    available_seats = models.IntegerField(null=True, blank=True)
    # (+) available seats
    registered_at = models.DateTimeField(auto_now_add=True)
    # registered date (auto)

    def __unicode__ (self):
        return self.name

class Review(models.Model):
    store = models.ForeignKey(Store, null=False)
    # foreign key pointing store
    saved_at = models.DateTimeField(auto_now_add=True)
    # date
    score = models.PositiveSmallIntegerField(null=True, default=0)
    # score
    writer = models.CharField(max_length=30, null=False)
    # writer
    comment = models.TextField(null=False)
    # comment (review)
    review_image = models.ImageField(upload_to="review_image", null=True, blank=True)
    # image

    def __unicode__ (self):
        return self.comment

class Picture(models.Model):
    store = models.ForeignKey(Store, null=False)
    # foreign key pointing store
    store_image = models.ImageField(upload_to="store_image", null=False)
    # image

class Menu(models.Model):
    store = models.ForeignKey(Store, null=False)
    # foreign key pointing store
    name = models.CharField(max_length=50, null=False)
    # menu name
    price = models.IntegerField(null=True, blank=True)
    # price
    menu_image = models.ImageField(upload_to="menu_image", null=True, blank=True)
    # image
    
    def __unicode__ (self):
        return self.name
    
