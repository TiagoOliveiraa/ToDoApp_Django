from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=100,blank=True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING ,related_name='owner', null=True)
    moderator = models.ManyToManyField(User, related_name='moderator', null=True)
    member = models.ManyToManyField(User, related_name='member', null=True)
    
    def __str__(self) -> str:
        return self.name

class invitations(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    teamID = models.ForeignKey(Team, on_delete=models.CASCADE)
    
    def __str__(self):
        name = self.userID.username + ' para ' + self.teamID.name
        return name



class Task(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    urgent = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["complete","created"]
        
    