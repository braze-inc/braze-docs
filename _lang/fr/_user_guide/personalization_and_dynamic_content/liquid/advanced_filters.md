---
nav_title: Filtres avancés
article_title: Filtres liquides avancés
page_order: 4
description: "Le présent article de référence répertorie les filtres avancés, les exemples et la manière dont ils peuvent être utilisés dans votre campagne."

---

# Filtres avancés

## Codage des filtres

{% raw %}
| nom du filtre | description du filtre | exemple d’entrée | exemple de sortie |
|---|---|---|---|
`md5` | Retourne une chaîne de caractères codée en md5 | `{{'hey' | md5}}` | 6057f13c496ecf7fd777ceb9e79ae285 |
`sha1` | Retourne la chaîne de caractères codée sha1 | `{{'hey' | sha1}}` | 7f550a9f4c44173a37664d938f1355f0f92a47a7 |
`sha2` | Retourne la chaîne de caractères codée sha2 (256 bits, également appelée SHA-256) | `{{'hey' | sha2}}` | fa690b82061edfd2852629aeba8a8977b57e40fcb77d1a7a28b26cba62591204 |
`base64` | Retourne la chaîne de caractères codée base64 | `{{’blah’ | base64_encode}}` | YmxhAa== |
`hmac_sha1_hex` (auparavant `hmac_sha1`) | Retourne la signature hmac-sha1, codée comme une chaîne de caractères hexagonale | `{{'hey' | hmac_sha1_hex: secret_clé’}}` | 2a3969bed25bfeefb00aca4063eb9590b4df8f0e |
`hmac_sha1_base64` | Retourne la signature hmac-sha1, codée comme une chaîne de caractères de base64 | `{{'hey' | hmac_sha1_base64: secret_clé’}}` | LpvtJb/u+wCspAY+uVkLTfjw4= |
`hmac_sha256_hex` | Retourne la signature hmac-sha256, codée comme une chaîne de caractères hexagonale | `{{'hey' | hmac_sha256_hex: secret_key’}}` | 8df897f8da3d7992fe57c8dbc6f27578cfbf2dcc4d0fbb4000b8c924841d508e |
`hmac_sha256_base64` | Retourne la signature hmac-sha256, codée comme une chaîne de caractères de base 64 | `{{'hey' | hmac_sha256_base64: secret_key’}}` | jFix+No9EzL+V8jbxvJ1Em+/LcxND7TaALJjJIQDuI4= |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Filtres URL

| nom du filtre | description du filtre | exemple d’entrée | exemple de sortie |
|---|---|---|---|
| `url_escape` | Identifie tous les caractères dans une chaîne de caractères qui ne sont pas autorisés dans les URL, et remplace les caractères par leurs variantes échues | `{{’hey<>bonjour' | URL_escape}}` | Bonjour %3C %3Ehi |
| `url_param_escape` | Remplace tous les caractères d'une chaîne de caractères qui ne sont pas autorisés dans les URL par leurs variantes échappées, y compris l'esperluette (&) | `{{’hey<&>bonjour' | URL_param._escape}` | hey%3C %26 %3Ehi |
| `url_encode` | Code une chaîne de caractères qui est conviviale | `{{ 'recherche google' | URL_encode }}` | google+recherche |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endraw %}
{% alert tip %}
Le `assign` tag peut être combiné avec HTML pour vous faire gagner du temps et des efforts lors de la création de plusieurs hyperliens.
{% raw %}
```
{% assign url = "https://www.examplelink.com" %}
<a href='{{url}}'>Shop the collection</a>
```
{% endraw %}
{% endalert %}
{% raw %}

## Filtre d’accès ou de propriété

| nom du filtre | description du filtre |
|---|---|---|---|
| `property_accessor` | Prend une touche dièse et renvoie la valeur dans ce hachage à cette clé |
{: .reset-td-br-1 .reset-td-br-2}

Exemple de hachage : `{“a” => 42, “b” => 0}`

Exemple d’entrée : `{{hash | property_accessor: ’a’}}`

Exemple de sortie : `42`

De plus, l’option de filtre de propriété vous permet de modéliser un attribut personnalisé dans une touche dièse pour accéder à une valeur de hachage particulière.

{% endraw %}

{% alert note %} 
Il n’y a aucune façon d’instancier un hachage comme variable (c.-à-d. expression) dans Liquid au sein de Braze. 
{% endalert %}

{% raw %}

## Filtres de formatage des nombres

| nom du filtre | description du filtre | exemple d’entrée | exemple de sortie |
|---|---|---|---|
| `number_with_delimiter` | Formater un nombre avec des virgules | `{{ 123456 | numéro_avec_délimiteur }}` | 123,456 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Filtre d'échappement/chaîne de caractères d'échappement JSON 

| nom du filtre | description du filtre |
|---|---|---|---|
| `json_escape` | S’échappe de caractères spéciaux dans une chaîne de caractères (c.-à-d., guillemets doubles) `""` et barre oblique arrière '\'). |
{: .reset-td-br-1 .reset-td-br-2}

Ce filtre doit toujours être utilisé lors de la personnalisation d’une chaîne de caractères dans un dictionnaire JSON et est utile pour les crochets Web en particulier.
{% endraw %}


[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[37]:#accounting-for-null-attribute-values
