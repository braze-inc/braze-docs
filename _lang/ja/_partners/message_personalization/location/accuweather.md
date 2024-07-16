---
nav_title: AccuWeather
article_title:AccuWeather
alias: /partners/accuweather/
description:この記事では、BrazeとAccuWeatherの提携について説明します。AccuWeatherは、マーケティングキャンペーンをパーソナライズするために使用できる天気APIです。
page_type: partner
search_tag:Partner

---

# AccuWeather

> [AccuWeather](https://www.accuweather.com/) は、世界中で天気予報サービスを提供するメディア企業です。AccuWeatherを使用すると、Braze \[Connected Content][60] を使用して、マーケティングキャンペーンを充実させ、パーソナライズし、翻訳を自動化することができます。 

## 前提条件

| 要件 | 説明 |
|---|---|
| AccuWeather APIキー | リクエストURLで使用する互換性のあるAPIキーについては、AccuWeatherのアカウントマネージャーにお問い合わせください。<br><br>さらなる指示は\[AccuWeather Enterprise API][57]ページで見つけることができます。 |
{: .reset-td-br-1 .reset-td-br-2}

## 利用可能なAccuWeather API

以下は、Brazeキャンペーンおよびキャンバス内で参照できるAccuWeather APIです。

| API | 説明 |
|---|---|
|\[場所][48] | ご希望の場所のロケーションキーを取得してください。位置キーを使用して、予報または現在の気象条件APIから気象データを取得します。 |
| 予報 | 特定の場所の予報情報を取得します。 |
| 現在の状況][50] | 特定の場所の現在の状況データを取得します。 |
| \[Indices][51] | 特定の場所の毎日のインデックス値を取得します。インデックスの利用可能性は場所によって異なります。 |
| \[天気警報][52] | 特定の場所の天気アラームを取得します。AccuWeatherの天気警報は、場所の日々の予報を使用して決定されます。特定の閾値][58]を満たすか超える予報天気がある場合、その場所にアラームが存在します。 |
| アラート][53] | 公式の政府気象機関および主要な世界の気象警報提供者からの}重大な天気警報を受け取ります。 |
| イメージ][54] | レーダーと衛星画像を取得します。 |
| トロピカル][55] | 世界中の熱帯低気圧の現在の位置、過去の位置、および予測を取得します。 |
| 翻訳][56] | 利用可能な言語のリストを取得します。特定のフレーズグループの翻訳を取得します。 |
{: .reset-td-br-1 .reset-td-br-2}

## 接続されたコンテンツの例

次の例は、米国のユーザーの郵便番号の現在の状況に基づいて、2種類の異なるメッセージを表示する接続されたコンテンツ呼び出しを示しています。AccuWeatherの場所と現在の状況APIエンドポイントが使用されます。
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

![「雨が降っています！」という内容の接続されたコンテンツプッシュメッセージAndroidデバイスに表示される「傘を持っていこう！」][17]{: style="max-width:40%"}

以下の例に、2つの接続されたコンテンツ呼び出しの内訳があります。

{% tabs %}
{% tab Locations %}
#### ロケーションAPIの例

{% raw %}
最初の`connected_content`タグ内で、[Locations API](https://apidev.accuweather.com/developers/locationsAPIguide)にGETリクエストが送信されます。この例では、郵便番号のカスタム属性がない場合、ユーザーの`{{${city}}}`を活用することもできます。

```
{% connected_content http://dataservice.accuweather.com/locations/v1/postalcodes/{{${country}}}/search?q={{custom_attribute.${Zip Code}}}&apikey={your API key} :save location_info %}
```
{% endraw %}

こちらは、AccuWeatherがJSONオブジェクトとして返す例です:

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

「キー」IDは、2番目のGETリクエストで使用されるため、便利な変数です。
このJSONオブジェクトは、URLの後に`:save location_info`を指定することによって、ローカル変数`location_info`に格納できます。
{% endtab %}
{% tab Current conditions %}

#### 現在の条件APIの例

2番目の`connected_content`タグの場合、[Current Conditions API](https://apidev.accuweather.com/developers/currentConditionsAPIGuide)にGETリクエストが送信されます。リクエストURLに**location key**を追加する必要があります。ここに例`connected_content`タグがあります:

{% raw %}
```
{% connected_content http://dataservice.accuweather.com/currentconditions/v1/{{location_info[0].Key}}?apikey={your API key} :save local_weather %}
```

ここに返されたJSONオブジェクトがあります:

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

URLの後に`:save local_weather`を追加することにより、JSONオブジェクトがローカル変数`local_weather`に格納されることが`connected_content`タグで確認できます。

[WeatherText](https://apidev.accuweather.com/developers/currentConditionsAPIGuide) の出力が `{{local_weather[0].WeatherText}}` を参照することによってテストできます。

APIコールが`{{local_weather[0].WeatherText}}`を返す`Rain`と応答した場合、ユーザーはプッシュを受信します。

{% endraw %}
{% endtab %}
{% endtabs %}

[16]: [success@braze.com](mailto:success@braze.com)
[17]: {% image_buster /assets/img_archive/connected_weather_push2.png %}「接続されたコンテンツプッシュ使用例」
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
