---
nav_title: "POST: Abo-Gruppenstatus der Nutzer:innen aktualisieren v2"
alias: /post_update_user_subscription_group_status_v2/
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-V2-Endpunkts zum Aktualisieren des Abo-Gruppenstatus von Nutzer:innen."

platform: API
channel:
  - Email
---

{% api %}
# Abo-Gruppenstatus von Nutzer:innen aktualisieren (V2)
{% apimethod post %}
/v2/subscription/status/set
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um den Abo-Status von bis zu 50 Nutzer:innen im Braze-Dashboard im Stapelverfahren zu aktualisieren.

Sie können auf die `subscription_group_id` einer Abo-Gruppe zugreifen, indem Sie zur Seite **Abo-Gruppe** navigieren.

Um Beispiele zu sehen oder diesen Endpunkt für **E-Mail-Abo-Gruppen** zu testen:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b1b9a0e0-6329-4df2-a465-53347f410662 {% endapiref %}

Um Beispiele zu sehen oder diesen Endpunkt für **SMS-Abo-Gruppen** zu testen:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

Um Beispiele zu sehen oder diesen Endpunkt für **WhatsApp-Gruppen** zu testen:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `subscription.status.set`.

{% alert note %}
Wenn Sie diesen Endpunkt mit [LINE-Abo-Gruppen]({{site.baseurl}}/user_guide/message_building_by_channel/line/line_users/subscription_groups/) verwenden möchten, wenden Sie sich bitte an Ihren Customer-Success-Manager.
{% endalert %}

## Unterschiede zu V1

Der V2-Endpunkt unterscheidet sich vom [V1-Endpunkt]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) in folgenden Punkten:

- **Mehrere Abo-Gruppen**: Mit V2 können Sie mehrere Abo-Gruppen in einer einzigen API-Anfrage aktualisieren, während V1 nur eine Abo-Gruppe pro Anfrage unterstützt.
- **E-Mail und SMS in einem Aufruf aktualisieren**: Bei Verwendung von `external_ids` können Sie sowohl E-Mail- als auch SMS-Abo-Gruppen für dieselben Nutzer:innen in einem einzigen API-Aufruf aktualisieren. Bei V1 müssen Sie separate API-Aufrufe für E-Mail- und SMS-Abo-Gruppen durchführen.
- **Verwendung von E-Mail- oder Telefon-Bezeichnern**: Wenn Sie `emails` oder `phones` anstelle von `external_ids` verwenden, können Sie nicht sowohl E-Mail- als auch SMS-Abo-Gruppen in derselben Anfrage aktualisieren. Sie müssen separate API-Aufrufe durchführen – einen für E-Mail-Abo-Gruppen und einen für SMS-Abo-Gruppen.

{% alert important %}
**Telefonnummernformat**: Telefonnummern müssen im [E.164-Format](https://en.wikipedia.org/wiki/E.164) angegeben werden (zum Beispiel `+12223334444`). Telefonnummern, die nicht im E.164-Format vorliegen, werden abgelehnt.
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
      "subscription_state": (required, string),
      "external_ids": (required*, array of strings),
      "emails": (required*, array of strings),
      "phones": (required*, array of strings in E.164 format),
      "use_double_opt_in_logic": (optional, boolean)
    }
  ]
}
```

{% alert tip %}
Bei der Erstellung neuer Nutzer:innen über den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) können Sie Abo-Gruppen innerhalb des Nutzerattribut-Objekts festlegen. So können Sie in einem einzigen API-Aufruf eine:n Nutzer:in erstellen und den Abo-Gruppenstatus festlegen.
{% endalert %}

## Anfrageparameter

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | Erforderlich | String | Die `id` Ihrer Abo-Gruppe. |
| `subscription_state` | Erforderlich | String | Verfügbare Werte sind `unsubscribed` (nicht in Abo-Gruppe) oder `subscribed` (in Abo-Gruppe). |
| `external_ids` | Erforderlich* | String-Array | Die `external_id` des Nutzers bzw. der Nutzer:innen, kann bis zu 50 `id`s umfassen. |
| `emails` | Erforderlich* | String oder String-Array | Die E-Mail-Adresse der Nutzer:innen, kann als String-Array übergeben werden. Es muss mindestens eine E-Mail-Adresse angegeben werden (maximal 50). <br><br>Wenn mehrere Nutzer:innen (`external_id`) im selben Workspace dieselbe E-Mail-Adresse haben, werden alle Nutzer:innen, die diese E-Mail-Adresse teilen, mit den Änderungen der Abo-Gruppe aktualisiert. |
| `phones` | Erforderlich* | String im [E.164](https://en.wikipedia.org/wiki/E.164)-Format | Sie können die Telefonnummern der Nutzer:innen als String-Array übergeben. Es muss mindestens eine Telefonnummer enthalten sein (bis zu 50). Telefonnummern müssen im E.164-Format angegeben werden (zum Beispiel `+12223334444`). <br><br>Wenn mehrere Nutzer:innen (`external_id`) im selben Workspace dieselbe Telefonnummer haben, werden alle Nutzer:innen, die diese Telefonnummer teilen, mit denselben Änderungen der Abo-Gruppe aktualisiert.|
| `use_double_opt_in_logic` | Optional | Boolescher Wert | Standardmäßig `false`, wenn nicht angegeben. Setzen Sie diesen Parameter für SMS-Abo-Gruppen auf `true`, um die Nutzer:innen in den [SMS-Double-Opt-in]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/)-Workflow aufzunehmen, wenn ihr Abo-Status auf `subscribed` gesetzt wird. Wenn dieser Parameter weggelassen oder auf `false` gesetzt wird, werden Nutzer:innen abonniert, ohne den Double-Opt-in-Workflow zu durchlaufen. Dieser Parameter gilt nicht für E-Mail-Abo-Gruppen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert important %}
**Auswahl des Bezeichners**: 
- Um sowohl E-Mail- als auch SMS-Abo-Gruppen in einem einzigen API-Aufruf zu aktualisieren, verwenden Sie `external_ids`. Es ist nicht möglich, sowohl `emails` als auch `phones` in derselben Anfrage anzugeben.
- Wenn Sie `emails` oder `phones` anstelle von `external_ids` verwenden, führen Sie separate API-Aufrufe durch – einen für E-Mail-Abo-Gruppen und einen für SMS-Abo-Gruppen.
- Sie können `emails`, `phones` oder `external_ids` einzeln senden.
{% endalert %}

### Beispielanfragen

Das folgende Beispiel verwendet `external_ids`, um sowohl E-Mail- als auch SMS-Abo-Gruppen in einem einzigen API-Aufruf zu aktualisieren. Dies ist nur bei Verwendung von `external_ids` möglich – bei Verwendung von `emails` oder `phones` können Sie nicht sowohl E-Mail- als auch SMS-Abo-Gruppen in einem Aufruf aktualisieren.

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