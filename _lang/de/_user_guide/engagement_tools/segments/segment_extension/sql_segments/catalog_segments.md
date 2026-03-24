---
nav_title: "Katalog-Segmente"
article_title: Katalog-Segmente
page_order: 0
page_type: reference
alias: "/catalog_segments/"
description: "Dieser Artikel erläutert, wie Sie Katalogsegmente erstellen und mithilfe von Katalogdaten in SQL-Segmenterweiterungen Zielgruppen aus Nutzer:innen bilden."
tool: Segments
---

# Katalog-Segmente

> Katalogsegmente sind eine Art von SQL-Segmenterweiterung, die durch die Kombination von Katalogdaten mit Daten aus angepassten Events oder Käufen erstellt wird. Sie können in einem Segment referenziert und dann durch Kampagnen und Canvase gezielt angesprochen werden. 

Katalogsegmente führen Daten aus Katalogen und angepassten Events oder Käufen per SQL zusammen. Dazu benötigen Sie ein einheitliches Bezeichnerfeld in Katalogen und angepassten Events oder Käufen. Zum Beispiel muss der Wert einer Artikel-ID in einem Katalog mit dem Wert einer Eigenschaft in einem angepassten Event übereinstimmen.

## Katalogsegmente erstellen

1. Gehen Sie zu **Segmenterweiterungen** > **Neue Erweiterung erstellen** > **Mit Template beginnen** und wählen Sie ein Template aus. <br>![Modal mit der Option, ein Katalogsegment für Events, Käufe oder RFM-Segmente zu erstellen.]({% image_buster /assets/img/catalog-segments-template.png %}){: style="max-width:80%" }

{: start="2"}
2. Der SQL-Editor füllt sich automatisch mit einem Template. <br>![SQL-Editor mit einem vorgenerierten Template.]({% image_buster /assets/img/catalog-segments-editor.png %}){: style="max-width:80%" }<br>Dieses Template verbindet Nutzer-Event-Daten mit Katalogdaten, um Nutzer:innen zu segmentieren, die mit bestimmten Katalogartikeln interagiert haben.

3. Verwenden Sie den Tab **Variablen**, um die erforderlichen Felder für Ihr Template bereitzustellen, bevor Sie Ihr Segment generieren. <br>So ermöglichen Sie Braze, Nutzer:innen anhand ihres Engagements mit Katalogartikeln zu identifizieren: <br> - Wählen Sie einen Katalog aus, der ein Katalogfeld enthält <br> - Wählen Sie ein angepasstes Event aus, das eine Event-Eigenschaft enthält <br> - Stimmen Sie die Werte Ihrer Katalogfelder und Event-Eigenschaften ab

Hier finden Sie Richtlinien für die Auswahl der Variablen:

| Variablenfeld | Beschreibung |
| --- | --- |
| `Catalog` | Der Name des Katalogs, den Sie für das Targeting von Nutzer:innen verwenden. |
| `Catalog field`| Das Feld in Ihrem Katalog, das die gleichen Werte wie Ihre `Custom event property` enthält. Dies ist oft eine Art von ID. Im E-Commerce-Anwendungsfall wäre dies `shopify_id`. |
| `Custom event` | Der Name Ihres angepassten Events, das eine Eigenschaft mit Werten enthält, die zu Ihrem `Catalog field` passen. Im E-Commerce-Anwendungsfall wäre dies `Made Order`. |
| `Custom event property` | Der Name der angepassten Event-Eigenschaft, deren Werte mit denen in `Catalog field` übereinstimmen. Im E-Commerce-Beispiel wäre dies `Shopify_ID.`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="4"}
4. Füllen Sie bei Bedarf weitere optionale Felder für Ihren Anwendungsfall aus, um nach einem bestimmten Feldwert in Ihrem Katalog zu segmentieren:
- `Catalog field`: Ein bestimmtes Feld (Spaltenname) in diesem Katalog
- `Value`: Ein bestimmter Wert in diesem Feld oder dieser Spalte <br><br> Nehmen wir die Gesundheits-App als Beispiel: Angenommen, im Katalog für jeden buchbaren Arzt gibt es ein Feld namens `specialty`, das einen Wert wie `vision` oder `dental` enthält. Um Nutzer:innen zu segmentieren, die einen Arzt mit dem Wert `dental` besucht haben, wählen Sie `specialty` als `Catalog field` und `dental` als `Value` aus.

5. Nachdem Sie ein SQL-Segment erstellt haben, empfehlen wir, auf **Vorschau erstellen** zu klicken. So können Sie prüfen, ob Ihre Abfrage Nutzer:innen zurückgibt oder ob Fehler vorliegen. Weitere Informationen über die [Vorschau von Abfrageergebnissen]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#previewing-results), die Verwaltung von [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#managing-sql-segment-extensions) und mehr finden Sie unter [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

{% alert note %}
Wenn Sie ein SQL-Segment erstellen, das die Tabelle `CATALOGS_ITEMS_SHARED` verwendet, müssen Sie eine Katalog-ID angeben. Zum Beispiel:

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### Feststellen, ob Sie SQL invertieren müssen

Es ist zwar nicht möglich, direkt nach Nutzer:innen mit null Events zu suchen, aber mit **SQL invertieren** können Sie diese Nutzer:innen gezielt ansprechen.

