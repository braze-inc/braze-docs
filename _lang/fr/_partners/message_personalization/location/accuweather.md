---
nav_title: AccuWeather
article_title: AccuWeather
alias: /partners/accuweather/
description: "Cet article de référence présente le partenariat entre Braze et AccuWeather, une API météo que vous pouvez utiliser pour personnaliser vos campagnes marketing."
page_type: partner
search_tag: Partenaire

---

# AccuWeather

> [AccuWeather](https://www.accuweather.com/) est une société de médias qui fournit des services de prévision météorologique dans le monde entier. Avec AccuWeather, vous pouvez enrichir et personnaliser vos campagnes marketing, ainsi que les traductions automatisées via l’utilisation de [Contenu connecté][60] de Braze. 

## Conditions préalables

| Condition | Description |
|---|---|
| Clé d’API AccuWeather | Contactez votre gestionnaire de compte AccuWeather pour les clés d’API compatibles à utiliser dans vos URL de demande.<br><br>Des instructions supplémentaires sont disponibles sur la page [AccuWeather Enterprise API][57]. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## API AccuWeather disponibles

Les API AccuWeather suivantes vous permettent de référencer vos campagnes et vos Canvas Braze.

| API | Description |
|---|---|
|[Emplacements][48] | Obtenez une clé d’emplacement pour l’emplacement souhaité. Utilisez la clé d’emplacement pour récupérer les données météorologiques de l’API Forecast (Prévisions) ou Current Conditions (Conditions actuelles). |
| [Prévisions][49] | Obtenez des informations sur les prévisions pour un emplacement spécifique. |
| [Conditions actuelles][50] | Obtenez les données des conditions actuelles pour un emplacement spécifique. |
| [Indices][51] | Obtenez des valeurs d’index quotidiennes pour un emplacement spécifique. La disponibilité des index varie selon l’emplacement. |
| [Alarmes météorologiques][52] | Obtenez des alarmes météorologiques pour un emplacement spécifique. Les alarmes météo AccuWeather sont déterminées à l’aide des prévisions quotidiennes pour un emplacement. Une alarme existe pour un emplacement si la météo prévue atteint ou dépasse des [seuils spécifiques][58]. |
| [Alertes][53] | Recevez des alertes d’événements météorologiques graves des agences météorologiques officielles gouvernementales et des principaux fournisseurs d’alertes météorologiques mondiales. |
| [Images][54] | Obtenez des images radar et satellite. |
| [Tropical][55] | Prenez la position actuelle, les positions passées et les prévisions pour les cyclones tropicaux dans le monde entier. |
| [Traductions][56] | Obtenez une liste des langues disponibles. Obtenez des traductions pour des groupes spécifiques de phrases. |
{: .reset-td-br-1 .reset-td-br-2}

## Exemple de Contenu connecté

L’exemple suivant montre un appel de Contenu connecté qui affiche deux types de messages différents en fonction des conditions actuelles du code postal d’un utilisateur aux États-Unis. Les emplacements AccuWeather et les conditions actuelles API sont utilisés.
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

![Message de Contenu connecté via notification push qui dit « Il pleut ! Prenez le parapluie ! » affiché sur un appareil Android][17]{: style="max-width:40%"}

Une décomposition des deux appels de Contenu connecté est disponible dans les exemples suivants.

{% tabs %}
{% tab Locations %}
#### Exemple d’API d’emplacement

{% raw %}
Dans la première balise `connected_content`, une demande GET est faite à l’[API d’emplacement](https://apidev.accuweather.com/developers/locationsAPIguide). Dans cet exemple, vous pouvez également exploiter la valeur `{{${city}}}` de l’utilisateur si vous n’avez pas d’attribut personnalisé pour le code postal.

```
{% connected_content http://api.accuweather.com/locations/v1/postalcodes/{{${country}}}/search?q={{custom_attribute.${Zip Code}}}&apikey={your API key} :save location_info %}
```
{% endraw %}

Voici un exemple de ce qu’AccuWeather renvoie comme objet JSON :

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

L’ID « Key » est une variable utile telle qu’elle est utilisée dans la deuxième demande GET. 
Cet objet JSON peut être stocké dans une variable locale `location_info` en spécifiant `:save location_info` après l’URL. 
{% endtab %}
{% tab Current conditions %}

#### Exemple d’API de conditions actuelles

Pour la deuxième balise `connected_content`, une demande GET est faite à l’API [Conditions actuelles](https://apidev.accuweather.com/developers/currentConditionsAPIGuide). La **clé d’emplacement** devra être ajoutée à l’URL de la demande. Voici l’exemple de balise `connected_content` :

{% raw %}
```
{% connected_content http://api.accuweather.com/currentconditions/v1/{{location_info[0].Key}}?apikey={your API key} :save local_weather %}
```

Voici l’objet JSON renvoyé :

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

Comme on le voit dans la balise `connected_content`, l’objet JSON est stocké dans une variable locale `local_weather` en ajoutant `:save local_weather` après l’URL.

Vous pouvez tester la valeur renvoyée par [WeatherText](https://apidev.accuweather.com/developers/currentConditionsAPIGuide) en faisant référence à `{{local_weather[0].WeatherText}}`.

Si l’appel API répond avec `{{local_weather[0].WeatherText}}` et renvoie `Rain` (pluie), l’utilisateur reçoit alors la notification push.

{% endraw %}
{% endtab %}
{% endtabs %}

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
[60]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
