---
nav_title: Datentransformation
article_title: Datentransformation
page_order: 0.3
layout: dev_guide
guide_top_header: "Datentransformation"
guide_top_text: "Braze Data Transformation erlaubt es Ihnen, Webhook-Integrationen zu erstellen und zu verwalten, um den Datenfluss von externen Plattformen in Braze zu automatisieren. Diese neu integrierten Benutzerdaten können dann für noch anspruchsvollere Marketinganwendungen genutzt werden. Braze Data Transformation kann Ihre Datenintegration beschleunigen, selbst wenn Sie nur wenig Erfahrung mit der Programmierung haben, und kann die Abhängigkeit Ihres Teams von manuellen API-Aufrufen, Integrations-Tools von Drittanbietern oder sogar Kundendaten-Plattformen ersetzen."
page_type: landing
description: "Auf dieser Landing Page finden Sie Artikel über die Braze Datentransformation, u.a. wie Sie eine Datentransformation erstellen und Anwendungsfälle."
alias: /data_transformation/

guide_featured_title: "Abschnittsartikel"
guide_featured_list:
  - name: Eine Transformation schaffen
    link: /docs/user_guide/data/unification/data_transformation/creating_a_transformation/
    image: /assets/img/braze_icons/flip-forward.svg
  - name: Anwendungsfälle
    link: /docs/user_guide/data/unification/data_transformation/use_cases/
    image: /assets/img/braze_icons/users-01.svg
---

## Funktionsweise

Viele moderne Plattformen verfügen über "Webhooks" oder Realtime API-Benachrichtigungen, um Informationen über ein neues Ereignis oder neue Daten von einer Plattform zur anderen zu senden. Datentransformation bietet:

* Eine Braze-URL-Adresse, um solche Webhooks zu empfangen.
* Fähigkeiten zur Transformation der Webhook-Nutzdaten mit JavaScript Code, um gültige Anfragen an verschiedene Braze API Endpunkte zu erstellen, einschließlich Braze `/users/track` oder `/catalogs`. Für das Ziel `/users/track` können Sie beispielsweise wählen, welche Informationen vom Webhook verwendet werden sollen und wie die Daten in den Benutzerprofilen von Braze als Benutzerattribute, Ereignisse oder Käufe dargestellt werden sollen.
* Protokollierung zur Qualitätssicherung, Fehlerbehebung und Überwachung der Performance Ihrer Transformationen.

Das Endergebnis ist eine Webhook-Integration, die eine Quellplattform Ihrer Wahl anbindet, indem sie deren Webhooks in Braze-Updates umwandelt.

{% details More on webhooks %}
Webhooks sind Realtime-Benachrichtigungen, die über eine HTTP POST-Anfrage an ein bestimmtes Ziel gesendet werden. Webhooks werden häufig verwendet, um Daten von einem Punkt zu einem anderen zu senden, wobei der Webhook Daten über eine stattgefundene Aktion und die an dieser Aktion beteiligten Personen übermitteln kann.

Eine Umfrageplattform kann zum Beispiel einen Webhook an ein Ziel Ihrer Wahl senden, sobald eine Umfrageantwort auf ein Online-Formular eingeht. Oder eine Kundendienstplattform kann einen Webhook an ein Ziel ihrer Wahl senden, wenn ein Ticket für den Dienst erstellt wird.
{% enddetails %}

## Datentransformationsebenen

Die folgende Tabelle beschreibt die Unterschiede zwischen der kostenlosen und der Pro-Version von Data Transformation.

| Bereich | Kostenlose Version | Datentransformation Pro |
|----|----|----|
| Aktive Transformationen | Bis zu 5 pro Unternehmen | Bis zu 55 pro Unternehmen |
| Pro Monat | 300.000 eingehende Anfragen pro Monat | 10.300.000 eingehende Anfragen pro Monat |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Um ein Upgrade auf Data Transformation Pro anzufordern, wenden Sie sich an Ihren Braze-Kundenbetreuer oder wählen Sie die Schaltfläche **Upgrade anfordern** im Braze-Dashboard.
{% endalert %}

### Rate-Limits

Das Rate-Limits für Braze Data Transformations liegt bei 1.000 eingehenden Anfragen pro Minute und Workspace. Wenn Sie Data Transformation Pro haben und ein höheres Rate-Limit benötigen, wenden Sie sich an Ihren Braze-Konto Manager:in.

## Häufig gestellte Fragen

### Was wird mit Braze Data Transformation synchronisiert?

Alle Daten, die die externe Plattform in einem Webhook zur Verfügung stellt, können mit Braze synchronisiert werden. Je mehr eine externe Plattform über Webhooks sendet, desto mehr Möglichkeiten haben Sie, auszuwählen, was synchronisiert werden soll.

### Ich bin ein Vermarkter. Benötige ich Entwickler:in, um Braze Data Transformation zu verwenden?

Wir würden uns freuen, wenn auch Entwickler diese Funktion nutzen würden, aber Sie müssen kein Entwickler sein, um diese Funktion zu nutzen! Marketer können Transformationen auch ohne Entwickler:in erfolgreich einrichten.

### Kann ich die Braze Datentransformation auch dann verwenden, wenn meine externe Plattform als Bezeichner nur eine E-Mail Adresse oder Telefonnummer angibt?

Ja Sie können Ihre Transformationen zum Update des Endpunkts `/users/track` mit der [E-Mail Adresse oder Telefonnummer als Bezeichner]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-email-address) verwenden.

Dies funktioniert, indem Sie `email` oder `phone` als Eigenschaft des Bezeichners im Code der Transformation anstelle von `external_id` oder `braze_id` verwenden. Der [Beispiel-Transformationscode]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/use_cases/#example-transformation-code) verwendet diese Funktion.

{% alert note %}
Nutzer:innen von Braze Data Transformation, die vor April 2023 begonnen haben, kennen vielleicht die Funktion `get_user_by_email`, die bei diesem Anwendungsfall hilfreich war. Diese Funktion ist jetzt veraltet.
{% endalert %}

### Protokolliert Braze Data Transformation Datenpunkte?

Ja, in den meisten Fällen. Braze Data Transformation erstellt schließlich einen `/users/track` Aufruf, der die gewünschten Attribute, Ereignisse und Käufe schreibt. Diese protokollieren die Datenpunkte so, als ob der Aufruf von `/users/track` unabhängig erfolgt wäre. Sie haben die Kontrolle darüber, wie viele Datenpunkte protokolliert werden, je nachdem, wie Sie Ihre Transformation schreiben.

### Wie kann ich Hilfe bei der Einrichtung meines Anwendungsfalls oder bei meinem Transformationscode erhalten?

Wenden Sie sich an Ihren Braze-Kundenbetreuer, wenn Sie weitere Hilfe benötigen.
