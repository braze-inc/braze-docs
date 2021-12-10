---
nav_title: Météo batterie
article_title: Météo batterie
alias: /fr/partners/accuweather/
description: "Cet article décrit le partenariat entre Braze et AccuWeather, une API météo que vous pouvez utiliser pour personnaliser vos campagnes de marketing."
page_type: partenaire
search_tag: Partenaire
---

# Météo batterie

> [AccuWeather](https://www.accuweather.com/) est une entreprise de médias qui fournit des services de prévision météo dans le monde entier. Avec AccuWeather, vous pouvez enrichir et personnaliser vos campagnes de marketing, ainsi que automatiser les traductions grâce à l'utilisation de Braze [Contenus connectés][60].

## Pré-requis

| Exigences           | Libellé                                                                                                                                                                                                                                                     |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Clé API AccuWeather | Contactez votre gestionnaire de compte AccuWeather pour obtenir des clés API compatibles à utiliser dans les URLs de votre requête.<br><br>Des instructions supplémentaires peuvent être trouvées sur la page [AccuWeather Enterprise API][57]. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## APIs AccuWeather disponibles

Voici les API AccuWeather que vous pouvez référencer dans vos campagnes Braze et Canvases.

| API                        | Libellé                                                                                                                                                                                                                                                                  |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Emplacements][48]         | Obtenez une clé de localisation pour l'emplacement que vous souhaitez. Utilisez la clé de localisation pour récupérer les données météo de l'API Prévisions ou Conditions Actuelles.                                                                                     |
| [Prévision][49]            | Obtenir des informations sur les prévisions pour un endroit spécifique.                                                                                                                                                                                                  |
| [Conditions actuelles][50] | Obtenir les données des conditions actuelles pour un emplacement spécifique.                                                                                                                                                                                             |
| [Indices][51]              | Obtenir des valeurs d'index quotidiennes pour un emplacement spécifique. La disponibilité de l'indice varie en fonction de l'emplacement.                                                                                                                                |
| [Alarmes Météo][52]        | Obtenir des alarmes météo pour un emplacement spécifique. Les alarmes météo AccuWeather sont déterminées en utilisant les prévisions quotidiennes pour un endroit. Une alarme existe pour un emplacement si la météo prévue atteint ou dépasse [seuils spécifiques][58]. |
| [Alertes][53]              | Recevez des alertes météorologiques sévères de la part des agences météorologiques officielles du gouvernement et des principaux fournisseurs mondiaux d'alerte météorologique.                                                                                          |
| [Imagerie][54]             | Obtenez des images radar et satellite.                                                                                                                                                                                                                                   |
| [Tropical][55]             | Obtenez la position, les positions passées et les prévisions des cyclones tropicaux dans le monde entier.                                                                                                                                                                |
| [Traductions][56]          | Obtenir une liste des langues disponibles. Obtenir des traductions pour des groupes spécifiques de phrases.                                                                                                                                                              |
{: .reset-td-br-1 .reset-td-br-2}

## Exemple de contenu connecté

L'exemple suivant montre un appel de contenu connecté affichant deux types de messages différents en fonction des conditions actuelles du code postal d'un utilisateur aux États-Unis. Les emplacements AccuWeather et les conditions actuelles des terminaux de l'API sont utilisés.
{% raw %}

```liquid
{% connected_content http://api.accuweather.com/locations/v1/postalcodes/{{${country}}}/search?q={{custom_attribute.${Zip Code}}}&apikey={your API key} :save location_info %}

{% connected_content http://api. ccuweather. om/currentconditions/v1/{{location_info[0].Key}}? pikey={your API key} :save local_weather %}

{% if {{local_weather[0].WeatherText}} == 'Cloudy' %}
Aucun écran solaire nécessaire :)
{% elsif {{local_weather[0].WeatherText}} == 'Pluie' %}
Il pleut ! Attrape un parapluie !
{% else %}
Profitez du temps !
{% endif %}
```
{% endraw %}

!\[Exemple\]\[17\]{: style="max-width:40%"}

Une ventilation des deux appels de contenu connecté se trouve ci-dessous.

{% tabs %}
{% tab Locations %}
#### Exemple d'API des emplacements

{% raw %}
Dans la première balise `connected_content` , une requête GET est faite à l'API [Emplacements](https://apidev.accuweather.com/developers/locationsAPIguide). Pour cet exemple, vous pouvez également tirer parti de l'attribut `{{${city}}}` de l'utilisateur si vous n'avez pas d'attribut personnalisé de code postal.

