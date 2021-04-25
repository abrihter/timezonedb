'''
config file
'''

class Config:
    '''config'''
    endpoint = "timezonedb.com"

    versions = {
        "api": {
            "prefix": "api",
        },
        "vip": {
            "prefix": "vip",
        },
    }

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
    }
