---
nav_title: AccuWeather
article_title: AccuWeather
alias: /partners/accuweather/
description: "Este artículo de referencia describe la asociación entre Braze y AccuWeather, una API meteorológica que puede utilizar para personalizar sus campañas de marketing."
page_type: partner
search_tag: Partner

---

# AccuWeather

> [AccuWeather](https://www.accuweather.com/) es una empresa de medios de comunicación que presta servicios de predicción meteorológica en todo el mundo. Con AccuWeather, puedes enriquecer y personalizar tus campañas de marketing, así como automatizar las traducciones mediante el uso de [contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/) Braze. 

_Esta integración está mantenida por AccuWeather._

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Clave API de AccuWeather | Póngase en contacto con su gestor de cuenta de AccuWeather para obtener las claves API compatibles que debe utilizar en sus URL de solicitud.<br><br>Encontrarás más instrucciones en la página de [la API empresarial de AccuWeather](https://apidev.accuweather.com/developers/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## API de AccuWeather disponibles

A continuación se indican las API de AccuWeather a las que puede hacer referencia en sus campañas y lienzos Braze.

| API | Descripción |
|---|---|
|[Ubicaciones](https://apidev.accuweather.com/developers/locationsAPIguide) | Obtenga una clave de localización para la ubicación deseada. Utilice la clave de ubicación para recuperar datos meteorológicos de la API de previsión o de condiciones actuales. |
| [Previsión](https://apidev.accuweather.com/developers/forecastsAPIguide) | Obtenga información de previsión para una ubicación específica. |
| [Condiciones actuales](https://apidev.accuweather.com/developers/currentConditionsAPIGuide) | Obtenga los datos de las condiciones actuales para una ubicación específica. |
| [Índices](https://apidev.accuweather.com/developers/indicesApiGuide) | Obtenga los valores diarios del índice para una ubicación específica. La disponibilidad del índice varía según el lugar. |
| [Alarmas meteorológicas](https://apidev.accuweather.com/developers/weatheralarmsAPIguide) | Obtener alarmas meteorológicas para una ubicación específica. Las Alarmas Meteorológicas AccuWeather se determinan utilizando las previsiones diarias para un lugar. Existe una alarma para una ubicación si el tiempo previsto alcanza o supera [unos umbrales específicos](https://apidev.accuweather.com/developers/weatheralarms). |
| [Alertas](https://apidev.accuweather.com/developers/alertsApiGuide) | Reciba alertas de condiciones meteorológicas adversas de las Agencias Meteorológicas oficiales y de los principales proveedores mundiales de alertas meteorológicas. |
| [Imágenes](https://apidev.accuweather.com/developers/imageryAPIguide) | Obtenga imágenes de radar y satélite. |
| [Tropical](https://apidev.accuweather.com/developers/tropicalAPIGuide) | Obtén la posición actual, las posiciones anteriores y las previsiones de ciclones tropicales en todo el mundo. |
| [Traducciones](https://apidev.accuweather.com/developers/translationsApiGuide) | Obtener una lista de los idiomas disponibles. Obtenga traducciones para grupos específicos de frases. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Ejemplo de contenido conectado

El siguiente ejemplo muestra una llamada de Connected Content mostrando dos tipos diferentes de mensajes basados en las condiciones actuales del código postal de un usuario en EEUU. Se utilizan los puntos finales de la API de localizaciones y condiciones actuales de AccuWeather.
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

![Un mensaje push de contenido conectado que dice "¡Está lloviendo! Coge un paraguas!" mostrado en un dispositivo Android]({% image_buster /assets/img_archive/connected_weather_push2.png %} "Ejemplo de uso de push de contenido conectado"){: style="max-width:40%"}

En los siguientes ejemplos se desglosan las dos llamadas a Contenidos Conectados.

{% tabs %}
{% tab Ubicaciones %}
#### Ejemplo de API de ubicaciones

{% raw %}
Dentro de la primera etiqueta `connected_content`, se realiza una solicitud GET a la [API de ubicaciones](https://apidev.accuweather.com/developers/locationsAPIguide). Para este ejemplo, puede aprovechar la dirección `{{${city}}}` del usuario si no dispone de un atributo personalizado de código postal.

```
{% connected_content http://dataservice.accuweather.com/locations/v1/postalcodes/{{${country}}}/search?q={{custom_attribute.${Zip Code}}}&apikey={your API key} :save location_info %}
```
{% endraw %}

He aquí un ejemplo de lo que AccuWeather devolverá como objeto JSON:

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

El ID "Clave" es una variable útil ya que se utiliza en la segunda petición GET.
Este objeto JSON puede almacenarse en una variable local `location_info` especificando `:save location_info` después de la URL.
{% endtab %}
{% tab Condiciones actuales %}

#### API de Condiciones actuales - Ejemplo

Para la segunda etiqueta `connected_content`, se hace una petición GET a la [API de Condiciones Actuales](https://apidev.accuweather.com/developers/currentConditionsAPIGuide). La **clave de ubicación** deberá añadirse a la URL de la solicitud. Este es el ejemplo de etiqueta `connected_content`:

{% raw %}
```
{% connected_content http://dataservice.accuweather.com/currentconditions/v1/{{location_info[0].Key}}?apikey={your API key} :save local_weather %}
```

Este es el objeto JSON devuelto:

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

Como se ve en la etiqueta `connected_content`, el objeto JSON se almacena en una variable local `local_weather` añadiendo `:save local_weather` después de la URL.

Puede comprobar cuál debería ser la salida de [WeatherText](https://apidev.accuweather.com/developers/currentConditionsAPIGuide) consultando `{{local_weather[0].WeatherText}}`.

Si la llamada a la API responde con `{{local_weather[0].WeatherText}}` devolviendo `Rain`, el usuario recibiría entonces el push.

{% endraw %}
{% endtab %}
{% endtabs %}


[16]: [success@braze.com](mailto:success@braze.com)
