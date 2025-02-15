---
nav_title: コネクテッドコンテンツのローカル変数
article_title: コネクテッドコンテンツのローカル変数
page_order: 1
description: "このリファレンス記事では、コネクテッドコンテンツのローカル変数の使用方法と保存方法について説明します。"
search_rank: 1
---

# コネクテッドコンテンツのローカル変数

Brazeは、`connected_content`タグ内に指定されたエンドポイントに送信時に標準のGETリクエストを行います。エンドポイントがJSONを返す場合、それは自動的に解析され、`connected`という変数に格納されます。エンドポイントがテキストを返す場合、それは`connected_content`タグの代わりにメッセージに直接挿入されます。

応答を変数に保存したい場合は、JSONオブジェクトを返すことをお勧めします。そして、コネクテッドコンテンツの応答でタグをテキストに置き換える場合は、応答が有効な JSON ([json.org][46] が定義) ではないことを確認してください。

URLの後に`:save your_variable_name`を指定して、データを別のものとして保存することもできます。例えば、次の`connected_content`タグは、`localweather`というローカル変数に応答を保存します（複数の`connected_content` JSON変数を保存できます）：

{% raw %}
```js
{% connected_content https://www.metaweather.com/api/location/2459115/ :save localweather %}
```
{% endraw %}

Metaweatherは、地域の天気を返すために「Where-on-Earth ID」を使用する無料の天気APIです。テストと学習の目的でのみこのコードを使用してください。

