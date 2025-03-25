---
nav_title: "GET: Liste Abonnementstatus mit E-Mail-Adresse oder Telefonnummer"
article_title: "GET: Liste Abonnementstatus mit E-Mail-Adresse oder Telefonnummer"
search_tag: Endpoint
page_order: 2
hidden: true
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts Listenabonnementstatus mit E-Mail-Adresse oder Telefonnummer."

---
{% api %}
# Angabe des Abonnementstatus mit einer E-Mail-Adresse oder Telefonnummer
{% apimethod get %}
/users/subscription
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um den Wert des Abonnementstatus auf der Grundlage einer E-Mail-Adresse oder Telefonnummer zurückzugeben.

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| --- | --- | --- | --- |
| `email` | Ja | String | Die E-Mail-Adresse des Benutzers (muss mindestens eine Adresse und höchstens 50 Adressen enthalten). |
| `phone` | Ja | String | Die Telefonnummer des Benutzers (muss mindestens eine Telefonnummer und höchstens 50 Telefonnummern enthalten). Wir empfehlen, dies im Format E.164 bereitzustellen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request GET 'https://rest.iad-01.braze.com/users/subscriptions?phone=+12123355555&email=example%40braze.com' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Antwort

Die Einträge sind in absteigender Reihenfolge aufgeführt.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "emails": [
    {
      "email": "example@braze.com",
      "email_subscribe": {
        "email_subscription_event_date": "2019-11-20T19:58:04.825Z",
        "email_subscription_state": "Subscribed"
      },
      "subscription_group": [
        {
          "subscription_group_id": "5f5536d2a76e0f4e323a1234",
          "subscription_group_event_date": "2021-03-11T21:29:22.347Z",
          "subscription_group_state": "Unsubscribed"
        }
      ],
      "hard_bounced_at": null,
      "spam_at": null
    }
  ],
	"phone": [{
		"phone": "+12123355555",
		"subscription_group": [{
			"subscription_group_id": "3f5536d2a76e0f4e323a5555",
			"subscription_group_state": "Subsscribed",
			"subscription_group_event_date": "2021-03-11T21:29:22.347Z"
		}]
	}],
	"message": "success"
}
```

{% endapi %}
