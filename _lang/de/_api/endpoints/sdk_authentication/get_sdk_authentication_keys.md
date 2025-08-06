---
nav_title: "GET: SDK-Authentifizierungsschlüssel auflisten"
article_title: "GET: SDK-Authentifizierungsschlüssel auflisten"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des SDK-Endpunkts List SDK Authentication keys Braze."
---

{% api %}
# SDK-Authentifizierungsschlüssel auflisten
{% apimethod get %}
/app_group/sdk_authentication/keys
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um alle SDK-Authentifizierungsschlüssel für Ihre App abzurufen.

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `sdk_authentication.keys`.

## Rate-Limits

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | -------- | --------- | ----------- |
| `app_id` | Erforderlich | String | Der Bezeichner der App APIs. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

```json
curl --location --request GET 'https://rest.iad-01.braze.com/app_group/sdk_authentication/keys?app_id=01234567-89ab-cdef-0123-456789abcdef' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
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
| `keys` | Array | Array von SDK Authentifizierungsschlüssel-Objekten. |
| `keys[].id` | String | Die ID des SDK Authentifizierungsschlüssels. |
| `keys[].rsa_public_key` | String | Der String für den öffentlichen RSA-Schlüssel. |
| `keys[].description` | String | Beschreibung des SDK-Authentifizierungsschlüssels. |
| `keys[].is_primary` | Boolesch | Ob dieser Schlüssel der primäre SDK Authentifizierungsschlüssel ist. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Validierungsregeln

Für diesen Endpunkt gelten die folgenden Validierungsregeln:

- Der Parameter `app_id` muss ein gültiger Bezeichner für eine App API sein.
- Die App muss in Ihrem Workspace vorhanden sein.

{% endapi %}
