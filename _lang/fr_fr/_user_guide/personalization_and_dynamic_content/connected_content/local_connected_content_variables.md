---
nav_title: Variables du contenu connecté local
article_title: Variables de contenu connecté local
page_order: 1
description: "Cet article de référence explique comment utiliser et stocker les variables locales du contenu connecté."
search_rank: 1
---

# Variables du contenu connecté local

> Cette page donne un aperçu des variables locales du contenu connecté et de la manière de les utiliser et de les stocker.

Au moment de l'envoi, Braze envoie une requête GET standard à l'endpoint spécifié dans l'étiquette `connected_content`. Si l'endpoint renvoie du JSON, il est automatiquement analysé et stocké dans une variable appelée `connected`. Si l'endpoint renvoie du texte, celui-ci sera directement inséré dans le message à la place de l'étiquette `connected_content`.

Si vous souhaitez enregistrer votre réponse dans une variable, il est recommandé de renvoyer des objets JSON. Et si vous voulez que la réponse de Contenu connecté remplace l'étiquette par le texte, assurez-vous que la réponse n'est pas un JSON valide (tel que défini par [json.org](http://www.json.org))

Vous pouvez également spécifier `:save your_variable_name` après l'URL pour enregistrer les données sous un autre nom. Par exemple, l'étiquette `connected_content` suivante enregistre la réponse dans une variable locale appelée `localweather` (vous pouvez enregistrer plusieurs variables JSON `connected_content` ) :

{% raw %}
```js
{% connected_content https://www.metaweather.com/api/location/2459115/ :save localweather %}
```
{% endraw %}

Metaweather est une API météorologique gratuite qui utilise un "Where-on-Earth ID" pour renvoyer les conditions météorologiques d'une région. Utilisez ce code uniquement à des fins de test et d'apprentissage.

>  La variable stockée n'est accessible que dans le champ qui contient la demande `connected_content`. Par exemple, si vous voulez utiliser la variable `localweather` à la fois dans le champ message et dans le champ titre, vous devez faire la demande `connected_content` dans les deux champs. Si la demande est identique, Braze utilisera les résultats mis en cache, plutôt que d'envoyer une deuxième demande au serveur de destination. Toutefois, les appels de contenu connecté effectués via HTTP POST ne sont pas mis en cache par défaut et effectuent une deuxième demande au serveur de destination. Si vous souhaitez ajouter la mise en cache aux appels POST, reportez-vous à l'option [`cache_max_age`](#configurable-caching) option.

## Analyse JSON

Le contenu connecté interprétera tous les résultats formatés en JSON dans une variable locale, lorsque vous spécifiez `:save`. Par exemple, un endpoint de contenu connecté lié à la météo renvoie l'objet JSON suivant, que vous stockez dans une variable locale `localweather` en spécifiant `:save localweather`.
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

Vous pouvez vérifier s'il pleut ou non en vous référant à `{{localweather.consolidated_weather[0].weather_state_name}}`, qui, s'il était utilisé sur cet objet, renverrait `Clear`. Si vous souhaitez également personnaliser le nom de l'emplacement/localisation obtenu, `{{localweather.title}}` renvoie à `New York`.
{% endraw %}

L'image suivante illustre le type de coloration syntaxique que vous devriez voir dans le tableau de bord si vous avez configuré les choses correctement. Il montre également comment vous pouvez tirer parti de l'exemple de demande `connected_content`!

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

Si l'API a répondu {%raw%}`{{localweather.consolidated_weather[0].weather_state_name}}`{%endraw%} en renvoyant `Rain`, l'utilisateur recevra alors ce message.

\![Notification push avec le message "Il pleut ! Prenez un parapluie !"]({% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"){:style="max-width:50%" }

{% multi_lang_include connected_content.md section='default behavior' %}

## HTTP POST

{% multi_lang_include connected_content.md section='http post' %}

### Fournir un corps JSON

Si vous souhaitez fournir votre propre corps JSON, vous pouvez l'écrire en ligne s'il n'y a pas d'espace. Si votre corps comporte des espaces, vous devez utiliser une instruction d'assignation ou de capture. En d'autres termes, l'un ou l'autre de ces trois éléments est acceptable :

{% raw %}
##### Inline : les espaces ne sont pas autorisés

```js
{% connected_content https://example.com/api/endpoint :method post :body {"foo":"bar","baz":"{{1|plus:1}}"} :content_type application/json %}
```

##### Corps d'une déclaration de capture : espaces autorisés

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
##### Corps dans une déclaration d'affectation : espaces autorisés

```js
{% assign postbody = '{"foo":"bar", "baz": "2"}' %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```
{% endraw %}

## Codes d'état HTTP

Vous pouvez utiliser le statut HTTP d'un appel au contenu connecté en l'enregistrant d'abord dans une variable locale, puis en utilisant la touche `__http_status_code__`. Par exemple :

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :save result %}
{% if result.__http_status_code__ != 200 %}
  {% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert important %}
Cette clé ne sera automatiquement ajoutée à l'objet Contenu connecté que si l'endpoint renvoie un objet JSON valide et une réponse `2XX`. Si l'endpoint renvoie un tableau ou un autre type, cette clé ne peut pas être automatiquement définie dans la réponse.
{% endalert %}


[16]: [success@braze.com](mailto:success@braze.com)
