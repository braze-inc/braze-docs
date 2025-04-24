---
nav_title: Erweiterte Filter
article_title: Erweiterte Flüssigkeitsfilter
page_order: 4
description: "In diesem Referenzartikel finden Sie eine Liste mit erweiterten Filtern, Beispielen und deren Verwendung in Ihrer Kampagne."

---

# Erweiterte Filter

> Dieser Referenzartikel bietet einen Überblick über die erweiterten Filter in Liquid und wie sie verwendet werden können.

## Kodierungsfilter

{% raw %}
| Filtername | Filterbeschreibung | Beispiel Eingabe | Beispiel Ausgabe |
\|---|---|---|---|
`md5` | Gibt eine md5 verschlüsselte Zeichenkette zurück | `{{'hey' | md5}}` | 6057f13c496ecf7fd777ceb9e79ae285 |
`sha1` | Gibt eine sha1 verschlüsselte Zeichenkette zurück | `{{'hey' | sha1}}` | 7f550a9f4c44173a37664d938f1355f0f92a47a7 |
`sha2` | Gibt eine SHA2-verschlüsselte Zeichenfolge (256 Bit, auch bekannt als SHA-256) zurück | `{{'hey' | sha2}}` | fa690b82061edfd2852629aeba8a8977b57e40fcb77d1a7a28b26cba62591204 |
`base64` | Gibt base64 kodierten String zurück | `{{'blah' | base64_encode}}` | YmxhaA== |
`hmac_sha1_hex` (vorher `hmac_sha1`) | Liefert eine hmac-sha1-Signatur, kodiert als Hex-String | `{{'hey' | hmac_sha1_hex: 'secret_key'}}` | 2a3969bed25bfeefb00aca4063eb9590b4df8f0e |
`hmac_sha1_base64` | Gibt die hmac-sha1-Signatur zurück, die als base64-Zeichenfolge verschlüsselt ist | `{{'hey' | hmac_sha1_base64: 'secret_key'}}` | KjlpvtJb/u+wCspAY+uVkLTfjw4= |
`hmac_sha256_hex` | Gibt die hmac-sha256-Signatur zurück, kodiert als Hex-String | `{{'hey' | hmac_sha256_hex: 'secret_key'}}` | 8df897f8da3d7992fe57c8dbc6f27578cfbf2dcc4d0fbb4000b8c924841d508e |
`hmac_sha256_base64` | Gibt hmac-sha256-Signatur zurück, kodiert als base64-String | `{{'hey' | hmac_sha256_base64: 'secret_key'}}` | jfiX+No9eZL+V8jbxvJ1eM+/LcxND7tAALjJJIQdUI4= |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## URL-Filter

| Filtername | Filterbeschreibung | Beispieleingabe | Beispiel-Ausgabe |
|---|---|---|---|
| `url_escape` | Erkennt alle Zeichen in einer Zeichenfolge, die in URLs nicht zulässig sind, und ersetzt die Zeichen durch ihre Escape-Varianten. | `{{'hey<>hi' | url_escape}}` | hey%3C%3Ehi |
| `url_param_escape` | Ersetzt alle Zeichen in einer Zeichenfolge, die in URLs nicht zulässig sind, durch ihre maskierten Varianten, einschließlich des kaufmännischen Und-Zeichens (&) | `{{'hey<&>hi' | url_param_escape}` | hey%3C%26%3Ehi |
| `url_encode` | Kodiert eine URL-freundliche Zeichenkette | `{{ 'google search' | url_encode }}` | Google+Suche |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endraw %}
{% alert tip %}
Der `assign` Tag kann mit HTML kombiniert werden, damit Sie bei der Erstellung mehrerer Hyperlinks Zeit und Mühe sparen.
{% raw %}
```
{% assign url = "https://www.examplelink.com" %}
<a href='{{url}}'>Shop the collection</a>
```
{% endraw %}
{% endalert %}
{% raw %}

## Filter für den Zugriff auf Eigenschaften

| Filtername | Filterbeschreibung |
|---|---|---|---|
| `property_accessor` | Nimmt einen Hash und einen Hash-Schlüssel und gibt den Wert in diesem Hash mit diesem Schlüssel zurück |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

**Beispiel-Hash:** `{"a" => 42, "b" => 0}`
**Beispielhafte Eingabe:** `{{hash | property_accessor: 'a'}}`
**Beispielhafte Ausgabe:** `42`

Darüber hinaus können Sie mit dem Filter für den Eigenschaftszugriff ein angepasstes Attribut als Template für einen Hash-Schlüssel verwenden, um auf einen bestimmten Hash-Wert zuzugreifen.

{% endraw %}

{% alert note %}
Es gibt keine Möglichkeit, einen Hash als Variable (z. B. als Ausdruck) in Liquid innerhalb von Braze zu instanziieren.
{% endalert %}

{% raw %}

## Filter für die Zahlenformatierung

| Filtername | Filterbeschreibung | Beispieleingabe | Beispiel-Ausgabe |
|---|---|---|---|
| `number_with_delimiter` | Formatiert eine Zahl mit Kommas | `{{ 123456 | number_with_delimiter }}` | 123,456 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## JSON-Escape/Zeichenfolgen-Escape-Filter

| Filtername | Filterbeschreibung |
|---|---|---|---|
| `json_escape` | Entfernt alle Sonderzeichen in einer Zeichenkette (z.B. doppelte Anführungszeichen `""` und Backslash ''). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Dieser Filter sollte immer verwendet werden, wenn Sie eine Zeichenkette in einem JSON-Dictionary personalisieren. Er ist insbesondere für Webhooks nützlich.
{% endraw %}


[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[37]:\#accounting-for-null-attribute-values
