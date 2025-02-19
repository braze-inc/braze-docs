---
nav_title: Lokal verknüpfte Inhaltsvariablen
article_title: Lokal verknüpfte Inhaltsvariablen
page_order: 1
description: "In diesem Referenzartikel erfahren Sie, wie Sie lokale Connected-Content-Variablen verwenden und speichern können."
search_rank: 1
---

# Lokale Variablen für verknüpfte Inhalte

Braze stellt zum Sendezeitpunkt eine standardmäßige GET-Anfrage an den im Tag `connected_content` angegebenen Endpunkt. Wenn der Endpunkt JSON zurückgibt, wird es automatisch geparst und in einer Variablen namens `connected` gespeichert. Wenn der Endpunkt Text zurückgibt, wird dieser direkt in die Nachricht anstelle des Tags `connected_content` eingefügt.

Wenn Sie Ihre Antwort in einer Variablen speichern möchten, empfiehlt es sich, JSON-Objekte zurückzugeben. Und wenn Sie möchten, dass die Antwort von Connected-Content den Tag durch den Text ersetzt, stellen Sie sicher, dass die Antwort kein gültiges JSON ist (wie von [json.org][46] definiert)

Sie können auch `:save your_variable_name` nach der URL angeben, um die Daten unter einem anderen Namen zu speichern. Der folgende Tag `connected_content` zum Beispiel speichert die Antwort in einer lokalen Variable namens `localweather` (Sie können mehrere `connected_content` JSON-Variablen speichern):

{% raw %}
```js
{% connected_content https://www.metaweather.com/api/location/2459115/ :save localweather %}
```
{% endraw %}

Metaweather ist eine kostenlose Wetter-API, die eine "Where-on-Earth ID" verwendet, um das Wetter in einem Gebiet anzuzeigen. Verwenden Sie diesen Code nur zu Test- und Lernzwecken.

>  Auf die gespeicherte Variable kann nur innerhalb des Feldes zugegriffen werden, das die Anfrage `connected_content` enthält. Wenn Sie zum Beispiel die Variable `localweather` sowohl im Feld Nachricht als auch im Feld Titel verwenden möchten, sollten Sie die Anfrage `connected_content` in beiden Feldern stellen. Wenn die Anfrage identisch ist, verwendet Braze die zwischengespeicherten Ergebnisse, anstatt eine zweite Anfrage an den Zielserver zu stellen. Connected-Content-Aufrufe, die über HTTP POST erfolgen, werden jedoch standardmäßig nicht zwischengespeichert, sondern es wird eine zweite Anfrage an den Zielserver gestellt. Wenn Sie die Zwischenspeicherung für POST-Aufrufe hinzufügen möchten, verwenden Sie die [`cache_max_age`](#configurable-caching) Option.

## JSON-Parsing

Connected-Content wird alle JSON-formatierten Ergebnisse in eine lokale Variable interpretieren, wenn Sie `:save` angeben. Ein wetterbezogener Connected-Content-Endpunkt gibt beispielsweise das folgende JSON-Objekt zurück, das Sie durch Angabe von `:save localweather` in einer lokalen Variable `localweather` speichern.
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

Sie können testen, ob es regnet oder nicht, indem Sie auf `{{localweather.consolidated_weather[0].weather_state_name}}` verweisen, das, wenn es auf dieses Objekt angewendet wird, `Clear` zurückgeben würde. Wenn Sie den resultierenden Standortnamen auch personalisieren möchten, gibt `{{localweather.title}}` `New York` zurück.
{% endraw %}

Das folgende Bild veranschaulicht die Art der Syntaxhervorhebung, die Sie im Dashboard sehen sollten, wenn Sie alles richtig eingerichtet haben. Es zeigt auch, wie Sie die Anfrage von `connected_content` nutzen können!

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

Wenn die API mit {%raw%}`{{localweather.consolidated_weather[0].weather_state_name}}`{%endraw%} antwortet und `Rain` zurückgibt, würde die:der Nutzer:in diesen Push erhalten.

![Push-Benachrichtigung mit der Nachricht "Es regnet! Nehmen Sie einen Regenschirm!"][17]{:style="max-width:50%" }

Standardmäßig setzt Connected-Content einen `Content-Type` -Header auf eine GET-HTTP-Anfrage, die es an `application/json` mit `Accept: */*` stellt. Wenn Sie einen anderen Content-Typ benötigen, geben Sie ihn explizit an, indem Sie dem Tag `:content_type your/content-type` hinzufügen. Braze setzt dann sowohl den Content-Type- als auch den Accept-Header auf den von Ihnen angegebenen Typ.

{% raw %}
```js
{% connected_content http://numbersapi.com/random/trivia :content_type application/json %}
```
{% endraw %}

## HTTP POST

Standardmäßig stellt Connected-Content eine HTTP GET-Anfrage an die angegebene URL. Um stattdessen eine POST-Anfrage zu stellen, geben Sie `:method post` an.

Sie können optional einen POST-Body bereitstellen, indem Sie `:body` angeben, gefolgt von entweder einem Abfrage-String des Formats `key1=value1&key2=value2&...` oder einem Verweis auf erfasste Werte. Content-Type ist standardmäßig auf `application/x-www-form-urlencoded` eingestellt. Wenn Sie `:content_type application/json` angeben und einen form-url-codierten Body wie `key1=value1&key2=value2` bereitstellen, codiert Braze den Body vor dem Senden automatisch in JSON.


#### Standard Content-Typ
{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 %}
```
#### Anwendung/JSON Inhalt-Typ
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 :content_type application/json %}
```
{% endraw %}

### JSON-Körper bereitstellen
Wenn Sie Ihren eigenen JSON-Body bereitstellen möchten, können Sie ihn inline schreiben, wenn keine Leerzeichen vorhanden sind. Wenn Ihr Body Leerzeichen enthält, sollten Sie eine assign- oder capture-Anweisung verwenden. Das heißt, jede dieser drei Varianten ist akzeptabel:

{% raw %}
##### Inline: Leerzeichen nicht erlaubt
```js
{% connected_content https://example.com/api/endpoint :method post :body {"foo":"bar","baz":"{{1|plus:1}}"} :content_type application/json %}
```

##### Körper in einer Capture-Anweisung: Leerzeichen erlaubt
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
##### Körper in einer assign-Anweisung: Leerzeichen erlaubt
```js
{% assign postbody = '{"foo":"bar", "baz": "2"}' %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```
{% endraw %}

## HTTP-Statuscodes

Sie können den HTTP-Status aus einem Connected-Content-Aufruf nutzen, indem Sie ihn zunächst als lokale Variable speichern und dann die Taste `__http_status_code__` verwenden. Zum Beispiel:

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :save result %}
{% if result.__http_status_code__ != 200 %}
  {% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert important %}
