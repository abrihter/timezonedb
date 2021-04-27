'''
config file
'''

__author__ = "Bojan"
__license__ = "MIT"
__maintainer__ = "Bojan"
__status__ = "Production"

class Config:
    '''config'''
    endpoint = "timezonedb.com"

    api_types = {
        "api": {
            "prefix": "api",
        },
        "vip": {
            "prefix": "vip",
        },
    }

    api_versions = ["2.1"]

    endpoints = {
        "list-time-zone": {
            "params": {
                "key": {
                    "required": True,
                },
                "format": {
                    "required": False,
                    "options": ["xml", "json"],
                    "default": "xml",
                },
                "callback": {
                    "required": False,
                },
                "fields": {
                    "required": False,
                    "fields": ["countryCode", "countryName", "zoneName",
                        "gmtOffset", "dst", "timestamp"],
                    "default": \
                        "countryCode,countryName,zoneName,gmtOffset,timestamp",
                },
                "country": {
                    "required": False,
                },
                "zone": {
                    "required": False,
                },
            }
        },
        "get-time-zone": {
            "params": {
                "key": {
                    "required": True,
                },
                "format": {
                    "required": False,
                    "options": ["xml", "json"],
                    "default": "xml",
                },
                "callback": {
                    "required": False,
                },
                "fields": {
                    "required": False,
                    "fields": ["countryCode", "countryName", "regionName",
                        "cityName", "zoneName", "abbreviation", "gmtOffset",
                        "dst", "zoneStart", "zoneEnd", "nextAbbreviation",
                        "timestamp", "formatted"],
                    "default": \
                        "countryCode,countryName,regionName,cityName,zoneName,abbreviation,gmtOffset,dst,zoneStart,zoneEnd,nextAbbreviation,timestamp,formatted",
                },
                "by": {
                    "required": True,
                    "options": ["zone", "position", "city", "ip"],
                },
                "zone": {
                    "required": False,
                    "required_field": "by",
                    "required_by": ["zone"],
                },
                "lat": {
                    "required": False,
                    "required_field": "by",
                    "required_by": ["position"],
                },
                "lng": {
                    "required": False,
                    "required_field": "by",
                    "required_by": ["position"],
                },
                "country": {
                    "required": False,
                    "required_field": "by",
                    "required_by": ["city"],
                },
                "region": {
                    "required": False,
                },
                "city": {
                    "required": False,
                    "required_field": "by",
                    "required_by": ["city"],
                },
                "ip": {
                    "required": False,
                    "required_field": "by",
                    "required_by": ["ip"],
                },
                "page": {
                    "required": False,
                },
                "time": {
                    "required": False,
                },
            },
        },
        "convert-time-zone": {
            "params": {
                "key": {
                    "required": True,
                },
                "format": {
                    "required": False,
                    "options": ["xml", "json"],
                    "default": "xml",
                },
                "callback": {
                    "required": False,
                },
                "fields": {
                    "required": False,
                    "fields": ["fromZoneName", "fromAbbreviation",
                        "fromTimestamp", "toZoneName", "toAbbreviation",
                        "toTimestamp", "toFormatted", "offset"],
                    "default": \
                        "fromZoneName,fromAbbreviation,fromTimestamp,toZoneName,toAbbreviation,toTimestamp,toFormatted,offset",
                },
                "from": {
                    "required": True,
                },
                "to": {
                    "required": True,
                },
                "time": {
                    "required": False,
                },
            },
        },
    }

