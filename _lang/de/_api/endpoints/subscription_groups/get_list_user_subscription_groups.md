---
nav_title: "GET: Nutzer:innen Abo-Gruppen auflisten"
article_title: "GET: Nutzer:innen Abo-Gruppen auflisten"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Nutzer:innen Abo-Gruppen auflisten."

---
{% api %}
# Abo-Gruppen des Nutzers:innen auflisten
{% apimethod get %}
/subscription/user/status
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um die Abo-Gruppen eines bestimmten Nutzers aufzulisten und abzurufen.

Wenn Sie Beispiele sehen oder diesen Endpunkt für **E-Mail Abo-Gruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d1c3b617-22f1-47bf-9ee8-499526824470 {% endapiref %}

Wenn Sie Beispiele sehen oder diesen Endpunkt für **SMS Abo-Gruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

Wenn Sie Beispiele sehen oder diesen Endpunkt für **WhatsApp-Gruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `subscription.groups.get`.

## Rate-Limits

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `external_id`  | Erforderlich | String | Die `external_id` des Nutzers:in (muss mindestens eine und darf höchstens 50 `external_ids` enthalten). |
| `email`  |  Erforderlich* | String | Die E-Mail Adresse des Nutzers:innen, kann als String-Array übergeben werden. Sie müssen mindestens eine E-Mail Adresse angeben (maximal 50). |
| `phone` | Erforderlich* | String in [E.164](https://en.wikipedia.org/wiki/E.164) Format | Die Telefonnummer der Nutzer:in. Muss mindestens eine Telefonnummer enthalten (maximal 50). |
| `limit` | Optional | Integer | Das Limit für die maximale Anzahl der zurückgegebenen Ergebnisse. Standard (und maximal) `limit` ist 100. |
| `offset`  |  Optional | Integer | Anzahl der Templates, die übersprungen werden sollen, bevor der Rest der Templates, die den Suchkriterien entsprechen, zurückgegeben wird. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert tip %}
Wenn es mehrere Nutzer:innen (mehrere `external_ids`) gibt, die dieselbe E-Mail Adresse haben, werden alle Nutzer:innen als separate Nutzer:innen angezeigt (auch wenn sie dieselbe E-Mail Adresse oder Abo-Gruppe haben).
{% endalert %}

## Beispiel Anfrage 

{% tabs %}
{% tab Mehrere Nutzer:innen %}
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

## Beispielhafte Antwort

```json
{
  "success": true,
  "subscription_groups": [
    {
      "subscription_group_id": "group_id_1",
      "subscription_status": "subscribed"
    },
    {
      "subscription_group_id": "group_id_2",
      "subscription_status": "unsubscribed"
    }
  ]
}
```

{% endapi %}