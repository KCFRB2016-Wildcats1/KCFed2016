from django.db import models

class User(models.Model):
    ADVISOR = 'Adv'
    STUDENT = 'Stu'
    VOLUNTEER = 'Vol'
    USERTYPE_CHOICES = (
        (ADVISOR, 'ADVISOR'),
        (STUDENT, 'STUDENT'),
        (VOLUNTEER, 'VOLUNTEER'),
    )

    userID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, null=False)
    email = models.EmailField(max_length=256)
    userType = models.CharField(max_length=3, choices=USERTYPE_CHOICES, default=STUDENT)

class Event(models.Model):
    eventID = models.AutoField(primary_key=True)
    eventName = models.CharField(max_length=256, null=False)
    eventTime = models.DateTimeField(null=False)

    """
    location = models.
    interests = models.
    """

class Request(models.Model):
    TUTORING = 'Tut'
    VOLUNTEER = 'Vol'
    EVENT = 'Eve'
    REQUESTTYPE_CHOICES = (
        (TUTORING, 'TUTORING'),
        (VOLUNTEER, 'VOLUNTEER'),
        (EVENT, 'EVENT'),
    )
    requestID = models.AutoField(primary_key=True)
    requestType = models.CharField(max_length=3, choices=REQUESTTYPE_CHOICES, default=EVENT)
    numberVols = models.IntegerField()
    requester = models.CharField(max_length=256, null=False)
    dateTime = models.DateTimeField(null=False)

class Post(models.Model):
    postID = models.AutoField(primary_key=True)
    dateTime = models.DateTimeField(null=False)
    postAcc = models.CharField(max_length=256, null=False)
    group = models.CharField(max_length=256, default='GLOBAL')

class Group(models.Model):
    groupID = models.AutoField(primary_key=True)
    groupName = models.CharField(max_length=256, null=False)
    """groupUsers = multiple list field"""

class Resource(models.Model):
    resourceID = models.AutoField(primary_key=True)
    hyperlink = models.URLField(max_length=256, null=False)
    dateTime = models.DateTimeField(null=False)
    """interests"""