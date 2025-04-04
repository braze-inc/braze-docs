---
nav_title: CDI Segmente
article_title: CDI Segmente
page_order: 0
page_type: reference
tool: 
- Segments
description: "In diesem Artikel erfahren Sie, wie Sie das Location Targeting einrichten, mit dem Sie Nutzer nach ihrem Standort segmentieren können."

---

# CDI-Segmente

> Mit Braze [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/) (CDI) können Sie eine direkte Verbindung von Ihrem Data Warehouse oder Dateispeichersystem zu Braze einrichten, um relevante Benutzer- oder Katalogdaten in regelmäßigen Abständen zu synchronisieren.

{% alert warning %}
Dieses Feature fragt Ihr Data Warehouse direkt ab, so dass Ihnen alle Kosten entstehen, die mit der Ausführung dieser Abfragen in Ihrem Data Warehouse verbunden sind. CDI-Segmente verbrauchen kein [SQL-Segmentguthaben]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#monitoring-your-sql-segments-usage), zählen nicht zu Ihrem Segmenterweiterungslimit und verbrauchen keine Datenpunkte.
{% endalert %}

## Voraussetzungen

Um Ihre Data Warehouse-Daten für die Segmentierung in Ihrem Braze-Arbeitsbereich zu verwenden, müssen Sie eine [verbundene Quelle]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/) erstellen und dann ein CDI-Segment innerhalb Ihrer [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) erstellen. CDI-Segmente ermöglichen es Ihnen, SQL zu schreiben, das Ihr eigenes Data Warehouse direkt abfragt, indem Sie Daten verwenden, die über Ihre CDI-Verbindungen zur Verfügung gestellt werden, und eine Gruppe von Benutzern zu erstellen, die in Braze gezielt angesprochen werden können.

## Ein CDI-Segment erstellen

### Schritt 1: Richten Sie Ihre Quelle ein

Bevor Sie Ihr erstes CDI-Segment erstellen, richten Sie eine neue Connected Source mit Ihrem Data Warehouse ein, indem Sie die Schritte unter [Connected Sources]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/) ausführen.

### Schritt 2: Ein Segment erstellen

Erstellen Sie zunächst eine neue [Segmenterweiterung]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) und wählen Sie dann **Vollständige Aktualisierung**.

![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:70%;"}

Wählen Sie für Ihre Datenquelle **CDI-Datentabellen**.

![]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:80%;"}

Als Teil Ihrer CDI-Einrichtung können Sie aus verschiedenen Verbindungen wählen, die Sie in CDI-Segmenten verwenden möchten. Jede Verbindung hat einen bestimmten Satz von Datentabellen. Ihr Entwicklungsteam kann Ihre Verbindungen und Datentabellen während der CDI-Einrichtung konfigurieren.

Um die verfügbaren Datentabellen anzuzeigen, wählen Sie **Referenz**. Wenn Sie bereit sind, wählen Sie eine Verbindung aus.

![]({% image_buster /assets/img/segment/connection_schema.png %}){: style="max-width:100%;"}

Als Nächstes schreiben Sie das SQL für Ihr Segment mit [der Braze SQL-Syntax]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#writing-sql).

Denken Sie daran, dass alle CDI-Segmente `external_user_id` als ausgewählte Spalte verwenden müssen, und dass Ihre `external_user_id` mit der in Braze für Benutzer eingestellten Spalte übereinstimmen sollte. Wenn Ihre Abfrageergebnisse Nutzer:innen enthalten, die in Braze nicht existieren, werden diese Nutzer:innen ignoriert. Braze erstellt keine neuen Benutzer auf der Grundlage der Ausgabe Ihres CDI-Segments.

{% alert tip %}
Wie Sie eine Vorschau Ihres Segments anzeigen, Ihr Segment verwalten und automatische Mitgliedschaftsaktualisierungen durchführen können, erfahren Sie unter [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/).
{% endalert %}

Schließlich können Sie [diese Segmenterweiterung innerhalb eines Braze-Segments verwenden]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-5-use-your-extension-in-a-segment), um eine Kampagne oder ein Canvas an diese Zielgruppe zu senden.

## Überlegungen

- Eine Segmenterweiterung kann nur auf Daten aus einer Verbindung verweisen, nicht aus mehreren.    
- Eine Segmenterweiterung kann eine der folgenden Datenquellen verwenden: CDI-Daten oder Braze Snowflake (Ströme) Daten. Sie können innerhalb einer Segmenterweiterung keine Datenquellen mischen, aber Sie können mehrere Segmenterweiterungen erstellen, auf die Sie innerhalb eines Segments gemeinsam verweisen können.

## Fehlersuche

- Ihre Abfrage kann eine Zeitüberschreitung erleiden, wenn sie die maximale Laufzeit erreicht, die für jede Verbindungssynchronisation auf der Seite **Cloud Data Ingestion** eingestellt ist. Die maximal zulässige Laufzeit beträgt 60 Minuten.
- Vergewissern Sie sich, dass Ihr SQL in einer für Ihr Data Warehouse geeigneten Syntax geschrieben ist. 
