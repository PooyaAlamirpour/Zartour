import json
import requests


class APIService(object):
    API_URL = 'http://sandbox.safarbooking.com/api/flight/'
    TOKEN = 'Bearer 31d14bd6687528582ebef6ee14c2962a94588feb'

    @staticmethod
    def get_new_token():
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            #'user': 'alvand',
            #'password': 'alvand123',
             #'user': 'zarafshan.ss',
             #'password': 'zar@afshan',
            'user': 'testfava',
            'password': 'fava1020',
            'Language': 'en'
        }
        response = requests.post('http://sandbox.safarbooking.com/api/accounting/getToken', verify=False, headers=headers)
        request_obj = json.loads(response.content)
        APIService.TOKEN = request_obj['client_token']
        return APIService.TOKEN

    @staticmethod
    def call_function(function, data):
        URL = APIService.API_URL+function
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Client-Token': APIService.TOKEN
        }
        response = requests.post(URL, json=data, verify=False, headers=headers)
        request_obj = json.loads(response.content)
        print request_obj['status']
        if request_obj['status'] == 'error':
            if request_obj['err'][0]['code']==60102:
                APIService.get_new_token()
                return APIService.call_function(function, data)
        else:
            return request_obj

    @staticmethod
    def lowFareSearch(data):
        return APIService.call_function('LowFareSearch', data)

    @staticmethod
    def fareSearchResult(data):
        return APIService.call_function('FareSearchResult', data)

    @staticmethod
    def book(data):
        return APIService.call_function('book', data)

    @staticmethod
    def fill_nationality():
        data={
            "data": "nationality"
        }
        return APIService.call_function('Information', data)

