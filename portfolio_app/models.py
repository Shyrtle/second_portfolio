from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=30)
    desc = models.TextField()
    date_complete = models.DateField()
    image = models.ImageField(upload_to='portfolio_app/images/')
    image2 = models.ImageField('Additional Image', upload_to='portfolio_app/images/', blank=True)
    image3 = models.ImageField('Additional Image', upload_to='portfolio_app/images/', blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Job(models.Model):
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    addr_1 = models.CharField(max_length=200)
    addr_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=20)
    image = models.ImageField(upload_to='portfolio_app/images/', blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.company
