---
nav_title: "POST: Update Nutzer:innen Abo-Gruppenstatus v2"
alias: /post_update_user_subscription_group_status_v2/
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Update Nutzer:innen Abo-Gruppenstatus Braze V2."

platform: API
channel:
  - Email
---

{% api %}
# Update des Abo-Gruppenstatus eines Nutzers:in (V2)
{% apimethod post %}
/v2/abo/status/set
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um das Update des Abo-Status von bis zu 50 Nutzer:innen auf dem Braze-Dashboard im Stapelverfahren durchzuführen. 

Sie können auf die `subscription_group_id` einer Abo-Gruppe zugreifen, indem Sie zur Seite **Abo-Gruppe** navigieren.

Wenn Sie Beispiele sehen oder diesen Endpunkt für **E-Mail Abo-Gruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b1b9a0e0-6329-4df2-a465-53347f410662 {% endapiref %}

Wenn Sie Beispiele sehen oder diesen Endpunkt für **SMS Abo-Gruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

Wenn Sie Beispiele sehen oder diesen Endpunkt für **WhatsApp-Gruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `subscription.status.set`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "subscription_groups":[
    {
      "subscription_group_id": (required, string),
      "subscription_state": (required, string)
      "external_ids": (required*, array of strings),
      "emails": (required*, array of strings),
      "phones": (required*, array of strings in E.164 format),
    }
  ]
}
```
\* Beachten Sie, dass Sie die Parameter `emails` und `phones` nicht gleichzeitig angeben können. Auch `emails`, `phones` und `external_ids` können einzeln gesendet werden.

{% alert tip %}
Bei der Erstellung neuer Nutzer:in über den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) können Sie Abo-Gruppen innerhalb des Objekts Benutzerattribute festlegen. So können Sie in einem einzigen API-Aufruf einen Nutzer erstellen und den Status der Abo-Gruppe festlegen.
{% endalert %}

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | Erforderlich | String | Die `id` Ihrer Abo-Gruppe. |
| `subscription_state` | Erforderlich | String | Verfügbare Werte sind `unsubscribed` (nicht in Abo-Gruppe) oder `subscribed` (in Abo-Gruppe). |
| `external_ids` | Erforderlich* | String-Array | Die `external_id` des Nutzers oder der Nutzer:innen kann bis zu 50 `id`s umfassen. |
| `emails` | Erforderlich* | String oder String-Array | Die E-Mail Adresse des Nutzers:innen, kann als String-Array übergeben werden. Sie müssen mindestens eine E-Mail Adresse angeben (maximal 50). <br><br>Wenn mehrere Nutzer:innen (`external_id`) im selben Workspace dieselbe E-Mail Adresse haben, werden alle Nutzer:innen mit den Änderungen der Abo-Gruppe aktualisiert. |
| `phones` | Erforderlich* | String in [E.164](https://en.wikipedia.org/wiki/E.164) Format | Die Telefonnummern der Nutzer:innen, können als String-Array übergeben werden. Muss mindestens eine Telefonnummer enthalten (bis zu 50). <br><br>Wenn mehrere Nutzer:innen (`external_id`) im selben Workspace dieselbe Telefonnummer haben, werden alle Nutzer:innen mit denselben Änderungen der Abo-Gruppe aktualisiert.|
| `use_double_opt_in_logic` | Optional | Boolesch | Wenn Sie diesen Parameter weglassen oder auf `false` setzen, werden die Nutzer:innen nicht in den SMS Double Opt-in Workflow aufgenommen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Beachten Sie, dass Sie die Parameter `emails` und `phones` nicht gleichzeitig verwenden können. Auch `emails`, `phones` und `external_ids` können einzeln gesendet werden.
{% endalert %}

### Beispiel-Anfragen

Das folgende Beispiel verwendet `external_id`, um einen API-Aufruf für E-Mail und SMS zu tätigen.

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    },
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    }
  ]
}
```

## E-Mail

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "emails":["example1@email.com","example2@email.com"]
    }
  ]
}
'
```

## SMS und WhatsApp

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "phones":["+12223334444","+15556667777"]
    }
  ]
}
'
```

{% endapi %}
