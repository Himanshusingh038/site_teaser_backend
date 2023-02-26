from django.db import models

# Create your models here.

class PropertySurrounding(models.Model):
    class PropertyType(models.TextChoices):
        MAP = 'map', 'Map'
        STATUS = 'status', 'Status'
        
    id = models.AutoField(primary_key=True)
    property_id = models.IntegerField(blank=True,null=True)
    title  = models.CharField(max_length=255, blank=True)
    desc = models.CharField(max_length=255, blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    property_type = models.CharField(max_length=10, choices=PropertyType.choices)
    
    class Meta:
        db_table = 'property_surroundings'
        
class PropertyAmenetyMappings(models.Model):
    id  = models.AutoField(primary_key=True)
    property_id = models.IntegerField(blank=True, null=True)
    amenetiy_id = models.IntegerField(blank=True, null=True)
    
    class Meta:
        db_table = 'property_ameneties'

class Property(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    property_desc = models.CharField(max_length=255, blank=True)
    
    class Meta:
        db_table = 'properties'
        
class Amenety(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    icon_url = models.URLField(blank=True, null=True)
    
    class Meta:
        db_table = 'ameneties'

class UserPromt(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, blank=True)
    prompt_sent = models.BooleanField(default=False)
    phone = models.CharField(max_length=255, blank=True)
    sv_scheduled = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'user_prompts'