---
nav_title: AccuWeather
alias: /partners/accuweather/

description: "This article outlines the partnership between Braze and AccuWeather, a weather API you can use to personalize your marketing campaigns."
page_type: partner

---

# AccuWeather

> If you have an AccuWeather&trade; account, you can enrich and personalize your marketing campaigns, as well as automate translations, through [Connected Content][60].

Here are all of the AccuWeather APIs you can reference within your Braze campaigns:

| API | Description |
|---|---|
|[Locations][48] | Get a location key for your desired location. Use the location key to retrieve weather data from the Forecast or Current Conditions API. |
| [Forecast][49] | Get forecast information for a specific location. |
| [Current Conditions][50] | Get Current Conditions data for a specific location. |
| [Indices][51] | Get daily index values for a specific location. Index availability varies by location. |
| [Weather Alarms][52] | Get Weather Alarms for a specific location. AccuWeather Weather Alarms are determined using the daily forecasts for a location. An alarm exists for a location if the forecast weather meets or exceeds [specific thresholds][58]. |
| [Alerts][53] | Get severe weather alerts from official Government Meteorological Agencies and leading global weather alert providers. |
| [Imagery][54] | Get radar and satellite images. |
| [Tropical][55] | Get current position, past positions, and forecasts for tropical cyclones worldwide. |
| [Translations][56] | Get a list of available languages. Get translations for specific groups of phrases. |
{: .reset-td-br-1 .reset-td-br-2}

In order to get started, you’ll need to have your app’s AccuWeather API key on-hand to use within your request urls. You will need to contact your Accuweather account manager for API keys that will work with the instructions listed on the [AccuWeather Enterprise API page][57].

For example, let’s say that you wanted to run a marketing campaign that has 3 different types of messages based on the current conditions of a user’s zip code in the US.

Within the first `connected_content` tag you will make a GET request to the [Locations API][48]. Here’s an example of what AccuWeather will return as the JSON object:

```json
[
  {
    "Version": 1,
    "Key": "41333_PC",
    "Type": "PostalCode",
    "Rank": 35,
    "LocalizedName": "Seattle",
    "EnglishName": "Seattle",
    "PrimaryPostalCode": "98102",
    "Region": {
      "ID": "NAM",
      "LocalizedName": "North America",
      "EnglishName": "North America"
    },
    "Country": {
      "ID": "US",
      "LocalizedName": "United States",
      "EnglishName": "United States"
    },
    "AdministrativeArea": {
      "ID": "WA",
      "LocalizedName": "Washington",
      "EnglishName": "Washington",
      "Level": 1,
      "LocalizedType": "State",
      "EnglishType": "State",
      "CountryID": "US"
    },
    "TimeZone": {
      "Code": "PDT",
      "Name": "America/Los_Angeles",
      "GmtOffset": -7.0,
      "IsDaylightSaving": true,
      "NextOffsetChange": "2018-11-04T09:00:00Z"
    },
    "GeoPosition": {
      "Latitude": 47.636,
      "Longitude": -122.327,
      "Elevation": {
        "Metric": {
          "Value": 26.0,
          "Unit": "m",
          "UnitType": 5
        },
        "Imperial": {
          "Value": 85.0,
          "Unit": "ft",
          "UnitType": 0
        }
      }
    },
    "IsAlias": false,
    "ParentCity": {
      "Key": "351409",
      "LocalizedName": "Seattle",
      "EnglishName": "Seattle"
    },
    "SupplementalAdminAreas": [
      {
        "Level": 2,
        "LocalizedName": "King",
        "EnglishName": "King"
      }
    ],
    "DataSets": [
      "Alerts",
      "DailyAirQualityForecast",
      "DailyPollenForecast",
      "ForecastConfidence",
      "MinuteCast"
    ]
  }
]
```

Keep the “Key” ID on hand as you’ll need this for the second GET request. You can store the above JSON object into local variable `location_info` by specifying `:save location_info` after the url. Here is the example of the `connected_content` tag:

{% raw %}
```
{% connected_content http://api.accuweather.com/locations/v1/postalcodes/{{${country}}}/search?q={{custom_attribute.${Zip Code}}}&apikey={your API key} :save location_info %}
```

_**Note**: Alternatively, you could also leverage the user’s `{{${city}}}` if you do not have a zip code custom attribute._

For the second `connected_content` tag, you will make a GET request to the [Current Conditions API][50]. You’ll need to add the **location key** to the request url. Here is the example `connected_content` tag:

```
{% connected_content http://api.accuweather.com/currentconditions/v1/{{location_info[0].Key}}?apikey={your API key} :save local_weather %}
```

Here is the returning JSON object:

```json
[
  {
    "LocalObservationDateTime": "2018-04-10T09:35:00-07:00",
    "EpochTime": 1523378100,
    "WeatherText": "Rain",
    "WeatherIcon": 18,
    "IsDayTime": true,
    "Temperature": {
      "Metric": {
        "Value": 11.0,
        "Unit": "C",
        "UnitType": 17
      },
      "Imperial": {
        "Value": 52.0,
        "Unit": "F",
        "UnitType": 18
      }
    },
    "MobileLink": "http://m.accuweather.com/en/us/seattle-wa/98104/current-weather/41333_pc?lang=en-us",
    "Link": "http://www.accuweather.com/en/us/seattle-wa/98104/current-weather/41333_pc?lang=en-us"
  }
]
```

As you can see from the `connect_content` tag above, we stored the JSON object into local variable `local_weather` by adding `:save local_weather` after the url.

You can test what the output of the [WeatherText][59] should be by referencing `{{local_weather[0].WeatherText}}`.

Bringing our use-case together, here is what the syntax of the campaign would look like:

```
{% connected_content
http://api.accuweather.com/locations/v1/postalcodes/{{${country}}}/search?q={{custom_attribute.${Zip Code}}}&apikey={your API key} :save location_info %}
{% connected_content
http://api.accuweather.com/currentconditions/v1/{{location_info[0].Key}}?apikey={your API key} :save local_weather %}
{% if {{local_weather[0].WeatherText}} == 'Cloudy' %}
No sunscreen needed :)
{% elsif {{local_weather[0].WeatherText}} == 'Rain' %}
It's raining! Grab an umbrella!
{% else %}
Enjoy the weather!
{% endif %}
```

If the API responded with `{{local_weather[0].WeatherText}}` returning `Rain`, the user would then receive the following push:

![Connected Content Push Example][17]

{% endraw %}

[16]: [success@braze.com](mailto:success@braze.com)
[17]: {% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"
[48]: https://apidev.accuweather.com/developers/locationsAPIguide
[49]: https://apidev.accuweather.com/developers/forecastsAPIguide
[50]: https://apidev.accuweather.com/developers/currentConditionsAPIGuide
[51]: https://apidev.accuweather.com/developers/indicesApiGuide
[52]: https://apidev.accuweather.com/developers/weatheralarmsAPIguide
[53]: https://apidev.accuweather.com/developers/alertsApiGuide
[54]: https://apidev.accuweather.com/developers/imageryAPIguide
[55]: https://apidev.accuweather.com/developers/tropicalAPIGuide
[56]: https://apidev.accuweather.com/developers/translationsApiGuide
[57]: https://apidev.accuweather.com/developers/
[58]: https://apidev.accuweather.com/developers/weatheralarms
[59]: https://apidev.accuweather.com/developers/weatheralarms
[60]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
