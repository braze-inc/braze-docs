---
nav_title: "DELETE : Supprimer le statut d’abonnement par adresse e-mail ou numéro de téléphone"
article_title: "DELETE : Supprimer le statut d’abonnement par adresse e-mail ou numéro de téléphone"
search_tag: Endpoint
page_order: 0
hidden: true
layout: api_page
page_type: reference
description: "Cet article présente les détails concernant l’endpoint Supprimer le statut d’abonnement par adresse e-mail ou numéro de téléphone de Braze."

---

{% api %}
# Supprimer le statut d’abonnement par adresse e-mail ou numéro de téléphone
{% apimethod delete %}
/utilisateurs/abonnement
{% endapimethod %}

> Utilisez cet endpoint pour supprimer la valeur de l'état de l'abonnement basée sur une adresse e-mail ou un numéro de téléphone.

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --- | --- | --- | --- |
| `email` | Oui | Chaîne de caractères | L'adresse e-mail de l'utilisateur (doit comprendre au moins une adresse et au plus 50 adresses). |
| `phone` | Oui | Chaîne de caractères | Le numéro de téléphone de l'utilisateur (doit comprendre au moins un numéro de téléphone et au plus 50 numéros de téléphone). Nous vous recommandons de fournir ces informations sous le format E.164. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  {phone: "+12125551212"},
  {email: "dont.spam@me.com"},
  {phone: "+17185551212"}
}
```

## Réponse

```json
{
  "status": "The emails and/or phone numbers have been queued for deletion",
  "message": "success"
}
```

{% endapi %}
