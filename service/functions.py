import json
from argparse import Namespace

import requests
from django.http import HttpResponse
from models import JustOneOtherPanelCategory,JustOneOtherPanelService,JustOneOtherPanelType

from models import ServerException
BASE_URL='https://justanotherpanel.com/api/v2'
API_KEY='b69d60aa8e1c11421065cb9bcd690d95'


def load_just_another_panel_services():
    data = {
        'key': API_KEY,
        'action': 'services',
        }
    response = requests.post(BASE_URL, data, verify=False)
    #response_object = json.loads(response.content)
    services = json.loads(response.content, object_hook=lambda d: Namespace(**d))

    for service in services:
        JustOneOtherPanelService.objects.create_from_obj(service)



    django_response = HttpResponse(
        content=response.content,
        status=response.status_code,
        content_type=response.headers['Content-Type']
    )

    return django_response
    #
    # if response.ok:
    #     return json.load(response)
    # else:
    #     raise ServerException(response.status_code + ":" +BASE_URL)
