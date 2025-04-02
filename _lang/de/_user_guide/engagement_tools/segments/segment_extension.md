---
nav_title: Segmenterweiterungen
article_title: Segmenterweiterungen
page_order: 3.1

page_type: tutorial
description: "In diesem Artikel erfahren Sie, wie Sie eine Segmenterweiterung einrichten und verwenden, um Ihre Segmentierungsfunktionen zu verbessern."
tool: Segments
---

# Segmenterweiterungen

> Mit der Braze-Segmentierung können Sie Benutzer auf der Grundlage von benutzerdefinierten Ereignissen oder Kaufverhalten ansprechen, die während der gesamten Lebensdauer des Benutzerprofils gespeichert werden. Beispiele hierfür sind die Suche nach Nutzern, die seit einem bestimmten Zeitpunkt ein bestimmtes benutzerdefiniertes Ereignis durchgeführt haben oder nicht, oder die Segmentierung von Nutzern auf der Grundlage der Produkte, die sie jemals gekauft haben, oder des Geldbetrags, den sie für Ihren Service ausgegeben haben.

Segmenterweiterungen sind Zielgruppendefinitionen, die es Ihnen erlauben, verschachtelte Event-Eigenschaften zu verwenden oder fensterbasierte Aggregationen von Angepasstes-Event- und Kauf-Event-Eigenschaften in den letzten 2 Jahren (730 Tage) zu erstellen. Mit der Braze-Segmentierung können Sie zum Beispiel Nutzer finden, die in ihrem Leben ein bestimmtes Produkt gekauft haben. Mit Segmenterweiterungen können Sie diese Zielgruppe weiter auf Nutzer eingrenzen, die in den letzten 2 Jahren mindestens zweimal eine bestimmte Farbe eines bestimmten Produkts gekauft haben. Bei der Erstellung einer Segmenterweiterung können Sie auch festlegen, dass die Zielgruppe statisch ist oder täglich neu generiert wird.

Die Verwendung von verschachtelten Event-Eigenschaften für die [aktionsbasierte Zustellung][19] erfordert keine Segmenterweiterungen, da die Event-Verarbeitung in Realtime erfolgt. Verschachtelte benutzerdefinierte Attribute erfordern ebenfalls nicht die Verwendung von Segmenterweiterungen.

{% alert important %}
Standardmäßig werden 25 aktive Segmenterweiterungen pro Workspace zu einem bestimmten Zeitpunkt zugeteilt. Wenn Sie dieses Limit erhöhen müssen, wenden Sie sich an Ihren Braze Customer Success Manager, um Ihren Anwendungsfall zu besprechen.
{% endalert %}

## Schritt 1: Navigieren Sie zu Segmenterweiterungen

Gehen Sie zu **Zielgruppe** > **Segmenterweiterungen**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie diese Seite unter **Engagement** > **Segmente** > **Segmenterweiterungen**.
{% endalert %}

Klicken Sie in der Tabelle Segmenterweiterungen auf **Neue Erweiterung erstellen** und wählen Sie dann Ihre Erfahrung bei der Erstellung von Segmenterweiterungen:

- **Einfache Erweiterung:** Erstellen Sie eine Segmenterweiterung, die sich auf ein einzelnes Event konzentriert, indem Sie ein geführtes Formular verwenden.
Am besten geeignet, wenn Sie kein SQL verwenden möchten.
- **Beginnen Sie mit einer Vorlage:** Erstellen Sie ein SQL-Segment mit einer anpassbaren Vorlage unter Verwendung von Snowflake-Daten.
- **Inkrementelle Aktualisierung:** Schreiben Sie ein Snowflake-SQL-Segment, das automatisch die Daten der letzten 2 Tage aktualisiert oder aktualisieren Sie sie bei Bedarf manuell. Die beste Lösung für ein ausgewogenes Verhältnis zwischen Genauigkeit und Kosteneffizienz.
- **Vollständige Auffrischung:** Schreiben Sie ein Snowflake-SQL-Segment, das die gesamte Zielgruppe bei einer manuellen Aktualisierung neu berechnet. Am besten geeignet, wenn Sie einen vollständigen, aktuellen Überblick über Ihre Zielgruppe benötigen.

