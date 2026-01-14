---
nav_title: Anwendungsfälle
article_title: Braze Anwendungsfälle zur Datentransformation
page_order: 2
page_type: reference
description: "Dieser referenzierte Artikel enthält einige Anwendungsfälle für Braze Data Transformation."
---

# Anwendungsfälle der Datentransformation

> Betrachten Sie die folgenden möglichen Anwendungsfälle mit Braze Data Transformation und einer Kombination aus Webhooks von den beispielhaften externen Plattformen.

## Leads generieren

Sie hosten ein Typeform-Formular zur Lead-Generierung auf Ihrer Website. Wenn neue Nutzer:innen dieses Formular ausfüllen, können Sie:
- Erstellen Sie neue Nutzer:innen in Braze.
- Fügen Sie sie zu einer Ihrer E-Mail-Listen von Braze hinzu.
- Synchronisieren Sie einige ihrer Antworten als angepasste Attribute in Braze, denn ihre Antworten sind wertvolle First-Party-Daten, die in Zukunft für personalisierte Messaging-Erlebnisse genutzt werden können.

## Öffnung von Dienst-Tickets

Wenn Kunden:in Tickets für den Dienst auf einer Plattform wie Zendesk öffnen, können Sie diese anpassen:
- Schreiben Sie ein angepasstes Event in Braze, wenn ein Zendesk Ticket erstellt wird.
- Schreiben Sie ein angepasstes Event mit Event-Eigenschaften in Braze, wenn eine negative CSAT-Bewertung an Zendesk übermittelt wird.

## Integration mit Braze

Braze verfügt über eine Integration mit [Iterate]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/surveys/iterate/), einer Plattform für Insights und Umfragen. Mit der Datentransformation können Sie mehrere Antworten auf Umfragen unter einem verschachtelten angepassten Attribut speichern, anstatt wie bei der bestehenden Integration mehrere angepasste Attribute zu speichern.

## Beispiel für einen Code zur Transformation

Sehen Sie sich diese Beispiel-Payload von Typeform an, einer Plattform für Umfragen, die immer dann gesendet wird, wenn eine Antwort auf eine Umfrage eingegangen ist.

![]({% image_buster /assets/img/data_transformation/data_transformation2.png %})

{% tabs local %}
{% tab Basic transformation %}

Dieses Beispiel nimmt die Antworten auf Umfragen als Attribute und schreibt ein Ereignis, um anzuzeigen, dass die Umfrage abgeschlossen wurde:

```
return {
  "attributes": [ 
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "home_city": payload.form_response.answers[0].text,
      "home_weather_rating": payload.form_response.answers[1].number
    }
  ],
  "events": [ 
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": new Date(),
      "properties": {
        "form_id": payload.form_response.form_id
      }
    }
  ]
}
```

{% endtab %}
{% tab Advanced transformation %}

Lassen Sie uns das Beispiel für die grundlegende Transformation weiter ausbauen und eine `if` Anweisung einführen, um den Nutzer:innen in eine der Antworten einzuordnen.

```
let nps_category;
let nps_number = payload.form_response.answers[1].number;
if (nps_number < 7) {
  nps_category = "Detractor";
} else if (nps_number == 7 || nps_number == 8) {
  nps_category = "Passive";
} else if (nps_number > 8) {
  nps_category = "Promoter";
}

return {
  "attributes": [ 
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "home_city": payload.form_response.answers[0].text,
      "home_weather_NPS_category": nps_category
    }
  ],
  "events": [
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": new Date(),
      "properties": {
        "form_id": payload.form_response.form_id
      }
    }
  ]
};
```
{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/data_transformation/data_transformation2.png %}