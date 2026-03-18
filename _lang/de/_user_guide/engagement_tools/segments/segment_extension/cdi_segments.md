---
nav_title: CDI-Segment-Erweiterungen
article_title: CDI-Segment-Erweiterungen
page_order: 0
page_type: reference
alias: /cdi_segment_extensions/
tool: 
- Segments
description: "In diesem Artikel erfahren Sie, wie Sie das Location Targeting einrichten, mit dem Sie Nutzer nach ihrem Standort segmentieren können."

---

# CDI-Segment-Erweiterungen

> Mit Braze [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/) (CDI) können Sie eine direkte Verbindung von Ihrem Data Warehouse oder Dateispeichersystem zu Braze einrichten, um relevante Benutzer- oder Katalogdaten in regelmäßigen Abständen zu synchronisieren.

{% alert warning %}
CDI-Segment-Erweiterungen fragen Ihr Data Warehouse direkt ab, sodass Ihnen alle Kosten entstehen, die mit der Ausführung dieser Abfragen in Ihrem Data Warehouse verbunden sind. CDI-Segment-Erweiterungen verbrauchen keine [SQL-Segment-Credits]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#monitoring-your-sql-segments-usage), werden nicht auf Ihr Limit für Segment-Erweiterungen angerechnet und protokollieren keine Datenpunkte.
{% endalert %}

## Voraussetzungen

Um Ihre Data Warehouse-Daten für die Segmentierung in Ihrem Braze-Arbeitsbereich zu verwenden, müssen Sie eine [verbundene Quelle]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/) erstellen und dann ein CDI-Segment innerhalb Ihrer [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) erstellen. Mit CDI-Segment-Erweiterungen können Sie SQL-Befehle schreiben, die Ihr eigenes Data Warehouse direkt abfragen, indem Sie die über Ihre CDI-Verbindungen verfügbaren Daten nutzen, und eine Gruppe von Nutzer:innen erstellen, die innerhalb von Braze angesprochen werden können.

## Ein CDI-Segment erstellen

### Schritt 1: Richten Sie Ihre Quelle ein

Bevor Sie Ihre erste CDI-Segment-Erweiterung erstellen, richten Sie bitte eine neue verbundene Quelle mit Ihrem Data Warehouse ein, indem Sie die Schritte unter [„Verbundene Quellen“]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/) befolgen.

### Schritt 2: Ein Segment erstellen

Erstellen Sie zunächst eine neue [Segmenterweiterung]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) und wählen Sie dann **Vollständige Aktualisierung**.

![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:60%;"}

Wählen Sie für Ihre Datenquelle **CDI-Datentabellen**.

![]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:60%;"}

Im Rahmen Ihrer CDI-Konfiguration können Sie aus verschiedenen Verbindungen auswählen, die in CDI-Segment-Erweiterungen verwendet werden sollen. Jede Verbindung hat einen bestimmten Satz von Datentabellen. Ihr Entwicklungsteam kann Ihre Verbindungen und Datentabellen während der CDI-Einrichtung konfigurieren.

Um die verfügbaren Datentabellen einschließlich ihres Schemas und aller verfügbaren Beschreibungen anzuzeigen, wählen Sie **„Referenz**“. Wenn Sie bereit sind, wählen Sie eine Verbindung aus.

![]({% image_buster /assets/img/segment/connection_schema_with_descriptions.png %}){: style="max-width:100%;"}

Als Nächstes schreiben Sie das SQL für Ihr Segment mit [der Braze SQL-Syntax]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#writing-sql).

Bitte beachten Sie, dass alle CDI-Segment-Erweiterungen die ausgewählte Spalte verwenden müssen`external_user_id`und Ihre mit der in Braze für Nutzer:innen`external_user_id` festgelegten übereinstimmen sollte.

{% alert important %}
`external_user_id` muss ein **String**-Wert sein. Wenn Ihre Quell-ID als Zahl gespeichert ist (z. B.`client_id`als Ganzzahl), [wandeln Sie sie in Ihrer SQL in einen String um](https://www.w3schools.com/sql/func_sqlserver_cast.asp), damit sie mit dem`external_id`Typ in Braze übereinstimmt.
{% endalert %}

Sollten Ihre Suchergebnisse Nutzer:innen enthalten, die nicht in Braze vorhanden sind, werden diese Nutzer:innen ignoriert. Braze erstellt keine neuen Nutzer:innen auf Grundlage der Ausgabe Ihrer CDI-Segment-Erweiterungen.

{% alert tip %}
Informationen dazu, wie Sie eine Vorschau Ihrer Segment-Erweiterungen anzeigen, Ihre Segment-Erweiterungen verwalten und automatische Aktualisierungen der Mitgliedschaft durchführen können, finden Sie unter [SQL-Segment-Erweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/).
{% endalert %}

Schließlich können Sie [diese Segmenterweiterung innerhalb eines Braze-Segments verwenden]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-5-use-your-extension-in-a-segment), um eine Kampagne oder ein Canvas an diese Zielgruppe zu senden.

## Überlegungen

- Eine Segmenterweiterung kann nur auf Daten aus einer Verbindung verweisen, nicht aus mehreren.    
- Eine Segmenterweiterung kann eine der folgenden Datenquellen verwenden: CDI-Daten oder Braze Snowflake (Ströme) Daten. Sie können innerhalb einer Segmenterweiterung keine Datenquellen mischen, aber Sie können mehrere Segmenterweiterungen erstellen, auf die Sie innerhalb eines Segments gemeinsam verweisen können.

## Fehlersuche

- Ihre Abfrage kann eine Zeitüberschreitung erleiden, wenn sie die maximale Laufzeit erreicht, die für jede Verbindungssynchronisation auf der Seite **Cloud Data Ingestion** eingestellt ist. Die maximal zulässige Laufzeit beträgt 60 Minuten.
- Vergewissern Sie sich, dass Ihr SQL in einer für Ihr Data Warehouse geeigneten Syntax geschrieben ist. 
