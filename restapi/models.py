from django.db import models
# Create your models here.
class Clients(models.Model):
	account_descriptive_name = models.CharField(max_length=200, null=True)
	campaign_id = models.IntegerField(null=True)
	campaign_name = models.CharField(max_length=200, null=True)
	campaign_status = models.CharField(max_length=200, null=True)
	city_criteria_id = models.CharField(max_length=200, null=True)
	country_criteria_id = models.IntegerField(null=True)
	customer_descriptive_name = models.CharField(max_length=200, null=True)
	external_customer_id = models.BigIntegerField(null=True)
	is_targeting_location = models.BooleanField(default=True)
	metro_criteria_id = models.CharField(max_length=200, null=True)
	most_specific_criteria_id = models.IntegerField(null=True)
	region_criteria_id = models.CharField(max_length=200, null=True)
	date = models.CharField(max_length=200, null=True)
	device = models.CharField(max_length=200, null=True)
	location_type = models.CharField(max_length=200, null=True)
	average_position = models.CharField(max_length=200, null=True)
	clicks = models.IntegerField(null=True)
	conversions = models.CharField(max_length=200, null=True)
	conversion_value = models.FloatField(null=True)
	cost = models.IntegerField(null=True)
	impressions = models.IntegerField(null=True)
	interactions = models.IntegerField(null=True)
	interaction_types = models.CharField(max_length=200, null=True)
	video_views = models.IntegerField(null=True)

	def __str__(self):
	  return self
