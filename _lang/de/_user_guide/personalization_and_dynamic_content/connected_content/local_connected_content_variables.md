---
nav_title: Lokale Variablen für verknüpfte Inhalte
article_title: Lokal verknüpfte Inhaltsvariablen
page_order: 1
description: "In diesem Referenzartikel erfahren Sie, wie Sie lokale Connected-Content-Variablen verwenden und speichern können."
search_rank: 1
---

# Lokale Variablen für verknüpfte Inhalte

> Diese Seite bietet eine Übersicht über die lokalen Connected-Content-Variablen und darüber, wie Sie diese verwenden und speichern können.

Braze stellt zum Sendezeitpunkt eine standardmäßige GET-Anfrage an den im Tag `connected_content` angegebenen Endpunkt. Wenn der Endpunkt JSON zurückgibt, wird es automatisch geparst und in einer Variablen namens `connected` gespeichert. Wenn der Endpunkt Text zurückgibt, wird dieser direkt in die Nachricht anstelle des Tags `connected_content` eingefügt.

Wenn Sie Ihre Antwort in einer Variablen speichern möchten, empfiehlt es sich, JSON-Objekte zurückzugeben. Und wenn Sie möchten, dass die Antwort von Connected-Content den Tag durch den Text ersetzt, stellen Sie sicher, dass die Antwort kein gültiges JSON ist (wie von [json.org](http://www.json.org))

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

![Push-Benachrichtigung mit der Nachricht "Es regnet! Nehmen Sie einen Regenschirm!"]({% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"){:style="max-width:50%" }

{% multi_lang_include connected_content.md section='default behavior' %}

## HTTP POST

{% multi_lang_include connected_content.md section='http post' %}

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


[16]: [success@braze.com](mailto:success@braze.com)
