---
nav_title: "Katalog-Segmente"
article_title: Katalog-Segmente
page_order: 1
page_type: reference
alias: "/catalog_segments/"
description: "Dieser Artikel erläutert, wie Sie Katalogsegmente erstellen und mithilfe von Katalogdaten in SQL-Segmenterweiterungen Nutzerzielgruppen bilden."
tool: Segments
---

# Katalog-Segmente

> Katalogsegmente sind eine Art von SQL-Segmenterweiterung, die durch die Kombination von Katalogdaten mit Daten aus benutzerdefinierten Ereignissen oder Käufen erstellt wird. Sie können in einem Segment referenziert und dann durch Kampagnen und Canvase gezielt angesprochen werden. 

{% alert important %}
Katalogsegmente befinden sich derzeit in der Early-Access-Phase. Wenden Sie sich an Ihren Customer Success Manager, wenn Sie an einem Vorabzugang interessiert sind.
{% endalert %}

Katalogsegmente führen Daten aus Katalogen und angepassten Events oder Käufen per SQL zusammen. Dazu benötigen Sie ein einheitliches Bezeichnerfeld in Katalogen und angepassten Events und Käufen. Zum Beispiel muss der Wert einer Artikel-ID in einem Katalog mit dem Wert einer Eigenschaft in einem benutzerdefinierten Ereignis übereinstimmen.

## Katalogsegmente erstellen

1. Gehen Sie zu **Segment-Erweiterungen** > **Neue Erweiterung erstellen** > **Mit Vorlage beginnen** und wählen Sie eine Vorlage aus. <br>![Modal mit der Option, ein Segment für Ereignisse oder Käufe zu erstellen.]({% image_buster /assets/img/catalog-segments-template.png %}){: style="max-width:80%" }

{: start="2"}
2\. Der SQL-Editor füllt sich automatisch mit einer Vorlage. <br>![SQL-Editor mit einer vorgenerierten Vorlage.]({% image_buster /assets/img/catalog-segments-editor.png %}){: style="max-width:80%" }<br>Dieses Template verbindet Nutzerereignis- mit Katalogdaten, um Nutzersegmente zu erstellen, die sich mit bestimmten Artikeln im Katalog beschäftigt haben.

3. Verwenden Sie die Registerkarte **Variablen**, um die erforderlichen Felder für Ihre Vorlage bereitzustellen, bevor Sie Ihr Segment erstellen. <br>So ermöglichen Sie Braze, das Nutzerengagement mit Katalogartikel zu erkennen: <br> \- Wählen Sie einen Katalog, der ein Katalogfeld enthält <br> \- Wählen Sie ein angepasstes Event mit einer Event-Eigenschaft aus. <br> \- Stimmen Sie die Werte Ihrer Katalogfelder und Ereigniseigenschaften ab

Hier finden Sie Richtlinien für die Auswahl der Variablen:

| Variablenfeld | Beschreibung |
| --- | --- |
| `Catalog` | Der Name des Katalogs, den Sie für das Nutzertargeting verwenden. |
| `Catalog field`| Das Feld in Ihrem Katalog, das die gleichen Werte wie Ihr `Custom event property` enthält. Dies ist oft eine Art von ID. Im E-Commerce Anwendungsfall wäre dies `shopify_id`. |
| `Custom event` | Der Name Ihres benutzerdefinierten Ereignisses, das dasselbe Ereignis ist, das eine Eigenschaft mit Werten enthält, die zu Ihrem `Catalog field` passen. Im E-Commerce Anwendungsfall wäre dies `Made Order`. |
| `Custom event property` | Der Name der angepassten Event-Eigenschaft, der mit den Werten in `Catalog field` übereinstimmt. Im E-Commerce-Beispiel wäre dies der Fall `Shopify_ID.`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="4"}
4\. Füllen Sie bei Bedarf weitere optionale Felder zu Ihrem Anwendungsfall aus, um Segmente anhand eines bestimmten Feldwerts in Ihrem Katalog zu bilden:
- `Catalog field`: Ein bestimmtes Feld (Spaltenname) in diesem Katalog
- `Value`: Ein bestimmter Wert in diesem Feld oder dieser Spalte <br><br> Nehmen wir die Gesundheits-App als Beispiel. Nehmen wir an, dass es im Katalog für jeden Arzt, den Sie buchen können, ein Feld namens `specialty` gibt, das einen Wert wie `vision` oder `dental` enthält. Um ein Segment aus allen Personen zu bilden, die einen Arzt mit dem Wert `dental` besucht haben, können Sie `specialty` als `Catalog field` und `dental` als `Value` auswählen.

5. Wenn Sie ein SQL-Segment erstellt haben, sollten Sie auf **Vorschau erstellen** klicken. So können Sie prüfen, ob Ihre Abfrage zu einem Ergebnis führt oder ein Fehler auftritt. Weitere Informationen über die [Vorschau von Abfrageergebnissen]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#previewing-results), die Verwaltung von [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#managing-sql-segment-extensions) und mehr finden Sie unter [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

{% alert note %}
Wenn Sie ein SQL-Segment erstellen, das die Tabelle `CATALOGS_ITEMS_SHARED` verwendet, müssen Sie eine Katalog ID angeben. Zum Beispiel:

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### Feststellen, ob Sie SQL invertieren müssen

Es ist zwar nicht möglich, direkt nach Nutzer:innen mit null Ereignissen zu suchen, aber mit **Invert SQL** können Sie diese Nutzer:innen gezielt zusammenstellen.

