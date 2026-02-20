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

Um Beispiele zu sehen oder diesen Endpunkt für **E-Mail Abo-Gruppen** zu testen:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b1b9a0e0-6329-4df2-a465-53347f410662 {% endapiref %}

Um Beispiele zu sehen oder diesen Endpunkt für **SMS Abo-Gruppen** zu testen:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

Um Beispiele zu sehen oder diesen Endpunkt für **WhatsApp-Gruppen** zu testen:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `subscription.status.set`.

{% alert note %}
Wenn Sie daran interessiert sind, diesen Endpunkt mit [Abo-Gruppen von LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line/line_users/subscription_groups/) zu verwenden, wenden Sie sich an Ihren Customer-Success-Manager.
{% endalert %}

## Unterschiede zu V1

Der V2 Endpunkt unterscheidet sich vom [V1 Endpunkt]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) in den folgenden Punkten:

- **Mehrere Abo-Gruppen**: Mit V2 können Sie mehrere Abo-Gruppen in einer einzigen API-Anfrage aktualisieren, während V1 nur eine Abo-Gruppe pro Anfrage unterstützt.
- **Aktualisieren Sie sowohl E-Mail als auch SMS in einem einzigen Anruf**: Wenn Sie `external_ids` verwenden, können Sie sowohl E-Mail- als auch SMS-Abo-Gruppen für dieselben Nutzer:innen mit einem einzigen API-Aufruf aktualisieren. Bei V1 müssen Sie für E-Mail- und SMS-Abo-Gruppen separate API-Aufrufe tätigen.
- **E-Mail oder telefonische Bezeichner verwenden**: Wenn Sie `emails` oder `phones` anstelle von `external_ids` verwenden, können Sie die E-Mail- und SMS-Abo-Gruppen nicht in derselben Anfrage aktualisieren. Sie müssen separate API-Aufrufe tätigen - einen für E-Mail-Abo-Gruppen und einen für SMS-Abo-Gruppen.

{% alert important %}
**Format der Rufnummer**: Telefonnummern müssen im [FormatE.164 ](https://en.wikipedia.org/wiki/E.164) angegeben werden (zum Beispiel `+12223334444`). Telefonnummern, die nicht im Format E.164 vorliegen, werden abgelehnt.
{% endalert %}

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
| `phones` | Erforderlich* | String in [E.164](https://en.wikipedia.org/wiki/E.164) Format | Sie können Nutzer:innen Telefonnummern als String-Array übergeben. Muss mindestens eine Telefonnummer enthalten (bis zu 50). Telefonnummern müssen im Format E.164 angegeben werden (zum Beispiel `+12223334444`). <br><br>Wenn mehrere Nutzer:innen (`external_id`) im selben Workspace dieselbe Telefonnummer haben, werden alle Nutzer:innen mit denselben Änderungen der Abo-Gruppe aktualisiert.|
| `use_double_opt_in_logic` | Optional | Boolesch | Wenn dieser Parameter weggelassen wird oder auf `false` gesetzt ist, werden Nutzer:innen nicht in den SMS Double Opt-in Workflow aufgenommen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert important %}
**Auswahl des Bezeichners**: 
- Um sowohl E-Mail- als auch SMS-Abo-Gruppen in einem einzigen API-Aufruf zu aktualisieren, verwenden Sie `external_ids`. Sie können nicht sowohl `emails` als auch `phones` in dieselbe Anfrage aufnehmen.
- Wenn Sie `emails` oder `phones` anstelle von `external_ids` verwenden, führen Sie separate API-Aufrufe durch - einen für E-Mail-Abo-Gruppen und einen für SMS-Abo-Gruppen.
- Sie können `emails`, `phones`, oder `external_ids` einzeln versenden.
{% endalert %}

### Beispiel-Anfragen

Das folgende Beispiel verwendet `external_ids`, um sowohl E-Mail- als auch SMS-Abo-Gruppen mit einem einzigen API-Aufruf zu aktualisieren. Dies ist nur möglich, wenn Sie `external_ids`verwenden. Wenn Sie `emails` oder `phones` verwenden, können Sie die Abo-Gruppen für E-Mail und SMS nicht in einem Anruf aktualisieren.

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
