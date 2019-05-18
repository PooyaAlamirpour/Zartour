from django import template
#from payment.models import Ticket
register = template.Library()

@register.simple_tag(name='get_new_ticket_list')
def get_new_ticket_list():
    tickets = None #Ticket.objects.filter(status = '0')
    return tickets
