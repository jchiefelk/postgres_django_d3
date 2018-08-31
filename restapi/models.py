from django.db import models

# Create your models here.
class Clients(models.Model):
	AccountDescriptiveName = models.CharField(max_length=200)
	CampaignId = models.IntegerField()
	CampaignName = models.CharField(max_length=200)
	CampaignStatus = models.CharField(max_length=200)
	CityCriteriaId = models.IntegerField()
	CountryCriteriaId = models.IntegerField()
	CustomerDescriptiveName = models.CharField(max_length=200)
	ExternalCustomerId = models.IntegerField()
	IsTargetingLocation = models.BooleanField(default=True)
	MetroCriteriaId = models.CharField(max_length=200)
	MostSpecificCriteriaId = models.IntegerField()
	RegionCriteriaId = models.IntegerField()
	Date = models.DateField()
	Device = models.CharField(max_length=200)
	LocationType = models.CharField(max_length=200)
	AveragePosition = models.IntegerField
	Clicks = models.IntegerField()
	Conversions = models.FloatField()
	ConversionValue = models.FloatField()
	Cost = models.IntegerField()
	Impressions = models.IntegerField()
	Interactions = models.IntegerField()
	InteractionTypes = models.CharField(max_length=200)
	VideoViews = models.IntegerField()