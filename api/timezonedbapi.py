'''
timezonedb.com API wrapper
'''

__author__ = "Bojan"
__license__ = "MIT"
__maintainer__ = "Bojan"
__status__ = "Production"

import requests
from api.config import Config

class TimezoneDBAPIGeneralException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return "TimezoneDBAPI -> {}".format(self.message)

class TimezoneDBAPI:
    '''timezonedb.com API wrapper'''
    __version__ = "0.1"

    def __init__(self, api_key, api_type="vip", api_version="2.1"):
        '''init

        :param str key: API key
        '''
        self.config = Config()

        if not api_type in self.config.versions.keys():
            raise TimezoneDBAPIGeneralException("API type not valid")
        if not api_key:
            raise TimezoneDBAPIGeneralException("You need to provide API key")

        self.api_key = api_key
        self.api_type = api_type
        self.api_version = api_version

    def __build_url(self, endpoint):
        '''build URL'''
        return "http://{}.timezonedb.com/v{}/{}".format(
            self.api_type, self.api_version, endpoint
        )

    def __check_params(self, endpoint, params):
        '''check params'''
        if not endpoint in self.config.endpoints.keys():
            raise TimezoneDBAPIGeneralException("Invalid endpoint selected")
        for param in self.config.endpoints[endpoint]["params"].keys():
            #check param validity
            param_data = self.config.endpoints[endpoint]["params"][param]
            if param_data["required"]:
                if param not in params.keys():
                    raise TimezoneDBAPIGeneralException(
                        "Param [{}] must be present in request".format(param))
            if param in params.keys():
                if params[param]:
                    if "options" in param_data:
                        if params[param] not in param_data["options"]:
                            raise TimezoneDBAPIGeneralException(
                                "Param [{}] must be one of the options {}".format(
                                    param, param_data["options"]))
                    if "fields" in param_data:
                        fields_data = params[param].split(',')
                        for fd in fields_data:
                            if fd not in param_data["fields"]:
                                raise TimezoneDBAPIGeneralException(
                                    "Param [{}] must contain only set of {} values".format(
                                        param, param_data["fields"]))
        return True

    def __make_call(self, url, params={}):
        '''make API call'''
        params = {param: params[param] for param in params if params[param]}
        data = requests.get(url, params=params)
        return data

    def __parse_result(self, params):
        '''parse API results'''
        if "format" in params:
            if params["format"] == "json":
                return res.json()
        return res.content

    def list_time_zone(self, response_format=None, callback=None, fields=None,
            country=None, zone=None):
        '''list timezone'''
        endpoint = "list-time-zone"
        params = {
            "key": self.api_key,
            "format": response_format,
            "callback": callback,
            "fields": fields,
            "country": country,
            "zone": zone,
        }
        self.__check_params(endpoint, params)
        url = self.__build_url(endpoint)
        res = self.__make_call(url, params)
        return self.__parse_result(params)