Dieser Schlüssel wird nur dann automatisch zum Connected-Content-Objekt hinzugefügt, wenn der Endpunkt ein gültiges JSON-Objekt und eine `2XX` Antwort zurückgibt. Wenn der Endpunkt ein Array oder einen anderen Typ zurückgibt, kann dieser Schlüssel nicht automatisch in der Antwort gesetzt werden.
{% endalert %}

## Konfigurierbare Zwischenspeicherung {#configurable-caching}

Antworten auf Connected Content können für verschiedene Kampagnen oder Nachrichten (innerhalb desselben Arbeitsbereichs) zwischengespeichert werden, um die Sendegeschwindigkeit zu optimieren.

Braze protokolliert oder speichert Connected-Content-Antworten nicht permanent. Wenn Sie sich explizit dafür entscheiden, eine Antwort auf einen Connected Content-Aufruf als Liquid-Variable zu speichern, speichert Braze diese nur im Arbeitsspeicher, d.h. auf einem temporären Speicher, der nach kurzer Zeit gelöscht wird, um die Liquid-Variable zu rendern und die Nachricht zu senden. Um die Zwischenspeicherung ganz zu verhindern, können Sie `:no_cache` angeben, was zu erhöhtem Netzwerkverkehr führen kann. Zur Fehlerbehebung und Überwachung des Systemzustands kann Braze auch fehlgeschlagene Connected-Content-Aufrufe (z. B. 404 und 429) protokollieren; diese Protokolle werden bis zu 30 Tage lang aufbewahrt.

### Begrenzung der Cache-Größe

Der Antwortkörper von Connected-Content darf 1 MB nicht überschreiten, sonst wird er nicht zwischengespeichert.

### Cache-Zeit

Connected-Content wird den Wert, den es von GET-Endpunkten zurückgibt, mindestens 5 Minuten lang zwischenspeichern. Wenn keine Cache-Zeit angegeben wird, beträgt die Standard-Cache-Zeit 5 Minuten. 

Die Cache-Zeit für Connected-Content kann mit `:cache_max_age` länger eingestellt werden, wie im folgenden Beispiel gezeigt. Die minimale Zwischenspeicherzeit beträgt 5 Minuten und die maximale Zwischenspeicherzeit beträgt 4 Stunden. Connected-Content-Daten werden mit einem flüchtigen Cache-System, wie z. B. Memcached, im Speicher zwischengespeichert. Daher kann es vorkommen, dass Connected-Content-Daten unabhängig von der angegebenen Cache-Zeit früher als angegeben aus dem In-Memory-Cache von Braze entfernt werden. Das bedeutet, dass es sich bei den Cache-Dauern um Vorschläge handelt, die nicht unbedingt der Dauer entsprechen, die Braze für die Daten im Cache garantiert, und dass Sie möglicherweise mehr Connected Content-Anfragen sehen, als Sie bei einer bestimmten Cache-Dauer erwarten.

Standardmäßig werden POST-Aufrufe von Connected Content nicht zwischengespeichert. Sie können dieses Verhalten ändern, indem Sie `:cache_max_age` zum Connected-Content-POST-Aufruf hinzufügen.

#### Cache für bestimmte Sekunden

Dieses Beispiel wird für 900 Sekunden (oder 15 Minuten) zwischengespeichert.
{% raw %}
```
{% connected_content https://example.com/webservice.json :cache_max_age 900 %}
```
{% endraw %}


#### Cache-Busting

Um zu verhindern, dass Connected-Content den Wert, den es von einer GET-Anfrage zurückgibt, zwischenspeichert, können Sie die Konfiguration `:no_cache` verwenden. Antworten von Braze-internen Hosts werden jedoch weiterhin zwischengespeichert.

{% raw %}
```js
{% connected_content https://example.com/webservice.json :no_cache %}
```
{% endraw %}

{% alert important %}
Vergewissern Sie sich, dass der bereitgestellte Connected-Content-Endpunkt große Datenmengen verarbeiten kann, bevor Sie diese Option verwenden. Andernfalls werden Sie wahrscheinlich eine erhöhte Versandlatenz (größere Verzögerungen oder längere Zeitabstände zwischen Anfrage und Antwort) feststellen, da Braze für jede einzelne Nachricht Connected-Content-Anfragen stellt.
{% endalert %}

Mit einer `POST` müssen Sie keine Büste zwischenspeichern, da Braze die Ergebnisse von `POST` Anfragen niemals zwischenspeichert.

[16]: [success@braze.com](mailto:success@braze.com)
[17]: {% image_buster /assets/img_archive/connected_weather_push2.png %} "Beispiel für die Verwendung von Connected Content Push"
[46]: http://www.json.org
