# This is an auto-generated Django model module.

# You'll have to do the following manually to clean this up:

#   * Rearrange models' order

#   * Make sure each model has one field with primary_key=True

#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior

#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table

# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class BidCrawling(models.Model):

    # Field name made lowercase.
    searchsubject = models.CharField(
        db_column='searchSubject', max_length=500, blank=True, null=True)

    title = models.CharField(blank=True, null=True, max_length=500)

    writer = models.CharField(blank=True, null=True, max_length=500)

    translator = models.CharField(blank=True, null=True, max_length=500)

    painter = models.CharField(blank=True, null=True, max_length=500)

    publisher = models.CharField(blank=True, null=True, max_length=500)

    # Field name made lowercase.
    publishdate = models.CharField(
        db_column='publishDate', max_length=50, blank=True, null=True)

    intro = models.CharField(blank=True, null=True, max_length=500)

    content = models.CharField(blank=True, null=True, max_length=500)

    # Field name made lowercase.
    authorintro = models.TextField(
        db_column='authorIntro', blank=True, null=True)

    # Field name made lowercase.
    categorytop = models.TextField(
        db_column='categoryTop', blank=True, null=True)

    # Field name made lowercase.
    categorymiddle = models.TextField(
        db_column='categoryMiddle', blank=True, null=True)

    # Field name made lowercase.
    categorybottom = models.TextField(
        db_column='categoryBottom', blank=True, null=True)

    # Field name made lowercase.
    isbn = models.CharField(db_column = 'ISBN', blank=True, null=True, max_length=500)

    bid = models.IntegerField(blank=True, null=True)

    grade = models.IntegerField(blank=True, null=True)

    review = models.CharField(blank=True, null=True, max_length=500)

    image = models.CharField(blank=True, null=True, max_length=500)

    class Meta:

        managed = False

        db_table = 'bid_crawling'

        ordering = ['-bid']
