from random import randint
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings
from tickets.models import *
from service.models import *
from service import services


@receiver(post_save, sender=TicketRequest)
def send_ticket_search_request(sender, instance, created, **kwargs):
    pass
    # if created:
    #     ticket_request = TicketRequest.objects.get(id = instance.id)
    #     services.APIService.get_new_token()
    #     data = instance.as_json()
    #     headers = {
    #         'Content-Type': 'application/x-www-form-urlencoded',
    #         'Client-Token': services.APIService.get_new_token()
    #     }
    #     response = requests.post(services.APIService.API_URL+'LowFareSearch', json=data, verify=False, headers=headers)
    #     request_obj = json.loads(response.content)
    #     print request_obj
    #     ticket_request.request_code = request_obj['request_code']
    #     ticket_request.save()
    #     print "search request sent and updated"
    #
    #
    #
    #
    #     data = {"request_id": ticket_request.request_code}
    #     headers = {
    #         'Content-Type': 'application/x-www-form-urlencoded',
    #         'Client-Token': services.APIService.get_new_token()
    #     }
    #     response = requests.post(services.APIService.API_URL + 'FareSearchResult', json=data, verify=False, headers=headers)
    #     request_obj = json.loads(response.content)
    #     if 'outbound' in request_obj:
    #         for ticket in request_obj['outbound']:
    #             print "RRRRRRRR"
    #             ticket_request.outbands.create(
    #                 ticket_request_return = None,
    #                 ref_number=ticket['ref_number'],
    #                 price = ticket['price'],
    #                 discount = ticket['discount'],
    #                 discount_percent = ticket['discount_percent'],
    #                 currency_code = ticket['currency_code'],
    #                 capacity = ticket['capacity'],
    #                 flight_type = ticket['flight_type'],
    #                 description = ticket['description'],
    #                 flight_details = FlightDetails.objects.create(
    #                     flight_number=ticket['flight_details']['flight_number'],
    #                     flight_class=ticket['flight_details']['class'],
    #                     cabin=ticket['flight_details']['cabin'],
    #                     refund=ticket['flight_details']['refund'],
    #                     operator=ticket['flight_details']['operator'],
    #                     airline=ticket['flight_details']['airline'],
    #                     airplane=ticket['flight_details']['airplane'],
    #                     airline_name_fa=ticket['flight_details']['airline_name_fa'],
    #                     airline_name_en=ticket['flight_details']['airline_name_en'],
    #                     airline_name=ticket['flight_details']['airline_name'],
    #                     source=ticket['flight_details']['source'],
    #                 ),
    #                 departure = AirportDate.objects.create(
    #                     location_code=ticket['departure']['location_code'],
    #                     airport_name_fa = ticket['departure']['airport_name_fa'],
    #                     airport_name_en = ticket['departure']['airport_name_en'],
    #                     city_name_fa = ticket['departure']['city_name_fa'],
    #                     city_name_en = ticket['departure']['city_name_en'],
    #                     country_code = ticket['departure']['country_code'],
    #                     date=datetime.datetime.strptime(ticket['departure']['date'], '%Y-%m-%d'),
    #                     time=datetime.datetime.strptime(ticket['departure']['time'], '%H:%M:%S')
    #                 ),
    #                 arrival =AirportDate.objects.create(
    #                     location_code=ticket['arrival']['location_code'],
    #                     airport_name_fa = ticket['arrival']['airport_name_fa'],
    #                     airport_name_en = ticket['arrival']['airport_name_en'],
    #                     city_name_fa = ticket['arrival']['city_name_fa'],
    #                     city_name_en = ticket['arrival']['city_name_en'],
    #                     country_code = ticket['arrival']['country_code'],
    #                     date = datetime.datetime.strptime(ticket['arrival']['date'], '%Y-%m-%d'),
    #                     time = datetime.datetime.strptime(ticket['arrival']['time'], '%H:%M:%S')
    #                 ),
    #                 # passenger_fare_adult = PassengerFare.objects.create(
    #                 #     fare=ticket['passenger_fare']['adult']['fare'],
    #                 #     fee=ticket['passenger_fare']['adult']['fee'],
    #                 #     tax=ticket['passenger_fare']['adult']['tax'],
    #                 # ),
    #                 # passenger_fare_child = PassengerFare.objects.create(
    #                 #     fare=ticket['passenger_fare']['child']['fare'],
    #                 #     fee=ticket['passenger_fare']['child']['fee'],
    #                 #     tax=ticket['passenger_fare']['child']['tax'],
    #                 # ),
    #                 # passenger_fare_infant =PassengerFare.objects.create(
    #                 #     fare=ticket['passenger_fare']['infant']['fare'],
    #                 #     fee=ticket['passenger_fare']['infant']['fee'],
    #                 #     tax=ticket['passenger_fare']['infant']['tax'],
    #                 # ),
    #                 # baggages = Baggage.objects.create(
    #                 #     baggage_type=ticket['baggages']['type'],
    #                 #     Quantity=ticket['baggages']['Quantity'],
    #                 #     Unit=ticket['baggages']['Unit'],
    #                 # ),
    #                 duration = "00:00:00"
    #             )
    #     if 'return' in request_obj:
    #         for ticket in request_obj['return']:
    #                 ticket_request.returns.create(
    #                     ticket_request_outband=None,
    #                     ref_number=ticket['ref_number'],
    #                     price=ticket['price'],
    #                     discount=ticket['discount'],
    #                     discount_percent=ticket['discount_percent'],
    #                     currency_code=ticket['currency_code'],
    #                     capacity=ticket['capacity'],
    #                     flight_type=ticket['flight_type'],
    #                     description=ticket['description'],
    #                     flight_details=FlightDetails.objects.create(
    #                         flight_number=ticket['flight_details']['flight_number'],
    #                         flight_class=ticket['flight_details']['class'],
    #                         cabin=ticket['flight_details']['cabin'],
    #                         refund=ticket['flight_details']['refund'],
    #                         operator=ticket['flight_details']['operator'],
    #                         airline=ticket['flight_details']['airline'],
    #                         airplane=ticket['flight_details']['airplane'],
    #                         airline_name_fa=ticket['flight_details']['airline_name_fa'],
    #                         airline_name_en=ticket['flight_details']['airline_name_en'],
    #                         airline_name=ticket['flight_details']['airline_name'],
    #                         source=ticket['flight_details']['source'],
    #                     ),
    #                     departure=AirportDate.objects.create(
    #                         location_code=ticket['departure']['location_code'],
    #                         airport_name_fa=ticket['departure']['airport_name_fa'],
    #                         airport_name_en=ticket['departure']['airport_name_en'],
    #                         city_name_fa=ticket['departure']['city_name_fa'],
    #                         city_name_en=ticket['departure']['city_name_en'],
    #                         country_code=ticket['departure']['country_code'],
    #                         date=datetime.datetime.strptime(ticket['departure']['date'], '%Y-%m-%d'),
    #                         time=datetime.datetime.strptime(ticket['departure']['time'], '%H:%M:%S')
    #                     ),
    #                     arrival=AirportDate.objects.create(
    #                         location_code=ticket['arrival']['location_code'],
    #                         airport_name_fa=ticket['arrival']['airport_name_fa'],
    #                         airport_name_en=ticket['arrival']['airport_name_en'],
    #                         city_name_fa=ticket['arrival']['city_name_fa'],
    #                         city_name_en=ticket['arrival']['city_name_en'],
    #                         country_code=ticket['arrival']['country_code'],
    #                         date=datetime.datetime.strptime(ticket['arrival']['date'], '%Y-%m-%d'),
    #                         time=datetime.datetime.strptime(ticket['arrival']['time'], '%H:%M:%S')
    #                     ),
    #                     # passenger_fare_adult = PassengerFare.objects.create(
    #                     #     fare=ticket['passenger_fare']['adult']['fare'],
    #                     #     fee=ticket['passenger_fare']['adult']['fee'],
    #                     #     tax=ticket['passenger_fare']['adult']['tax'],
    #                     # ),
    #                     # passenger_fare_child = PassengerFare.objects.create(
    #                     #     fare=ticket['passenger_fare']['child']['fare'],
    #                     #     fee=ticket['passenger_fare']['child']['fee'],
    #                     #     tax=ticket['passenger_fare']['child']['tax'],
    #                     # ),
    #                     # passenger_fare_infant =PassengerFare.objects.create(
    #                     #     fare=ticket['passenger_fare']['infant']['fare'],
    #                     #     fee=ticket['passenger_fare']['infant']['fee'],
    #                     #     tax=ticket['passenger_fare']['infant']['tax'],
    #                     # ),
    #                     # baggages = Baggage.objects.create(
    #                     #     baggage_type=ticket['baggages']['type'],
    #                     #     Quantity=ticket['baggages']['Quantity'],
    #                     #     Unit=ticket['baggages']['Unit'],
    #                     # ),
    #                     duration="00:00:00"
    #                 )
    #     ticket_request.save()
    #     if request_obj.has_key("return"):
    #         for ticket in request_obj['return']:
    #             print ticket['ref_number']
