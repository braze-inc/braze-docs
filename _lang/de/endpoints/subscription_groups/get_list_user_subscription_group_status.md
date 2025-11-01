---
nav_title: "GET: Abo-Gruppenstatus der Nutzer:innen auflisten"
article_title: "GET: Status der Abo-Gruppe des Nutzers auflisten"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Abo-Gruppenstatus Nutzer:innen auflisten."

---
{% api %}
# Abo-Gruppenstatus des Nutzers:innen auflisten
{% apimethod get %}
/abo/status/get
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um den Status eines Nutzers:innen in einer Abo-Gruppe abzurufen.

Diese Gruppen werden auf der Seite **Abo-Gruppe** verfügbar sein. Die Antwort von diesem Endpunkt enthält die externe ID und entweder abonniert, abgemeldet oder unbekannt für die spezifische Abo-Gruppe, die im API-Aufruf angefragt wurde. Dies kann zum Update des Status der Abo-Gruppe in nachfolgenden API-Aufrufen oder zur Anzeige auf einer gehosteten Webseite verwendet werden.

Wenn Sie Beispiele sehen oder diesen Endpunkt für **E-Mail Abo-Gruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#488c8923-fa44-4124-9245-036d13c615f2 {% endapiref %}

Wenn Sie Beispiele sehen oder diesen Endpunkt für **SMS Abo-Gruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

Wenn Sie Beispiele sehen oder diesen Endpunkt für **WhatsApp-Gruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `subscription.status.get`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids)  | Erforderlich | String | Die `id` Ihrer Abo-Gruppe. |
| `external_id`  |  Erforderlich* | String | Die `external_id` des Nutzers:in (muss mindestens eine und darf höchstens 50 `external_ids` enthalten). <br><br>Wenn sowohl ein `external_id` als auch `email`/`phone` übermittelt werden, wird nur der/die angegebene(n) `external_id` auf die Ergebnisabfrage angewendet. |
| `email` | Erforderlich* | String | Die E-Mail Adresse des Nutzers:innen. Es kann als String-Array mit maximal 50 Strings übergeben werden.<br><br> Wenn Sie sowohl eine E-Mail Adresse als auch eine Telefonnummer (ohne `external_id`) angeben, wird ein Fehler angezeigt. |
| `phone` | Erforderlich* | String in [E.164](https://en.wikipedia.org/wiki/E.164) Format | Die Telefonnummer der Nutzer:in. Wenn Sie keine E-Mail angeben, müssen Sie mindestens eine Telefonnummer angeben (maximal 50).<br><br> Wenn Sie sowohl eine E-Mail Adresse als auch eine Telefonnummer (ohne `external_id`) angeben, wird ein Fehler angezeigt. |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

\*Für jeden Nutzer:innen ist eine der Optionen `external_id` oder `email` oder `phone` erforderlich.

- Für SMS- und WhatsApp-Abo-Gruppen ist entweder `external_id` oder `phone` erforderlich.  Wenn beide übermittelt werden, wird nur die `external_id` für die Abfrage verwendet und die Telefonnummer wird diesem Nutzer:innen zugeordnet.
- Für E-Mail Abo-Gruppen ist entweder `external_id` oder `email` erforderlich.  Wenn beide eingegeben werden, wird nur die `external_id` für die Abfrage verwendet und die E-Mail wird auf diese Nutzer:innen angewendet.

## Beispiel Anfrage 

{% tabs %}
{% tab Multiple Users %}
{% raw %}
```
https://rest.iad-03.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&external_id[]=1&external_id[]=2
```
{% endraw %}
{% endtab %}
{% tab SMS and WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab Email %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&email=example@braze.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Antwort

Alle erfolgreichen Antworten geben `Subscribed`, `Unsubscribed` oder `Unknown` zurück, je nach Status und Nutzer:innen-Verlauf mit der Abo-Gruppe.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "status": {
    "1": "Unsubscribed",
    "2": "Subscribed"
  },
  "message": "success"
}
```

{% endapi %}
