---
nav_title: AccuWeather
article_title: AccuWeather
alias: /partners/accuweather/
description: "この参考記事では、BrazeとAccuWeatherのパートナーシップについて概説している。AccuWeatherは、マーケティング・キャンペーンをパーソナライズするために使用できる天気APIである。"
page_type: partner
search_tag: Partner

---

# AccuWeather

> [AccuWeather](https://www.accuweather.com/) は、世界中で気象予報サービスを提供するメディア企業です。AccuWeather を使用すると、マーケティングキャンペーンを強化、パーソナライズし、Braze [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/) を使用して翻訳を自動化できます。 

_この統合は AccuWeather によって管理されます。_

## 前提条件

| 必要条件 | 説明 |
|---|---|
| AccuWeather API キー | リクエスト URL で使用する互換性のある API キーについては、AccuWeather アカウントマネージャーにお問い合わせください。<br><br>詳細な手順は、[AccuWeather Enterprise API](https://apidev.accuweather.com/developers/) ページに記載されています。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 利用可能なAccuWeather API

以下は、BrazeのキャンペーンやCanvasで参照できるAccuWeather APIである。

| API | 説明 |
|---|---|
|[Locations](https://apidev.accuweather.com/developers/locationsAPIguide) | 希望の場所のロケーションキーを取得する。ロケーションキーを使用して、Forecast API または Current Conditions API から気象データを取得します。 |
| [Forecast](https://apidev.accuweather.com/developers/forecastsAPIguide) | 特定の場所の予報情報を得る。 |
| [Current Conditions](https://apidev.accuweather.com/developers/currentConditionsAPIGuide) | 特定のロケーションの Current Conditions データを取得します。 |
| [Indices](https://apidev.accuweather.com/developers/indicesApiGuide) | 特定の場所の日次指数値を取得する。インデックスの入手可能性は地域によって異なる。 |
| [Weather Alarms](https://apidev.accuweather.com/developers/weatheralarmsAPIguide) | 特定の場所の天気アラームを取得する。AccuWeatherの天気予報アラームは、その場所の毎日の予報を使って決定される。天気予報が[特定のしきい値](https://apidev.accuweather.com/developers/weatheralarms)に一致するか、これを超過している場合、当該のロケーションにアラートが存在します。 |
| [Alerts](https://apidev.accuweather.com/developers/alertsApiGuide) | 政府の気象庁や世界的な気象警報プロバイダーから悪天候警報を取得します。 |
| [Imagery](https://apidev.accuweather.com/developers/imageryAPIguide) | レーダーと衛星画像を入手する。 |
| [Tropical](https://apidev.accuweather.com/developers/tropicalAPIGuide) | 世界中の熱帯低気圧の現在位置、過去の位置、予報を取得します。 |
| [翻訳](https://apidev.accuweather.com/developers/translationsApiGuide) | 利用可能な言語のリストを取得する。特定のフレーズグループの翻訳を取得します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## コネクテッドコンテンツの例

次に、米国内のユーザーの郵便番号に対応する場所の現在の状況に基づいて、2つの異なるタイプのメッセージを表示するコネクテッドコンテンツ呼び出しの例を示します。AccuWeather の Locations API エンドポイントと Current Conditions API エンドポイントが使用されています。
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

![雨が降っています」というコネクテッド・コンテンツのプッシュメッセージ！Android デバイスに表示される「傘のご用意を!」というメッセージ]({% image_buster /assets/img_archive/connected_weather_push2.png %}「Connected Content のプッシュ使用例」){: style="max-width:40%"}

2つのコネクテッドコンテンツ呼び出しの詳細を以下の例に示します。

{% tabs %}
{% tab Locations %}
#### ロケーションAPIの例

{% raw %}
1番目の `connected_content` タグ内で、[Locations API](https://apidev.accuweather.com/developers/locationsAPIguide) に対する GET リクエストが実行されます。この例では、郵便番号のカスタム属性がない場合には、代わりにユーザーの `{{${city}}}` を利用できます。

```
{% connected_content http://dataservice.accuweather.com/locations/v1/postalcodes/{{${country}}}/search?q={{custom_attribute.${Zip Code}}}&apikey={your API key} :save location_info %}
```
{% endraw %}

以下は、AccuWeatherがJSONオブジェクトとして返すものの例である：

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

「Key」ID は有用な変数であり、2番目の GET リクエストで使用されています。
この JSON オブジェクトは、URL の後に `:save location_info` を指定することで、ローカル変数 `location_info` に格納できます。
{% endtab %}
{% tab Current Conditions %}

#### Current Conditions API の例

2番目の `connected_content` タグで、[Current Conditions API](https://apidev.accuweather.com/developers/currentConditionsAPIGuide) に対する GET リクエストが実行されます。リクエスト URLに **ロケーションキー**を追加する必要があります。`connected_content` タグの例を次に示します。

{% raw %}
```
{% connected_content http://dataservice.accuweather.com/currentconditions/v1/{{location_info[0].Key}}?apikey={your API key} :save local_weather %}
```

以下は、返されたJSONオブジェクトである：

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

`connected_content` タグに見られるように、JSONオブジェクトは、URLの後に`:save local_weather` を追加することで、ローカル変数`local_weather` に格納される。

`{{local_weather[0].WeatherText}}` を参照することで、[WeatherText](https://apidev.accuweather.com/developers/currentConditionsAPIGuide)の出力がどうなるかをテストすることができる。

API 呼び出しが `{{local_weather[0].WeatherText}}` で応答し、`Rain` を返す場合、ユーザーはプッシュを受信します。

{% endraw %}
{% endtab %}
{% endtabs %}


[16]: [success@braze.com](mailto:success@braze.com)
