---
nav_title: Filtros avanzados
article_title: Filtros de líquidos avanzados
page_order: 4
description: "Este artículo de referencia enumera filtros avanzados, ejemplos y cómo pueden utilizarse en tu campaña."

---

# Filtros avanzados

> Este artículo de referencia ofrece un resumen de los filtros avanzados en Liquid y cómo pueden utilizarse.

## Filtros de codificación

{% raw %}
| nombre del filtro | descripción del filtro | ejemplo de entrada | ejemplo de salida |
\|---|---|---|---|
`md5` | Devuelve cadena codificada md5 | `{{'hey' | md5}}` | 6057f13c496ecf7fd777ceb9e79ae285 |
`sha1` | Devuelve cadena codificada sha1 | `{{'hey' | sha1}}` | 7f550a9f4c44173a37664d938f1355f0f92a47a7 |
`sha2` | Devuelve la cadena codificada sha2 (256 bits, también conocida como SHA-256) | `{{'hey' | sha2}}` | fa690b82061edfd2852629aeba8a8977b57e40fcb77d1a7a28b26cba62591204 |
`base64` | Devuelve cadena codificada en base64 | `{{'blah' | base64_encode}}` | YmxhaA== |
`hmac_sha1_hex` (antes `hmac_sha1`) | Devuelve la firma hmac-sha1, codificada como una cadena hexadecimal | `{{'hey' | hmac_sha1_hex: 'secret_key'}}` | 2a3969bed25bfeefb00aca4063eb9590b4df8f0e |
`hmac_sha1_base64` | Devuelve la firma hmac-sha1, codificada como una cadena base64 | `{{'hey' | hmac_sha1_base64: 'secret_key'}}` | KjlpvtJb/u+wCspAY+uVkLTfjw4= |
`hmac_sha256_hex` | Devuelve la firma hmac-sha256, codificada como una cadena hexadecimal | `{{'hey' | hmac_sha256_hex: 'secret_key'}}` | 8df897f8da3d7992fe57c8dbc6f27578cfbf2dcc4d0fbb4000b8c924841d508e |
`hmac_sha256_base64` | Devuelve la firma hmac-sha256, codificada como una cadena base64 | `{{'hey' | hmac_sha256_base64: 'secret_key'}}` | jfiX+No9eZL+V8jbxvJ1eM+/LcxND7tAALjJIQdUI4= |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Filtros de URL

| nombre del filtro | descripción del filtro | ejemplo de entrada | ejemplo de salida |
|---|---|---|---|
| `url_escape` | Identifica todos los caracteres de una cadena que no están permitidos en las URLS y los sustituye por sus variantes escapadas. | `{{'hey<>hi' | url_escape}}` | hey%3C%3Ehi |
| `url_param_escape` | Sustituye todos los caracteres de una cadena no permitidos en las URL por sus variantes escapadas, incluido el ampersand (&). | `{{'hey<&>hi' | url_param_escape}` | hey%3C%26%3Ehi |
| `url_encode` | Codifica una cadena que sea compatible con la URL | `{{ 'google search' | url_encode }}` | google+search |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endraw %}
{% alert tip %}
La etiqueta `assign` puede combinarse con HTML para ahorrarle tiempo y esfuerzo a la hora de crear varios hipervínculos.
{% raw %}
```
{% assign url = "https://www.examplelink.com" %}
<a href='{{url}}'>Shop the collection</a>
```
{% endraw %}
{% endalert %}
{% raw %}

## Filtro accesorio de propiedad

| nombre del filtro | descripción del filtro |
|---|---|---|---|
| `property_accessor` | Toma un hash y una clave hash y devuelve el valor de ese hash en esa clave |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

**Ejemplo de hash:** `{"a" => 42, "b" => 0}`
**Ejemplo de entrada:** `{{hash | property_accessor: 'a'}}`
**Ejemplo de salida:** `42`

Además, el filtro de accesos a propiedades permite modelar un atributo personalizado en una clave hash para acceder a un valor hash concreto.

{% endraw %}

{% alert note %}
No hay forma de instanciar un hash como variable (como una expresión) en Liquid dentro de Braze.
{% endalert %}

{% raw %}

## Filtros de formato numérico

| nombre del filtro | descripción del filtro | ejemplo de entrada | ejemplo de salida |
|---|---|---|---|
| `number_with_delimiter` | Formatea un número con comas | `{{ 123456 | number_with_delimiter }}` | 123,456 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Filtro de escape JSON / escape de cadena

| nombre del filtro | descripción del filtro |
|---|---|---|---|
| `json_escape` | Escapa los caracteres especiales de una cadena (como las comillas dobles `""` y la barra invertida ''). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Este filtro debe utilizarse siempre que se personalice una cadena en un diccionario JSON y es útil para los webhooks en particular.
{% endraw %}


[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[37]:\#accounting-for-null-attribute-values
