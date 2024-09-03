---
nav_title: アキュウェザー
article_title: アキュウェザー
alias: /partners/accuweather/
description: "この参考記事では、BrazeとAccuWeatherのパートナーシップについて概説している。AccuWeatherは、マーケティング・キャンペーンをパーソナライズするために使用できる天気APIである。"
page_type: partner
search_tag: Partner

---

# アキュウェザー

> [アキュウェザーは](https://www.accuweather.com/)、世界中の天気予報サービスを提供するメディア企業である。アキュウェザーでは、Braze \[Connected Content][60]. 

## 前提条件

| 必要条件 | 説明 |
|---|---|
| アキュウェザーAPIキー | リクエストURLに使用する互換性のあるAPIキーについては、アキュウェザーアカウントマネージャーに問い合わせること。<br><br>詳細な手順は、\[AccuWeather Enterprise API][57] page]に記載されている。 |
{: .reset-td-br-1 .reset-td-br-2}

## 利用可能なAccuWeather API

以下は、BrazeのキャンペーンやCanvasで参照できるAccuWeather APIである。

| API | 説明 |
|---|---|
|\[所在地][48] | 希望の場所のロケーションキーを取得する。ロケーションキーを使って、ForecastまたはCurrent Conditions APIから気象データを取得する。 |
| 予想][49] | 特定の場所の予報情報を得る。 |
| \[現在の状況][50] | 特定の場所の現況データを取得する。 |
| \[インデックス][51] | 特定の場所の日次指数値を取得する。インデックスの入手可能性は地域によって異なる。 |
| \[ウェザーアラーム][52] | 特定の場所の天気アラームを取得する。AccuWeatherの天気予報アラームは、その場所の毎日の予報を使って決定される。予報天候が\[特定の閾値][58]]を満たすか超える場合、その場所にアラームが存在する。 |
| \[アラート][53] | 政府気象機関や世界的な気象警報プロバイダーから、悪天候警報を受け取ることができる。 |
| \[イメージ][54] | レーダーと衛星画像を入手する。 |
| \[トロピカル][55] | 世界中の熱帯低気圧の現在位置、過去位置、予報を入手できる。 |
| 翻訳][56] | 利用可能な言語のリストを取得する。特定のフレーズグループの翻訳を取得する。 |
{: .reset-td-br-1 .reset-td-br-2}

## コネクテッド・コンテンツの例

次の例は、コネクテッド・コンテンツの呼び出しが、ユーザーのアメリカの郵便番号の現在の状況に基づいて、2つの異なるタイプのメッセージを表示することを示している。AccuWeather locations and current conditions APIエンドポイントが使用される。
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

![雨が降っています」というコネクテッド・コンテンツのプッシュメッセージ！アンドロイド端末で表示される「傘を持とう][17]{: style="max-width:40%"}

つのコネクテッド・コンテンツの呼び出しの内訳は、以下の例で見ることができる。

{% tabs %}
{% tab 所在地 %}
#### ロケーションAPIの例

{% raw %}
最初の`connected_content` タグ内で、[Locations APIへの](https://apidev.accuweather.com/developers/locationsAPIguide)GETリクエストが行われる。この例では、郵便番号のカスタム属性がない場合、ユーザーの`{{${city}}}` 。

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

Key "IDは、2番目のGETリクエストで使われるので、便利な変数である。
このJSONオブジェクトは、URLの後に`:save location_info` を指定することで、ローカル変数`location_info` に格納することができる。
{% endtab %}
{% tab 現在の状況 %}

#### 現状APIの例

2つ目の`connected_content` 、[現在の状況APIに](https://apidev.accuweather.com/developers/currentConditionsAPIGuide)GETリクエストが行われる。リクエストURLに**ロケーションキーを**追加する必要がある。`connected_content` ：

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

APIコールが`{{local_weather[0].WeatherText}}` 、`Rain` を返すと、ユーザーはプッシュを受け取る。

{% endraw %}
{% endtab %}
{% endtabs %}

[16]: [success@braze.com](mailto:success@braze.com)
[17]: {% image_buster /assets/img_archive/connected_weather_push2.png %} 「コネクテッド・コンテンツ・プッシュの使用例
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
[60]: {{site.baseurl}}/user_guide/パーソナライゼーションとダイナミックスcontent/connected_content/about_connected_content/
