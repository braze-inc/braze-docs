{% if include.section == "default behavior" %}

コネクテッドコンテンツはデフォルトで、作成する GET HTTP リクエストの `Content-Type` ヘッダーを、`Accept: */*` を持つ `application/json` に設定します。別のコンテンツタイプが必要な場合は、タグに`:content_type your/content-type`を追加して明示的に指定してください。Brazeは、指定したタイプにContent-TypeおよびAcceptヘッダーの両方を設定します。

{% raw %}
```js
{% connected_content http://numbersapi.com/random/trivia :content_type application/json %}
```
{% endraw %}

{% endif %}

{% if include.section == "http post" %}

デフォルトでは、コネクテッドコンテンツは指定されたURLにHTTP GETリクエストを送信します。代わりにPOSTリクエストを行うには、`:method post`を指定します。

指定された`:body`の後に`key1=value1&key2=value2&...`形式のクエリ文字列またはキャプチャされた値への参照を指定することで、オプションでPOSTボディを提供できます。Content-Typeのデフォルトは`application/x-www-form-urlencoded`です。`:content_type application/json`を指定し、`key1=value1&key2=value2`のようなフォームURLエンコードされた本文を提供すると、Brazeは送信前に自動的に本文をJSONエンコードします。

また、接続されたコンテンツは、デフォルトではPOST 呼び出しをキャッシュしません。`:cache_max_age` をコネクテッドコンテンツの POST 呼び出しに追加することで、この動作を更新できます。

{% tabs %}
{% tab デフォルトのコンテントタイプ %}

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 %}
```
{% endraw %}

{% endtab %}
{% tab Application/JSON Content-Type %}

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 :content_type application/json %}
```
{% endraw %}

{% endtab %}
{% endtabs %}


{% endif %}