Um beispielsweise Nutzer:innen mit weniger als drei Käufen anzusprechen, schreiben Sie zunächst eine Abfrage, die Nutzer:innen mit drei oder mehr Käufen auswählt. Wählen Sie dann **SQL invertieren** aus, um Nutzer:innen mit weniger als drei Käufen (einschließlich derer mit null Käufen) anzusprechen.

![Segmenterweiterung mit dem Namen „In den letzten 30 Tagen auf 1–4 E-Mails geklickt" mit der ausgewählten Option, SQL zu invertieren.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:70%;"}

{% alert important %}
Sofern Sie nicht speziell Nutzer:innen mit null Events ansprechen möchten, brauchen Sie SQL nicht zu invertieren. Wenn **SQL invertieren** ausgewählt ist, vergewissern Sie sich, dass das Feature benötigt wird und dass das Segment Ihrer gewünschten Zielgruppe entspricht. Wenn eine Abfrage beispielsweise auf Nutzer:innen mit mindestens einem Event abzielt, wird sie bei Invertierung nur auf Nutzer:innen mit null Events abzielen.
{% endalert %}

## Segmentmitgliedschaft aktualisieren

Um die Segmentzugehörigkeit eines beliebigen Katalogsegments zu aktualisieren, öffnen Sie das Katalogsegment und wählen Sie **Aktionen** > **Aktualisieren** > **Ja, aktualisieren**.

{% alert tip %}
Wenn Sie ein Segment erstellt haben, bei dem Sie davon ausgehen, dass Nutzer:innen regelmäßig ein- und austreten, aktualisieren Sie das verwendete Katalogsegment manuell, bevor Sie dieses Segment in einer Kampagne oder einem Canvas als Zielgruppe verwenden.
{% endalert %}

### Aktualisierungseinstellungen festlegen

{% multi_lang_include segments.md section='Refresh settings' %}

## Anwendungsfälle

{% tabs local %}
{% tab Health %}

### Gesundheits-App

Nehmen wir an, Sie haben eine Gesundheits-App und möchten Nutzer:innen segmentieren, die einen Zahnarztbesuch gebucht haben. Sie haben außerdem Folgendes:

- Einen Katalog `Doctors` mit allen Ärzten, bei denen ein Termin gebucht werden kann, jeweils mit einer `doctor ID`
- Ein angepasstes Event `Booked Visit` mit einer Eigenschaft `doctor ID`, die die gleichen Werte wie das Feld `doctor ID` in Ihrem Katalog hat
- Ein `speciality`-Feld in Ihrem Katalog, das den Wert `dental` enthält

Sie würden ein Katalogsegment mit den folgenden Variablen einrichten:

| Variable | Eigenschaft |
| --- | --- |
| `Catalog`| Doctors |
| `Catalog field` | doctor ID |
| `Custom event`| Booked Visit|
| `Custom event property` | doctor ID |
| `(Under Filter SQL Results) Catalog field` | Specialty |
| `(Under Filter SQL Results) Value`| Dental |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab SaaS %}

### SaaS-Plattform

Angenommen, Sie betreiben eine B2B-SaaS-Plattform und möchten Nutzer:innen segmentieren, die Mitarbeitende eines Bestandskunden sind. Sie haben außerdem Folgendes:

- Einen Katalog `Accounts` mit allen Konten, die derzeit Ihre SaaS-Plattform nutzen, jeweils mit einer `account ID`
- Ein angepasstes Event `Event Attendance` mit einer Eigenschaft „account ID", deren Werte mit dem Feld „account ID" in Ihrem Katalog übereinstimmen
- Ein `Classification`-Feld in Ihrem Katalog, das den Wert `enterprise` enthält

Sie würden ein Katalogsegment mit den folgenden Variablen einrichten:

| Variable | Eigenschaft |
| --- | --- |
| `Catalog` | Accounts |
| `Catalog field `| account ID |
| `Custom event` | Event Attendance |
| `Custom event property` | account ID |
| `(Under Filter SQL Results) Catalog field` | Classification |
| `(Under Filter SQL Results) Value` | Enterprise |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Häufig gestellte Fragen

### Verbraucht die Ausführung eines Katalogsegments Guthaben für SQL-Segmenterweiterungen?

Ja, Katalogsegmente basieren auf SQL und verbrauchen Guthaben für SQL-Segmenterweiterungen. Weitere Informationen finden Sie unter [Nutzung von SQL-Segmenten]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments#monitoring-your-sql-segments-usage).

### Verbraucht die Erstellung eines Katalogsegments Kontingente für SQL-Segmenterweiterungen?

Ja. So wie SQL-Segmenterweiterungen auf Ihr Kontingent an Segmenterweiterungen angerechnet werden, werden auch Katalogsegmente auf dieses Kontingent angerechnet.

### Ich habe einen Anwendungsfall für ein Katalogsegment, den das aktuelle Template nicht abdeckt. Wie sollte ich das einrichten?

Kontaktieren Sie Ihre:n Customer-Success-Manager:in oder den [Braze Support]({{site.baseurl}}/user_guide/administrative/access_braze/support/) für weitere Unterstützung.