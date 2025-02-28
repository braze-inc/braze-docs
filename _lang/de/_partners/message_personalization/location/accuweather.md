---
nav_title: AccuWeather
article_title: AccuWeather
alias: /partners/accuweather/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und AccuWeather, einer Wetter-API, die Sie zur Personalisierung Ihrer Marketingkampagnen nutzen können."
page_type: partner
search_tag: Partner

---

# AccuWeather

> [AccuWeather](https://www.accuweather.com/) ist ein Medienunternehmen, das weltweit Wettervorhersagedienste anbietet. Mit AccuWeather können Sie Ihre Marketingkampagnen bereichern und personalisieren sowie Übersetzungen durch den Einsatz von Braze [Connected Content][60] automatisieren. 

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| AccuWeather API-Schlüssel | Wenden Sie sich an Ihren AccuWeather-Kundenbetreuer, um kompatible API-Schlüssel für Ihre Anfrage-URLs zu erhalten.<br><br>Weitere Anweisungen finden Sie auf der Seite [AccuWeather Enterprise API][57] ]. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Verfügbare AccuWeather APIs

Im Folgenden finden Sie die AccuWeather-APIs, auf die Sie in Ihren Braze-Kampagnen und Canvases verweisen können.

| API | Beschreibung |
|---|---|
|[Standorte][48] | Holen Sie sich einen Standortschlüssel für Ihren gewünschten Standort. Verwenden Sie den Standortschlüssel, um Wetterdaten von der API für die Vorhersage oder die aktuellen Bedingungen abzurufen. |
| [Vorhersage][49] | Erhalten Sie Vorhersageinformationen für einen bestimmten Ort. |
| [Aktuelle Bedingungen][50] | Rufen Sie die Daten zu den aktuellen Bedingungen für einen bestimmten Ort ab. |
| [Indizes][51] | Erhalten Sie tägliche Indexwerte für einen bestimmten Ort. Die Verfügbarkeit der Indizes variiert je nach Standort. |
| [Wetteralarm][52] | Erhalten Sie Wetteralarme für einen bestimmten Ort. AccuWeather Wetteralarme werden anhand der täglichen Vorhersagen für einen Ort ermittelt. Ein Alarm besteht für einen Ort, wenn die Wettervorhersage [bestimmte Schwellenwerte][58]] erreicht oder überschreitet. |
| [Alerts][53] | Erhalten Sie Unwetterwarnungen von offiziellen staatlichen Wetterdiensten und führenden globalen Wetterwarnungsanbietern. |
| [Bildmaterial][54] | Erhalten Sie Radar- und Satellitenbilder. |
| [Tropisch][55] | Erhalten Sie die aktuelle Position, frühere Positionen und Vorhersagen für tropische Wirbelstürme weltweit. |
| [Übersetzungen][56] | Erhalten Sie eine Liste der verfügbaren Sprachen. Holen Sie sich Übersetzungen für bestimmte Gruppen von Phrasen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Beispiel für verknüpfte Inhalte

Das folgende Beispiel zeigt einen Aufruf von Connected Content, der zwei verschiedene Arten von Nachrichten anzeigt, die auf den aktuellen Bedingungen der Postleitzahl eines Benutzers in den USA basieren. Es werden die API-Endpunkte für AccuWeather-Standorte und aktuelle Bedingungen verwendet.
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

![Eine Connected Content-Push-Nachricht mit dem Inhalt "Es regnet! Schnappen Sie sich einen Regenschirm!", angezeigt auf einem Android-Gerät][17]{: style="max-width:40%"}

Eine Aufschlüsselung der beiden Connected Content-Aufrufe finden Sie in den folgenden Beispielen.

{% tabs %}
{% tab Standorte %}
#### Standorte API Beispiel

{% raw %}
Innerhalb des ersten `connected_content` Tags wird eine GET-Anfrage an die [Locations API](https://apidev.accuweather.com/developers/locationsAPIguide) gestellt. Für dieses Beispiel können Sie alternativ die `{{${city}}}` des Benutzers verwenden, wenn Sie kein benutzerdefiniertes Attribut für die Postleitzahl haben.

```
{% connected_content http://dataservice.accuweather.com/locations/v1/postalcodes/{{${country}}}/search?q={{custom_attribute.${Zip Code}}}&apikey={your API key} :save location_info %}
```
{% endraw %}

Hier ist ein Beispiel dafür, was AccuWeather als JSON-Objekt zurückgibt:

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

Die ID "Schlüssel" ist eine nützliche Variable, da sie in der zweiten GET-Anfrage verwendet wird.
Dieses JSON-Objekt kann in einer lokalen Variable `location_info` gespeichert werden, indem Sie `:save location_info` nach der URL angeben.
{% endtab %}
{% tab Aktuelle Bedingungen %}

#### Aktuelle Bedingungen API Beispiel

Für das zweite `connected_content` Tag wird eine GET-Anfrage an die [Current Conditions API](https://apidev.accuweather.com/developers/currentConditionsAPIGuide) gestellt. Der **Standortschlüssel** muss der Anfrage-URL hinzugefügt werden. Hier ist das Beispiel `connected_content` tag:

{% raw %}
```
{% connected_content http://dataservice.accuweather.com/currentconditions/v1/{{location_info[0].Key}}?apikey={your API key} :save local_weather %}
```

Hier ist das zurückgegebene JSON-Objekt:

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

Wie im Tag `connected_content` zu sehen ist, wird das JSON-Objekt in einer lokalen Variablen `local_weather` gespeichert, indem `:save local_weather` nach der URL hinzugefügt wird.

Sie können testen, wie die Ausgabe von [WeatherText](https://apidev.accuweather.com/developers/currentConditionsAPIGuide) aussehen soll, indem Sie auf `{{local_weather[0].WeatherText}}` verweisen.

Wenn der API-Aufruf mit `{{local_weather[0].WeatherText}}` antwortet und `Rain` zurückgibt, würde der Benutzer den Push erhalten.

{% endraw %}
{% endtab %}
{% endtabs %}

[16]: [success@braze.com](mailto:success@braze.com)
[17]: {% image_buster /assets/img_archive/connected_weather_push2.png %} "Beispiel für die Verwendung von Connected Content Push"
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
/user_guide content/connected_content/about_connected_content//personalization_and_dynamic_
