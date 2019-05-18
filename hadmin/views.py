# -*- coding: utf-8 -*-
#!/usr/bin/python
from django.shortcuts import render
from service import jalali

from CMS.models import Article, Catagory, CharityPage, Page, Product_Catagory, Tag, TeamMember, Comment, Customer, \
    Project, Setting, Slider, Product, Feedback
from master.models import City, Country, Airline
from django.shortcuts import get_object_or_404, redirect
from datetime import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,  login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from hotels.models import Hotel, HotelOption, HotelImage
from tickets.models import BookedTicket
from tours.models import Tour, TourHotel, TourImage, TourDestination, TourType, TourService
from userprofile.models import UserProfile, Subscriber
from service.functions import *
from django.contrib.admin.views.decorators import staff_member_required
#from kavenegar import *


from django.views import generic

import StringIO
import xlsxwriter
import csv
from django.http import HttpResponse



def subscriber_excel(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Subscribers.xlsx'
    subscriber_data = Subscriber.objects.all()
    xlsx_data = WriteSubscriberToExcel(subscriber_data)
    response.write(xlsx_data)
    return response


def WriteSubscriberToExcel(data):
    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet_s = workbook.add_worksheet("Summary")

    header = workbook.add_format({
        'bg_color': '#F7F7F7',
        'color': 'black',
        'align': 'center',
        'valign': 'top',
        'border': 1
    })
    # the rest of the headers from the HTML file
    worksheet_s.write_string('A1', 'ID', header)
    worksheet_s.write_string('B1', 'First Name', header)
    worksheet_s.write_string('C1', 'Last Name', header)
    worksheet_s.write_string('D1', 'Mobile', header)
    worksheet_s.write_string('E1', 'Subscription Date', header)
    worksheet_s.write_string('F1', 'Domestic Tour', header)
    row_number = 1
    for sub in data:
        row_number = row_number + 1
        worksheet_s.write_string('A'+str(row_number), unicode(sub.id) )
        worksheet_s.write_string('B'+str(row_number), unicode(sub.first_name))
        worksheet_s.write_string('C'+str(row_number), unicode(sub.last_name))
        worksheet_s.write_string('D'+str(row_number), unicode(sub.mobile))
        worksheet_s.write_string('E'+str(row_number), unicode(sub.subscription_date))
        worksheet_s.write_string('F'+str(row_number), unicode(sub.domestic_tour))
    # Here we will adding the code to add data
    workbook.close()
    xlsx_data = output.getvalue()
    # xlsx_data contains the Excel file
    return xlsx_data


def users_excel(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Users.xlsx'
    user_data = UserProfile.objects.all()
    xlsx_data = WriteUsersToExcel(user_data)
    response.write(xlsx_data)
    return response


def WriteUsersToExcel(data):
    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet_s = workbook.add_worksheet("Summary")

    header = workbook.add_format({
        'bg_color': '#F7F7F7',
        'color': 'black',
        'align': 'center',
        'valign': 'top',
        'border': 1
    })
    # the rest of the headers from the HTML file
    worksheet_s.write_string('A1', 'ID', header)
    worksheet_s.write_string('B1', 'Username', header)
    worksheet_s.write_string('C1', 'Email', header)
    worksheet_s.write_string('D1', 'Mobile', header)
    worksheet_s.write_string('E1', 'First Name', header)
    worksheet_s.write_string('F1', 'Last Name', header)
    worksheet_s.write_string('G1', 'Code Melli', header)
    worksheet_s.write_string('H1', 'Postal Code', header)
    worksheet_s.write_string('I1', 'Phone', header)
    row_number = 1
    for user in data:
        row_number = row_number + 1
        worksheet_s.write_string('A'+str(row_number), unicode(user.id) )
        worksheet_s.write_string('B'+str(row_number), unicode(user.username) )
        worksheet_s.write_string('C'+str(row_number), unicode(user.email) )
        worksheet_s.write_string('D'+str(row_number), unicode(user.mobile) )
        worksheet_s.write_string('E'+str(row_number), unicode(user.first_name))
        worksheet_s.write_string('F'+str(row_number), unicode(user.last_name))
        worksheet_s.write_string('G'+str(row_number), unicode(user.code_meli))
        worksheet_s.write_string('H'+str(row_number), unicode(user.postal_code))
        worksheet_s.write_string('I'+str(row_number), unicode(user.phone))
    # Here we will adding the code to add data
    workbook.close()
    xlsx_data = output.getvalue()
    # xlsx_data contains the Excel file
    return xlsx_data


def flights_excel(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=FlightReport.xlsx'
    flight_data = BookedTicket.objects.all()
    xlsx_data = WriteFlightToExcel(flight_data)
    response.write(xlsx_data)
    return response


def WriteFlightToExcel(data):
    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet_s = workbook.add_worksheet("Summary")

    header = workbook.add_format({
        'bg_color': '#F7F7F7',
        'color': 'black',
        'align': 'center',
        'valign': 'top',
        'border': 1
    })
    # the rest of the headers from the HTML file
    worksheet_s.write_string('A1', 'ID', header)
    worksheet_s.write_string('B1', 'RefIF', header)
    worksheet_s.write_string('C1', 'Airplane', header)
    worksheet_s.write_string('D1', 'FirstName', header)
    worksheet_s.write_string('E1', 'LastName', header)
    worksheet_s.write_string('F1', 'FlightNumber', header)
    worksheet_s.write_string('G1', 'DepartureIATA', header)
    worksheet_s.write_string('H1', 'Departure', header)
    worksheet_s.write_string('I1', 'ArrivalIATA', header)
    worksheet_s.write_string('J1', 'Arrival', header)
    row_number = 1
    for flight in data:
        row_number = row_number + 1
        worksheet_s.write_string('A'+str(row_number), str(flight.id) )
        worksheet_s.write_string('B'+str(row_number), str(flight.refrence_id) )
        worksheet_s.write_string('C'+str(row_number), flight.ticket.flight_details.airline_name_fa )
        worksheet_s.write_string('D'+str(row_number), flight.ticket.passenger_set.all()[0].persian_given_name )
        worksheet_s.write_string('E'+str(row_number), flight.ticket.passenger_set.all()[0].persian_surname )
        worksheet_s.write_string('F'+str(row_number), flight.ticket.flight_details.flight_number )
        worksheet_s.write_string('G'+str(row_number), flight.ticket.departure.location_code )
        worksheet_s.write_string('H'+str(row_number), flight.ticket.departure.airport_name_fa )
        worksheet_s.write_string('I'+str(row_number), flight.ticket.arrival.location_code )
        worksheet_s.write_string('J'+str(row_number), flight.ticket.arrival.airport_name_fa )
    # Here we will adding the code to add data

    workbook.close()
    xlsx_data = output.getvalue()
    # xlsx_data contains the Excel file
    return xlsx_data


class TicketListView(generic.ListView):
    model = BookedTicket
    template_name = "hadmin/flight/list.html"


@login_required
def edit_settings(request):
    return render(
        request,
        "hadmin/settings/edit.html",
        {
            "settings": Setting.objects.get(is_active = True)
        }
    )

@login_required
def set_article(request):
    if request.POST:
        post = Article(
            author = request.user,
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            creation_date = datetime.now(),
            publish_date = datetime.now(),
            slug = request.POST.get('title').replace('  ',' ').replace(' ', '-').replace('/', '-'),
            catagory = Catagory.objects.get(id = request.POST.get('catagory')),
            image = request.FILES.get('image'),
            image_alt = request.POST.get('image_alt')
        )
        post.save()
    return render(
        request,
        "hadmin/post/add.html",
        {
            "tags" : Tag.objects.all(),
            "catagories" : Catagory.objects.all()
        }
    )

@login_required
def get_articles(request):
    return render(
        request,
        "hadmin/post/list.html",
        {
            "tags" : Tag.objects.all(),
            "catagories" : Catagory.objects.all(),
            "posts" : Article.objects.all()
        }
    )

@login_required
def edit_article(request, post_id):
    post = Article.objects.get(id=post_id)
    if request.POST:
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        if request.POST.get('catagory'):
            if request.POST.get('catagory') == 0:
                post.catagory = None
            else:
                post.catagory = Catagory.objects.get(id = request.POST.get('catagory'))
        post.image_alt = request.POST.get('image_alt')
        if request.FILES.get('image'):
            post.image = request.FILES.get('image')
        post.save()
    return render(
        request,
        "hadmin/post/edit.html",
        {
            "post" : post,
            "catagories" : Catagory.objects.all(),
            "tags" : Tag.objects.all(),
        }
    )


@login_required
def delete_article(request,  post_id):
    article = Article.objects.get(id = post_id)
    article.delete()
    return HttpResponseRedirect(reverse('get_articles'))


@login_required
def set_hotel(request):
    options = HotelOption.objects.all()
    if request.POST:
        hotel = Hotel.objects.create(
            HotelName = request.POST.get('HotelName'),
            HotelEnName = request.POST.get('HotelEnName'),
            HotelTell = request.POST.get('HotelTell'),
            HotelFax = request.POST.get('HotelFax'),
            HotelSite = request.POST.get('HotelSite'),
            HotelAddress = request.POST.get('HotelAddress'),
            HotelRules = request.POST.get('rules'),
            HotelDescription = request.POST.get('content'),
        )
        if request.POST.get('HotelStar'):
            hotel.HotelStar = request.POST.get('HotelStar')
        else:
            hotel.HotelStar = 0
        if request.POST.get('city'):
            if request.POST.get('city') == 0:
                city = None
            else:
                city = City.objects.get(id=request.POST.get('city'))
                hotel.city=city
        if request.POST.get('country'):
            if request.POST.get('country') == 0:
                country = None
            else:
                country = Country.objects.get(id=request.POST.get('country'))
                hotel.country = country
        if request.FILES.get('image'):
            image = request.FILES.get('image')
            hotel.image = image
        for option in options:
            if request.POST.get('option'+str(option.pk)):
                hotel.options.add(option)
        for i in range(0, 20):
            if request.FILES.get('category-group['+str(i)+'][image]'):
                img = request.FILES.get('category-group['+str(i)+'][image]')
                image = hotel.hotelimage_set.create(image=img)
            else:
                break
        hotel.save()
        return HttpResponseRedirect(reverse('hadmin:get_hotels'))
    return render(
        request,
        "hadmin/hotels/add.html",
        {
            "options" : options,
            "countries" : Country.objects.all(),
            "stars": range(1, 6),
        }
    )


@login_required
def get_hotels(request):
    return render(
        request,
        "hadmin/hotels/list.html",
        {
            "hotels" : Hotel.objects.all(),
        }
    )


@login_required
def edit_hotel(request, hotel_id):
    options = HotelOption.objects.all()
    hotel = Hotel.objects.get(id=hotel_id)
    if request.POST:
        hotel.HotelName = request.POST.get('HotelName')
        hotel.HotelEnName = request.POST.get('HotelEnName')
        if request.POST.get('HotelStar'):
            hotel.HotelStar = request.POST.get('HotelStar')
        hotel.HotelTell = request.POST.get('HotelTell')
        hotel.HotelFax = request.POST.get('HotelFax')
        hotel.HotelSite = request.POST.get('HotelSite')
        hotel.HotelAddress = request.POST.get('HotelAddress')
        if request.POST.get('city'):
            if request.POST.get('city') == 0:
                hotel.city = None
            else:
                hotel.city = City.objects.get(id = request.POST.get('city'))
        if request.POST.get('country'):
            if request.POST.get('country') == 0:
                hotel.country = None
            else:
                hotel.country = Country.objects.get(id=request.POST.get('country'))
        if request.FILES.get('image'):
            hotel.image = request.FILES.get('image')
        hotel.HotelRules = request.POST.get('rules')
        hotel.HotelDescription = request.POST.get('content')
        for option in options:
            if request.POST.get('option'+str(option.pk)):
                hotel.options.add(option)
            else:
                hotel.options.remove(option)

        hotelimages = HotelImage.objects.filter(hotel_id=hotel.id)
        for img in hotelimages:
            if not request.POST.get('hotelimage'+str(img.id)):
                img = HotelImage.objects.get(id = img.id)
                img.delete()

        for i in range(0, 20):
            if request.FILES.get('category-group['+str(i)+'][image]'):
                img = request.FILES.get('category-group['+str(i)+'][image]')
                image = hotel.hotelimage_set.create(image=img)
            else:
                break

        hotel.save()

    return render(
        request,
        "hadmin/hotels/edit.html",
        {
            "hotel" : Hotel.objects.get(id=hotel_id),
            "options" : HotelOption.objects.all(),
            "countries" : Country.objects.all(),
            "stars": range(1, 6),
        }
    )


@login_required
def delete_hotel(request,  hotel_id):
    hotel = Hotel.objects.get(id = hotel_id)
    hotel.delete()
    return HttpResponseRedirect(reverse('hadmin:get_hotels'))


@login_required
def get_options(request):
    if request.POST:
        name = request.POST.get('name')
        icon = None
        if request.FILES.get('icon'):
            icon = request.FILES.get('icon')
        HotelOption.objects.create(name=name, icon=icon)
    return render(
        request,
        "hadmin/hotels/hoteloptions/list.html",
        {
            "options" : HotelOption.objects.all(),
        }
    )


@login_required
def delete_option(request, option_id):
    option = HotelOption.objects.get(id = option_id)
    option.delete()
    return HttpResponseRedirect(reverse('hadmin:get_options'))


@login_required
def get_services(request):
    if request.POST:
        name = request.POST.get('name')
        TourService.objects.create(name=name)
    return render(
        request,
        "hadmin/tours/tourservices/list.html",
        {
            "services" : TourService.objects.all(),
        }
    )


@login_required
def delete_service(request, service_id):
    service = TourService.objects.get(id = service_id)
    service.delete()
    return HttpResponseRedirect(reverse('hadmin:get_services'))



@login_required
def set_hotel_tour(request, tour_id):
    if request.POST:
        hotelName = request.POST.get('hotelName')
        hotelStar =request.POST.get('hotelStar')
        if request.POST.get('singlePrice'):
            singlePrice = request.POST.get('singlePrice')
        else:
            singlePrice = 0
        if request.POST.get('doublePrice'):
            doublePrice = request.POST.get('doublePrice')
        else:
            doublePrice = 0
        if request.POST.get('childPrice'):
            childPrice = request.POST.get('childPrice')
        else:
            childPrice = 0
        if request.POST.get('childWOBedPrice'):
            childWOBedPrice = request.POST.get('childWOBedPrice')
        else:
            childWOBedPrice = 0
        if request.POST.get('infPrice'):
            infPrice = request.POST.get('infPrice')
        else:
            infPrice = 0
        if request.POST.get('service'):
            service = TourService.objects.get(id=request.POST.get('service'))
        else:
            service = 0
        if request.POST.get('hotelLink'):
            hotelLink = request.POST.get('hotelLink')
        else:
            hotelLink = None

        tour = Tour.objects.get(id = tour_id)
        tour.tourhotel_set.create(
            hotelName=hotelName,
            hotelStar = int(hotelStar),
            service = service,
            singlePrice = int(singlePrice),
            doublePrice = doublePrice,
            childPrice = childPrice,
            childWOBedPrice = childWOBedPrice,
            infPrice = infPrice,
            hotelLink = hotelLink,
        )
    url = reverse('hadmin:edit_tour', kwargs={'tour_id': tour_id})
    return HttpResponseRedirect(url)


@login_required
def edit_hotel_tour(request,tour_id, hotel_id):
    tourhotel = TourHotel.objects.get(id=hotel_id)
    if request.POST:
        tourhotel.hotelName = request.POST.get('hotelName')
        tourhotel.hotelStar =request.POST.get('hotelStar')
        if request.POST.get('singlePrice'):
            tourhotel.singlePrice = request.POST.get('singlePrice')
        if request.POST.get('doublePrice'):
            tourhotel.doublePrice = request.POST.get('doublePrice')
        if request.POST.get('childPrice'):
            tourhotel.childPrice = request.POST.get('childPrice')
        if request.POST.get('childWOBedPrice'):
            tourhotel.childWOBedPrice = request.POST.get('childWOBedPrice')
        if request.POST.get('infPrice'):
            tourhotel.infPrice = request.POST.get('infPrice')
        if request.POST.get('service'):
            tourhotel.service = TourService.objects.get(id=request.POST.get('service'))
        if request.POST.get('hotelLink'):
            tourhotel.hotelLink = request.POST.get('hotelLink')
        tourhotel.save()
    url = reverse('hadmin:edit_tour', kwargs={'tour_id': tour_id})
    return HttpResponseRedirect(url)


@login_required
def delete_hotel_tour(request, hotel_id, tour_id):
    hotel = TourHotel.objects.get(id = hotel_id)
    hotel.delete()
    url = reverse('hadmin:edit_tour', kwargs={'tour_id': tour_id})
    return HttpResponseRedirect(url)

@login_required
def set_tour(request):
    if request.POST:
        if request.POST.get('title'):
            title = request.POST.get('title')
        else:
            title = None
        if request.POST.get('code'):
            code = request.POST.get('code')
        else:
            code = None
        if request.POST.get('stay_nights'):
            stay_nights = request.POST.get('stay_nights')
        else:
            stay_nights = 0
        if request.POST.get('capacity'):
            capacity = request.POST.get('capacity')
        else:
            capacity = 0
        if request.POST.get('min_price'):
            min_price = request.POST.get('min_price')
        else:
            min_price = 0
        if request.POST.get('outband_time'):
            outband_time = request.POST.get('outband_time')
        else:
            outband_time = datetime.now().time()
        if request.POST.get('return_time'):
            return_time = request.POST.get('return_time')
        else:
            return_time = datetime.now().time()
        if request.POST.get('outband_date'):
            outband_date = get_georgian_date(request.POST.get('outband_date'))
        else:
            outband_date = datetime.now().time()
        if request.POST.get('expire_date'):
            expire_date = get_georgian_date(request.POST.get('expire_date'))
        else:
            expire_date = datetime.now().time()
        if request.POST.get('documents'):
            documents =request.POST.get('documents')
        else:
            documents = None
        if request.POST.get('description'):
            description = request.POST.get('description')
        else:
            description = None
        tour = Tour.objects.create(
            title = title,
            code = code,
            stay_nights = stay_nights,
            capacity=capacity,
            min_price= min_price,
            outband_date = outband_date,
            outband_time = outband_time,
            return_time = return_time,
            expire_date = expire_date,
            documents = documents,
            description = description,
        )
        if request.POST.get('is_domestic'):
            tour.type = TourType.objects.get(id=request.POST.get('is_domestic'))
        if request.POST.get('city'):
            if request.POST.get('city') == 0:
                tour.origin = None
            else:
                tour.origin = City.objects.get(id=request.POST.get('city'))
        if request.POST.get('airline'):
            if request.POST.get('airline') == 0:
                tour.airline = None
            else:
                tour.airline = Airline.objects.get(id=request.POST.get('airline'))
        if request.FILES.get('image'):
            tour.image = request.FILES.get('image')
        for i in range(0, 20):
            if request.FILES.get('category-group[' + str(i) + '][image]'):
                img = request.FILES.get('category-group[' + str(i) + '][image]')
                image = tour.tourimage_set.create(image=img)
            else:
                break
        for i in range(0, 20):
            if request.POST.get('category-group[' + str(i) + '][city]'):
                city_id = request.POST.get('category-group[' + str(i) + '][city]')
                dest = TourDestination.objects.get_or_create(city=City.objects.get(id=city_id))[0]
                tour.destinations.add(dest)
            else:
                break
        tour.save()
        url = reverse('hadmin:edit_tour', kwargs={'tour_id': tour.id})
        return HttpResponseRedirect(url)
    return render(
        request,
        "hadmin/tours/add.html",
        {
            "airlines" : Airline.objects.all(),
            "cities" : City.objects.all(),
            "countries": Country.objects.all(),
        }
    )


@login_required
def get_tours(request):
    return render(
        request,
        "hadmin/tours/list.html",
        {
            "tours" : Tour.objects.all(),
        }
    )


def get_georgian_date(jalali_date):
    jalali_date = jalali_date.split("/")
    year = None
    month = None
    day = None
    if int(jalali_date[0]) > 1000:
        year = str(jalali_date[0])
        month = str(jalali_date[1])
        day = str(jalali_date[2])
    else:
        year = str(jalali_date[2])
        month = str(jalali_date[1])
        day = str(jalali_date[0])
    return jalali.Persian(year, month, day).gregorian_datetime()


@login_required
def edit_tour(request, tour_id):
    tour = Tour.objects.get(id=tour_id)
    if request.POST:
        tour.title = request.POST.get('title')
        tour.code = request.POST.get('code')
        tour.stay_nights = request.POST.get('stay_nights')
        tour.capacity = request.POST.get('capacity')
        tour.min_price = request.POST.get('min_price')
        tour.outband_time = request.POST.get('outband_time')
        tour.return_time = request.POST.get('return_time')
        tour.outband_date = get_georgian_date(request.POST.get('outband_date'))
        tour.expire_date = get_georgian_date(request.POST.get('expire_date'))
        tour.documents = request.POST.get('documents')
        tour.description = request.POST.get('description')
        if request.POST.get('is_domestic'):
            tour.type = TourType.objects.get(id=request.POST.get('is_domestic'))
        if request.POST.get('city'):
            if request.POST.get('city') == 0:
                tour.origin = None
            else:
                tour.origin = City.objects.get(id = request.POST.get('city'))
        if request.POST.get('airline'):
            if request.POST.get('airline') == 0:
                tour.airline = None
            else:
                tour.airline = Airline.objects.get(id=request.POST.get('airline'))
        if request.FILES.get('image'):
            tour.image = request.FILES.get('image')
        destinations = TourDestination.objects.all()
        for dest in destinations:
            if not request.POST.get('dest'+str(dest.pk)):
                tour.destinations.remove(dest)
        tourimages = TourImage.objects.filter(tour_id=tour.id)
        for img in tourimages:
            if not request.POST.get('hotelimage'+str(img.id)):
                img = TourImage.objects.get(id = img.id)
                img.delete()
        for i in range(0, 20):
            if request.FILES.get('category-group['+str(i)+'][image]'):
                img = request.FILES.get('category-group['+str(i)+'][image]')
                image = tour.tourimage_set.create(image=img)
            else:
                break
        for i in range(0, 20):
            if request.POST.get('category-group['+str(i)+'][city]'):
                city_id = request.POST.get('category-group['+str(i)+'][city]')
                dest = TourDestination.objects.get_or_create(city=City.objects.get(id = city_id))[0]
                tour.destinations.add(dest)
            else:
                break
        tour.save()
    return render(
        request,
        "hadmin/tours/edit.html",
        {
            "tour": Tour.objects.get(id=tour_id),
            "airlines" : Airline.objects.all(),
            "cities" : City.objects.all(),
            "countries":Country.objects.all(),
            "hotels":Hotel.objects.all(),
            "services":TourService.objects.all()
        }
    )


@login_required
def delete_tour(request,  tour_id):
    tour = Tour.objects.get(id = tour_id)
    tour.delete()
    return HttpResponseRedirect(reverse('hadmin:get_tours'))


@login_required
def get_cities(request, country_id):
    country = Country.objects.get(id = country_id)
    if request.POST:
        name = request.POST.get ('name')
        country.city_set.create(CityName=name)
    return render(
        request,
        "hadmin/master/city/list.html",
        {
            "cities" : City.objects.filter(country_id = country_id),
            "country": country,
        }
    )


@login_required
def delete_city(request, city_id):
    city = City.objects.get(id = city_id)
    city.delete()
    url = reverse('hadmin:get_cities', kwargs={'country_id': city.country_id})
    return HttpResponseRedirect(url)


@login_required
def get_countries(request):
    if request.POST:
        name = request.POST.get ('name')
        Country.objects.create(CountryName=name)
    return render(
        request,
        "hadmin/master/country/list.html",
        {
            "countries" : Country.objects.all(),
        }
    )


@login_required
def delete_country(request, country_id):
    country = Country.objects.get(id = country_id)
    country.delete()
    return HttpResponseRedirect(reverse('hadmin:get_countries'))


@login_required
def get_airlines(request):
    if request.POST:
        name_en = request.POST.get('name_en')
        name_fa = request.POST.get('name_fa')
        iata = request.POST.get('iata')
        logo = request.FILES.get('logo')
        Airline.objects.create(name_en=name_en, name_fa=name_fa, iata=iata, logo=logo)
    return render(
        request,
        "hadmin/master/airline/list.html",
        {
            "airlines" : Airline.objects.all(),
        }
    )


@login_required
def delete_airline(request, airline_id):
    airline = Airline.objects.get(id = airline_id)
    airline.delete()
    return HttpResponseRedirect(reverse('hadmin:get_airlines'))


@login_required
def set_project(request):
    if request.POST:
        post = Project(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            creation_date = datetime.now(),
            publish_date = datetime.now(),
            slug = request.POST.get('title').replace('  ',' ').replace(' ', '-').replace('/', '-'),
            #catagory = Catagory.objects.get(name = request.POST.get('catagory')),
            image = request.FILES.get('image'),
            image_alt = request.POST.get('image_alt')
        )
        post.save()
    return render(
        request,
        "hadmin/project/add.html",
        {
            "tags" : Tag.objects.all(),
            "catagories" : Catagory.objects.all()
        }
    )


@login_required
def get_projects(request):
    return render(
        request,
        "hadmin/project/list.html",
        {
            "tags" : Tag.objects.all(),
            "catagories" : Catagory.objects.all(),
            "projects" : Project.objects.all()
        }
    )


@login_required
def edit_project(request, post_id):
    post = Project.objects.get(id=post_id)
    if request.POST:
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        #post.catagory = Catagory.objects.get(name = request.POST.get('catagory'))
        post.image_alt = request.POST.get('image_alt')
        if request.FILES.get('image'):
            post.image = request.FILES.get('image')
        post.save()
    return render(
        request,
        "hadmin/project/edit.html",
        {
            "post" : post,
            "catagories" : Catagory.objects.all(),
            "tags" : Tag.objects.all(),
        }
    )


@login_required
def delete_project(request,  post_id):
    project = Project.objects.get(id = post_id)
    project.delete()
    return HttpResponseRedirect(reverse('get_projects'))


@login_required
def set_page(request):
    if request.POST:
        Page.objects.create(
            author = request.user,
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            creation_date = datetime.now(),
            publish_date = datetime.now(),
            link_address = request.POST.get('title').replace('  ',' ').replace(' ', '-').replace('/', '-'),
            navbar_name= request.POST.get('navbar_name'),
            is_in_navbar= (request.POST.get('is_in_navbar') == '1')
        )
        return HttpResponseRedirect(reverse('get_pages'))
    return render(
        request,
        "hadmin/page/add.html",
        {}
    )


@login_required
def get_pages(request):
    return render(
        request,
        "hadmin/page/list.html",
        {
            "pages" : Page.objects.all()
        }
    )


@login_required
def edit_page(request, page_id):
    page = Page.objects.get(id=page_id)
    if request.POST:
            page.author = request.user
            page.title = request.POST.get('title')
            page.content = request.POST.get('content')
            page.link_address = request.POST.get('title').replace('  ',' ').replace(' ', '-').replace('/', '-'),
            page.navbar_name= request.POST.get('navbar_name'),
            page.is_in_navbar= (request.POST.get('is_in_navbar') == '1')
            page.save()
            return HttpResponseRedirect(reverse('get_pages'))
    return render(
        request,
        "hadmin/page/edit.html",
        {
            'page':page,
        }
    )


@login_required
def delete_page(request, page_id):
    page = Page.objects.get(id = page_id)
    page.delete()
    return HttpResponseRedirect(reverse('get_pages'))


@login_required
def set_slider(request):
    if request.POST:
        if request.FILES.get('image'):
            image = request.FILES.get('image'),
            Slider.objects.create(
                caption=request.POST.get('caption'),
                description=request.POST.get('description'),
                order_no=request.POST.get('order_no'),
                image=request.FILES.get('image')
            )
        return HttpResponseRedirect(reverse('get_sliders'))
    return render(
        request,
        "hadmin/slider/add.html",
        {}
    )

@login_required
def get_sliders(request):
    return render(
        request,
        "hadmin/slider/list.html",
        {
            "sliders" : Slider.objects.all().order_by('order_no'),
        }
    )

@login_required
def edit_slider(request, slider_id):
    slider = Slider.objects.get(id = slider_id)
    if request.POST:
        if request.FILES.get('image'):
            slider.image = request.FILES.get('image')
        slider.caption=request.POST.get('caption')
        slider.description=request.POST.get('description')
        slider.order_no=request.POST.get('order_no')
        slider.save()
        return HttpResponseRedirect(reverse('get_sliders'))
    return render(
        request,
        "hadmin/slider/edit.html",
        {
            'slider':slider
        }
    )

@login_required
def delete_slider(request, slider_id):
    slider = Slider.objects.get(id = slider_id)
    slider.delete()
    return HttpResponseRedirect(reverse('get_sliders'))




@login_required
def set_product(request):
    if request.POST:
        name = request.POST.get('name')
        Product.objects.create(
            name=name,
            description=request.POST.get('description'),
            product_catagory=Product_Catagory.objects.get(id=request.POST.get('category')),
            location=request.POST.get('location'),
            slug=name.replace('  ',' ').replace(' ', '-').replace('/', '-'),
            image=request.FILES.get('image')
        )
        return HttpResponseRedirect(reverse('get_products'))
    return render(
        request,
        "hadmin/product/add.html",
        {
            'cats' : Product_Catagory.objects.all(),
        }
    )

@login_required
def get_products(request):
    return render(
        request,
        "hadmin/product/list.html",
        {
            "products" : Product.objects.all(),
        }
    )

@login_required
def edit_product(request, product_id):
    product = Product.objects.get(id = product_id)
    if request.POST:
        if request.FILES.get('image'):
            product.image = request.FILES.get('image')
        product.name=request.POST.get('name')
        product.description=request.POST.get('description')
        product.location=request.POST.get('location')
        product.product_catagory=Product_Catagory.objects.get(id=request.POST.get('category'))
        product.save()
        return HttpResponseRedirect(reverse('get_products'))
    return render(
        request,
        "hadmin/product/edit.html",
        {
            'product':product,
            'cats': Product_Catagory.objects.all(),

        }
    )

@login_required
def delete_product(request, product_id):
    product = Product.objects.get(id = product_id)
    product.delete()
    return HttpResponseRedirect(reverse('get_products'))

@login_required
def get_comments(request):
    return render(
        request,
        "hadmin/comment/list.html",
        {
            "comments" : Comment.objects.all(),
        }
    )
@login_required
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id = comment_id)
    comment.delete()
    return HttpResponseRedirect(reverse('get_comments'))


@login_required
def get_tags(request):
    if request.POST:
        keyword = request.POST.get ('keyword')
        Tag.objects.create(keyword=keyword, slug=keyword.replace('  ',' ').replace(' ', '-').replace('/', '-'))
    return render(
        request,
        "hadmin/tags/list.html",
        {
            "tags" : Tag.objects.all(),
        }
    )


@login_required
def delete_tag(request, tag_id):
    tag = Tag.objects.get(id = tag_id)
    tag.delete()
    return HttpResponseRedirect(reverse('get_tags'))


@login_required
def get_cats(request):
    if request.POST:
        name = request.POST.get ('name')
        Catagory.objects.create(name=name)
    return render(
        request,
        "hadmin/cats/list.html",
        {
            "cats" : Catagory.objects.all(),
        }
    )


@login_required
def delete_cat(request, cat_id):
    cat = Catagory.objects.get(id = cat_id)
    cat.delete()
    return HttpResponseRedirect(reverse('get_cats'))

@login_required
def edit_charity(request):
    charity = CharityPage.objects.all()[0]
    if request.POST:
        charity.title = request.POST.get('title')
        charity.text = request.POST.get('content')
        charity.save()
    return render(
        request,
        "hadmin/pages/charity.html",
        {
            "charity" : charity
        }
    )

@login_required
def edit_about(request):
    settings = Setting.objects.get(is_active=True)
    if request.POST:
        settings.long_descriptioon = request.POST.get('content')
        settings.save()
    return render(
        request,
        "hadmin/pages/about.html",
        {
            "Team" : TeamMember.objects.all(),
            "Customers" : Customer.objects.all(),
            "settings" : settings
        }
    )

@login_required
def edit_contact(request):
    settings = Setting.objects.get(is_active=True)
    if request.POST:
        settings.brief_description = request.POST.get('brief')
        settings.facebook_link = request.POST.get('facebook_link')
        settings.instagram_link = request.POST.get('instagram_link')
        settings.telegram_link = request.POST.get('telegram_link')
        settings.gplus_link = request.POST.get('gplus_link')
        settings.phone_number_1 = request.POST.get('phone_number_1')
        settings.phone_number_2 = request.POST.get('phone_number_2')
        settings.phone_number_3 = request.POST.get('phone_number_3')
        settings.phone_number_4 = request.POST.get('phone_number_4')
        settings.fax_number = request.POST.get('fax_number')
        settings.header_phone = request.POST.get('header_phone')
        settings.address_line_1 = request.POST.get('address_line_1')
        settings.info_email = request.POST.get('info_email')
        settings.save()
    return render(
        request,
        "hadmin/pages/contact.html",
        {
            "settings" : settings
        }
    )



def admin_login(request):
    next_url = request.GET.get('next')
    if request.user.is_authenticated():
        if next_url:
            return HttpResponseRedirect(next_url)
        else:
            return HttpResponseRedirect(reverse('get_articles'))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                if next_url:
                    return HttpResponseRedirect(next_url)
                else:
                    return HttpResponseRedirect(reverse('get_articles'))
            else:
                return HttpResponse("Your User is inactive")
        else:
            return HttpResponse("Invalid login details")
    else:
        return render(request, 'hadmin/login.html')



@login_required
def admin_logout(request):
    logout(request)
    return HttpResponseRedirect('/admin/')


@login_required
def user_list(request):
    users = UserProfile.objects.all()
    return render(
        request,
        "hadmin/user/list.html",
        {
            "users" : users
        }
    )


@login_required
def feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(
        request,
        "hadmin/feedback/list.html",
        {
            "feedbacks" : feedbacks,
        }
    )


@login_required
def feedback_delete(request,  feedback_id):
    feedback = Feedback.objects.get(id=feedback_id)
    feedback.delete()
    return HttpResponseRedirect(reverse('hadmin:feedback_list'))




@login_required
def subscriber_list(request):
    subscribers = Subscriber.objects.all()
    return render(
        request,
        "hadmin/subscriber/list.html",
        {
            "subscribers" : subscribers
        }
    )


@login_required
def edit_user(request, profile_id):
    UserProfile.objects.get(id=profile_id)
    return render(
        request,
        "hadmin/user/edit.html",
        {
            "user" : user
        }
    )

@login_required
def settings(request):
    #api = KavenegarAPI()
    #response = api.sms_send_phone("09351103026", "hello from method")
    print response
    users = User.objects.all()
    return render(
        request,
        "hadmin/settings.html",
        {
            "users" : users
        }
    )

def order(request):
    return render(request, "hadmin/order/list.html", locals())

def ticket(request):
    return render(request, "hadmin/ticket/list.html", locals())

def invoicepay(request):
    return render(request, "hadmin/invoicepay.html", locals())

def noinvoicepay(request):
    return render(request, "hadmin/noinvoicepay.html", locals())

def ticketitem(request):
    return render(request, "hadmin/ticket/ticketitem.html", locals())

########################################

def profile_details(request):
    return render(request, "userpanel/profile/details.html", locals())


def cart(request):
    return render(request, "userpanel/cart.html", locals())

def addfunds(request):
    return render(request, "userpanel/addfunds.html", locals())

def invoices(request):
    return render(request, "userpanel/invoices.html", locals())

def products(request):
    return render(request, "userpanel/products.html", locals())

def instagrampost(request):
    return render(request, "userpanel/instagrampost.html", locals())

def profile(request):
    return render(request, "userpanel/profile.html", locals())

def dashboarduser(request):
    return render(request, "userpanel/dashboarduser.html", locals())

def ticketuser(request):
    return render(request, "userpanel/ticket.html", locals())

def PIncreaseCharge(request):
    return render(request, "userpanel/PIncreaseCharge.html", locals())

def pmassage(request):
    return render(request, "userpanel/pmassage.html", locals())


def fillJ(request):
    return load_just_another_panel_services()
