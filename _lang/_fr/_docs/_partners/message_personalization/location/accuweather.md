---
nav_title: AccuWeather
article_title: AccuWeather
alias: /partners/accuweather/
description: "This article outlines the partnership between Braze and AccuWeather, a weather API you can use to personalize your marketing campaigns."
page_type: partner
search_tag: Partner
---

# AccuWeather

> [AccuWeather](https://www.accuweather.com/) is a media company that provides weather forecasting services worldwide. With AccuWeather, you can enrich and personalize your marketing campaigns, as well as automate translations through the use of Braze [Connected Content][60].

## Prerequisites

| Requirement         | Description                                                                                                                                                                                      |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AccuWeather API Key | Contact your Accuweather account manager for comaptible API keys to use in your request URLs.<br><br>Further instructions can be found on the [AccuWeather enterprise API page][57]. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Available AccuWeather APIs

The following are the AccuWeather APIs you can reference within your Braze campaigns and Canvases.

| API                      | Description                                                                                                                                                                                                                        |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Locations][48]          | Get a location key for your desired location. Use the location key to retrieve weather data from the Forecast or Current Conditions API.                                                                                           |
| [Forecast][49]           | Get forecast information for a specific location.                                                                                                                                                                                  |
| [Current Conditions][50] | Get Current Conditions data for a specific location.                                                                                                                                                                               |
| [Indices][51]            | Get daily index values for a specific location. Index availability varies by location.                                                                                                                                             |
| [Weather Alarms][52]     | Get Weather Alarms for a specific location. AccuWeather Weather Alarms are determined using the daily forecasts for a location. An alarm exists for a location if the forecast weather meets or exceeds [specific thresholds][58]. |
| [Alerts][53]             | Get severe weather alerts from official Government Meteorological Agencies and leading global weather alert providers.                                                                                                             |
| [Imagery][54]            | Get radar and satellite images.                                                                                                                                                                                                    |
| [Tropical][55]           | Get current position, past positions, and forecasts for tropical cyclones worldwide.                                                                                                                                               |
| [Translations][56]       | Get a list of available languages. Get translations for specific groups of phrases.                                                                                                                                                |
{: .reset-td-br-1 .reset-td-br-2}

## Connected Content example

The following example shows a Connected Content call displaying two different types of messages based on the current conditions of a user's zip code in the US. The AccuWeather locations and current conditions API endpoints are used.
{% raw %}

```liquid
{% connected_content http://api.accuweather.com/locations/v1/postalcodes/{{${country}}}/search?q={{custom_attribute.${Zip Code}}}&apikey={your API key} :save location_info %}

{% connected_content http://api.accuweather.com/currentconditions/v1/{{location_info[0].Key}}?apikey={your API key} :save local_weather %}

{% if {{local_weather[0].WeatherText}} == 'Cloudy' %}
No sunscreen needed :)
{% elsif {{local_weather[0].WeatherText}} == 'Rain' %}
It's raining! Grab an umbrella!
{% else %}
Enjoy the weather!
{% endif %}
```
{% endraw %}

!\[Connected Content Push Example\]\[17\]{: style="max-width:40%"}

A breakdown of the two Connected Content calls can be found below.

{% tabs %}
{% tab Locations %}
#### Locations API example

{% raw %}
Within the first `connected_content` tag, a GET request is made to the [Locations API](https://apidev.accuweather.com/developers/locationsAPIguide). For this example, you can alternatively leverage the user's `{{${city}}}` if you do not have a zip code custom attribute.

```
{% connected_content http://api.accuweather.com/locations/v1/postalcodes/{{${country}}}/search?q={{custom_attribute.${Zip Code}}}&apikey={your API key} :save location_info %}
```
{% endraw %}

Here's an example of what AccuWeather will return as the JSON object:

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

The "Key" ID is a useful variable as it is used in the second GET request. The above JSON object can be stored into a local variable `location_info` by specifying `:save location_info` after the URL.
{% endtab %}
{% tab Current conditions %}

#### Current conditions API example

For the second `connected_content` tag, a GET request is made to the [Current Conditions API](https://apidev.accuweather.com/developers/currentConditionsAPIGuide). The **location key** will need to be added to the request URL. Here is the example `connected_content` tag:

{% raw %}
```
{% connected_content http://api.accuweather.com/currentconditions/v1/{{location_info[0].Key}}?apikey={your API key} :save local_weather %}
```

Here is the returned JSON object:

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

As seen in the `connected_content` tag above, the JSON object is stored into a local variable `local_weather` by adding `:save local_weather` after the URL.

You can test what the output of the [WeatherText](https://apidev.accuweather.com/developers/currentConditionsAPIGuide) should be by referencing `{{local_weather[0].WeatherText}}`.

If the API call responds with `{{local_weather[0].WeatherText}}` returning `Rain`, the user would then receive the push shown above.

{% endraw %}
{% endtab %}
{% endtabs %}
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
[60]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
