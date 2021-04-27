'''
timezonedb.com API wrapper
'''

__author__ = "Bojan"
__license__ = "MIT"
__maintainer__ = "Bojan"
__status__ = "Production"

import requests
from timezonedb.config import Config

class TimezoneDBAPIGeneralException(Exception):
    '''custom exception'''
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
        :param str api_type: API type
        :param str api_version: API version to use
        '''
        self.config = Config()

        if not api_type in self.config.api_types.keys():
            raise TimezoneDBAPIGeneralException("API type not valid")
        if not api_key:
            raise TimezoneDBAPIGeneralException("You need to provide API key")
        if not api_version in self.config.api_versions:
            raise TimezoneDBAPIGeneralException("API type not valid")

        self.api_key = api_key
        self.api_type = api_type
        self.api_version = api_version

    def __build_url(self, endpoint):
        '''build URL

        :param str endpoint: Endpoint to use
        :return str: Return formatted URL
        '''
        return "http://{}.timezonedb.com/v{}/{}".format(
            self.api_type, self.api_version, endpoint
        )

    def __check_params(self, endpoint, params):
        '''check params

        :param str endpoint: Endpoint to use
        :param dict params: Params used for request
        :return bool: Return True or raise error on issue
        '''
        if not endpoint in self.config.endpoints.keys():
            raise TimezoneDBAPIGeneralException("Invalid endpoint selected")
        params = {param: params[param] for param in params if params[param]}
        for param in self.config.endpoints[endpoint]["params"].keys():
            #check param validity
            param_data = self.config.endpoints[endpoint]["params"][param]
            if param_data["required"]:
                if param not in params.keys():
                    raise TimezoneDBAPIGeneralException(
                        "Param [{}] must be present in request".format(param))
                if not params[param]:
                    raise TimezoneDBAPIGeneralException(
                        "Param [{}] must have value".format(param))

            if param in params.keys():
                #check param additional options
                if params[param]:
                    if "options" in param_data.keys():
                        if params[param] not in param_data["options"]:
                            raise TimezoneDBAPIGeneralException(
                                "Param [{}] must be one of the options {}".format(
                                    param, param_data["options"]))
                    if "fields" in param_data.keys():
                        fields_data = params[param].split(',')
                        for fd in fields_data:
                            if fd not in param_data["fields"]:
                                raise TimezoneDBAPIGeneralException(
                                    "Param [{}] must contain only set of {} values".format(
                                        param, param_data["fields"]))

            #check constraints related to additional fields
            #(like 'by' field in get-time-zone)
            if "required_field" not in param_data.keys() \
                    or param_data["required_field"] not in params.keys() \
                    or not params[param_data["required_field"]]:
                continue
            for param_by in param_data["required_by"]:
                if param_by == params[param_data["required_field"]]:
                    if param in params.keys():
                        if not params[param]:
                            raise TimezoneDBAPIGeneralException(
                                "Param [{}] must have value when [{}] param value is '{}'".format(
                                    param,
                                    param_data["required_field"],
                                    params[param_data["required_field"]],
                                )
                            )
                    else:
                        raise TimezoneDBAPIGeneralException(
                            "Param [{}] must be present in request when [{}] param value is '{}'".format(
                                param,
                                param_data["required_field"],
                                params[param_data["required_field"]],
                            )
                        )
        return True

    def __make_call(self, url, params={}):
        '''make API call

        :param str url: Request to execute
        :param dict params: Params to use with request
        :return Response: Returns response_format from request GET
        '''
        params = {param: params[param] for param in params if params[param]}
        data = requests.get(url, params=params)
        return data

    def __parse_result(self, res, params):
        '''parse API results

        :param Response res: Response from requests
        :param dict params: Params used with request
        :return: Returns json if format is set to jason
                 or bytes object on other options
        '''
        if "format" in params:
            if params["format"] == "json":
                return res.json()
        return res.content

    def __generic_full_api_call(self, endpoint, params):
        '''generic full API call

        :param str endpoint: Endpoint to use
        :param dict params: Params used with request
        :return: Returns json if format is set to jason
                 or bytes object on other options
        '''
        self.__check_params(endpoint, params)
        url = self.__build_url(endpoint)
        res = self.__make_call(url, params)
        return self.__parse_result(res, params)

    def list_time_zone(self, response_format=None, callback=None, fields=None,
            country=None, zone=None):
        '''list timezone

        :param str response_format: The response format from API.
                                    It can be either xml or json.
        :param str callback: Use for JavaScript JSON callback.
        :param str fields: Customize the field to display in response.
                           Use commas ("," without spaces) to
                           separate the field names.
        :param str country: A valid ISO 3166 country code.
                            Only time zones of provided country will list out.
        :param str zone: The name of a time zone.
                         Use asterisk (*) for wildcard search.
        :return: Returns json if format is set to jason
                 or bytes object on other options
        '''
        params = {
            "key": self.api_key,
            "format": response_format,
            "callback": callback,
            "fields": fields,
            "country": country,
            "zone": zone,
        }
        return self.__generic_full_api_call("list-time-zone", params)

    def get_time_zone(self, response_format=None, callback=None, fields=None,
            by=None, zone=None, lat=None, lng=None, country=None, region=None,
            city=None, ip=None, page=None, time=None):
        '''get timezone

        :param str response_format: The response format from API.
                                    It can be either xml or json.
        :param str callback: Use for JavaScript JSON callback.
        :param str fields: Customize the field to display in response.
                           Use commas ("," without spaces) to
                           separate the field names.
        :param str by: The method of lookup.
                       zone - Lookup local time by using a time zone name.
                       position - Lookup local time by using latitude & longitude of a city.
                       city - Lookup time zone by searching city name.
                       ip - Lookup time zone based on visitor IP address.
        :param str zone: A time zone abbreviation or time zone name.
                         Required if lookup by zone method.
        :param str lat: Latitude of a city.
                        Required if lookup by position method.
        :param str lng: Longitude of a city.
                        Required if lookup by position method.
        :param str country: A valid ISO 3166 country code.
                            Required if lookup by city method.
        :param str region: A valid region code of United States.
                           Optional when lookup by city method
                           to limit the search result.
        :param str city: The name of a city.
                         Use asterisk (*) for wildcard search.
                         Required if lookup by city method.
        :param str page: Navigate to other page
                         when result is more than 10 records.
        :param str time: Unix time in UTC.
        :return: Returns json if format is set to jason
                 or bytes object on other options
        '''
        params = {
            "key": self.api_key,
            "format": response_format,
            "callback": callback,
            "fields": fields,
            "by": by,
            "zone": zone,
            "lat": lat,
            "lng": lng,
            "country": country,
            "region": region,
            "city": city,
            "ip": ip,
            "page": page,
            "time": time,
        }
        return self.__generic_full_api_call("get-time-zone", params)

    def convert_time_zone(self, response_format=None, callback=None,
            fields=None, from_zone=None, to_zone=None, time=None):
        '''convert timezone

        :param str response_format: The response format from API.
                                    It can be either xml or json.
        :param str callback: Use for JavaScript JSON callback.
        :param str fields: Customize the field to display in response.
                           Use commas ("," without spaces) to
                           separate the field names.
        :param str from_zone: A valid abbreviation or name
                              of time zone to convert from.
        :param str to_zone: A valid abbreviation or name
                            of time zone to convert to.
        :param str time: Unix time in UTC.
        :return: Returns json if format is set to jason
                 or bytes object on other options
        '''
        params = {
            "key": self.api_key,
            "format": response_format,
            "callback": callback,
            "fields": fields,
            "from": from_zone,
            "to": to_zone,
            "time": time,
        }
        return self.__generic_full_api_call("convert-time-zone", params)
