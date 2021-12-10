---
nav_title: Filtres avancés
article_title: Filtres liquides avancés
page_order: 4
description: "Cet article de référence liste des filtres avancés, des exemples et comment ils peuvent être utilisés dans votre campagne."
---

# Filtres avancés

## Filtres d'encodage

{% raw %}
| nom du filtre | description du filtre | example input | exemple de sortie |
| ------------- | --------------------- | ------------- | ----------------- |
|               |                       |               |                   |


`md5` | Renvoie une chaîne encodée md5 | `{{'hey' | md5}}` | 6057f13c496ecf7fd777ceb9e79ae285 | `sha1` | Renvoie une chaîne encodée sha1 | `{{'hey' | sha1}}` | 7f550a9f4c44173a37664d938f1355f0f92a47a7 | `sha2` | Retourne sha2 (256-bit, également connu sous le nom de chaîne SHA-256) encodée | `{{'hey' | sha2}}` | fa690b82061edfd2852629aeba8a8977b57e40fcb77d1a7a28b26cba62591204 | `base64` | Retourne une chaîne encodée en base64 | `{{'blah' | base64_encode}}` | YmxhaA== | `hmac_sha1_hex` (précédemment `hmac_sha1`) | Retourne une signature hmac-sha1, encodée en tant que chaîne hexadécimale | `{{'hey' | hmac_sha1_hex: 'secret_key'}}` | 2a3969bed25bfeefb00aca4063eb9590b4df8f0e | `hmac_sha1_base64` | Retourne une signature hmac-sha1, encodée comme une chaîne de caractères base64 | `{{'hey' | hmac_sha1_base64: 'secret_key'}}` | KjlpvtJb/u+wCspAY+uVkLTfjw4= | `hmac_sha256_hex` | Retourne une signature hmac-sha256, encodée en tant que chaîne hexadécimale | `{{'hey' | hmac_sha256_hex: 'secret_key'}}` | 8df897f8da3d7992fe57c8dbc6f27578cfbf2dcc4d0fbb4000b8c924841d508e | `hmac_sha256_base64` | Retourne la signature hmac-sha256, encodée comme une chaîne de caractères base64 | `{{'hey' | hmac_sha256_base64: 'secret_key'}}` | jfiX+No9eZL+V8jbxvJ1eM+/LcxND7tAALjJJIQdUI4= |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Filtres d'URL

| nom du filtre           | description du filtre                                                                                                                                     | example input                                | exemple de sortie |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | ----------------- |
| `Echappe_URL`           | Identifie tous les caractères dans une chaîne qui ne sont pas autorisés dans les URLs, et remplace les caractères par leurs variantes échappées           | `{{'hey<>hi' | url_escape}}`           | hey%3C%3Ehi       |
| `Echapper un paramètre` | Remplace tous les caractères d'une chaîne de caractères qui ne sont pas autorisés dans les URL par leurs variantes échappées, y compris l'esperluette (&) | `{{'hey<&>hi' | url_param_escape}` | hey%3C%26%3Ehi    |
| `Encoder l'url`         | Encode une chaîne de caractères conviviale                                                                                                                | `{{ 'google search' | url_encode }}`         | google+search     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endraw %}
{% alert tip %}
La balise `assigner` peut être combinée avec du HTML pour vous faire gagner du temps et de l'effort lors de la création de plusieurs hyperliens.
{% raw %}
```
{% assigner url = "https://www.examplelink.com" %}
<a href='{{url}}'>Cliquez sur ce lien !</a>
```
{% endraw %}
{% endalert %}
{% raw %}

## Filtre d'accesseur de propriété

| nom du filtre                | description du filtre                                                                  |
| ---------------------------- | -------------------------------------------------------------------------------------- |
| `Propriétés de l'accessoire` | Prend un hachage et une clé de hachage et retourne la valeur de ce hachage à cette clé |
{: .reset-td-br-1 .reset-td-br-2}

Exemple de hachage : `{« a » => 42, « b » => 0}`

Example input: `{{hash | property_accessor: 'a'}}`

Exemple de sortie : `42`

De plus, le filtre d'accesseur de propriété vous permet de modéliser un attribut personnalisé dans une clé de hachage pour accéder à une valeur de hachage particulière.

{% endraw %}

{% alert note %}
Il n'y a aucun moyen d'instancier un hachage en tant que variable (i.e. l'expression) dans Liquid à l'intérieur du Brésil.
{% endalert %}

{% raw %}

## Filtres de mise en forme des nombres

| nom du filtre            | description du filtre                | example input                          | exemple de sortie |
| ------------------------ | ------------------------------------ | -------------------------------------- | ----------------- |
| `nombre avec délimiteur` | Formater un nombre avec des virgules | `{{ 123456 | number_with_delimiter }}` | 123,456           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Filtre d'échappement JSON / chaîne d'échappement

| nom du filtre           | description du filtre                                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------------------- |
| `format@@0 json_escape` | Échappe tous les caractères spéciaux dans une chaîne (c.-à-d. guillemet double `""` et antislash '\'). |
{: .reset-td-br-1 .reset-td-br-2}

Ce filtre doit toujours être utilisé lors de la personnalisation d'une chaîne dans un dictionnaire JSON et est utile pour les webhooks en particulier.
{% endraw %}
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
