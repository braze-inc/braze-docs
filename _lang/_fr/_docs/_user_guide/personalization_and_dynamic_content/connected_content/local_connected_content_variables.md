---
nav_title: Variables de contenu locales connectées
article_title: Variables de contenu locales connectées
page_order: 1
description: "Cet article de référence couvre la façon d'utiliser et de stocker les variables locales de contenu connecté."
---

# Variables de contenu local connecté

Braze effectue une requête GET standard au moment de l'envoi au point de terminaison spécifié dans la balise `connected_content`. Si le point de terminaison retourne du JSON, il est automatiquement analysé et stocké dans une variable appelée `connectée`.  Si le point de terminaison renvoie du texte, il sera directement inséré dans le message à la place de la balise `connected_content`.

> Si vous voulez enregistrer votre réponse à une variable, il est recommandé de retourner des objets JSON. Et si vous voulez que la réponse du contenu connecté remplace la balise par le texte, assurez-vous que la réponse n'est pas un JSON valide (comme défini par [json. rg][46])

Vous pouvez également spécifier `:save your_variable_name` après l'URL afin d'enregistrer les données comme autre chose. Par exemple, la balise `connected_content` suivante stockera la réponse à une variable locale appelée `localweather` (vous pouvez enregistrer plusieurs `connected_content` variables JSON) :

{% raw %}
```js
{% connected_content https://www.metaweather.com/api/location/2459115/ :save localweather %}
```
{% endraw %}

