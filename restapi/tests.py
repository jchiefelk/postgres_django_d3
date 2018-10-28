from django.test import TestCase

class ClientModelTests(TestCase):

  def test_string_represetation(self):
	  clients = Clients(
		account_descriptive_name="My test company",
		campaign_name="test campaign name",
		campaign_status="test status",
		customer_descriptive_name="test description",
		is_targeting_location="San Antonino",
		date="1010",
		device="android",
		location_type="city",
		average_position="test position",
		conversions="0.00",
		conversion_value="0.00",
		interaction_types="[\"Clicks\"]",
		metro_criteria_id="1332",
		most_specific_criteria_id="1111",
		region_criteria_id="3333",
		city_criteria_id="3434",
		)
	  self.assertEqual(str(clients.account_descriptive_name), clients.account_descriptive_name)  
	  self.assertEqual(str(clients.campaign_name), clients.campaign_name)
	  self.assertEqual(str(clients.campaign_status), clients.campaign_status)
	  self.assertEqual(str(clients.customer_descriptive_name), clients.customer_descriptive_name)
	  self.assertEqual(str(clients.is_targeting_location), clients.is_targeting_location)
	  self.assertEqual(str(clients.date), clients.date)
	  self.assertEqual(str(clients.device), clients.device)
	  self.assertEqual(str(clients.location_type), clients.location_type)
	  self.assertEqual(str(clients.average_position), clients.average_position)
	  self.assertEqual(str(clients.conversions), clients.conversions)
	  self.assertEqual(str(clients.conversion_value), clients.conversion_value)
	  self.assertEqual(str(clients.interaction_types), clients.interaction_types)
	  self.assertEqual(str(clients.metro_criteria_id), clients.metro_criteria_id)
	  self.assertEqual(str(clients.most_specific_criteria_id), clients.most_specific_criteria_id)
	  self.assertEqual(str(clients.region_criteria_id), clients.region_criteria_id)
	  self.assertEqual(str(clients.city_criteria_id), clients.city_criteria_id)

  def test_integer_representation(self):
			clients = Clients(
		  campaign_id=1212,
			country_criteria_id=9090,
			external_customer_id=1010,
			clicks=6,
			cost=100000,
			impressions=4,
			interactions=1,
			video_views=2
			)

			self.assertEqual(int(clients.campaign_id), clients.campaign_id)
			self.assertEqual(int(clients.country_criteria_id), clients.country_criteria_id)
			self.assertEqual(int(clients.external_customer_id), clients.external_customer_id)
			self.assertEqual(int(clients.clicks), clients.clicks)
			self.assertEqual(int(clients.cost), clients.cost)
			self.assertEqual(int(clients.video_views), clients.video_views)
			self.assertEqual(int(clients.impressions), clients.impressions)
			self.assertEqual(int(clients.interactions), clients.interactions)
