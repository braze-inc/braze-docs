---
nav_title: Accuweather
article_title: AccuWeather
alias: /partners/accuweather/
description: "This reference article outlines the partnership between Braze and AccuWeather, a weather API you can use to personalize your marketing campaigns."
page_type: partner
search_tag: Partner

---

# AccuWeather

> [AccuWeather](https://www.accuweather.com/) is a media company that provides weather forecasting services worldwide. With AccuWeather, you can enrich and personalize your marketing campaigns, as well as automate translations through the use of Braze [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/). 

_This integration is maintained by AccuWeather._

## Prerequisites

| Requirement | Description |
|---|---|
| AccuWeather API Key | Contact your AccuWeather account manager for compatible API keys to use in your request URLs.<br><br>Further instructions can be found on the [AccuWeather Enterprise API](https://apidev.accuweather.com/developers/) page. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Available AccuWeather APIs

The following are the AccuWeather APIs you can reference within your Braze campaigns and Canvases.

| API | Description |
|---|---|
|[Locations](https://apidev.accuweather.com/developers/locationsAPIguide) | Get a location key for your desired location. Use the location key to retrieve weather data from the Forecast or Current Conditions API. |
| [Forecast](https://apidev.accuweather.com/developers/forecastsAPIguide) | Get forecast information for a specific location. |
| [Current Conditions](https://apidev.accuweather.com/developers/currentConditionsAPIGuide) | Get Current Conditions data for a specific location. |
| [Indices](https://apidev.accuweather.com/developers/indicesApiGuide) | Get daily index values for a specific location. Index availability varies by location. |
| [Weather Alarms](https://apidev.accuweather.com/developers/weatheralarmsAPIguide) | Get Weather Alarms for a specific location. AccuWeather Weather Alarms are determined using the daily forecasts for a location. An alarm exists for a location if the forecast weather meets or exceeds [specific thresholds](https://apidev.accuweather.com/developers/weatheralarms). |
| [Alerts](https://apidev.accuweather.com/developers/alertsApiGuide) | Get severe weather alerts from official Government Meteorological Agencies and leading global weather alert providers. |
| [Imagery](https://apidev.accuweather.com/developers/imageryAPIguide) | Get radar and satellite images. |
| [Tropical](https://apidev.accuweather.com/developers/tropicalAPIGuide) | Get current position, past positions, and forecasts for tropical cyclones worldwide. |
| [Translations](https://apidev.accuweather.com/developers/translationsApiGuide) | Get a list of available languages. Get translations for specific groups of phrases. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Connected Content example

The following example shows a Connected Content call displaying two different types of messages based on the current conditions of a user's zip code in the US. The AccuWeather locations and current conditions API endpoints are used.
{% raw %}

```liquid
{% connected_content http:///dataservice.accuweather.com/locations/v1/postalcodes/{{${country}}}/search?q={{custom_attribute.${Zip Code}}}&apikey={your API key} :save location_info %}

{% connected_content http://dataservice.accuweather.com/currentconditions/v1/{{location_info[0].Key}}?apikey={your API key} :save local_weather %}

{% if {{local_weather[0].WeatherText}} == 'Cloudy' %}
No sunscreen needed :)
{% elsif {{local_weather[0].WeatherText}} == 'Rain' %}
It's raining! Grab an umbrella!
{% else %}
Enjoy the weather!
{% endif %}
```
{% endraw %}

![A Connected Content push message that says "It's raining! Grab an Umbrella!" shown on an Android device]({% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"){: style="max-width:40%"}

A breakdown of the two Connected Content calls can be found in the following examples.

{% tabs %}
{% tab Locations %}
#### Locations API example

{% raw %}
Within the first `connected_content` tag, a GET request is made to the [Locations API](https://apidev.accuweather.com/developers/locationsAPIguide). For this example, you can alternatively leverage the user's `{{${city}}}` if you do not have a zip code custom attribute.

```
{% connected_content http://dataservice.accuweather.com/locations/v1/postalcodes/{{${country}}}/search?q={{custom_attribute.${Zip Code}}}&apikey={your API key} :save location_info %}
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

The "Key" ID is a useful variable as it is used in the second GET request. 
This JSON object can be stored into a local variable `location_info` by specifying `:save location_info` after the URL. 
{% endtab %}
{% tab Current conditions %}

#### Current conditions API example

For the second `connected_content` tag, a GET request is made to the [Current Conditions API](https://apidev.accuweather.com/developers/currentConditionsAPIGuide). The **location key** will need to be added to the request URL. Here is the example `connected_content` tag:

{% raw %}
```
{% connected_content http://dataservice.accuweather.com/currentconditions/v1/{{location_info[0].Key}}?apikey={your API key} :save local_weather %}
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

As seen in the `connected_content` tag, the JSON object is stored into a local variable `local_weather` by adding `:save local_weather` after the URL.

You can test what the output of the [WeatherText](https://apidev.accuweather.com/developers/currentConditionsAPIGuide) should be by referencing `{{local_weather[0].WeatherText}}`.

If the API call responds with `{{local_weather[0].WeatherText}}` returning `Rain`, the user would then receive the push.

{% endraw %}
{% endtab %}
{% endtabs %}


[16]: [success@braze.com](mailto:success@braze.com)