Metaweather est une API météo gratuite qui utilise un identifiant "Where-on-Earth ID" pour retourner la météo dans une zone. Utilisez ce code uniquement à des fins de test et d'apprentissage. Pour plus d'informations sur cette API, voir [ici](https://www.metaweather.com/api/ "Metaweather API Details").

> La variable stockée n'est accessible que dans le champ qui contient la requête `connected_content`. Par exemple, si vous voulez utiliser la variable `localweather` dans le champ message et titre, vous devriez faire la requête `connected_content` dans les deux champs. Si la requête est identique, Braze utilisera les résultats du cache, plutôt que de faire une deuxième requête au serveur de destination. Cependant, les appels de contenu connecté effectués via HTTP POST ne mettent pas en cache par défaut et feront une deuxième requête au serveur de destination. Si vous souhaitez ajouter la mise en cache aux appels POST, reportez-vous à l'option [`cache_max_age`](#configurable-caching) ci-dessous.

## JSON parsing

Le contenu connecté interprétera tous les résultats au format JSON dans une variable locale, lorsque vous spécifierez `:save`. Par exemple, un point de terminaison de contenu connecté lié à la météo retourne l'objet JSON suivant, que vous stockez dans une variable locale `localweather` en spécifiant `:save localweather`.
{% raw %}

```js
{
  "consolidated_weather": [
    {
      "id": 5. 143475362693e+15,
      "weather_state_name": "Clear",
      "weather_state_abbr": "c",
      "wind_direction_compass": "WSW",
      "created": "2017-06-12T14:14:46. 68110Z",
      "applicable_date": "2017-06-12",
      "min_temp": 22. 11666666667,
      "max_temp": 31.963333333333,
      "the_temp": 27. 03333333333,
      "wind_speed": 6.8884690250312,
      "wind_direction": 251. 2921994166,
      "air_pressure": 1021. 35,
      "humidité": 50,
      "visibilité": 14. 45530601288,
      "prévisibilité": 68
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

Vous pouvez tester si oui ou non il pleut en référençant `{{localweather.consolidated_weather[0].weather_state_name}}`, qui si elle est utilisée sur l'objet ci-dessus retournerait `Effacer`. Si vous voulez également personnaliser avec le nom de l'emplacement résultant, `{{localweather.title}}` renvoie `New York`.
{% endraw %}

L'image suivante illustre le type de coloration de syntaxe que vous devriez voir dans le tableau de bord si vous configurez les choses correctement. Cela démontre également comment vous pouvez tirer parti de la requête `connected_content` ci-dessus !

!\[Exemple de syntaxe de contenu connecté\]\[6\]

Si l'API répond avec {%raw%}`{{localweather.consolidated_weather[0].weather_state_name}}`{%endraw%} renvoyant `Pluie`, l'utilisateur recevra alors ce push.

!\[Exemple de Push de contenu connecté\]\[17\]

Par défaut, Le contenu connecté va définir un en-tête Content-Type sur une requête HTTP GET qu'il fait à `application/json` avec `Accept: */*`. Si vous avez besoin d'un autre type de contenu, spécifiez-le explicitement en ajoutant `:content_type votre/type de contenu` à la balise. Braze définira ensuite l'en-tête Content-Type et Accept sur le type que vous spécifiez.

{% raw %}
```js
{% connected_content http://numbersapi.com/random/trivia :content_type application/json %}
```
{% endraw %}

## Publication HTTP

Par défaut, le contenu connecté fait une requête HTTP GET à l'URL spécifiée. Pour faire une requête POST à la place, spécifiez `:method post`.

Vous pouvez éventuellement fournir un corps POST en spécifiant `:body` suivi d'une chaîne de requête au format `key1=value1&key2=value2&. .`. Content-Type par défaut à `application/x-www-form-urlencoded`. Si vous spécifiez `:content_type application/json` et fournissez un corps form-urlencodé tel que `key1=value1&key2=value2`, Braze encode automatiquement le corps du JSON avant l'envoi.

#### Type de contenu par défaut
{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 %}
```
#### Application/JSON Type de contenu
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 :content_type application/json %}
```
{% endraw %}

### Fournir le corps de json
Si vous voulez fournir votre propre corps JSON, vous pouvez l'écrire en ligne s'il n'y a pas d'espaces. Si votre corps a des espaces, vous devez utiliser une instruction d'assignation ou de capture. C'est-à-dire que chacun de ces trois éléments est acceptable:

{% raw %}
##### En ligne : Les espaces ne sont pas autorisés
```js
{% connected_content https://example.com/api/endpoint :method post :body {"foo":"bar","baz":"{{1|plus:1}}"} :content_type application/json %}
```

##### Corps dans une instruction de capture : espaces autorisés
```js
{% capture postbody %}
{"foo": "bar", "baz": "{{ 1 | plus: 1 }}"}
{% endcapture %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```

##### Corps dans une instruction d'assignation : espaces autorisés
```js
{% assigner postbody = '{"foo":"bar", "baz": "2"}' %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```
{% endraw %}

## Codes de statut HTTP

Vous pouvez utiliser le statut HTTP à partir d'un appel de contenu connecté en l'enregistrant d'abord comme variable locale, puis en utilisant la touche `__http_status_code__`. Par exemple :

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :save result %}
{% if result.__http_status_code__ != 200 %}
  {% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert important %}
Cette clé ne sera automatiquement ajoutée à l'objet Contenu connecté que si le point de terminaison renvoie un objet JSON. Si le point de terminaison retourne un tableau ou un autre type, alors cette clé ne peut pas être définie automatiquement dans la réponse.
{% endalert %}

## Mise en cache configurable {#configurable-caching}

Le contenu connecté mettra en cache la valeur qu'il retourne des points de terminaison GET pendant un minimum de 5 minutes. Si un temps de cache n'est pas spécifié, le temps de cache par défaut est de 5 minutes.

L'heure du cache de contenu connecté peut être configurée pour être plus longue avec `:cache_max_age`, comme indiqué ci-dessous. Le temps de cache minimum est de 5 minutes et le temps de cache maximum est de 4 heures. Les données de contenu connecté sont mises en cache en mémoire à l'aide d'un système de cache volatile, tel que memcached. Par conséquent, indépendamment du temps de cache spécifié, les données de contenu connecté peuvent être expulsées du cache en mémoire de Braze plus tôt que prévu. Cela signifie que les durées de cache sont des suggestions et peuvent ne pas représenter la durée de mise en cache garantie par Braze et que vous pouvez voir plus de requêtes de contenu connecté que vous ne pouvez vous attendre avec une durée de cache donnée.

Par défaut, le contenu connecté ne met pas en cache les appels POST. Vous pouvez modifier ce comportement en ajoutant `:cache_max_age` à l'appel POST de contenu connecté.

#### Cache pour les secondes spécifiées

Cet exemple mettra en cache pendant 900 secondes (ou 15 minutes).
{% raw %}
```
{% connected_content https://example.com/webservice.json :cache_max_age 900 %}
```
{% endraw %}


#### Détruire le cache

Pour empêcher le Contenu Connecté de mettre en cache la valeur qu'il renvoie d'une requête GET, vous pouvez utiliser la configuration `:no_cache` , comme indiqué ci-dessous.

{% raw %}
```js
{% connected_content https://example.com/webservice.json :no_cache %}
```
{% endraw %}

{% alert important %}
Assurez-vous que le point de terminaison de contenu connecté peut gérer de gros débordements de trafic avant d'utiliser cette option, ou vous verrez probablement une augmentation de la latence d'envoi (des délais accrus ou des intervalles de temps plus larges entre la demande et la réponse) en raison de Braze faisant des requêtes de contenu connecté pour chaque message.
{% endalert %}

Avec un `POST` vous n'avez pas besoin de mettre en cache, car Braze ne met jamais en cache les résultats des requêtes `POST`.
[6]: {% image_buster /assets/img_archive/Connected_Content_Syntax.png %} "Exemple d'utilisation de la syntaxe de contenu connecté" [17]: {% image_buster /assets/img_archive/connected_weather_push2.png %} "Exemple d'utilisation de l'Usage de contenu connecté"

[46]: http://www.json.org
