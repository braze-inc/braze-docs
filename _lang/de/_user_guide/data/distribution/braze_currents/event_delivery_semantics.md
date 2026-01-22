---
nav_title: Semantik der Zustellung von Events
article_title: Zustellung
page_order: 3
page_type: reference
description: "In diesem Referenzartikel wird erläutert und definiert, wie Currents die von uns an Data Warehouse-Speicherpartner gesendeten Flat File-Event-Daten verwaltet."
tool: Currents

---

# Semantik der Zustellung von Events

> Auf dieser Seite wird beschrieben und definiert, wie Currents die Flat File-Ereignisdaten verwaltet, die wir an Data Warehouse-Speicherpartner senden.

„Currents für Datenspeicher“ ist ein kontinuierlicher Datenstrom von unserer Plattform zu einem Speicherbereich auf einer unserer Data Warehouse-[Partnerverbindungen]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/). Currents schreibt Avro-Dateien in regelmäßigen Abständen in Ihren Speicher-Bucket, sodass Sie die Event-Daten mit Ihrem eigenen Business Intelligence (BI)-Toolset verarbeiten und analysieren können.

{% alert important %}
Dieser Content **gilt nur für die Flat File-Event-Daten, die wir an Data Warehouse-Speicherpartner (Google Cloud Storage, Amazon S3 und Microsoft Azure Blob Storage) senden**. <br><br>Inhalte, die für andere Partner gelten, finden Sie in unserer Liste der [verfügbaren Partner]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) und auf den jeweiligen Seiten.
{% endalert %}

## Mindestens einmal durchgeführte Zustellung

Als System mit hohem Durchsatz bietet Currents eine Zustellung von Events, die mindestens einmal erfolgt, was bedeutet, dass gelegentlich doppelte Events in Ihren Speicherbereich geschrieben werden können. Dies kann passieren, wenn Events aus unserer Warteschlange aus irgendeinem Grund erneut verarbeitet werden.

Wenn Ihre Anwendungsfälle eine „exakt einmalige“ Zustellung erfordern, können Sie das Feld „Eindeutiger Bezeichner“ verwenden, das mit jedem Event (`id`) gesendet wird, um Events zu deduplizieren. Da die Datei unsere Kontrolle verlässt, wenn sie in Ihren Bucket geschrieben wird, können wir die Deduplizierung von unserer Seite aus nicht garantieren.

## Zeitstempel

Alle von Currents exportierten Zeitstempel werden in der UTC-Zeitzone gesendet. Bei einigen Events, bei denen dies möglich ist, wird auch ein Feld für die Zeitzone angezeigt, das das IANA-Format (Internet Assigned Numbers Authority) der lokalen Zeitzone des Nutzers oder der Nutzerin zum Zeitpunkt des Events anzeigt.

### Latenz

Events, die über SDK oder API an Braze gesendet werden, können einen Zeitstempel aus der Vergangenheit enthalten. Das auffälligste Beispiel ist die Warteschlange für SDK-Daten, z. B. wenn keine mobile Verbindung besteht. In diesem Fall gibt der Zeitstempel des Events an, wann der Event erzeugt wurde. Das bedeutet, dass ein bestimmter Prozentsatz der Ereignisse eine hohe Latenzzeit aufweist.

## Apache Avro Format

