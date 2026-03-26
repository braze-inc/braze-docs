---
nav_title: "POST: Nutzer:innen löschen"
article_title: "POST: Nutzer:innen löschen"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „Nutzer:innen löschen"."

---
{% api %}
# Nutzer:innen löschen
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/delete
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um ein beliebiges Nutzerprofil zu löschen, indem Sie einen bekannten Bezeichner angeben.

Bis zu 50 `external_ids`, `user_aliases`, `braze_ids`, `email_addresses` oder `phone_numbers` können in einer einzigen Anfrage enthalten sein. In einer Anfrage kann nur eine der Optionen `external_ids`, `user_aliases`, `braze_ids`, `email_addresses` oder `phone_numbers` enthalten sein.

Wenn Sie einen Anwendungsfall haben, der nicht mit der Massenlöschung von Nutzer:innen über die API gelöst werden kann, kontaktieren Sie das [Braze Support-Team]({{site.baseurl}}/user_guide/administrative/access_braze/support/) für Unterstützung.

{% alert warning %}
Das Löschen von Nutzerprofilen kann nicht rückgängig gemacht werden. Es entfernt Nutzer:innen dauerhaft, was zu Unstimmigkeiten in Ihren Daten führen kann. Mehr erfahren Sie darüber, was passiert, wenn Sie [ein Nutzerprofil über die API löschen]({{site.baseurl}}/help/help_articles/api/delete_user/), in unserer Hilfe-Dokumentation.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#22e91d00-d178-4b4f-a3df-0073ecfcc992 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `users.delete`.

## Rate-Limits

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
### Anfrageparameter

| Parameter         | Erforderlich | Datentyp                  | Beschreibung                                                                                      |
|-------------------|----------|----------------------------|--------------------------------------------------------------------------------------------------|
| `external_ids`    | Optional | String-Array           | Zu löschende externe Bezeichner.                                                    |
| `user_aliases`    | Optional | Array von Nutzer-Alias-Objekten | Zu löschende [Nutzer-Aliase]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `braze_ids`       | Optional | String-Array           | Zu löschende Braze-Nutzer:innen-Bezeichner.                                                  |
| `email_addresses` | Optional | String-Array           | Zu löschende Nutzer:innen-E-Mails. Weitere Informationen finden Sie unter [Löschen von Nutzer:innen per E-Mail](#deleting-users-by-email).                                                             |
| `phone_numbers` | Optional | String-Array | Zu löschende Nutzer:innen-Telefonnummern. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Löschen von Nutzer:innen nach E-Mail-Adressen und Telefonnummern

Wenn eine E-Mail-Adresse oder Telefonnummer als Bezeichner angegeben wird, ist ein zusätzlicher `prioritization`-Wert im Bezeichner erforderlich. `prioritization` muss ein geordnetes Array sein und sollte angeben, welche Nutzer:innen gelöscht werden sollen, wenn mehrere Nutzer:innen vorhanden sind. Das bedeutet, dass keine Löschung erfolgt, wenn mehr als eine Person einer Priorisierung entspricht.

Die zulässigen Werte für das Array sind:

- `identified`
- `unidentified`
- `most_recently_updated` (bezieht sich auf die Priorisierung der zuletzt aktualisierten Nutzer:innen)

Im Array `prioritization` darf jeweils nur eine der folgenden Optionen vorhanden sein:

- `identified` bezieht sich auf die Priorisierung von Nutzer:innen mit einer `external_id`
- `unidentified` bezieht sich auf die Priorisierung von Nutzer:innen ohne eine `external_id`

## Beispielanfrage

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
{
  "deleted" : (required, integer) number of user IDs queued for deletion
}
```

## Fehlerbehebung

### Eine Erfolgsantwort wurde zurückgegeben, aber die Nutzer:innen sind noch sichtbar

Eine erfolgreiche Antwort bestätigt, dass die Anfrage in die Warteschlange gestellt wurde – nicht, dass die Löschung abgeschlossen ist. Die Löschung ist in der Regel in weniger als einer Sekunde abgeschlossen, es kann jedoch bis zu fünf Minuten dauern, bis die Änderung in allen Caches propagiert ist. Wenn Sie unmittelbar danach im Dashboard nach den Nutzer:innen suchen oder deren Daten über die API exportieren, können während dieses Propagierungsfensters noch Ergebnisse angezeigt werden.

Wenn die Nutzer:innen nach mehreren Minuten noch vorhanden sind, überprüfen Sie, ob der Bezeichner in Ihrer Anfrage mit dem tatsächlichen Profil übereinstimmt:

- **`external_ids`-Array:** Stellen Sie sicher, dass jeder Wert exakt mit der externen ID der Nutzer:innen übereinstimmt.
- **`braze_id`:** Sie können die `braze_id` von Nutzer:innen ermitteln, indem Sie deren Daten mit dem [`/users/export/ids`-Endpunkt]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) exportieren oder ein Segment als CSV exportieren (wobei die `braze_id` als „Appboy ID" erscheint).
- **Alias-only- oder E-Mail-only-Profile:** Wenn das Profil keine `external_id` hat, erstellen Sie ein Segment mit dem Filter **Externe Nutzer-ID ist leer** in Kombination mit der bekannten E-Mail-Adresse oder Telefonnummer und exportieren Sie es als CSV, um die `braze_id` abzurufen.

Um zu bestätigen, ob Nutzer:innen gelöscht wurden, rufen Sie den [`/users/export/ids`-Endpunkt]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) mit demselben Bezeichnertyp auf, den Sie in der Löschanfrage verwendet haben (z. B. den Wert in `external_ids`, `braze_id` oder `user_aliases`). Wenn die Nutzer:innen nicht mehr existieren, enthält die Antwort `"users": []` und möglicherweise `"invalid_user_ids"` mit dem entsprechenden Bezeichner.

{% endapi %}