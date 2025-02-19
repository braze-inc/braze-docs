---
nav_title: "PUT: Dashboard-Benutzerkonto aktualisieren"
article_title: "PUT: Dashboard-Benutzerkonto aktualisieren"
alias: /post_update_existing_user_account/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts Vorhandenes Dashboard-Benutzerkonto aktualisieren."
---

{% api %}
# Dashboard-Benutzerkonto aktualisieren
{% apimethod put %}
/scim/v2/Users/{id}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um ein bestehendes Dashboard-Benutzerkonto zu aktualisieren, indem Sie die Ressource `id` angeben, die von der SCIM [`POST`]({{site.baseurl}}/scim/post_create_user_account/) Methode zurückgegeben wird.

Es ermöglicht Ihnen die Aktualisierung von Vor- und Nachnamen, Berechtigungen (zum Festlegen von Berechtigungen auf Unternehmens-, Arbeitsbereichs- und Teamebene) und Abteilung.

Aus Sicherheitsgründen kann `userName` (E-Mail Adresse) nicht über diesen Endpunkt aktualisiert werden. Wenn Sie die `userName` (E-Mail-Adresse) für einen Benutzer ändern möchten, wenden Sie sich an den [Support]({{site.baseurl}}/support_contact/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f9a1642-988e-4011-8fb8-db4340ea1ac7 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie ein SCIM-Token. Sie verwenden den Ursprung Ihres Dienstes als `X-Request-Origin` Kopfzeile. Weitere Informationen finden Sie unter [Automatisierte Benutzerbereitstellung]({{site.baseurl}}/scim/automated_user_provisioning/).

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='update dashboard user' %}

## Pfad-Parameter

| Parameter | Erforderlich | Daten Typ | Beschreibung |
|---|---|---|---|
| `id` | Erforderlich | String | Die Ressourcen-ID des Benutzers. Dieser Parameter wird von den Methoden `POST` `/scim/v2/Users/` oder `GET`  `/scim/v2/Users?filter=userName eq "user@test.com"` zurückgegeben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Körper der Anfrage
```
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-KEY
```
```json
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "name": {"name": {
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
                         "teamPermissions": ["admin"]
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

## Parameter anfordern

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | -------- | --------- | ----------- |
| `schemas` | Erforderlich | Array von Zeichenketten | Erwarteter SCIM 2.0 Schemaname für Benutzerobjekt. |
| `name` | Erforderlich | JSON-Objekt | Dieses Objekt enthält den Vornamen und den Nachnamen des Benutzers. |
| `department` | Erforderlich | String | Gültige Abteilungszeichenfolge aus der [Dokumentation der Abteilungszeichenfolge]({{site.baseurl}}/scim_api_appendix/#department-strings). |
| `permissions` | Erforderlich | JSON-Objekt | Berechtigungsobjekt wie in der [Dokumentation des Berechtigungsobjekts]({{site.baseurl}}/scim_api_appendix/#permissions-object) beschrieben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## Beispiel Anfrage
```json
curl --location --request PUT 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
--data raw '{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
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
                "appGroupPermissions": ["basic_access","send_campaign_canvases"],
                "team": [
                    {
                         "teamName": "Test Team",                  
                         "teamPermissions": ["admin"]
                    }
                ]
            } 
        ]
    }
}
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
                         "teamPermissions": ["admin"]
                    }
                ]
            } 
        ]
    }
}
```

### Fehlerzustände
Wenn ein Benutzer mit dieser ID nicht in Braze existiert, antwortet der Endpunkt mit:

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
