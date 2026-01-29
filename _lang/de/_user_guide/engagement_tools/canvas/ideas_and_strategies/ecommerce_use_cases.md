---
nav_title: E-Commerce Anwendungsfälle
article_title: E-Commerce Anwendungsfälle
alias: /ecommerce_use_cases/
page_order: 4
description: "Dieser Artikel referenziert mehrere vorgefertigte Templates von Braze, die speziell auf E-Commerce Marketer zugeschnitten sind und die Umsetzung wichtiger Strategien erleichtern."
toc_headers: h2
---

# So nutzen Sie die vom E-Commerce empfohlenen Veranstaltungen

> Auf dieser Seite erfahren Sie, wie und wo Sie die empfohlenen E-Commerce-Ereignisse auf der gesamten Plattform verwenden können, einschließlich der Verwendung von Braze E-Commerce Canvas Templates.

{% alert important %}
[E-Commerce empfohlene Veranstaltungen]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/) sind derzeit im frühen Zugriff. Wenden Sie sich an Ihren Customer-Success-Manager:in von Braze, wenn Sie an diesem frühzeitigen Zugang teilnehmen möchten. <br><br>Wenn Sie den neuen Shopify Konnektor verwenden, werden die empfohlenen E-Commerce-Ereignisse automatisch über die Integration verfügbar sein.
{% endalert %}

## Verwendung einer Canvas-Vorlage

So verwenden Sie eine Canvas-Vorlage:
1. Gehen Sie zu **Messaging** > **Canvas**.
2. Wählen Sie **Canvas erstellen** > **Eine Canvas-Vorlage verwenden**.
3. Suchen Sie auf dem Tab **Braze-Vorlagen** nach der gewünschten Vorlage. Sie können eine Vorschau eines Templates anzeigen, indem Sie seinen Namen auswählen.
4. Wählen Sie **Vorlage anwenden** für die Vorlage, die Sie verwenden möchten.<br><br>![Die Seite "Canvas-Vorlagen" wurde auf dem Tab "Braze-Vorlagen" geöffnet und zeigt eine Liste der zuletzt verwendeten Templates und der auswählbaren Braze-Vorlagen.]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## E-Commerce Canvas Templates

Braze bietet vier E-Commerce Canvas Templates an.

{% multi_lang_include canvas/ecommerce_templates.md %}

## Personalisierung von Nachrichten

[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) ist eine leistungsstarke Template-Sprache, die von Braze verwendet wird und mit der Sie dynamische und personalisierte Inhalte für Ihre Kund:in erstellen können. Mit Liquid-Tags können Sie Nachrichten auf der Grundlage von Kundendaten, Produktinformationen und anderen Variablen anpassen, um das Einkaufserlebnis zu verbessern und das Engagement zu fördern.

### Wichtigste Features von Liquid

- **Dynamische Inhalte:** Fügen Sie kundenspezifische Informationen wie Namen, Bestelldetails und Präferenzen in Ihre Nachrichten ein.
- **Bedingte Logik:** Verwenden Sie if/else-Anweisungen, um anhand bestimmter Bedingungen (z.B. Standort der Kund:in und Verlauf des Einkaufs) unterschiedliche Inhalte anzuzeigen.
- **Schleifen:** Iterieren Sie über Sammlungen von Produkten oder Kundendaten, um Listen oder Raster von Artikeln anzuzeigen.

### Erste Schritte mit Liquid

Um mit der Personalisierung Ihrer Nachrichten mit Liquid-Tags zu beginnen, können Sie auf die folgenden Ressourcen referenzieren:

