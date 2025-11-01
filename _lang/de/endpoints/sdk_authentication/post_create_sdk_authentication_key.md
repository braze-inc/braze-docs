---
nav_title: "POST: SDK-Authentifizierungsschlüssel erstellen"
article_title: "POST: SDK-Authentifizierungsschlüssel erstellen"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum SDK-Authentifizierungsschlüssel Braze Endpunkt erstellen."
---

{% api %}
# SDK Authentifizierungsschlüssel erstellen
{% apimethod post %}
/app_group/sdk_authentication/create
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um einen neuen SDK-Authentifizierungsschlüssel für Ihre App zu erstellen.

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `sdk_authentication.create`.

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
  "rsa_public_key_str": "RSA public key string", 
  "description": "description", 
  "make_primary": false
}
```

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | -------- | --------- | ----------- |
| `app_id` | Erforderlich | String | Der Bezeichner der App APIs. |
| `rsa_public_key_str` | Erforderlich | String | Der String für den öffentlichen RSA-Schlüssel. Muss ein gültiger öffentlicher RSA-Schlüssel sein, sonst wird ein Fehler zurückgegeben. |
| `description` | Erforderlich | String | Beschreibung für den SDK-Authentifizierungsschlüssel. |
| `make_primary` | Optional | Boolesch | Wenn er auf `true` gesetzt ist, wird dieser Schlüssel zum primären SDK-Authentifizierungsschlüssel, wenn er erstellt wird. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

```json
curl --location --request POST 'https://rest.iad-01.braze.com/app_group/sdk_authentication/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "rsa_public_key_str": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvD+fgA0YuCUd/v35htn...\n-----END PUBLIC KEY-----", 
  "description": "SDK Authentication Key for iOS App", 
  "make_primary": false
}'
```

## Antwort
```json
{
  "id": "key id"
}
```

## Antwort-Parameter

| Parameter | Datentyp | Beschreibung |
| --------- | --------- | ----------- |
| `id` | String | Die ID des neu erstellten SDK Authentifizierungsschlüssels. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Validierungsregeln

Für diesen Endpunkt gelten die folgenden Validierungsregeln:

- Sie können bis zu 3 SDK Authentifizierungsschlüssel pro App haben.
- Der RSA Public Key String muss ein gültiger RSA Public Key im richtigen Format sein.
- Die `app_id` muss ein gültiger Bezeichner für die App API sein.
- Die Beschreibung darf nicht leer sein.

{% endapi %}
