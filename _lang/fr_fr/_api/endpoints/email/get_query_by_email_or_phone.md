---
nav_title: "GET : Répertorier l’état de l’abonnement avec l’adresse e-mail ou le numéro de téléphone"
article_title: "GET : Répertorier l’état de l’abonnement avec l’adresse e-mail ou le numéro de téléphone"
search_tag: Endpoint
page_order: 2
hidden: true
layout: api_page
page_type: reference
description: "Cet article décrit les détails de l’état d’abonnement à la liste avec une adresse e-mail ou un point de terminaison Braze de numéro de téléphone."

---
{% api %}
# Répertorier l’état de l’abonnement avec une adresse e-mail ou un numéro de téléphone
{% apimethod get %}
/users/subscription
{% endapimethod %}

> Utilisez ce point de terminaison pour renvoyer la valeur de l’état de l’abonnement en fonction d’une adresse e-mail ou d’un numéro de téléphone.

## Paramètres de demande

| Paramètre | Obligatoire | Type de données | Descriptif |
| --- | --- | --- | --- |
| `email` | Oui | Chaîne | L’adresse e-mail de l’utilisateur (doit inclure au moins une adresse et au maximum 50 adresses). |
| `phone` | Oui | Chaîne | Le numéro de téléphone de l’utilisateur (doit inclure au moins un numéro de téléphone et au maximum 50 numéros de téléphone). Nous vous recommandons de le fournir au format E.164\. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request GET 'https://rest.iad-01.braze.com/users/subscriptions?phone=+12123355555&email=example%40braze.com' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Réponse

Les entrées sont répertoriées par ordre décroissant.

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