- [Shopify Daten]({{site.baseurl}}/shopify_features/#shopify-data) referenzieren mit vordefinierten Liquid-Tags
- [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)

## Segmentierung

Verwenden Sie Braze Segmente, um gezielte Kundensegmente auf der Grundlage bestimmter Attribute und Verhaltensweisen zu erstellen und personalisierte Messaging-Nachrichten und Kampagnen zu liefern. Mit diesem leistungsstarken Feature können Sie Ihre Kund:in effektiv einbinden, indem Sie die richtige Zielgruppe mit der richtigen Nachricht zur richtigen Zeit erreichen.

Weitere Informationen zu den ersten Schritten mit Segmenten finden Sie unter [Über Braze Segmente]({{site.baseurl}}/user_guide/engagement_tools/segments#about-braze-segments).

### Empfohlene Ereignisse

Die E-Commerce-Ereignisse basieren auf den [empfohlenen Ereignissen]({{site.baseurl}}/recommended_events/).
Da es sich bei den empfohlenen Events um angepasste Events handelt, können Sie nach den Namen der empfohlenen E-Commerce Events suchen, indem Sie einen beliebigen [angepassten Event-Filter]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#segmentation-filters) auswählen.

### E-Commerce Filter

Segmentieren Sie Ihre Nutzer:innen mit E-Commerce-Filtern, wie z.B. **E-Commerce-Quelle** und **Gesamtumsatz**, indem Sie den Abschnitt **E-Commerce** im Segmentierer aufrufen. 

Eine Liste der E-Commerce-Filter und ihrer Definitionen finden Sie unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) und wählen Sie die Suchkategorie "E-Commerce".

![Segmente Filter Dropdown mit "E-Commerce" Filtern.]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:50%"}

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation for eCommerce filters' %}

## Verschachtelte Event-Eigenschaften

Um nach verschachtelten Event-Eigenschaften zu segmentieren, können Sie [Segment-Erweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#why-use-segment-extensions) nutzen. Mit Segment-Erweiterungen können Sie zum Beispiel herausfinden, wer das Produkt "SKU-123" in den letzten 90 Tagen gekauft hat.

## Analytics

### Angepasste Events Bericht

Im [Bericht Angepasste Events]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/#analytics) können Sie das Volumen der im E-Commerce empfohlenen Events verfolgen. Filtern Sie nach **Angepasstes Event durchführen** und geben Sie dann den [Namen des empfohlenen E-Commerce Events]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/#types-of-ecommerce-recommended-events) an, um dessen Performance im Zeitverlauf zu sehen.

![Angepasstes Chart für Events, das die Ergebnisse für sechs angepasste Events anzeigt.]({% image_buster /assets/img/ecommerce/custom_events_chart.png %})

### Bericht über Konversionen 

### Angepasste Events Bericht

Um einen [Bericht über angepasste Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#analytics) zu erstellen, der darauf basiert, wer ein durch die Integration unterstütztes Event durchgeführt hat, können Sie den spezifischen [Eventnamen]({{site.baseurl}}/shopify_data_features/) angeben.

### Dashboards

#### Dashboard für Konversionen

Um Insights zu den Trends bei den Bestellungen zu erhalten, die von Ihren lancierten Canvase aus getätigt wurden, richten Sie ein [Dashboard für Konversionen]({{site.baseurl}}/user_guide/data_and_analytics/analytics/conversions_dashboard#conversions-dashboard) ein und geben Ihre Canvase an.

#### E-Commerce Umsatz Dashboard

Um Insights über die Attribution der letzten Kampagne oder des letzten Canvas zu erhalten, mit dem ein Nutzer:innen vor der Bestellung interagiert hat, verwenden Sie das [Dashboard für E-Commerce-Umsätze]({{site.baseurl}}/ecommerce_revenue_dashboard/) und wählen Sie ein Konversionsfenster aus.

### Abfrage-Builder

### Bericht über die Einnahmen 

Um Daten aus diesen neuen Ereignissen zu analysieren, gehen Sie zum [Dashboard Builder]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/) und sehen Sie sich das [Dashboard**E-Commerce Umsatz - Last Touch Attribution**]({{site.baseurl}}/ecommerce_revenue_dashboard/) an.