![][20]{: style="max-width:50%"}

Wenn Sie eine Erfahrung auswählen, die SQL verwendet, finden Sie weitere Informationen unter [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/).

Wenn Sie **Einfache Erweiterung** wählen, fahren Sie mit den folgenden Schritten fort.

## Schritt 2: Benennen Sie Ihre Segmenterweiterung

Benennen Sie Ihre Segmenterweiterung, indem Sie die Art der Nutzer:innen beschreiben, nach denen Sie filtern möchten. Dadurch wird sichergestellt, dass diese Erweiterung bei der Anwendung als Filter in Ihrem Segment leicht und genau entdeckt werden kann.

![Segmenterweiterung mit dem Namen "Online-Shopper-Erweiterung - 90 Tage", wobei das Kontrollkästchen "Erweiterung täglich neu generieren" ausgewählt ist.][2]

## Schritt 3: Wählen Sie Ihre Kriterien

Wählen Sie zwischen den Kriterien Kauf, Nachrichteninteraktion oder benutzerdefiniertes Ereignis für die Zielgruppenansprache. Nachdem Sie die gewünschten Kriterien für den Event-Typ ausgewählt haben, wählen Sie aus, welchen gekauften Artikel, welche Nachrichten-Interaktion oder welches angepasste Event Sie für Ihre Nutzerliste als Targeting verwenden möchten. Wählen Sie dann aus, wie oft (mehr, weniger oder gleich) die:der Nutzer:in das Event abgeschlossen haben muss, und den Zeitraum - speziell für Segmenterweiterungen können Sie bis zu den letzten 730 Tagen (2 Jahre) zurückgehen.

Die Segmentierung auf der Grundlage von Event-Daten aus mehr als 730 Tagen kann mit anderen Filtern unter **Segmente** vorgenommen werden. Bei der Auswahl Ihres Zeitraums können Sie einen relativen Datumsbereich (z.B. die letzten X Tage), ein Startdatum, ein Enddatum oder einen genauen Datumsbereich (Datum A bis Datum B) angeben.

![][3]

### Segmentierung der Eigenschaften von Events

Um die Targeting-Präzision zu erhöhen, wählen Sie das Kontrollkästchen **Eigenschaften-Filter hinzufügen** aus. Auf diese Weise können Sie nach den spezifischen Eigenschaften Ihres Kaufs oder Ihres benutzerdefinierten Ereignisses suchen. Wir unterstützen die Segmentierung von Event-Eigenschaften auf der Basis von String-, numerischen, booleschen und zeitlichen Objekten.

Bei String-Eigenschaften können Sie mehrere Werte auf einmal eingeben. In dem folgenden Beispiel sucht dieser Filter nach Benutzern mit einem der folgenden Status: Gold, Silber oder Bronze.

![Segmentierung anhand von String-Eigenschaften.][13.5]

![Segmentierung basierend auf numerischen Eigenschaften.][13]

![Segmentierung basierend auf booleschen Eigenschaften.][14]

![Segmentierung anhand von Datumsobjekten.][15]

Wir unterstützen auch die Segmentierung auf der Grundlage [verschachtelter Event-Eigenschaften]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/nested_objects/).

![Segmentierung basierend auf verschachtelten Ereigniseigenschaften.][18]

Segmenterweiterungen beruhen auf der langfristigen Speicherung von Event-Eigenschaften und haben kein Limit für die Speicherung von zeitgestempelten Eigenschaften. Sie können auf die Event-Eigenschaften zurückblicken, die in den letzten zwei Jahren getrackt wurden.

{% alert note %}
Die Verwendung von Ereigniseigenschaften innerhalb von Segment Extensions hat keinen Einfluss auf die Verwendung von Datenpunkten.
{% endalert %}

## Schritt 4: Einstellungen für die Aktualisierung festlegen (optional)

