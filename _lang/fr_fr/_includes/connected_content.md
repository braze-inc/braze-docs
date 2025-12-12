{% if include.section == "default behavior" %}

Par défaut, le contenu connecté définit un `Content-Type` en-tête d’une demande GET HTTP que cela rend `application/json` avec `Accept: */*`. Si vous avez besoin d’un autre type de contenu, spécifiez-le explicitement en ajoutant `:content_type your/content-type` à la balise. Braze définira alors l’en-tête Type de contenu et Accepter au type que vous spécifiez.

{% raw %}
```js
{% connected_content http://numbersapi.com/random/trivia :content_type application/json %}
```
{% endraw %}

{% endif %}

{% if include.section == "http post" %}

Par défaut, le contenu connecté fait une demande HTTP GET à l’URL spécifiée. Pour effectuer une demande POST, précisez `:method post`.

Vous pouvez éventuellement fournir un corps POST en spécifiant `:body` suivi d’une chaîne de caractères de requête du format `key1=value1&key2=value2&...` ou une référence à des valeurs capturées. Type de contenu par défaut `application/x-www-form-urlencoded`. Si vous spécifiez `:content_type application/json` et fournir un corps sous forme de code-urétroté, comme `key1=value1&key2=value2`, Braze jSON automatiquement le code de l’organisme avant d’envoyer.

Par défaut, le contenu connecté ne met pas non plus en cache les appels POST. Vous pouvez modifier ce comportement en ajoutant `:cache_max_age` à l'appel POST du contenu connecté.

{% tabs %}
{% tab Content-Type par défaut %}

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