Um beispielsweise Nutzer:innen mit weniger als drei Einkäufen als Zielgruppe zusammenzustellen, schreiben Sie zunächst eine Abfrage, um Nutzer:innen mit drei oder mehr Einkäufen auszuwählen. Wählen Sie dann **SQL invertieren** aus, um Nutzer:innen mit weniger als drei Käufen (einschließlich derer mit null Käufen) als Targeting zusammenzustellen.

![Segment-Erweiterung mit dem Namen "In den letzten 30 Tagen auf 1-4 E-Mails geklickt" mit der ausgewählten Option, SQL zu invertieren.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:70%;"}

{% alert important %}
Sofern Sie nicht speziell Nutzer:innen mit Null-Ereignissen als Targeting zusammenstellen wollen, brauchen Sie SQL nicht zu invertieren. Wenn Sie **SQL invertieren** auswählen, bestätigen Sie, dass das Feature benötigt wird und dass das Segment Ihrer gewünschten Zielgruppe entspricht. Wenn eine Abfrage beispielsweise auf Nutzer:innen mit mindestens einem Ereignis abzielt, wird sie nur auf Nutzer:innen mit null Ereignissen abzielen, wenn sie invertiert wird.
{% endalert %}

## Segmentmitgliedschaft aktualisieren

Um die Segmentzugehörigkeit eines beliebigen Katalogsegments zu aktualisieren, öffnen Sie das Segment und wählen Sie **Aktionen** > **Aktualisieren** > **Ja, Aktualisieren**.

{% alert tip %}
Wenn Sie ein Segment erstellt haben, bei dem Sie davon ausgehen, dass Nutzer:innen regelmäßig ein- und ausgehen, aktualisieren Sie das verwendete Katalogsegment manuell, bevor Sie dieses Segment in einer Kampagne oder einem Canvas targetieren.
{% endalert %}

### Festlegen der Aktualisierungseinstellungen

{% multi_lang_include segments.md section='Refresh settings' %}

## Anwendungsfälle

{% tabs local %}
{% tab Health %}

### Gesundheitsapp

Nehmen wir an, Sie haben eine Gesundheits-App und möchten die Nutzer segmentieren, die einen Zahnarztbesuch gebucht haben. Sie haben außerdem Folgendes:

- Ein Katalog `Doctors` mit allen Ärzten mit jeweils einer `doctor ID`, bei denen ein Termin gebucht werden kann
- Ein benutzerdefiniertes Ereignis `Booked Visit` mit einer Eigenschaft `doctor ID`, die die gleichen Werte wie das Feld `doctor ID` in Ihrem Katalog hat
- Ein `speciality`-Feld in Ihrem Katalog, das den Wert `dental` enthält

Sie würden ein Katalogsegment mit Hilfe der folgenden Variablen einrichten:

| Variabel | Eigenschaft |
| --- | --- |
| `Catalog`| Ärzte |
| `Catalog field` | Arztkennung |
| `Custom event`| Gebuchter Besuch|
| `Custom event property` | Arztkennung |
| `(Under Filter SQL Results) Catalog field` | Fachgebiet |
| `(Under Filter SQL Results) Value`| Dental |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab SaaS %}

### SaaS-Plattform

Angenommen, Sie betreiben eine B2B SaaS-Plattform und möchten Nutzersegmente zu Mitarbeitern eines Bestandskunden erstellen. Sie haben außerdem Folgendes:

- Einen Katalog `Accounts` mit allen Konten, die derzeit Ihre SaaS-Plattform nutzen und jeweils eine `account ID` besitzen
- Ein angepasstes Event `Event Attendance` mit einer Eigenschaft "Konto-ID", deren Inhalt mit dem Feld "Konto-ID" in Ihrem Katalog übereinstimmt
- Ein `Classification`-Feld in Ihrem Katalog, das den Wert `enterprise` enthält

Sie würden ein Katalogsegment mit Hilfe der folgenden Variablen einrichten:

| Variabel | Eigenschaft |
| --- | --- |
| `Catalog` | Konten |
| `Catalog field `| Konto-ID |
| `Custom event` | Teilnahme |
| `Custom event property` | Konto-ID |
| `(Under Filter SQL Results) Catalog field` | Klassifizierung |
| `(Under Filter SQL Results) Value` | Unternehmen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Häufig gestellte Fragen

### Verbraucht die Ausführung eines Katalogsegments Guthaben für die SQL-Segmenterweiterung?

Ja, Katalogsegmente werden von SQL unterstützt und verbrauchen Guthaben für die SQL-Segmenterweiterung. Weitere Informationen finden Sie unter [Verwendung von SQL-Segmenten]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments#monitoring-your-sql-segments-usage).

### Verbraucht die Erstellung eines Katalogsegments die Kontingente der SQL-Segmenterweiterung?

Ja So wie SQL-Segmenterweiterungen auf Ihr Kontingent an Segmenterweiterungen angerechnet werden, werden auch Katalogsegmente auf das entsprechende Kontingent angerechnet.

### Ein Template eignet sich nicht für ein bestimmtes Katalogsegment. Wie soll ich das einrichten?

Wenden Sie sich an Ihren Kundenbetreuer oder den [Braze-Support]({{site.baseurl}}/user_guide/administrative/access_braze/support/), wenn Sie weitere Hilfe benötigen.

