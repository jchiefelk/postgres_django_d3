from django.db import models

# Create your models here.
class Clients(models.Model):
	account_descriptive_name = models.CharField(max_length=200)
	campaign_id = models.IntegerField()
	campaign_name = models.CharField(max_length=200)
	campaign_status = models.CharField(max_length=200)
	city_criteria_id = models.IntegerField()
	country_criteria_id = models.IntegerField()
	customer_descriptive_name = models.CharField(max_length=200)
	external_customer_id = models.IntegerField()
	is_targeting_location = models.BooleanField(default=True)
	metro_criteria_id = models.CharField(max_length=200)
	most_specific_criteria_id = models.IntegerField()
	region_criteria_id = models.IntegerField()
	date = models.DateField()
	device = models.CharField(max_length=200)
	location_type = models.CharField(max_length=200)
	average_position = models.IntegerField
	clicks = models.IntegerField()
	conversions = models.FloatField()
	conversion_value = models.FloatField()
	cost = models.IntegerField()
	impressions = models.IntegerField()
	interactions = models.IntegerField()
	interaction_types = models.CharField(max_length=200)
	video_views = models.IntegerField()