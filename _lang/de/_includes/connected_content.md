{% if include.section == "default behavior" %}

Standardmäßig setzt Connected-Content einen `Content-Type` -Header auf eine GET-HTTP-Anfrage, die es an `application/json` mit `Accept: */*` stellt. Wenn Sie einen anderen Content-Typ benötigen, geben Sie ihn explizit an, indem Sie dem Tag `:content_type your/content-type` hinzufügen. Braze setzt dann sowohl den Content-Type- als auch den Accept-Header auf den von Ihnen angegebenen Typ.

{% raw %}
```js
{% connected_content http://numbersapi.com/random/trivia :content_type application/json %}
```
{% endraw %}

{% endif %}

{% if include.section == "http post" %}

Standardmäßig stellt Connected-Content eine HTTP GET-Anfrage an die angegebene URL. Um stattdessen eine POST-Anfrage zu stellen, geben Sie `:method post` an.

Sie können optional einen POST-Body bereitstellen, indem Sie `:body` angeben, gefolgt von entweder einem Abfrage-String des Formats `key1=value1&key2=value2&...` oder einem Verweis auf erfasste Werte. Content-Type ist standardmäßig auf `application/x-www-form-urlencoded` eingestellt. Wenn Sie `:content_type application/json` angeben und einen form-url-codierten Body wie `key1=value1&key2=value2` bereitstellen, codiert Braze den Body vor dem Senden automatisch in JSON.

Connected-Content zwischenspeichert standardmäßig auch keine POST-Aufrufe. Sie können dieses Verhalten aktualisieren, indem Sie `:cache_max_age` zum Connected-Content-POST-Aufruf hinzufügen.

{% tabs %}
{% tab Standard Content-Typ %}

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 %}
```
{% endraw %}

{% endtab %}
{% tab Anwendung/JSON Content-Typ %}

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 :content_type application/json %}
```
{% endraw %}

{% endtab %}
{% endtabs %}


{% endif %}