Die Braze-Currents-Integrationen zur Datenspeicherung geben Daten im Format `.avro` aus. Wir haben uns für [Apache Avro](https://avro.apache.org/) entschieden, weil es ein flexibles Datenformat ist, das von Haus aus die Entwicklung von Schemata unterstützt und von einer Vielzahl von Datenprodukten unterstützt wird: 

- Avro wird von fast allen großen Data Warehouses unterstützt.
- Falls Sie Ihre Daten in S3 belassen möchten, komprimiert Avro besser als CSV und JSON, sodass Sie weniger für die Speicherung bezahlen und möglicherweise weniger CPU zum Parsen der Daten verwenden müssen.
- Avro benötigt Schemata, wenn Daten geschrieben oder gelesen werden. Schemas können im Laufe der Zeit weiterentwickelt werden, um das Hinzufügen von Feldern zu verarbeiten, ohne dass es zu Brüchen kommt.

Currents erstellt für jeden Event-Typ eine Datei in folgendem Format:

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>/event_type=<event-type>/date=<date>/<schema-id>/<zone>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>+<partition>+<offset>.avro
```

{% alert tip %}
Sie können den Code wegen der Bildlaufleiste nicht sehen? Erfahren Sie [hier]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/), wie Sie das beheben können.
{% endalert %}

|Dateiname Segment |Definition|
|---|---|
| `<your-bucket-prefix>` | Das Präfix, das für diese Currents-Integration festgelegt wurde. |
| `<cluster-identifier>` | Zur internen Verwendung durch Braze. Wird ein String wie „prod-01“, „prod-02“, „prod-03“ oder „prod-04“ sein. Alle Dateien haben denselben Bezeichner für den Cluster.|
| `<connection-type-identifier>` | Der Bezeichner für die Art der Verbindung. Optionen sind „S3“, „AzureBlob“ oder „GCS“. |
| `<integration-id>` | Die eindeutige ID für diese Currents-Integration. |
| `<event-type>` | Der Typ des Events in der Datei. |
| `<date>` | Die Stunde, in der Ereignisse in unserem System zur Verarbeitung in der UTC-Zeitzone in die Warteschlange gestellt werden. Im Format JJJJ-MM-TT-HH. |
| `<schema-id>` | Wird zur Versionierung von `.avro`-Schemata für Abwärtskompatibilität und Schemaentwicklung verwendet. Ganzzahl. |
| `<zone>` | Zur internen Verwendung durch Braze. |
| `<partition>` | Zur internen Verwendung durch Braze. Ganzzahl. |
| `<offset>`| Zur internen Verwendung durch Braze. Ganzzahl. Beachten Sie, dass verschiedene Dateien, die innerhalb derselben Stunde gesendet werden, einen anderen `<offset>`-Parameter haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Die Namenskonventionen für Dateien können sich in Zukunft ändern. Braze empfiehlt, alle Schlüssel in Ihrem Bucket zu durchsuchen, die das Präfix <your-bucket-prefix> haben.
{% endalert %}

### Avro Schreibschwelle

Unter normalen Umständen schreibt Braze alle 5 Minuten oder 15.000 Ereignisse, je nachdem, was früher eintritt, Daten in Ihren Bucket. Bei starker Belastung können wir größere Daten mit bis zu 100.000 Events pro Datei schreiben.

{% alert important %}
Currents wird niemals leere Dateien schreiben.
{% endalert %}

### Änderungen am Avro-Schema

Von Zeit zu Zeit kann Braze Änderungen am Avro-Schema vornehmen, wenn Felder hinzugefügt, geändert oder entfernt werden. Für unsere Zwecke gibt es hier zwei Arten von Änderungen: wesentliche und unwesentliche. In allen Fällen wird `<schema-id>` vorangetrieben, um anzuzeigen, dass das Schema aktualisiert wurde. Bei aktuellen Events, die in Azure Blob Storage, Google Cloud Storage und Amazon S3 geschrieben werden, wird die `<schema-id>` in den Pfad geschrieben. Zum Beispiel `<your-bucket-name0>/<currents-integration-id>/<event-type>/<date-of-event>/<schema-id>/<environment>/<avro-file>`.

#### Unwesentliche Änderungen

Wenn ein Feld zum Avro-Schema hinzugefügt wird, betrachten wir dies als eine unwesentliche Änderung. Hinzugefügte Felder sind immer "optionale" Avro-Felder (z.B. mit einem Standardwert von `null`), so dass sie gemäß der [Avro-Schemaauflösungsspezifikation](http://avro.apache.org/docs/current/spec.html#schema+resolution) mit älteren Schemata "übereinstimmen". Diese Ergänzungen sollten sich nicht auf bestehende ETL-Prozesse (Extract, Transform, Load) auswirken, da das Feld einfach ignoriert wird, bis es Ihrem ETL-Prozess hinzugefügt wird. 

{% alert important %}
Um zu vermeiden, dass der Ablauf unterbrochen wird, wenn neue Felder hinzugefügt werden, empfehlen wir, dass Sie in Ihr ETL-Setup explizit angeben, welche Felder verarbeitet werden.
{% endalert %}

Wir bemühen uns, Sie im Voraus über alle Änderungen zu informieren, können jedoch jederzeit unwesentliche Änderungen am Schema vornehmen.

#### Wesentliche Änderungen

Wenn ein Feld aus dem Avro-Schema entfernt oder geändert wird, betrachten wir dies als eine wesentliche Änderung. Wesentliche Änderungen können Änderungen an bestehenden ETL-Prozessen erfordern, da Felder, die verwendet wurden, möglicherweise nicht mehr wie erwartet aufgezeichnet werden.

Alle wesentlichen Änderungen am Schema werden vor der Änderung mitgeteilt.
