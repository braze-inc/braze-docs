---
nav_title: "GET: Bestehendes Dashboard-Benutzerkonto per E-Mail durchsuchen"
article_title: "GET: Bestehendes Dashboard-Benutzerkonto per E-Mail durchsuchen"
alias: /get_search_existing_dashboard_user_email/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Suche nach einem bestehenden Dashboard Nutzer:in-Konto per E-Mail Braze Endpunkt."
---

{% api %}
# Bestehendes Dashboard-Benutzerkonto per E-Mail durchsuchen
{% apimethod get %}
scim/v2/Benutzer?filter=Benutzername%20eq%20 "Nutzer:innen%40test.com"
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um ein bestehendes Dashboard-Benutzerkonto zu suchen, indem Sie dessen E-Mail im Filter-Abfrageparameter angeben. 

Beachten Sie, dass der Abfrageparameter, wenn er URL-kodiert ist, wie folgt aussieht:

`/scim/v2/Users?filter=userName%20eq%20%22user@test.com%22`

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5037d810-b822-4c54-bb51-f30470a42a95 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie ein SCIM-Token. Sie verwenden die Herkunft Ihres Dienstes in der Kopfzeile `X-Request-Origin`. Weitere Informationen finden Sie unter [Automatisierte Bereitstellung von Nutzer:innen]({{site.baseurl}}/scim/automated_user_provisioning/).

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='look up dashboard user email' %}

## Pfad-Parameter

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `userName@example.com` | Erforderlich | String | Die E-Mail des Nutzers:innen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parameter der Anfrage

```json
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
```

## Beispiel Anfrage
```json
curl --location --request GET \ 'https://rest.iad-01.braze.com/scim/v2/Users?filter=userName%20eq%20%22user@test.com%22' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
```

## Antwort
```json
{
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:ListResponse"],
    "totalResults": 1,
    "Resources": [
        {
            "userName": "user@test.com",
            "id": "dfa245b7-24195aec-887bb3ad-602b3340",
            "name": {
                "givenName": "Test",
                "familyName": "User"
            },
            "department": "finance",
            "lastSignInAt": "Thursday, January 1, 1970 12:00:00 AM",
            "permissions": {
                "companyPermissions": ["manage_company_settings"],
                "appGroup": [
                    {
                        "appGroupId": "241adcd25789fabcded",
                        "appGroupName": "Test Workspace",
                        "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                        "team": [
                            {
                                "teamId": "241adcd25789fabcded",
                                "teamName": "Test Team",                  
                                "teamPermissions": ["admin"]
                            }
                        ]
                    } 
                ]
            }
        }
    ]
}
```

{% endapi %}

