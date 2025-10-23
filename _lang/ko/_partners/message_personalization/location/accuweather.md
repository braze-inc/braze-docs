---
nav_title: AccuWeather
article_title: AccuWeather
alias: /partners/accuweather/
description: "이 참고 문서에서는 마케팅 캠페인을 개인화하는 데 사용할 수 있는 날씨 API인 Braze와 AccuWeather 간의 파트너십을 설명합니다."
page_type: partner
search_tag: Partner

---

# AccuWeather

> [Accuweather](https://www.accuweather.com/)는 전 세계에 기상 예보 서비스를 제공하는 미디어 회사입니다. With AccuWeather, you can enrich and personalize your marketing campaigns, as well as automate translations through the use of Braze [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/). 

_This integration is maintained by AccuWeather._

## 필수 조건

| 요구 사항 | 설명 |
|---|---|
| Accuweather API 키 | 요청 URL에서 사용할 호환 API 키에 대해 Accuweather 계정 매니저에게 문의하세요.<br><br>Further instructions can be found on the [AccuWeather Enterprise API](https://apidev.accuweather.com/developers/) page. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 가능한 Accuweather API

다음은 Braze 캠페인 및 캔버스에서 참조할 수 있는 AccuWeather API입니다.

| API | 설명 |
|---|---|
|[Locations](https://apidev.accuweather.com/developers/locationsAPIguide) | 원하는 위치에 대한 위치 키를 얻으십시오. 위치 키를 사용하여 예보 또는 현재 조건 API에서 날씨 데이터를 검색합니다. |
| [Forecast](https://apidev.accuweather.com/developers/forecastsAPIguide) | 특정 위치에 대한 예보 정보를 얻으십시오. |
| [Current Conditions](https://apidev.accuweather.com/developers/currentConditionsAPIGuide) | 특정 위치에 대한 현재 조건 데이터를 가져옵니다. |
| [Indices](https://apidev.accuweather.com/developers/indicesApiGuide) | 특정 위치에 대한 일일 지수 값을 가져옵니다. 색인 가용성은 위치에 따라 다릅니다. |
| [Weather Alarms](https://apidev.accuweather.com/developers/weatheralarmsAPIguide) | 특정 위치에 대한 날씨 경보를 받으세요. Accuweather 날씨 경보는 위치에 대한 일일 예보를 사용하여 결정됩니다. An alarm exists for a location if the forecast weather meets or exceeds [specific thresholds](https://apidev.accuweather.com/developers/weatheralarms). |
| [Alerts](https://apidev.accuweather.com/developers/alertsApiGuide) | 공식 정부 기상청 및 주요 글로벌 기상 경보 공급자로부터 악천후 경고를 받습니다. |
| [Imagery](https://apidev.accuweather.com/developers/imageryAPIguide) | 레이더 및 위성 이미지를 얻으십시오. |
| [Tropical](https://apidev.accuweather.com/developers/tropicalAPIGuide) | 전 세계 열대성 저기압의 현재 위치, 과거 위치 및 예보를 확인합니다. |
| [Translations](https://apidev.accuweather.com/developers/translationsApiGuide) | 사용 가능한 언어 목록을 가져옵니다. 특정 그룹의 구문에 대한 번역을 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 연결된 콘텐츠 예시

다음 예제에서는 사용자의 미국 내 우편번호의 현재 조건에 따라 두 가지 다른 유형의 메시지를 표시하는 연결된 콘텐츠 호출을 보여줍니다. Accuweather 위치 및 현재 조건 API 엔드포인트가 사용됩니다.
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

![연결된 콘텐츠 푸시 메시지 "비가 오고 있어요!" Grab an Umbrella!" shown on an Android device]({% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"){: style="max-width:40%"}

다음 예제에서 두 개의 연결된 콘텐츠 호출에 대한 분석을 확인할 수 있습니다.

{% tabs %}
{% tab 위치 %}
#### 위치 API 예시

{% raw %}
첫 번째 `connected_content` 태그 내에서 [위치 API](https://apidev.accuweather.com/developers/locationsAPIguide)에 대한 GET 요청이 수행됩니다. 이 예제에서는 우편번호 커스텀 속성이 없는 경우 사용자의 `{{${city}}}`를 대신 활용할 수 있습니다.

```
{% connected_content http://dataservice.accuweather.com/locations/v1/postalcodes/{{${country}}}/search?q={{custom_attribute.${Zip Code}}}&apikey={your API key} :save location_info %}
```
{% endraw %}

다음은 Accuweather가 JSON 객체로 반환할 예입니다:

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

'키' ID는 두 번째 GET 요청에서 사용되므로 유용한 변수입니다.
이 JSON 오브젝트는 URL 뒤에 `:save location_info`를 지정하여 로컬 변수 `location_info`에 저장할 수 있습니다.
{% endtab %}
{% tab 현재 조건 %}

#### 현재 조건 API 예시

두 번째 `connected_content` 태그의 경우, [현재 조건 API](https://apidev.accuweather.com/developers/currentConditionsAPIGuide)에 대한 GET 요청이 수행됩니다. 요청 URL에 **위치 키**를 추가해야 합니다. 여기에 예시 `connected_content` 태그가 있습니다:

{% raw %}
```
{% connected_content http://dataservice.accuweather.com/currentconditions/v1/{{location_info[0].Key}}?apikey={your API key} :save local_weather %}
```

다음은 반환된 JSON 객체입니다:

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

`connected_content` 태그에서 볼 수 있듯이 JSON 오브젝트는 URL 뒤에 `:save local_weather`를 추가하여 로컬 변수 `local_weather`에 저장됩니다.

[WeatherText](https://apidev.accuweather.com/developers/currentConditionsAPIGuide)의 출력 결과를 `{{local_weather[0].WeatherText}}`을 참조하여 테스트할 수 있습니다.

API 호출이 `{{local_weather[0].WeatherText}}`로 응답하고 `Rain`을 반환하면 사용자는 푸시를 받습니다

{% endraw %}
{% endtab %}
{% endtabs %}


[16]: [success@braze.com](mailto:success@braze.com)
