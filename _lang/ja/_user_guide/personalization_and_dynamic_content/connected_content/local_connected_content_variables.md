---
nav_title: ローカル接続コンテンツ変数
article_title: ローカル接続コンテンツ変数
page_order: 1
description: "この参照記事では、ローカルのConnected Content 変数の使用方法と保存方法について説明します。"
search_rank: 1
---

# ローカル接続コンテンツ変数

Braze は、`connected_content` タグ内で指定されたエンドポイントへの送信時に標準のGET 要求を行います。エンドポイントがJSON を返すと、自動的に解析され、`connected` という変数に保存されます。エンドポイントがテキストを返す場合、`connected_content` タグの代わりにメッセージに直接挿入されます。

変数に応答を保存する場合は、JSON オブジェクトを返すことをお勧めします。また、Connected Content の応答でタグをテキストに置き換える場合は、応答が([json.org][46] で定義されているように) 有効でないことを確認します。

URLの後に`:save your_variable_name`を指定して、データを別のものとして保存することもできます。たとえば、次の`connected_content` タグは、`localweather` というローカル変数への応答を格納します(複数の`connected_content` JSON 変数を保存できます)。

{% raw %}
```js
{% connected_content https://www.metaweather.com/api/location/2459115/ :save localweather %}
```
{% endraw %}

メタウェザーは、"Where-on-Earth ID"を使用して、エリア内の天気を返すフリーウェザーAPI です。このコードは、テストおよび学習目的でのみ使用してください。

