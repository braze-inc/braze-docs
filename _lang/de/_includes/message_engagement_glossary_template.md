---
nav_title: Nachrichtenengagement-Events
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "Dieses Glossar listet die verschiedenen Nachrichten Engagement Events auf, die Braze mit Currents verfolgen und an ausgewählte Data Warehouses senden kann."
tool: Currents
search_rank: 6
---

Speicherschemata gelten für die Flat File-Ereignisdaten, die wir an Data Warehouse Storage Partner (Google Cloud Storage, Amazon S3 und Microsoft Azure Blob Storage) senden. Schemata, die für andere Partner gelten, finden Sie in unserer Liste der [verfügbaren Partner]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) und auf den entsprechenden Seiten.

Wenden Sie sich an Ihren Account Manager:in oder öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/), wenn Sie Zugang zu zusätzlichen Veranstaltungsberechtigungen benötigen. Wenn Sie in diesem Artikel nicht finden, was Sie brauchen, sehen Sie sich unsere [Bibliothek für Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) oder unsere [Currents-Beispiele für Daten](https://github.com/Appboy/currents-examples/tree/master/sample-data) an.

{% details Erläuterung der Ereignisstruktur für das Engagement von Nachrichten und der Plattformwerte %}

### Event-Struktur

Diese Aufschlüsselung der Ereignisse zeigt, welche Art von Informationen im Allgemeinen in einem Ereignis zum Engagement für Nachrichten enthalten sind. Mit einem soliden Verständnis seiner Komponenten können Ihre Entwickler:in und Ihr Business-Intelligence Strategie Team die eingehenden Currents Ereignisdaten nutzen, um datengestützte Berichte und Charts zu erstellen und andere wertvolle Metriken zu nutzen.

![Aufschlüsselung eines Nachrichten-Engagements mit einem E-Mail-Abmelde-Ereignis mit den aufgeführten Eigenschaften, gruppiert nach benutzerspezifischen Eigenschaften, Kampagnen- oder Canvas-Tracking-Eigenschaften und ereignisspezifischen Eigenschaften]({% image_buster /assets/img/message_engagement_event.png %})

Nachrichten-Engagement-Ereignisse setzen sich aus **benutzerspezifischen** Eigenschaften, **Kampagnen/Canvas Tracking-Eigenschaften** und **ereignisspezifischen** Eigenschaften zusammen.

### Schema der Nutzer:innen ID

Beachten Sie die Namenskonventionen für Nutzer:innen.

| Braze Schema | Currents Schema | Beschreibung |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Der eindeutige Bezeichner, der automatisch von Braze zugewiesen wird. |
| `external_id` | `"EXTERNAL_USER_ID"` | Der eindeutige Bezeichner des Profils eines Nutzers:in, der vom Kunden festgelegt wird. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

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
Currents verwirft Events mit übermäßig großen Nutzdaten von mehr als 900 KB.
{% endalert %}

{% alert note %}
Objekte, die sich auf Canvas Flow beziehen, haben IDs, die zur Gruppierung verwendet und über den [Endpunkt Canvas-Details exportieren]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) in menschenlesbare Namen übersetzt werden können.
{% endalert %}

{% alert note %}
Bei bestimmten Feldern kann es länger dauern, bis der neueste Stand angezeigt wird, nachdem eine Kampagne oder ein Canvas aktualisiert wurde. Diese Felder sind:
<ul>
  <li>"campaign_name"</li>
  <li>"canvas_name"</li>
  <li>"canvas_step_name"</li>
  <li>"conversion_behavior"</li>
  <li>"canvas_variation_name"</li>
  <li>"experiment_split_name"</li>
  <li>"message_variation_name"</li>
</ul>
Wenn eine vollständige Konsistenz erforderlich ist, empfehlen wir, eine Stunde nach dem letzten Update dieser Felder zu warten, bevor Sie Ihre Nachrichten an Ihre Nutzer:innen versenden.
{% endalert %}