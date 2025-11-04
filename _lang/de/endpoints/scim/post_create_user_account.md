---
nav_title: "POST: Neues Dashboard-Benutzerkonto erstellen"
article_title: "POST: Neues Dashboard-Benutzerkonto erstellen"
alias: /post_create_user_account/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Endpunkt Neues Dashboard Nutzer:innen-Konto erstellen Braze."

---

{% api %}
# Neues Dashboard-Benutzerkonto erstellen
{% apimethod post %}
/scim/v2/Benutzer:innen
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um ein neues Dashboard-Benutzerkonto zu erstellen, indem Sie E-Mail, Vor- und Nachnamen sowie Berechtigungen (für die Festlegung von Berechtigungen auf Unternehmens-, Workspace- und Teamebene) angeben.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#768a3c9d-ce1d-44fc-a0e4-d556b09f7aa3 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie ein SCIM-Token. Sie verwenden die Herkunft Ihres Dienstes in der Kopfzeile `X-Request-Origin`. Weitere Informationen finden Sie unter [Automatisierte Bereitstellung von Nutzer:innen]({{site.baseurl}}/scim/automated_user_provisioning/).

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='create dashboard user' %}

## Anfragetext
```
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-KEY
```
```
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "userName": "user@test.com",
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
            {
                "roleName": "Test Role"
            },
            {
                "roleId": "2519dafcdba238ae7"
            }
        ],
        "appGroup": [
            {
                "appGroupName": "Test Workspace",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamName": "Test Team",                  
                         "teamPermissions": ["basic_access","export_user_data"]
                    }
                ]
            },
            {
                "appGroupName": "Other Test Workspace",
                "appGroupPermissionSets": [
                    {
                        "appGroupPermissionSetName":  "Test Permission Set"
                    }
                ]
            }
        ]
    }
}
```

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | -------- | --------- | ----------- |
| `schemas` | Erforderlich | String-Array | Erwarteter SCIM 2.0 Schemaname für das Nutzer:in Objekt. |
| `userName` | Erforderlich | String | Die E-Mail Adresse des Nutzers:innen. |
| `name` | Erforderlich | JSON-Objekt | Dieses Objekt enthält den Vornamen und den Nachnamen des Nutzers:innen. |
| `department` | Erforderlich | String | Gültiger String für die Abteilung aus der [Dokumentation für die Abteilung]({{site.baseurl}}/scim_api_appendix/#department-strings). |
| `permissions` | Optional | JSON-Objekt | Berechtigungsobjekt wie in der [Dokumentation zum Berechtigungsobjekt]({{site.baseurl}}/scim_api_appendix/#permissions-object) beschrieben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```json
curl --location --request POST 'https://rest.iad-01.braze.com/scim/v2/Users' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM–TOKEN-HERE' \
--data raw '{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "userName": "user@test.com",
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
            {
                "roleName": "Test Role"
            },
            {
                "roleId": "2519dafcdba238ae7"
            }
        ],
        "appGroup": [
            {
                "appGroupName": "Test Workspace",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamName": "Test Team",                  
                         "teamPermissions": ["basic_access","export_user_data"]
                    }
                ]
            } 
        ]
    }
}'
```

## Antwort
```json
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "id": "dfa245b7-24195aec-887bb3ad-602b3340",
    "userName": "user@test.com",
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "lastSignInAt": "Thursday, January 1, 1970 12:00:00 AM",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
            {
                "roleName": "Test Role",
                "roleId": "519dafcdba23dfaae7,
                "appGroup": [
                    {
                        "appGroupId": "241adcd25789fabcded",
                        "appGroupName": "Some Workspace",
                        "appGroupPermissions": ["basic_access", "publish_cards"],
                        "team": [
                            {
                                "teamId": "2519dafcdba238ae7",
                                "teamName": "Some Team",                  
                                "teamPermissions": ["export_user_data"]
                            }
                        ]
                    } 
                ]
            },
            {
                "roleName": "Another Test Role",
                "roleId": "23125dad23dfaae7,
                "appGroup": [
                    {
                        "appGroupId": "241adcd25adfabcded",
                        "appGroupName": "Production Workspace",
                        "appGroupPermissionSets": [
                            {
                                "appGroupPermissionSetName": "A Permission Set",
                                "appGroupPermissionSetId": "dfa385109bc38",
                                "permissions": ["basic_access","publish_cards"]
                            }
                        ]
                    } 
                ]
            }
        ],
        "appGroup": [
            {
                "appGroupId": "241adcd25789fabcded",
                "appGroupName": "Test Workspace",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamId": "2519dafcdba238ae7",
                         "teamName": "Test Team",                  
                         "teamPermissions": ["basic_access","export_user_data"]
                    }
                ]
            },
            {
                "appGroupName": "Other Test Workspace",
                "appGroupPermissionSets": [
                    {
                        "appGroupPermissionSetName":  "Test Permission Set"
                    }
                ]
            } 
        ]
    }
}
```

## Antwort-Parameter

| Parameter | Datentyp | Beschreibung |
| --------- | --------- | ----------- |
| `schemas` | String-Array | Erwarteter SCIM 2.0 Schemaname für das Nutzer:in Objekt. |
| `userName` | String | Die E-Mail Adresse des Nutzers:innen. |
| `name` | JSON-Objekt | Dieses Objekt enthält den Vor- und Nachnamen des Nutzers:innen. |
| `department` | String | Gültiger String für die Abteilung aus der [Dokumentation für die Abteilung]({{site.baseurl}}/scim_api_appendix/#department-strings). |
| `permissions` | JSON-Objekt | Berechtigungsobjekt wie in der [Dokumentation zum Berechtigungsobjekt]({{site.baseurl}}/scim_api_appendix/#permissions-object) beschrieben. |
| `id` | String | Von Braze generierte ID, die für die Suche und Verwaltung von Nutzer:innen-Konten verwendet wird. |
| `lastSignInAt` | String | Datum der letzten erfolgreichen Anmeldung in UTC-Zeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Fehlerzustände

Wenn ein Nutzer:in mit dieser `userName` oder E-Mail Adresse bereits in Braze existiert, antwortet der Endpunkt mit:

```json
HTTP/1.1 409 Conflict
Date: Tue, 10 Sep 2019 02:22:30 GMT
Content-Type: text/json;charset=UTF-8

{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
  "detail": "User already exists in the database.",
  "status": 409
}
```

{% endapi %}
