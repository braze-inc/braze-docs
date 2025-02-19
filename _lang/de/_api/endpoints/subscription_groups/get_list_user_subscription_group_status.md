---
nav_title: "GET: Status der Abonnementgruppe der Benutzer auflisten"
article_title: "GET: Status der Abonnementgruppe des Benutzers auflisten"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts Abonnementgruppenstatus des Benutzers auflisten."

---
{% api %}
# Status der Abonnementgruppe des Benutzers auflisten
{% apimethod get %}
/subscription/status/get
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um den Abonnementstatus eines Benutzers in einer Abonnementgruppe abzurufen.

Diese Gruppen werden auf der Seite **Abonnementgruppen** verfügbar sein. Die Antwort von diesem Endpunkt enthält die externe ID und entweder abonniert, nicht abonniert oder unbekannt für die spezifische Abonnementgruppe, die im API-Aufruf angefordert wurde. Dies kann verwendet werden, um den Status der Abonnementgruppe in nachfolgenden API-Aufrufen zu aktualisieren oder um auf einer gehosteten Webseite angezeigt zu werden.

Wenn Sie Beispiele sehen oder diesen Endpunkt für **E-Mail-Abonnementgruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#488c8923-fa44-4124-9245-036d13c615f2 {% endapiref %}

Wenn Sie Beispiele sehen oder diesen Endpunkt für **SMS-Abonnementgruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

Wenn Sie Beispiele sehen oder diesen Endpunkt für **WhatsApp-Gruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `subscription.status.get`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids)  | Erforderlich | String | Die `id` Ihrer Abonnementgruppe. |
| `external_id`  |  Erforderlich* | String | Die `external_id` des Benutzers (muss mindestens eine und höchstens 50 `external_ids` enthalten). <br><br>Wenn sowohl ein `external_id` als auch `email`/`phone` übermittelt werden, wird nur der/die angegebene(n) `external_id` auf die Ergebnisabfrage angewendet. |
| `email` | Erforderlich* | String | Die E-Mail-Adresse des Benutzers. Er kann als Array von Strings mit maximal 50 übergeben werden.<br><br> Wenn Sie sowohl eine E-Mail-Adresse als auch eine Telefonnummer (ohne `external_id`) eingeben, wird ein Fehler angezeigt. |
| `phone` | Erforderlich* | Zeichenkette im [E.164](https://en.wikipedia.org/wiki/E.164) Format | Die Rufnummer des Benutzers. Wenn Sie keine E-Mail angeben, müssen Sie mindestens eine Telefonnummer angeben (maximal 50).<br><br> Wenn Sie sowohl eine E-Mail-Adresse als auch eine Telefonnummer (ohne `external_id`) eingeben, wird ein Fehler angezeigt. |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

\*Eine der Optionen `external_id` oder `email` oder `phone` ist für jeden Benutzer erforderlich.

- Für SMS- und WhatsApp-Abonnementgruppen ist entweder `external_id` oder `phone` erforderlich.  Wenn beide übermittelt werden, wird nur die `external_id` für die Abfrage verwendet und die Telefonnummer wird auf diesen Benutzer angewendet.
- Für E-Mail-Abonnementgruppen ist entweder `external_id` oder `email` erforderlich.  Wenn beide eingegeben werden, wird nur die `external_id` für die Abfrage verwendet und die E-Mail-Adresse wird auf diesen Benutzer angewendet.

## Beispiel Anfrage 

{% tabs %}
{% tab Mehrere Benutzer %}
{% raw %}
```
https://rest.iad-03.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&external_id[]=1&external_id[]=2
```
{% endraw %}
{% endtab %}
{% tab SMS und WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab E-Mail %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&email=example@braze.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Antwort

Alle erfolgreichen Antworten geben `Subscribed`, `Unsubscribed` oder `Unknown` zurück, je nach Status und Benutzergeschichte mit der Abonnementgruppe.

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
