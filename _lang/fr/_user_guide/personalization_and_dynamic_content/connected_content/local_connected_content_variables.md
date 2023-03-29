---
nav_title: Variables du contenu connecté local
article_title: Variables du contenu connecté local
page_order: 1
description: "Le présent article de référence explique comment utiliser et stocker les variables du contenu connecté local."
search_rank: 1
---

# Variables du contenu connecté local

Braze effectue une requête GET standard à l’heure d’envoi à l’endpoint spécifié dans la balise `connected_content`. Si l’endpoint retourne du JSON, il est automatiquement analysé et stocké dans une variable appelée `connected`.  Si l’endpoint renvoie du texte, il sera directement inséré dans le message à la place de la balise `connected_content`.

>  Si vous souhaitez enregistrer votre réponse à une variable, il est recommandé de retourner les objets JSON. Si vous souhaitez que la réponse du Contenu connecté remplace la balise par le texte, assurez-vous que la réponse n’est pas valide (tel que défini par [json.org][46])

Vous pouvez également spécifier `:save your_variable_name` après l’URL afin d’enregistrer les données comme autre chose. Par exemple, la balise `connected_content` suivante enregistrera la réponse à une variable locale appelée `localweather` (vous pouvez enregistrer plusieurs variables JSON `connected_content`) :

{% raw %}
```js
{% connected_content https://www.metaweather.com/api/location/2459115/ :save localweather %}
```
{% endraw %}

