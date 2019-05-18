# api/urls.py
from django.conf.urls import url, include
import tickets.views as ticket_views
from views import *
urlpatterns = [
    url(r'^fill/airports', fill_airports),
    url(r'^fill/airlines', fill_airlines),
    url(r'^fill/nationality', fill_nationality),
    url(r'^step1', show_calender, name="show_calender"),
    url(r'^req', req, name="req"),
    url(r'^step2', show_tickets, name="show_tickets"),
    url(r'^step3', book_form, name="book_form"),
    url(r'^cancel', cancel, name="cancel"),
    url(r'^reserve/step4', book_ticket, name="book_ticket"),
    url(r'^reserve/pay', payment, name="payment"),
    url(r'^pay', pay, name="pay"),
    url(r'^ticket/(?P<pk>\d+)/$$', ticket_views.BookedTicketDetails.as_view(), name="booked_ticket_details"),

]