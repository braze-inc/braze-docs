---
nav_title: "Kundenverhalten und Nutzer:innen-Events"
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "In diesem Glossar finden Sie eine Auflistung der verschiedenen Kundenverhaltens- und Benutzerereignisse, die Braze mit Currents verfolgen und an ausgewählte Data Warehouses senden kann."
tool: Currents
search_rank: 7
---

Wenden Sie sich an Ihre Braze-Vertretung oder öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/), wenn Sie Zugang zu zusätzlichen Event-Berechtigungen benötigen. Wenn Sie auf dieser Seite nicht finden können, was Sie brauchen, sehen Sie sich unsere [Bibliothek mit den Ereignissen zum Thema Message Engagement]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) oder unsere [Beispieldaten von Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data) an.

{% details Erläuterung des Kundenverhaltens und der Nutzer:in-Event-Struktur und Plattformwerte %}

### Event-Struktur

Diese Aufschlüsselung des Kundenverhaltens und der Benutzerereignisse zeigt, welche Art von Informationen im Allgemeinen in einem Kundenverhalten oder Benutzerereignis enthalten sind. Mit einem soliden Verständnis seiner Komponenten können Ihre Entwickler:in und Ihr Business-Intelligence Strategie Team die eingehenden Currents Ereignisdaten nutzen, um datengestützte Berichte und Charts zu erstellen und andere wertvolle Metriken zu nutzen.

![Aufschlüsselung eines Benutzerereignisses, das ein Kaufereignis mit den aufgelisteten Eigenschaften gruppiert nach benutzerspezifischen Eigenschaften, verhaltensspezifischen Eigenschaften und gerätespezifischen Eigenschaften zeigt]({% image_buster /assets/img/customer_engagement_event.png %})

Kundenverhalten und Nutzer-Events setzen sich aus **nutzerspezifischen** Eigenschaften, **verhaltensspezifischen** Eigenschaften und **gerätespezifischen** Eigenschaften zusammen.

### Plattformwerte

Bestimmte Ereignisse geben einen `platform`-Wert zurück, der die Plattform des Nutzergeräts angibt.
<br>In der folgenden Tabelle finden Sie die möglichen Rückgabewerte:

| Nutzer:in-Gerät | Plattformwert |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Internet | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% enddetails %}

{% alert important %}
Speicherschemata gelten für die Flat File-Event-Daten, die wir an Data Warehouse-Speicherpartner (wie Google Cloud Storage, Amazon S3 und Microsoft Azure Blob Storage) senden. Einige der hier aufgeführten Kombinationen von Veranstaltungen und Zielen sind noch nicht allgemein verfügbar. Informationen darüber, welche Veranstaltungen von verschiedenen Partnern unterstützt werden, finden Sie in unserer Liste der [verfügbaren Partner]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) und auf den jeweiligen Seiten.<br><br>Beachten Sie außerdem, dass Currents Events mit übermäßig großen Nutzlasten von mehr als 900 KB löscht.
{% endalert %}