Wenn Sie Ihre Erweiterung nicht regelmäßig aktualisieren müssen, können Sie sie auch ohne Aktualisierungseinstellungen speichern. Braze generiert Ihre Segmenterweiterung dann standardmäßig auf der Grundlage Ihrer aktuellen Benutzerzugehörigkeit. Verwenden Sie das Standardverhalten, wenn Sie die Zielgruppe nur einmal generieren und sie dann mit einer einmaligen Kampagne ansprechen möchten.

Die Verarbeitung Ihres Segments beginnt immer nach dem ersten Speichern. Jedes Mal, wenn Ihr Segment aktualisiert wird, führt Braze das Segment erneut aus und aktualisiert die Segmentmitgliedschaft, um die Benutzer in Ihrem Segment zum Zeitpunkt der Aktualisierung wiederzugeben. So können Ihre wiederkehrenden Kampagnen die relevantesten Nutzer erreichen.

### Einrichten einer wiederkehrenden Aktualisierung

Um einen wiederkehrenden Zeitplan einzurichten, wählen Sie **Einstellungen aktualisieren** in der oberen rechten Ecke Ihrer spezifischen Erweiterung. Die Option zur Festlegung von Aktualisierungseinstellungen ist für alle Arten von Segmenterweiterungen verfügbar, einschließlich SQL-Segmente, CDI-Segmente und einfache formularbasierte Segmenterweiterungen.

{% alert important %}
Die Aktualisierungseinstellungen werden für nicht verwendete Segmenterweiterungen automatisch deaktiviert. Braze definiert unbenutzte Erweiterungen als solche, die die folgenden Kriterien erfüllen:

- Keine Verwendung in aktiven Kampagnen, Canvasen oder Segmenten
- Keine Verwendung in inaktiven Kampagnen, Canvases oder Segmenten (mit dem Status „Entwurf“, „Angehalten“ oder „Archiviert“)
- Keine Änderungen in den letzten 7 Tagen

Braze benachrichtigt den Firmenkontakt und den Ersteller der Erweiterung, wenn diese Einstellung deaktiviert ist. Die Option, die Erweiterungen täglich zu regenerieren, kann jederzeit wieder aktiviert werden.
{% endalert %}

#### Auswählen Ihrer Aktualisierungseinstellungen

![Aktualisierungsintervall Einstellungen mit einer wöchentlichen Aktualisierungsfrequenz, einer Startzeit von 10 Uhr und dem ausgewählten Montag als Tag.][21]{: style="max-width:60%;"}

Im Bereich **Aktualisierungseinstellungen** können Sie die Häufigkeit auswählen, mit der diese Segmenterweiterung aktualisiert wird: stündlich, täglich, wöchentlich oder monatlich. Sie müssen auch die genaue Uhrzeit (die in der Zeitzone Ihres Unternehmens liegt) für die Aktualisierung auswählen, z. B:

- Wenn Sie eine E-Mail-Kampagne haben, die jeden Montag um 11 Uhr Unternehmenszeit versendet wird, und Sie sicherstellen möchten, dass Ihr Segment kurz vor dem Versand aktualisiert wird, sollten Sie einen Aktualisierungszeitplan wählen, der wöchentlich montags um 10 Uhr gilt.
- Wenn Sie möchten, dass Ihr Segment jeden Tag aktualisiert wird, wählen Sie die tägliche Aktualisierungshäufigkeit und dann die Tageszeit für die Aktualisierung aus.

{% alert note %}
Die Möglichkeit, einen stündlichen Zeitplan für die Aktualisierung festzulegen, ist für formularbasierte Segmenterweiterungen nicht verfügbar (Sie können jedoch tägliche, wöchentliche oder monatliche Zeitpläne festlegen).
{% endalert %}

### Kreditverbrauch und zusätzliche Kosten

Da bei Aktualisierungen die Abfrage Ihres Segments erneut ausgeführt wird, verbraucht jede Aktualisierung für SQL-Segmente SQL-Segmentguthaben, und jede Aktualisierung für CDI-Segmente verursacht Kosten in Ihren Drittanbieter-Data-Warehouse.

