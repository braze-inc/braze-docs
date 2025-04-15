---
nav_title: "LÖSCHEN: Abonnementstatus nach E-Mail-Adresse oder Telefonnummer löschen"
article_title: "LÖSCHEN: Abonnementstatus nach E-Mail-Adresse oder Telefonnummer löschen"
search_tag: Endpoint
page_order: 0
hidden: true
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts Abonnementstatus nach E-Mail-Adresse oder Telefonnummer löschen."

---

{% api %}
# Abonnementstatus nach E-Mail-Adresse oder Telefonnummer löschen
{% apimethod delete %}
/users/subscription
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um den Wert des Abonnementstatus basierend auf einer E-Mail-Adresse oder Telefonnummer zu löschen.

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| --- | --- | --- | --- |
| `email` | Ja | String | Die E-Mail-Adresse des Benutzers (muss mindestens eine Adresse und höchstens 50 Adressen enthalten). |
| `phone` | Ja | String | Die Telefonnummer des Benutzers (muss mindestens eine Telefonnummer und höchstens 50 Telefonnummern enthalten). Wir empfehlen, dies im Format E.164 bereitzustellen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  {phone: "+12125551212"},
  {email: "dont.spam@me.com"},
  {phone: "+17185551212"}
}
```

## Antwort

```json
{
  "status": "The emails and/or phone numbers have been queued for deletion",
  "message": "success"
}
```

{% endapi %}
