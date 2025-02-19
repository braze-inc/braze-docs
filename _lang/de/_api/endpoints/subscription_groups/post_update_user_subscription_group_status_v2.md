---
nav_title: "POST: Status der Abonnementgruppe eines Benutzers aktualisieren V2"
alias: /post_update_user_subscription_group_status_v2/
layout: api_page
page_type: reference
description: "In diesem Artikel finden Sie Einzelheiten über den Status der Abonnementgruppe des Benutzers aktualisieren Braze V2 Endpunkt."

platform: API
channel:
  - Email
---

{% api %}
# Status der Abonnementgruppe des Benutzers aktualisieren (V2)
{% apimethod post %}
/v2/subscription/status/set
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um den Abonnementstatus von bis zu 50 Benutzern auf dem Braze-Dashboard im Stapel zu aktualisieren. 

Sie können auf die `subscription_group_id` einer Abonnementgruppe zugreifen, indem Sie zur Seite **Abonnementgruppe** navigieren.

Wenn Sie Beispiele sehen oder diesen Endpunkt für **E-Mail-Abonnementgruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b1b9a0e0-6329-4df2-a465-53347f410662 {% endapiref %}

Wenn Sie Beispiele sehen oder diesen Endpunkt für **SMS-Abonnementgruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

Wenn Sie Beispiele sehen oder diesen Endpunkt für **WhatsApp-Gruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `subscription.status.set`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

## Körper der Anfrage

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
Bei der Erstellung neuer Benutzer über den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) können Sie Abonnementgruppen innerhalb des Objekts Benutzerattribute festlegen. So können Sie einen Benutzer erstellen und den Status der Abonnementgruppe in einem einzigen API-Aufruf festlegen.
{% endalert %}

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | Erforderlich | String | Die `id` Ihrer Abonnementgruppe. |
| `subscription_state` | Erforderlich | String | Verfügbare Werte sind `unsubscribed` (nicht in der Abonnementgruppe) oder `subscribed` (in der Abonnementgruppe). |
| `external_ids` | Erforderlich* | Array von Zeichenketten | Die `external_id` des Nutzers oder der Nutzer, kann bis zu 50 `id`s umfassen. |
| `emails` | Erforderlich* | String oder Array von Strings | Die E-Mail-Adresse des Benutzers, kann als Array von Strings übergeben werden. Sie müssen mindestens eine E-Mail-Adresse angeben (maximal 50). <br><br>Wenn mehrere Benutzer (`external_id`) im gleichen Arbeitsbereich die gleiche E-Mail-Adresse verwenden, werden alle Benutzer, die die E-Mail-Adresse verwenden, mit den Änderungen der Abonnementgruppe aktualisiert. |
| `phones` | Erforderlich* | Zeichenkette im [E.164](https://en.wikipedia.org/wiki/E.164) Format | Die Telefonnummern des Benutzers können als Array von Strings übergeben werden. Muss mindestens eine Telefonnummer enthalten (maximal 50). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Beachten Sie, dass Sie die Parameter `emails` und `phones` nicht gleichzeitig verwenden können. Auch `emails`, `phones` und `external_ids` können einzeln gesendet werden.
{% endalert %}

### Beispiel Anfragen

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
