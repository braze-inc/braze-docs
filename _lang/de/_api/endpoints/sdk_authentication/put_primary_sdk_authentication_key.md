---
nav_title: "PUT: Primären SDK-Authentifizierungsschlüssel festlegen"
article_title: "PUT: Primären SDK-Authentifizierungsschlüssel festlegen"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des SDK-Endpunkts Set primary SDK Authentication key Braze."
---

{% api %}
# Primären SDK-Authentifizierungsschlüssel festlegen
{% apimethod put %}
/app_group/sdk_authentication/primary
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um einen SDK-Authentifizierungsschlüssel als Primärschlüssel für Ihre App festzulegen.

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `sdk_authentication.primary`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```
```json
{
  "app_id": "App API identifier",
  "key_id": "key id"
}
```

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | -------- | --------- | ----------- |
| `app_id` | Erforderlich | String | Der Bezeichner der App APIs. |
| `key_id` | Erforderlich | String | Die ID des SDK Authentifizierungsschlüssels, der als primär markiert werden soll. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```json
curl --location --request PUT 'https://rest.iad-01.braze.com/app_group/sdk_authentication/primary' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "key_id": "abcdef12-3456-7890-abcd-ef1234567890"
}'
```

## Antwort
```json
{
  "keys": [
    {
      "id": "abcdef12-3456-7890-abcd-ef1234567890",
      "rsa_public_key": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvD+fgA0YuCUd/v35htn...\n-----END PUBLIC KEY-----",
      "description": "SDK Authentication Key for iOS App",
      "is_primary": true
    },
    {
      "id": "fedcba98-7654-3210-fedc-ba9876543210",
      "rsa_public_key": "-----BEGIN PUBLIC KEY-----\nqWGfHOAiIwVzC/bTxwQZQQVzm/3ktgdNXRUDm5aIwVzCtxbNm5aIxOAiIwVzVHOA...\n-----END PUBLIC KEY-----",
      "description": "SDK Authentication Key for Android App",
      "is_primary": false
    }
  ]
}
```

## Antwort-Parameter

| Parameter | Datentyp | Beschreibung |
| --------- | --------- | ----------- |
| `keys` | Array | Array mit allen SDK Authentifizierungsschlüssel-Objekten. |
| `keys[].id` | String | Die ID des SDK Authentifizierungsschlüssels. |
| `keys[].rsa_public_key` | String | Der String für den öffentlichen RSA-Schlüssel. |
| `keys[].description` | String | Beschreibung des SDK-Authentifizierungsschlüssels. |
| `keys[].is_primary` | Boolesch | Ob dieser Schlüssel der primäre SDK Authentifizierungsschlüssel ist. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Validierungsregeln

Für diesen Endpunkt gelten die folgenden Validierungsregeln:

- Die `key_id` muss eine gültige SDK Authentication Key ID sein.
- Die `app_id` muss ein gültiger Bezeichner für die App API sein.
- Der SDK-Authentifizierungsschlüssel muss für die angegebene App existieren.

{% endapi %}
