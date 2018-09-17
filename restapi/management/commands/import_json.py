from django.core.management.base import BaseCommand, CommandError
import psycopg2, os, json, sys

class Command(BaseCommand):
	help = "Imports Json data into PostgreSQL"

	def add_arguments(self, parser):
		parser.add_argument(
	    '--filepath', dest='filepath', required=True,
	    help='add path to json file to import',
		)

	def handle(self, *args, **options):
		print(options['filepath'])
		conn = psycopg2.connect(dbname=os.environ.get('POSTGRES_DB_NAME', ''), user=os.environ.get('POSTGRES_USER', ''), password=os.environ.get('POSTGRES_PASSWORD', ''))
		cur = conn.cursor()
		with open(options['filepath']) as f:
			data = json.load(f)
			for row in data:
				sqldata = '('+"'"+row['AccountDescriptiveName']+"','"+row['CampaignId']+"','"+row['CampaignName']+"','"+row['CampaignStatus']+"','"+row['CityCriteriaId']+"','"+row['CountryCriteriaId']+"','"+row['CustomerDescriptiveName']+"','"+row['ExternalCustomerId']+"','"+row['IsTargetingLocation']+"','"+row['MetroCriteriaId']+"','"+row['MostSpecificCriteriaId']+"','"+row['RegionCriteriaId']+"','"+row['Date']+"','"+row['Device']+"','"+row['LocationType']+"','"+row['AveragePosition']+"','"+row['Clicks'] +"','"+row['Conversions']+"','"+row['ConversionValue']+"','"+row['Cost']+"','"+row['Impressions']+"','"+row['Interactions']+"','"+row['InteractionTypes']+"','"+row['VideoViews']+"')"
				sql = "INSERT INTO restapi_clients(account_descriptive_name, campaign_id, campaign_name, campaign_status, city_criteria_id, country_criteria_id, customer_descriptive_name, external_customer_id, is_targeting_location, metro_criteria_id, most_specific_criteria_id, region_criteria_id, date, device, location_type, average_position, clicks, conversions, conversion_value, cost, impressions, interactions, interaction_types, video_views) VALUES "+sqldata
				cur.execute(sql)
		conn.commit()
