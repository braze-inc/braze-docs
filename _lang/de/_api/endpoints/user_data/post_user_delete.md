---
nav_title: "POST: Benutzer löschen"
article_title: "POST: Benutzer löschen"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten zum Braze-Endpunkt Benutzer löschen."

---
{% api %}
# Benutzer löschen
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/delete
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um ein beliebiges Benutzerprofil zu löschen, indem Sie einen bekannten Benutzeridentifikator angeben.

Bis zu 50 `external_ids`, `user_aliases`, `braze_ids`, oder `email_addresses` können in einer einzigen Anfrage enthalten sein. Nur eine der Optionen `external_ids`, `user_aliases`, `braze_ids` oder `email_addresses` kann in einer einzigen Anfrage enthalten sein.

{% alert warning %}
Das Löschen von Benutzerprofilen kann nicht rückgängig gemacht werden. Es entfernt dauerhaft Benutzer, die Unstimmigkeiten in Ihren Daten verursachen können. Erfahren Sie mehr darüber, was passiert, wenn Sie [ein Benutzerprofil über die API löschen]({{site.baseurl}}/help/help_articles/api/delete_user/), in unserer Hilfe-Dokumentation.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#22e91d00-d178-4b4f-a3df-0073ecfcc992 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `users.delete`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='users delete' %}

## Körper der Anfrage

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_ids" : (optional, array of string) External IDs for the users to delete,
  "user_aliases" : (optional, array of user alias objects) User aliases for the users to delete,
  "braze_ids" : (optional, array of string) Braze user identifiers for the users to delete,
  "email_addresses": (optional, array of string) User emails for the users to delete
}
```
### Parameter anfordern

| Parameter         | Erforderlich | Daten Typ                  | Beschreibung                                                                                      |
|-------------------|----------|----------------------------|--------------------------------------------------------------------------------------------------|
| `external_ids`    | Optional | Array von Zeichenketten           | Externe Identifikatoren für die zu löschenden Benutzer.                                                    |
| `user_aliases`    | Optional | Array mit Benutzer-Alias-Objekt | [Benutzer-Aliase]({{site.baseurl}}/api/objects_filters/user_alias_object/) für die zu löschenden Benutzer. |
| `braze_ids`       | Optional | Array von Zeichenketten           | Braze-Benutzerkennungen für die zu löschenden Benutzer.                                                  |
| `email_addresses` | Optional | Array von Zeichenketten           | Benutzer-E-Mails, die die Benutzer löschen können. Weitere Informationen finden Sie unter [Löschen von Benutzern per E-Mail](#deleting-users-by-email).                                                             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Löschen von Benutzern per E-Mail

Wenn ein `email` als Bezeichner angegeben wird, ist ein zusätzlicher `prioritization` Wert im Bezeichner erforderlich. Die `prioritization` ist ein geordnetes Array und sollte angeben, welcher Benutzer gelöscht werden soll, wenn mehrere Benutzer gefunden werden. Das bedeutet, dass das Löschen von Benutzern nicht erfolgt, wenn mehr als ein Benutzer einer Priorisierung entspricht.

Die zulässigen Werte für das Array sind: `identified`, `unidentified`, `most_recently_updated`. `most_recently_updated` bezieht sich auf die Priorisierung des zuletzt aktualisierten Benutzers.

Es kann jeweils nur eine der folgenden Optionen im Prioritätsfeld vorhanden sein:

- `identified` bezieht sich auf die Priorisierung eines Benutzers mit einer `external_id`
- `unidentified` bezieht sich auf die Priorisierung eines Benutzers ohne `external_id`

## Beispiel Anfrage

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "external_ids": ["external_identifier1", "external_identifier2"],
  "braze_ids": ["braze_identifier1", "braze_identifier2"],
  "user_aliases": [
    {
      "alias_name": "user_alias1", "alias_label": "alias_label1"
    },
    {
      "alias_name": "user_alias2", "alias_label": "alias_label2"
    }
  ],
  "email_addresses": [
    {
      "email": "john.smith@braze.com",
      "prioritization": ["unidentified", "most_recently_updated"]
    }
  ]
}'
```

## Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "deleted" : (required, integer) number of user IDs queued for deletion
}
```
{% endapi %}