>  格納された変数は、`connected_content`リクエストを含むフィールド内でのみアクセスできます。例えば、メッセージとタイトルフィールドの両方で`localweather`変数を使用したい場合は、両方のフィールド内で`connected_content`リクエストを行う必要があります。リクエストが同一である場合、Brazeは送信先サーバーへの2回目のリクエストを行うのではなく、キャッシュされた結果を使用します。ただし、HTTP POST 経由で行われたコネクテッドコンテンツの呼び出しははデフォルトでキャッシュされず、送信先サーバーに 2 回目のリクエストを行います。POST呼び出しにキャッシュを追加したい場合は、[`cache_max_age`](#configurable-caching)オプションを参照してください。

## JSON解析

コネクテッドコンテンツは、`:save` が指定されると、JSON 形式の結果をローカル変数に解釈します。例えば、天気関連のコネクテッドコンテンツエンドポイントは、次のJSONオブジェクトを返します。これを`:save localweather`を指定してローカル変数`localweather`に格納します。
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

雨が降っているかどうかをテストするには、`{{localweather.consolidated_weather[0].weather_state_name}}`を参照してください。これをこのオブジェクトで使用すると、`Clear`が返されます。もし結果の場所の名前でもパーソナライズしたい場合は、`{{localweather.title}}`は`New York`を返します。
{% endraw %}

次の画像は、設定が正しく行われている場合にダッシュボードで表示される構文のハイライトの種類を示しています。また、例の`connected_content`リクエストを活用する方法も示しています！

{% raw %}
```liquid
{% connected_content https://www.metaweather.com/api/location/search/?query={{custom_attribute.${customCity}}} :save locationjson %}
{% connected_content https://www.metaweather.com/api/location/{{locationjson[0].woeid}}/ :save localweather %}

{% if {{localweather.consolidated_weather[0].weather_state_name}} == 'Rain' %}
It's raining! Grab an umbrella!
{% elsif {{localweather.consolidated_weather[0].weather_state_name}} == 'Clouds' %}
No sunscreen needed :)
{% else %}
Enjoy the weather!
{% endif %}
```
{% endraw %}

APIが{%raw%}`{{localweather.consolidated_weather[0].weather_state_name}}`{%endraw%}で`Rain`を返した場合、ユーザーはこのプッシュを受け取ります。

![プッシュ通知 with the message "It's raining!"Grab an umbrella!"][17]{:style="max-width:50%" }

コネクテッドコンテンツはデフォルトで、作成する GET HTTP リクエストの `Content-Type` ヘッダーを、`Accept: */*` を持つ `application/json` に設定します。別のコンテンツタイプが必要な場合は、タグに`:content_type your/content-type`を追加して明示的に指定してください。Brazeは、指定したタイプにContent-TypeおよびAcceptヘッダーの両方を設定します。

{% raw %}
```js
{% connected_content http://numbersapi.com/random/trivia :content_type application/json %}
```
{% endraw %}

## HTTP POST

デフォルトでは、コネクテッドコンテンツは指定されたURLにHTTP GETリクエストを送信します。代わりにPOSTリクエストを行うには、`:method post`を指定します。

指定された`:body`の後に`key1=value1&key2=value2&...`形式のクエリ文字列またはキャプチャされた値への参照を指定することで、オプションでPOSTボディを提供できます。Content-Typeのデフォルトは`application/x-www-form-urlencoded`です。`:content_type application/json`を指定し、`key1=value1&key2=value2`のようなフォームURLエンコードされた本文を提供すると、Brazeは送信前に自動的に本文をJSONエンコードします。


#### デフォルトのコンテンツタイプ
{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 %}
```
#### Application/JSON Content-Type
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 :content_type application/json %}
```
{% endraw %}

### JSONボディの提供
独自のJSONボディを提供したい場合、スペースがない場合はインラインで記述できます。体にスペースがある場合は、割り当てまたはキャプチャのステートメントを使用する必要があります。つまり、以下の 3 つのいずれも使用できます。

{% raw %}
##### インライン: スペースがない場合
```js
{% connected_content https://example.com/api/endpoint :method post :body {"foo":"bar","baz":"{{1|plus:1}}"} :content_type application/json %}
```

##### capture ステートメント内の本文: スペースがある場合
```js
{% capture postbody %}
{"foo": "bar", "baz": "{{ 1 | plus: 1 }}"}
{% endcapture %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```
{% endraw %}

{% raw %}
```js
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
  :save result
%}
```
{% endraw %}
{% raw %}
##### 代入文の本文：スペースが許可されている
```js
{% assign postbody = '{"foo":"bar", "baz": "2"}' %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```
{% endraw %}

## HTTPステータスコード

コネクテッドコンテンツの呼び出しから HTTP ステータスを使用するには、まず HTTP ステータスをローカル変数として保存してから、`__http_status_code__` キーを使用します。以下に例を示します。

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :save result %}
{% if result.__http_status_code__ != 200 %}
  {% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert important %}
このキーは、有効な JSON オブジェクトと `2XX` 応答をエンドポイントが返す場合にのみ、コネクテッドコンテンツオブジェクトに自動的に追加されます。エンドポイントが配列や他の型を返す場合、そのキーは応答に自動的に設定されることはありません。
{% endalert %}

## 設定可能なキャッシュ{#configurable-caching}

コネクテッドコンテンツの応答は、異なるキャンペーンやメッセージにわたって (同じワークスペース内で) キャッシュして、送信速度を最適化できます。

Braze は、コネクテッドコンテンツの応答を永続的にログに記録または格納しません。コネクテッドコンテンツのコール応答をLiquid 変数として格納することを明示的に選択した場合、Braze では、Liquid 変数をレンダリングしてメッセージを送信するために、これがインメモリでのみ (つまり短い期間の経過後に削除される一時的なメモリに) 格納されます。キャッシュを完全に防止するには、`:no_cache` を指定できます。これにより、ネットワークトラフィックが増加する可能性があります。システムの正常性のトラブルシューティングと監視に役立つように、Braze は、失敗した接続コンテンツコール(404s や429s など) をログに記録することもできます。これらのログは最大30 日間保持されます。

### キャッシュサイズの制限

コネクテッドコンテンツの応答本文は 1 MBを超えてはなりません。超えた場合はキャッシュされません。

### キャッシュ時間

コネクテッドコンテンツは、GETエンドポイントから返される値を最低5分間キャッシュします。キャッシュ時間が指定されていない場合、デフォルトのキャッシュ時間は5分です。 

コネクテッドコンテンツのキャッシュ時間は、次の例に示すように `:cache_max_age` で長く構成できます。最小キャッシュ時間は5分で、最大キャッシュ時間は4時間です。コネクテッドコンテンツデータは、Memcachedなどの揮発性キャッシュシステムを使用してインメモリでキャッシュされます。その結果、指定されたキャッシュ時間に関係なく、コネクテッドコンテンツデータは指定された時間よりも早くBrazeのインメモリキャッシュから削除される可能性があります。これは、キャッシュ期間が提案であり、実際にBrazeによってデータがキャッシュされる期間を保証するものではないことを意味します。また、指定されたキャッシュ期間で予想されるよりも多くのコネクテッドコンテンツリクエストが発生する可能性があります。

デフォルトでは、コネクテッドコンテンツはPOST呼び出しをキャッシュしません。`:cache_max_age` をコネクテッドコンテンツの POST 呼び出しに追加することで、この動作を変更できます。

#### 指定秒間のキャッシュ

この例は900秒（または15分）キャッシュされます。
{% raw %}
```
{% connected_content https://example.com/webservice.json :cache_max_age 900 %}
```
{% endraw %}


#### キャッシュバスティング

コネクテッドコンテンツによる、GET リクエストからの戻り値のキャッシュを防ぐには、`:no_cache` 構成を使用します。ただし、Braze 内部のホストからの応答は引き続きキャッシュされます。

{% raw %}
```js
{% connected_content https://example.com/webservice.json :no_cache %}
```
{% endraw %}

{% alert important %}
このオプションを使用する前に、指定したコネクテッドコンテンツのエンドポイントが集中的な大量のトラフィックを処理できることを確認してください。そうしないと、Brazeがすべてのメッセージについてコネクテッドコンテンツのリクエストを行うため、送信遅延の増加 (リクエストから応答までの遅延や時間間隔の増加) が発生する可能性があります。
{% endalert %}

`POST` では、キャッシュを停止する必要はありません。Braze は `POST` リクエストの結果を決してキャッシュしないためです。

[16]: [success@braze.com](mailto:success@braze.com)
[17]: {% image_buster /assets/img_archive/connected_weather_push2.png %}「コネクテッドコンテンツプッシュ使用例」
[46]: http://www.json.org
