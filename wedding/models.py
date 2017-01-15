from django.db import models

from datetime import date

# Meal options should only be editable by admin, and is referenced by Guest model.
class Meal(models.Model):
    choice = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __repr__(self):
        return "<Meal(choice='%s')>" % (self.choice)

    def __str__(self):
        return self.choice

# List of guests, their relationship to Kevin or Melissa, whether they are attending, meal choice, comments, and any plus ones. Plus ones are also added to the guest list and are indicated by the added_by field.
class Guest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    relationship_to_wedding_party = models.CharField(max_length=200)
    attending = models.NullBooleanField()
    meal = models.ForeignKey(Meal)
    comments = models.TextField()
    plus_ones = models.IntegerField()
    date_created = models.DateField(default=date.today)
    # added_by = models.ForeignKey()

    def __repr__(self):
        return "<Guest(first_name='%s', last_name='%s')>" % (self.first_name, self.last_name)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
