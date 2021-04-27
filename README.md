# timezonedb.com API [python wrapper]

Wrapper for [timezonedb.com](https://timezonedb.com) API

## API Reference

Full timezonedb.com API reference can be found [here](https://timezonedb.com/api)

## HOW TO USE

### TO USE - list timezone

List out all available time zones supported by TimeZoneDB.

```python

from timezonedb import TimezoneDBAPI

#get timezones
api = TimezoneDBAPI(api_key={TIMEZONEDB_API_KEY})
res = api.list_time_zone(response_format="json")
print(res)
```

### TO USE - get timezone

Get local time of a city by its name, time zone, latitude & longtiude, or IP address.

```python

from timezonedb import TimezoneDBAPI

#get timezones
api = TimezoneDBAPI(api_key={TIMEZONEDB_API_KEY})
res = api.get_time_zone(
    response_format="json",
    by="position",
    lat="40.689247",
    lng="-74.044502",
)
print(res)
```
```python

from timezonedb import TimezoneDBAPI

#get timezones
api = TimezoneDBAPI(api_key={TIMEZONEDB_API_KEY})
res = api.get_time_zone(
    response_format="json",
    by="city",
    city="chicago",
    country="US",
)
print(res)
```


### TO USE - convert timezones

Convert timestamp between two different time zone.

```python

from timezonedb import TimezoneDBAPI

#get timezones
api = TimezoneDBAPI(api_key={TIMEZONEDB_API_KEY})
res = api.convert_time_zone(
    response_format="json",
    from_zone="America/Los_Angeles",
    to_zone="Australia/Sydney",
)
print(res)
```