```
{% connected_content http://api.accuweather.com/locations/v1/postalcodes/{{${country}}}/search?q={{custom_attribute.${Zip Code}}}&apikey={your API key} :save location_info %}
```
{% endraw %}

Voici un exemple de ce que AccuWeather retournera en tant qu'objet JSON:

```json
[
  {
    "Version": 1,
    "Key": "41333_PC",
    "Type": "Code Postal",
    "Rang": 35,
    "LocalizedName": "Seattle",
    "EnglishName": "Seattle",
    "PrimaryPostalCode": "98102",
    "Région": {
      "ID": "NOM",
      "Nom localisé": "Amérique du Nord",
      "FrenhName": "Amérique du Nord"
    },
    "Pays": {
      "ID": "US",
      "Nom localisé": "États-Unis",
      "FrenhName": "United States"
    },
    "Zone Administrative": {
      "ID": "WA",
      "Nom localisé": "Washington",
      "FrenhName": "Washington",
      "Level": 1,
      "LocalizedType": "État",
      "EnglishType": "État",
      "CountryID": "US"
    },
    "Fuseau horaire": {
      "Code": "PDT",
      "Nom": "Amérique/Los_Angeles",
      "GmtOffset": -7. ,
      "IsDaylightSaving": true,
      "NextOffsetChange": "2018-11-04T09:00Z"
    },
    "Géoposition": {
      "Latitude": 47. 36,
      "Longitude": -122. 27,
      "Elevation": {
        "Metric": {
          "Valeur": 26. ,
          "Unité": "m",
          "UnitéType": 5
        },
        "Imperial": {
          "Value": 85. ,
          "Unité": "ft",
          "UnitType": 0
        }
      }
    },
    "IsAlias": false,
    "ParentCity": {
      "Key": "351409",
      "LocalizedName": "Seattle",
      "FrenhName": "Seattle"
    },
    "SupplementalAdminAreas": [
      {
        "Level": 2,
        "Nom localisé": "Roi",
        "Nom Français": "Roi"
      }
    ],
    "Jeu de données": [
      "Alertes",
      "DailyAirQualityForecast",
      "DailyPollenForecast",
      "Confiance des prévisions",
      "MinuteCast"
    ]
  }
]
```

L'identifiant "Key" est une variable utile car il est utilisé dans la deuxième requête GET. L'objet JSON ci-dessus peut être stocké dans une variable locale `location_info` en spécifiant `:save location_info` après l'URL.
{% endtab %}
{% tab Current conditions %}

#### Exemple d'API des conditions actuelles

Pour la seconde balise `connected_content` , une requête GET est faite à la [API des conditions actuelles](https://apidev.accuweather.com/developers/currentConditionsAPIGuide). La **clé de localisation** devra être ajoutée à l'URL de la requête. Voici l'exemple `balise connected_content`:

{% raw %}
```
{% connected_content http://api.accuweather.com/currentconditions/v1/{{location_info[0].Key}}?apikey={your API key} :save local_weather %}
```

Voici l'objet JSON retourné :

```json
[
  {
    "LocalObservationDateTime": "2018-04-10T09:35:00-07:00",
    "EpochTime": 1523378100,
    "Météotexte": "Pluie",
    "WeatherIcon": 18,
    "IsDayTime": vrai,
    "Température": {
      "Metric": {
        "Valeur": 11. ,
        "Unité": "C",
        "UnitType": 17
      },
      "Impérial": {
        "Valeur": 52. ,
        "Unité": "F",
        "UnitType": 18
      }
    },
    "MobileLink": "http://m. ccuweather. om/fr/us/seattle-wa/98104/current-weather/41333_pc?lang=en-us",
    "Link": "http://www.accuweather.com/fr/us/seattle-wa/98104/current-weather/41333_pc?lang=en-us"
  }
]
```

Comme vu dans la balise `connected_content` ci-dessus, l'objet JSON est stocké dans une variable locale `local_weather` en ajoutant `:save local_weather` après l'URL.

Vous pouvez tester ce que la sortie du [WeatherText](https://apidev.accuweather.com/developers/currentConditionsAPIGuide) doit être en référençant `{{local_weather[0].WeatherText}}`.

Si l'appel API répond avec `{{local_weather[0].WeatherText}}` renvoyant `Pluie`, l'utilisateur recevra alors le push indiqué ci-dessus.

{% endraw %}
{% endtab %}
{% endtabs %}
[17]: {% image_buster /assets/img_archive/connected_weather_push2.png %} "Exemple d'utilisation de push de contenu connecté"

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
