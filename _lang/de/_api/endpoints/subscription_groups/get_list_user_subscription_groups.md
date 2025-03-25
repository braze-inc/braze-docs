---
nav_title: "GET: Abonnementgruppen des Benutzers auflisten"
article_title: "GET: Abonnementgruppen des Benutzers auflisten"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten über den Braze-Endpunkt Abonnementgruppen des Benutzers auflisten."

---
{% api %}
# Liste der Abonnementgruppen des Benutzers
{% apimethod get %}
/subscription/user/status
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um die Abonnementgruppen eines bestimmten Benutzers aufzulisten und abzurufen.

Wenn Sie Beispiele sehen oder diesen Endpunkt für **E-Mail-Abonnementgruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d1c3b617-22f1-47bf-9ee8-499526824470 {% endapiref %}

Wenn Sie Beispiele sehen oder diesen Endpunkt für **SMS-Abonnementgruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

Wenn Sie Beispiele sehen oder diesen Endpunkt für **WhatsApp-Gruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `subscription.groups.get`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
|---|---|---|---|
| `external_id`  | Erforderlich | String | Die `external_id` des Benutzers (muss mindestens eine und höchstens 50 `external_ids` enthalten). |
| `email`  |  Erforderlich* | String | Die E-Mail-Adresse des Benutzers, kann als Array von Strings übergeben werden. Sie müssen mindestens eine E-Mail-Adresse angeben (maximal 50). |
| `phone` | Erforderlich* | Zeichenkette im [E.164](https://en.wikipedia.org/wiki/E.164) Format | Die Rufnummer des Benutzers. Muss mindestens eine Telefonnummer enthalten (maximal 50). |
| `limit` | Optional | Integer | Das Limit für die maximale Anzahl der zurückgegebenen Ergebnisse. Die Standardeinstellung (und das Maximum) `limit` ist 100. |
| `offset`  |  Optional | Integer | Anzahl der Vorlagen, die übersprungen werden sollen, bevor der Rest der Vorlagen, die den Suchkriterien entsprechen, zurückgegeben wird. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert tip %}
Wenn es mehrere Benutzer (mehrere `external_ids`) gibt, die dieselbe E-Mail-Adresse haben, werden alle Benutzer als separate Benutzer angezeigt (auch wenn sie dieselbe E-Mail-Adresse oder Abonnementgruppe haben).
{% endalert %}

## Beispiel Anfrage 

{% tabs %}
{% tab Mehrere Benutzer %}
{% raw %}
`https://rest.iad-03.braze.com/subscription/user/status?external_id[]=1&external_id[]=2`
{% endraw %}
{% endtab %}
{% tab SMS und WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&limit=100&offset=1&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab E-Mail %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&email=example@braze.com&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}
{% endapi %}
