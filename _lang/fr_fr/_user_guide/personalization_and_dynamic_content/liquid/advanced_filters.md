---
nav_title: Filtres avancés
article_title: Filtres à liquides avancés
page_order: 4
description: "Cet article de référence répertorie les filtres avancés, des exemples et la manière dont ils peuvent être utilisés dans votre campagne."

---

# Filtres avancés

> Cet article de référence donne un aperçu des filtres avancés dans Liquid et de la manière dont ils peuvent être utilisés.

## Filtres d'encodage

{% raw %}
| Le nom du filtre, la description du filtre, l'exemple d'entrée, l'exemple de sortie, la description du filtre.
\|---|---|---|---|
`md5` | Retourne une chaîne de caractères encodée en md5 | `{{'hey' | md5}}` | 6057f13c496ecf7fd777ceb9e79ae285 |
`sha1` | Retourne une chaîne de caractères codée en sha1 | `{{'hey' | sha1}}` | 7f550a9f4c44173a37664d938f1355f0f92a47a7 |
`sha2` | Renvoie une chaîne de caractères codée en sha2 (256 bits, également connue sous le nom de SHA-256) | `{{'hey' | sha2}}` | fa690b82061edfd2852629aeba8a8977b57e40fcb77d1a7a28b26cba62591204 | | fa690b82061edfd2852629aeba8a8977b57e40fcb77d1a7a28b26cba62591204 | 
`base64` | Retourne une chaîne de caractères encodée en base64 | `{{'blah' | base64_encode}}` | YmxhaA== |
`hmac_sha1_hex` (précédemment `hmac_sha1`) | Renvoie la signature hmac-sha1, encodée sous forme de chaîne de caractères hexagonale | `{{'hey' | hmac_sha1_hex: 'secret_key'}}` | 2a3969bed25bfeefb00aca4063eb9590b4df8f0e |
`hmac_sha1_base64` | Retourne la signature hmac-sha1, encodée sous forme de chaîne de caractères base64 | `{{'hey' | hmac_sha1_base64: 'secret_key'}}` | KjlpvtJb/u+wCspAY+uVkLTfjw4= |
`hmac_sha256_hex` | Retourne la signature hmac-sha256, encodée sous forme de chaîne de caractères hexagonale | `{{'hey' | hmac_sha256_hex: 'secret_key'}}` | 8df897f8da3d7992fe57c8dbc6f27578cfbf2dcc4d0fbb4000b8c924841d508e | | 8df897f8da3d7992fe57c8dbc6f27578cfbf2dcc4d0fbb4000b8c924841d508e | | 
`hmac_sha256_base64` | Retourne la signature hmac-sha256, encodée sous forme de chaîne de caractères base64 | `{{'hey' | hmac_sha256_base64: 'secret_key'}}` | jfiX+No9eZL+V8jbxvJ1eM+/LcxND7tAALjJJIQdUI4= |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Filtres URL

| nom du filtre | description du filtre | exemple de saisie | exemple de sortie |
|---|---|---|---|
| `url_escape` | Identifie tous les caractères d'une chaîne de caractères qui ne sont pas autorisés dans les URLS et remplace les caractères par leurs variantes échappées. | `{{'hey<>hi' | url_escape}}` | hey%3C%3Ehi |
| `url_param_escape` | Remplace tous les caractères d'une chaîne qui ne sont pas autorisés dans les URL par leurs variantes échappées, y compris l'esperluette. (&) | `{{'hey<&>hi' | url_param_escape}` | hey%3C%26%3Ehi |
| `url_encode` | Encode une chaîne de caractères adaptée à l'URL | `{{ 'google search' | url_encode }}` | google+search |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endraw %}
{% alert tip %}
L'étiquette `assign` peut être combinée avec le langage HTML pour vous permettre d'enregistrer des liens hypertextes multiples.
{% raw %}
```
{% assign url = "https://www.examplelink.com" %}
<a href='{{url}}'>Shop the collection</a>
```
{% endraw %}
{% endalert %}
{% raw %}

## Filtre d'accès à la propriété

| nom du filtre | description du filtre |
|---|---|---|---|
| `property_accessor` | Prend un hachage et une clé de hachage et renvoie la valeur de ce hachage à cette clé. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

**Exemple de hachage :** `{"a" => 42, "b" => 0}`
**Exemple d'entrée :** `{{hash | property_accessor: 'a'}}`
**Exemple de sortie :** `42`

En outre, le filtre d'accès aux propriétés vous permet d'insérer un attribut personnalisé dans une clé de hachage afin d'accéder à une valeur de hachage particulière.

{% endraw %}

{% alert note %}
Il n'existe aucun moyen d'instancier un hachage en tant que variable (telle qu'une expression) dans Liquid au sein de Braze.
{% endalert %}

{% raw %}

## Filtres de formatage des nombres

| nom du filtre | description du filtre | exemple de saisie | exemple de sortie |
|---|---|---|---|
| `number_with_delimiter` | Formate un nombre avec des virgules | `{{ 123456 | number_with_delimiter }}` | 123,456 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Filtre d'échappement JSON / chaîne de caractères

| nom du filtre | description du filtre |
|---|---|
| `json_escape` | Échappe tous les caractères spéciaux d'une chaîne de caractères (tels que les guillemets doubles `""` et la barre oblique inverse ''). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ce filtre devrait toujours être utilisé lors de la personnalisation d'une chaîne de caractères dans un dictionnaire JSON et est utile pour les webhooks en particulier.

## Filtres de formatage JSON

| nom du filtre | description du filtre |
|---|---|
| `json_parse` | Convertit une chaîne JSON en une structure de données correspondante, telle qu'un objet ou un tableau. | 
| `as_json_string` | Convertit une structure de données, telle qu'un objet ou un tableau, en une chaîne JSON correspondante. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

{% details json_parse example input and output %}

### Entrée 

{% raw %}
```liquid
{% assign my_data_string = '[{"id":"1","store_name":"demo-store"}]'  %}
{% assign my_data = my_data_string | json_parse %}
```

### Sortie

```liquid
{% for item in my_data %}
Item ID: {{ item.id }}
Item Name: {{ item.store_name }}
{% endfor %}
```
{% endraw %}

{% enddetails %}

{% details as_json_string example input and output %}

### Entrée

{% raw %}
```liquid
{% assign my_data_string = '[{"id":"1","store_name":"demo-store"}]'  %}
{% assign my_data = my_data_string | json_parse %}
{% assign json_string = my_data | as_json_string %}
```

### Sortie

```liquid
{{json_string}}
```
{% endraw %}
{% enddetails %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[37]:#accounting-for-null-attribute-values