[Metaweather](https://www.metaweather.com/api/) est une API météo gratuite qui utilise un « Where-on-Earth ID » pour renvoyer la météo dans une zone. Utilisez ce code à des fins de test et d’apprentissage uniquement.

>  La variable stockée ne peut être consultée que dans le champ qui contient la requête `connected_content`. Par exemple, si vous souhaitez utiliser la variable `localweather` dans le champ Message et Titre, vous devez effectuer la requête `connected_content` dans les deux champs. Si la demande est identique, Braze utilisera les résultats mis en cache plutôt que d’effectuer une seconde demande au serveur de destination. Cependant, les appels de contenu connecté effectués via HTTP POST ne sont pas mis en cache par défaut et feront une seconde demande au serveur de destination. Si vous souhaitez ajouter la mise en cache aux appels POST, reportez-vous à l’option [`cache_max_age`](#configurable-caching).

## Analyse JSON

Le contenu connecté interprète tous les résultats formatés JSON dans une variable locale, lorsque vous spécifiez `:save`. Par exemple, un endpoint de contenu connecté lié à la météo renvoie l’objet JSON suivant, que vous stockez dans une variable locale `localweather` en spécifiant `:save localweather`.
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

Vous pouvez tester s’il pleut ou non en faisant référence à `{{localweather.consolidated_weather[0].weather_state_name}}`, qui, si utilisé sur cet objet, renverrait `Clear`. Si vous souhaitez également personnaliser avec le nom de l’emplacement en résultant, `{{localweather.title}}` retournera  `New York`.
{% endraw %}

L’image suivante illustre le type de syntaxe que vous devez voir dans le tableau de bord si vous configurez correctement les choses. Cela montre également comment vous pourriez tirer parti de l’exemple de requête `connected_content` !

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

Si l’API a répondu par {%raw%}`{{localweather.consolidated_weather[0].weather_state_name}}`{%endraw%} retournant `Rain`, l’utilisateur recevrait alors cette notification push.

![Notification push avec le message « Il pleut ! Prenez le parapluie ! »][17]{:style="max-width:50%" }

Par défaut, le contenu connecté définit un en-tête `Content-Type` pour une requête GET HTTP faite à `application/json` avec `Accept: */*`. Si vous avez besoin d’un autre type de contenu, spécifiez-le explicitement en ajoutant `:content_type your/content-type` à la balise. Braze définira alors l’en-tête Type de contenu et Accepter au type que vous spécifiez.

{% raw %}
```js
{% connected_content http://numbersapi.com/random/trivia :content_type application/json %}
```
{% endraw %}

## POST HTTP

Par défaut, le contenu connecté fait une requête HTTP GET à l’URL spécifiée. Pour effectuer une requête POST, précisez `:method post`.

Vous pouvez éventuellement fournir un corps POST en spécifiant `:body` suivi d’une chaîne de caractères de requête au format `key1=value1&key2=value2&...` ou une référence à des valeurs capturées. Type de contenu par défaut `application/x-www-form-urlencoded`. Si vous spécifiez `:content_type application/json` et fournissez un corps codé en tant qu’URL de formulaire, comme `key1=value1&key2=value2`, Braze codera le corps en JSON automatiquement avant d’envoyer.


#### Type de contenu par défaut
{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 %}
```
#### Type de contenu Application/JSON
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 :content_type application/json %}
```
{% endraw %}

### Fournir le corps JSON
Si vous souhaitez fournir votre propre corps JSON, vous pouvez l’écrire sous forme insérée s’il n’y a pas d’espace. Si votre corps dispose d’espaces, vous devez utiliser une déclaration d’assignation ou de capture. C’est-à-dire que l’un de ces trois éléments est acceptable :

{% raw %}
##### Inseré : espaces non autorisés
```js
{% connected_content https://example.com/api/endpoint :method post :body {"foo":"bar","baz":"{{1|plus:1}}"} :content_type application/json %}
```

##### Corps dans une déclaration de capture : espaces autorisés
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
##### Corps dans une déclaration d’affectation : espaces autorisés
```js
{% assign postbody = '{"foo":"bar", "baz": "2"}' %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```
{% endraw %}

## Codes de statut HTTP

Vous pouvez utiliser l’état HTTP à partir d’un appel de contenu connecté en l’enregistrant d’abord en tant que variable locale, puis en utilisant la clé `__http_status_code__`. Par exemple :

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :save result %}
{% if result.__http_status_code__ != 200 %}
  {% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert important %}
Cette clé ne sera ajoutée automatiquement à l’objet Contenu connecté que si l’endpoint renvoie un objet JSON. Si l’endpoint renvoie un tableau ou un autre type, cette clé ne peut alors pas être définie automatiquement dans la réponse.
{% endalert %}

## Mise en cache configurable {#configurable-caching}

### Limite de la taille du cache
Le corps de réponse du contenu connecté ne doit pas dépasser 1 Mo, ou il ne sera pas mis en cache.

### Temps de cache
Le contenu connecté mettra en cache la valeur qu’il renvoie à partir des endpoints GET pendant au moins 5 minutes. Si un temps de cache n’est pas spécifié, sa durée par défaut est de 5 minutes. 

Le temps de cache de contenu connecté peut être configuré pour être plus long avec `:cache_max_age`, comme illustré dans l’exemple suivant. Le temps de cache minimum est de 5 minutes et le temps de cache maximum est de 4 heures. Les données de contenu connecté sont mises en cache en mémoire à l’aide d’un système de cache volatil, tel que memcached. Par conséquent, indépendamment di temps de cache spécifié, les données du contenu connecté peuvent être supprimées depuis le cache en mémoire de Braze plus tôt que spécifié. Cela signifie que les durées de cache sont des suggestions et qu’elles ne représentent pas réellement la durée pendant laquelle les données sont garanties comme mises en cache par Braze et que vous pouvez voir plus de requêtes de contenu connecté que vous ne pensiez avec une durée de cache donnée.

Par défaut, le contenu connecté ne place pas en cache les appels POST. Vous pouvez modifier ce comportement en ajoutant `:cache_max_age` à l’appel POST de contenu connecté.

#### Cache pour les secondes spécifiées

Cet exemple met en cache pendant 900 secondes (ou 15 minutes).
{% raw %}
```
{% connected_content https://example.com/webservice.json :cache_max_age 900 %}
```
{% endraw %}


#### Arrêter le cache

Pour empêcher le contenu connecté de mettre en cache la valeur qu’il renvoie à partir d’une requête GET, vous pouvez utiliser la configuration `:no_cache`.

{% raw %}
```js
{% connected_content https://example.com/webservice.json :no_cache %}
```
{% endraw %}

{% alert important %}
Assurez-vous que l’endpoint de contenu connecté fourni peut gérer de grandes quantité de trafic avant d'utiliser cette option, ou vous verrez probablement une latence d'envoi accrue (des retards accrus ou des intervalles de temps plus longs entre la demande et la réponse) en raison du fait que Braze effectue des demandes de contenu connecté pour chaque message.
{% endalert %}

Avec un `POST` vous n’avez pas besoin d’arrêter la mise en cache, car Braze ne met jamais en cache les résultats des requêtes `POST`.

[16]: [success@braze.com](mailto:success@braze.com)
[17]: {% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"
[46]: http://www.json.org