>  格納された変数は、`connected_content` 要求を含むフィールド内でのみアクセスできます。たとえば、message フィールドとtitle フィールドの両方で`localweather` 変数を使用する場合は、両方のフィールドで`connected_content` 要求を行う必要があります。リクエストが同一の場合、Braze は、宛先サーバーに対して2 回目のリクエストを行うのではなく、キャッシュされた結果を使用します。ただし、HTTP POST 経由で行われた接続コンテンツコールは、デフォルトではキャッシュされず、宛先サーバに対して2 回目の要求を行います。POST 呼び出しにキャッシュを追加する場合は、[`cache_max_age`](#configurable-caching) オプションを参照してください。

## JSON解析

接続されたコンテンツは、`:save`を指定すると、JSON形式の結果をローカル変数に解釈します。たとえば、weather-related Connected Content エンドポイントは、`localweather` というローカル変数に`:save localweather` を指定して保存した次のJSON オブジェクトを返します。
{% raw %}

```js
{
  "consolidated_weather": [
    {
      "id": 5.8143475362693e+15,
      "weather_state_name": "Clear",
      "weather_state_abbr": "c",
      "wind_direction_compass": "WSW",
      "created": "2017-06-12T14:14:46.268110Z",
      "applicable_date": "2017-06-12",
      "min_temp": 22.511666666667,
      "max_temp": 31.963333333333,
      "the_temp": 27.803333333333,
      "wind_speed": 6.8884690250312,
      "wind_direction": 251.62921994166,
      "air_pressure": 1021.335,
      "humidity": 50,
      "visibility": 14.945530601288,
      "predictability": 68
    },
    .
    .
    .
    "title": "New York",
    "location_type": "City",
    "woeid": 2459115,
    "latt_long": "40.71455,-74.007118",
    "timezone": "US\/Eastern"
  }
```

雨が降っているかどうかは、`{{localweather.consolidated_weather[0].weather_state_name}}` を参照してテストできます。このオブジェクトで使用した場合、`Clear` が返されます。結果のロケーション名でパーソナライズする場合、`{{localweather.title}}` は`New York` を返します。
{% endraw %}

次の図は、正しく設定している場合にダッシュボードに表示される構文ハイライトのタイプを示しています。また、`connected_content` リクエストの例を活用する方法も示しています!

{% raw %}
\`\`\`liquid
{% connected_content https://www.metaweather.com/api/location/search/?query={{custom_attribute.${customCity}}} :save locationjson %}
{% connected_content https://www.metaweather.com/api/location/{{locationjson[0].woeid}}/ :save localweather %}

{% if {{localweather.consolidated\_weather[0].weather\_state\_name}} == 'Rain' %}
雨が降っています！傘を握ろう！
{% elsif {{localweather.consolidated\_weather[0].weather\_state\_name}} == 'Clouds' %}
日焼け止め不要:)
{% else %}
天気をお楽しみください！
{% endif %}
\`\`\`
{% endraw %}

API が{%raw%}`{{localweather.consolidated_weather[0].weather_state_name}}`{%endraw%} で応答し、`Rain` を返した場合、ユーザはこのプッシュを受け取ります。

![メッセージ&quotでプッシュ通知;雨が降っているよ!傘をつかむ!"][17]{:style="max-width:50%" }

デフォルトでは、Connected Content は、`application/json` に`Accept: */*` を設定するGET HTTP 要求に`Content-Type` ヘッダを設定します。別のコンテンツタイプが必要な場合は、`:content_type your/content-type` をタグに追加して明示的に指定します。Braze は、Content-Type ヘッダーとAccept ヘッダーの両方を指定したタイプに設定します。

{% raw %}
```js
{% connected_content http://numbersapi.com/random/trivia :content_type application/json %}
```
{% endraw %}

## HTTP POST

デフォルトでは、Connected Content は指定されたURL に対してHTTP GET 要求を行います。代わりにPOST 要求を行うには、`:method post` を指定します。

オプションで、`:body` を指定し、その後に`key1=value1&key2=value2&...` 形式のクエリ文字列、またはキャプチャされた値への参照を指定して、POST 本文を指定できます。Content-Type のデフォルトは`application/x-www-form-urlencoded` です。`:content_type application/json` を指定し、`key1=value1&key2=value2` などのフォームURL コード化された本文を指定した場合、Braze は送信前に自動的に本文をJSON エンコードします。


#### デフォルトのコンテンツタイプ
{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 %}
```
#### アプリケーション/JSON コンテンツタイプ
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 :content_type application/json %}
```
{% endraw %}

### JSONボディの提供
独自のJSON 本文を指定する場合は、スペースがない場合にインラインで記述できます。身体にスペースがある場合は、assignまたはcaptureステートメントを使用する必要があります。つまり、次の3 つのいずれかを使用できます。

{% raw %}
##### インライン: スペースは使用できません
```js
{% connected_content https://example.com/api/endpoint :method post :body {"foo":"bar","baz":"{{1|plus:1}}"} :content_type application/json %}
```

##### capture 文の本文: 使用可能なスペース
```js
{% capture postbody %}
{"foo": "bar", "baz": "{{ 1 | plus: 1 }}"}
{% endcapture %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```
{% endraw %}

{% raw %}
\`\`\`js
{% capture postbody %}
{
"ids":[ca_57832,ca_75869],"include":{"attributes":{"withKey":["daily_deals"]}}
}
{% endcapture %}

{% connected_content
https://example.com/api/endpoint
:method post
:headers {
"Content-Type": "application/json"
}
    :body {{postbody}}
    結果保存
    %}
      \`\`\`
  {% endraw %}
  {% raw %}
##### assign 文の本文: 使用可能なスペース
```js
{% assign postbody = '{"foo":"bar", "baz": "2"}' %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```
{% endraw %}

## HTTPステータスコード

Connected Content コールのHTTP ステータスを使用するには、まずローカル変数として保存し、次に`__http_status_code__` キーを使用します。次に例を示します。

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :save result %}
{% if result.__http_status_code__ != 200 %}
  {% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert important %}
このキーは、エンドポイントが有効なJSON オブジェクトと`2XX` 応答を返す場合にのみ、自動的に接続コンテンツオブジェクトに追加されます。エンドポイントが配列またはその他のタイプを返す場合、そのキーは応答で自動的に設定できません。
{% endalert %}

## 設定可能なキャッシュ {#configurable-caching}

接続コンテンツレスポンスは、異なるキャンペーンまたはメッセージ(同じワークスペース内) にキャッシュして、送信速度を最適化することができます。

### キャッシュサイズの制限
Connected Content レスポンスボディは、1MB を超えないようにする必要があります。超えない場合、キャッシュされません。

### キャッシュ時間
Connected Content は、GET エンドポイントから返される値を最低5 分間キャッシュします。キャッシュ時間が指定されていない場合、デフォルトのキャッシュ時間は5分です。 

次の例に示すように、接続されたコンテンツキャッシュ時間を`:cache_max_age` で長く設定できます。最小キャッシュ時間は5 分、最大キャッシュ時間は4 時間です。接続されたコンテンツデータは、Memcached などの揮発性キャッシュシステムを使用してメモリ内にキャッシュされます。その結果、指定されたキャッシュ時間に関係なく、接続コンテンツデータは指定されたよりも前にBrazeのメモリ内キャッシュから削除される可能性があります。これは、キャッシュの継続時間が提案であり、データがBrazeによってキャッシュされることが保証されている期間を実際に表わしていない場合があることを意味します。また、特定のキャッシュの継続時間で予想されるよりも多くの接続コンテンツリクエストが表示される場合があります。

デフォルトでは、接続コンテンツはPOST 呼び出しをキャッシュしません。この動作を変更するには、`:cache_max_age` をConnected Content POST コールに追加します。

#### 指定した秒のキャッシュ

この例では、900秒(または15分)間キャッシュします。
{% raw %}
```
{% connected_content https://example.com/webservice.json :cache_max_age 900 %}
```
{% endraw %}


#### キャッシュバスト

接続コンテンツがGET 要求から返される値をキャッシュしないようにするには、`:no_cache` 設定を使用します。

{% raw %}
```js
{% connected_content https://example.com/webservice.json :no_cache %}
```
{% endraw %}

{% alert important %}
このオプションを使用する前に、接続コンテンツエンドポイントが大量のトラフィックを処理できることを確認してください。または、1 つのメッセージごとに接続コンテンツリクエストを作成するため、送信遅延が増加(リクエストとレスポンスの間の遅延または時間間隔が長くなる)する可能性があります。
{% endalert %}

`POST` では、Braze は`POST` リクエストの結果をキャッシュしないため、bust をキャッシュする必要はありません。

[16]: [success@braze.com](mailto:success@braze.com)
[17]: {% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"
[46]: http://www.json.org
