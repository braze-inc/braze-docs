---
nav_title: "POST: Nutzer:innen löschen"
article_title: "POST: Nutzer:innen löschen"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Nutzer:innen löschen."

---
{% api %}
# Nutzer:innen löschen
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/benutzer:innen/löschen
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um ein beliebiges Nutzerprofil zu löschen, indem Sie einen bekannten Bezeichner für Nutzer:in angeben.

Bis zu 50 `external_ids`, `user_aliases`, `braze_ids`, `email_addresses` oder `phone_numbers` können in einer einzigen Anfrage enthalten sein. In einer Anfrage kann nur eine der Optionen `external_ids`, `user_aliases`, `braze_ids`, `email_addresses` oder `phone_numbers` enthalten sein. 

Wenn Sie einen Anwendungsfall haben, der nicht mit der Massenlöschung von Nutzer:innen über die API gelöst werden kann, wenden Sie sich bitte an das [Braze Support Team]({{site.baseurl}}/user_guide/administrative/access_braze/support/), um Hilfe zu erhalten.

{% alert warning %}
Das Löschen von Benutzerprofilen kann nicht rückgängig gemacht werden. Es entfernt dauerhaft Benutzer, die Unstimmigkeiten in Ihren Daten verursachen könnten. Erfahren Sie mehr darüber, was passiert, wenn Sie [ein Nutzerprofil über die API löschen]({{site.baseurl}}/help/help_articles/api/delete_user/), in unserer Dokumentation Hilfe.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#22e91d00-d178-4b4f-a3df-0073ecfcc992 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `users.delete`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='users delete' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_ids" : (optional, array of string) External IDs to be deleted,
  "user_aliases" : (optional, array of user alias objects) User aliases to be deleted,
  "braze_ids" : (optional, array of string) Braze user identifiers to be deleted,
  "email_addresses": (optional, array of string) User emails to be deleted,
  "phone_numbers": (optional, array of string) User phone numbers to be deleted
}
```
### Parameter der Anfrage

| Parameter         | Erforderlich | Datentyp                  | Beschreibung                                                                                      |
|-------------------|----------|----------------------------|--------------------------------------------------------------------------------------------------|
| `external_ids`    | Optional | String-Array           | Zu löschende externe Bezeichner.                                                    |
| `user_aliases`    | Optional | Array des Nutzer:in-Alias-Objekts | Zu löschende [Nutzer:innen]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `braze_ids`       | Optional | String-Array           | Zu löschende Braze Nutzer:innen-Bezeichner.                                                  |
| `email_addresses` | Optional | String-Array           | Zu löschende Nutzer:innen-E-Mails. Weitere Informationen finden Sie unter [Löschen von Nutzer:innen per E-Mail](#deleting-users-by-email).                                                             |
| `phone_numbers` | Optional | String-Array | Zu löschende Nutzer:innen-Telefonnummern. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Löschen von Nutzer:innen nach E-Mail-Adressen und Telefonnummern

Wenn eine E-Mail Adresse oder Telefonnummer als Bezeichner angegeben wird, ist ein zusätzlicher `prioritization` Wert im Bezeichner erforderlich. `prioritization` muss ein geordnetes Array sein und sollte angeben, welcher Nutzer:innen zu löschen ist, wenn es mehrere Nutzer:innen gibt. Das bedeutet, dass Nutzer:innen nicht gelöscht werden, wenn mehr als ein Nutzer einer Priorisierung entspricht.

Die zulässigen Werte für das Array sind:

- `identified`
- `unidentified`
- `most_recently_updated` (referenziert auf den zuletzt aktualisierten Nutzer:in)

Im Array `prioritization` darf jeweils nur eine der folgenden Optionen vorhanden sein:

- `identified` bezieht sich auf die Priorisierung eines Nutzer:innen mit einem `external_id`
- `unidentified` bezieht sich auf die Priorisierung eines Nutzer:in ohne ein `external_id`

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


