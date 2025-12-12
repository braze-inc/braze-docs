---
nav_title: "LÖSCHEN: Dashboard-Benutzerkonto entfernen"
article_title: "LÖSCHEN: Dashboard-Benutzerkonto entfernen"
alias: /delete_existing_dashboard_user/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Endpunkt Nutzer:innen des Dashboard-Kontos Braze entfernen."
---

{% api %}
# Dashboard-Benutzerkonto entfernen
{% apimethod delete %}
/scim/v2/Benutzer:innen/{id}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um einen bestehenden Nutzer:in des Dashboards dauerhaft zu löschen, indem Sie die Ressource `id` angeben, die von der SCIM [`POST`]({{site.baseurl}}/api/endpoints/scim/post_create_user_account/) Methode zurückgegeben wird. 

Dies ist vergleichbar mit dem Löschen eines Nutzers:innen im Bereich **Unternehmensnutzer** des Braze-Dashboards.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9c7c71ea-afd6-414a-99d1-4eb1fe274f16 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie ein SCIM-Token. Sie verwenden die Herkunft Ihres Dienstes in der Kopfzeile `X-Request-Origin`. Weitere Informationen finden Sie unter [Automatisierte Bereitstellung von Nutzer:innen]({{site.baseurl}}/scim/automated_user_provisioning/).

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='delete dashboard user' %}

## Pfad-Parameter

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `id` | Erforderlich | String | Die ID des Nutzers:innen. Dieser Parameter wird von den Methoden `POST` `/scim/v2/Users/` oder `GET`  `/scim/v2/Users?filter=userName eq "user@test.com"` zurückgegeben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Körper der Anfrage

```json
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
```

## Beispiel Anfrage
```json
curl --location --request DELETE 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## Antwort

### Beispiel einer Fehlerantwort

```json
HTTP/1.1 204 Not Found
Content-Type: text/html; charset=UTF-8
```

Wenn ein Entwickler:in mit dieser ID nicht in Braze existiert, antwortet der Endpunkt mit:
```json
HTTP/1.1 404 Not Found
Content-Type: text/html; charset=UTF-8

{
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
    "detail": "User not found",
    "status": 404
}
```
{% endapi %}