{% alert note %}
Segmente können aufgrund von Datenverarbeitungszeiten bis zu 60 Minuten für die Aktualisierung benötigen. Segmente, die gerade aktualisiert werden, haben in Ihrer Liste Segmenterweiterungen den Status "In Bearbeitung". Dies hat einige Auswirkungen:

- Um die Verarbeitung Ihres Segments vor einer bestimmten Zeit abzuschließen, wählen Sie eine Aktualisierungszeit, die 60 Minuten früher liegt. 
- Für eine bestimmte Segmenterweiterung kann jeweils nur eine Aktualisierung erfolgen. Wenn es einen Konflikt gibt, bei dem eine neue Anfrage zur Aktualisierung gestartet wird, während die Verarbeitung einer bestehenden Aktualisierung bereits begonnen hat, bricht Braze die neue Anfrage zur Aktualisierung ab und setzt die laufende Verarbeitung fort.
{% endalert %}

## Schritt 5: Speichern Sie Ihre Segmenterweiterung

Sobald Sie auf **Speichern** klicken, beginnt die Bearbeitung Ihrer Erweiterung. Wie lange es dauert, Ihre Erweiterung zu generieren, hängt davon ab, wie viele Nutzer:innen Sie haben, wie viele angepasste Events oder Kauf-Events Sie erfassen und wie viele Tage Sie im Verlauf zurückblicken wollen.

Während Ihre Erweiterung in Bearbeitung ist, sehen Sie eine kleine Animation neben dem Namen der Erweiterung und das Wort "In Bearbeitung" in der Spalte **"Zuletzt bearbeitet"** in der Erweiterungsliste. Beachten Sie, dass Sie eine Erweiterung nicht bearbeiten können, solange sie in Bearbeitung ist.

![][5]

## Schritt 6: Verwenden Sie Ihre Erweiterung in einem Segment

Sobald Sie eine Erweiterung erstellt haben, können Sie sie als Filter verwenden, wenn Sie ein Segment erstellen oder eine Zielgruppe für eine Kampagne oder ein Canvas definieren. Beginnen Sie mit der Auswahl von **Braze Segment Extension** aus der Filterliste unter dem Abschnitt **Benutzerattribute**.

![][6]

Wählen Sie in der Filterliste Braze-Segmenterweiterung die Erweiterung aus, die Sie in dieses Segment aufnehmen oder ausschließen möchten.

![][7]

Um die Kriterien für die Erweiterung anzuzeigen, klicken Sie auf **Erweiterungsdetails anzeigen**, um die Details in einem modalen Popup anzuzeigen.

![][8]{: style="max-width:70%;"}

Jetzt können Sie wie gewohnt mit der [Erstellung Ihrer Segmente][11] fortfahren.

[2]: {% image_buster /assets/img/segment/segment_extension2.png %}
[3]: {% image_buster /assets/img/segment/segment_extension1.png %}
[5]: {% image_buster /assets/img/segment/segment_extension5.png %}
[6]: {% image_buster /assets/img/segment/segment_extension7.png %}
[7]: {% image_buster /assets/img/segment/segment_extension6.png %}
[8]: {% image_buster /assets/img/segment/segment_extension8.png %}
[10]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/
[11]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
[12]: {% image_buster /assets/img/segment/property1.png %}
[13]: {% image_buster /assets/img/segment/property2.png %}
[13.5]: {% image_buster /assets/img/segment/property5.png %}
[14]: {% image_buster /assets/img/segment/property3.png %}
[15]: {% image_buster /assets/img/segment/property4.png %}
[16]: {% image_buster /assets/img/Shopify/arrow.jpeg %}
[17]: {% image_buster /assets/img/segment/segment_extension9.png %}
[18]: {% image_buster /assets/img/segment/nested_segment_extensions.png %}
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[20]: {% image_buster /assets/img/segment/segment_extension_modal.png %}
[21]: {% image_buster /assets/img/segment/segment_interval_settings.png %}
