---
nav_title: Segment-Erweiterungen
article_title: Segmenterweiterungen
page_order: 6
page_type: reference
description: "In diesem Artikel erfahren Sie, wie Sie eine Segmenterweiterung einrichten und verwenden, um Ihre Segmentierungsfunktionen zu verbessern."
tool: Segments
---

# Segmenterweiterungen

> Segment-Erweiterungen erlauben es Ihnen, sehr präzise Segmente über einen längeren Zeitraum im Verlauf eines Nutzer:innen zu erstellen. Mit Segment-Erweiterungen können Sie beispielsweise Nutzer:innen ansprechen, die in den letzten sechzehn Monaten ein bestimmtes Produkt gekauft oder einen bestimmten Geldbetrag für Ihren Dienst ausgegeben haben. Verfeinern Sie diese Zielgruppe mit Event-Eigenschaften, um das Targeting noch feiner zu gestalten.

Mit der Segmentierung von Braze können Sie Nutzer:innen auf der Grundlage eines angepassten Events oder Kauf-Events gezielt ansprechen. Segment-Erweiterungen verbessern diese Fähigkeit, indem Sie auf historische Daten zurückgreifen können, die im Nutzerprofil gespeichert sind. Mit Segment-Erweiterungen können Sie Nutzer:innen identifizieren und erreichen, die ein angepasstes Event oder Kauf-Event beliebig oft in den letzten zwei Jahren (730 Tage) abgeschlossen haben. 

## Warum Segment-Erweiterungen verwenden?

Segmente von Braze geben Ihnen leistungsstarke Targeting-Tools an die Hand, mit denen Sie dynamische Gruppen von Nutzer:innen zusammenstellen können. Für die meisten Anwendungsfälle ist dies ausreichend, um Ihre Zielgruppe effektiv zu erreichen. Segment-Erweiterungen wurden für fortgeschrittene Anwendungsfälle entwickelt, in denen Sie Verhaltensweisen von vor bis zu zwei Jahren analysieren oder eine komplexe Logik anwenden müssen - ohne die Bindung von Daten oder die Performance des Systems zu beeinträchtigen. Sie können [SQL-Anfragen]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments) (SQL Segment-Erweiterungen) oder Daten aus Ihrem eigenen [Data Warehouse]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments) verwenden, um Ihre Zielgruppe weiter zu verfeinern.

Die Standard Segmentierung von Braze findet beispielsweise Nutzer:innen, die bestimmte von Ihnen definierte Kriterien erfüllen, wie z.B. die Identifizierung eines Nutzers, der kürzlich eines Ihrer Produkte gekauft hat. Mit Segment-Erweiterungen können Sie tiefer gehen - wie z.B. die Identifizierung von Nutzer:innen, die vor 18 bis 24 Monaten mindestens zweimal eine bestimmte Farbe eines bestimmten Produkts gekauft haben. Segment-Erweiterungen sind eine Erweiterung, keine Voraussetzung. Wenn Sie fortschrittlichere Filter oder ein längeres Rückblicksfenster benötigen, sind sie ein großartiges Hilfsmittel, um Ihre Datennutzung zu optimieren.

{% alert note %}
Standardmäßig werden 25 aktive Segmenterweiterungen pro Workspace zu einem bestimmten Zeitpunkt zugeteilt. Wenn Sie dieses Limit erhöhen müssen, wenden Sie sich an Ihren Braze Customer Success Manager, um Ihren Anwendungsfall zu besprechen.
{% endalert %}

## Erstellen einer Segment-Erweiterung

Um eine Segment-Erweiterung zu erstellen, erstellen Sie einen Filter zur Verfeinerung eines Segments Ihrer Nutzer:innen auf der Grundlage angepasster Event-Eigenschaften. Bei der Erstellung einer Segment-Erweiterung wählen Sie, ob das Segment statisch oder dynamisch in einem bestimmten Intervall aktualisiert werden soll.

### Schritt 1: Navigieren Sie zu Segmenterweiterungen

Gehen Sie zu **Zielgruppe** > **Segmenterweiterungen**.

Wählen Sie in der Tabelle Segment-Erweiterungen die Option **Neue Erweiterung erstellen** und wählen Sie dann Ihre Erfahrung bei der Erstellung von Segment-Erweiterungen aus:

- **Einfache Erweiterung:** Erstellen Sie eine Segmenterweiterung, die sich auf ein einzelnes Event konzentriert, indem Sie ein geführtes Formular verwenden.
Am besten geeignet, wenn Sie kein SQL verwenden möchten.
- **Beginnen Sie mit einer Vorlage:** Erstellen Sie ein SQL-Segment mit einer anpassbaren Vorlage unter Verwendung von Snowflake-Daten.
- **Inkrementelle Aktualisierung:** Schreiben Sie ein Snowflake-SQL-Segment, das automatisch die Daten der letzten 2 Tage aktualisiert oder aktualisieren Sie sie bei Bedarf manuell. Die beste Lösung für ein ausgewogenes Verhältnis zwischen Genauigkeit und Kosteneffizienz.
- **Vollständige Auffrischung:** Schreiben Sie ein SQL-Segment mit Snowflake-Daten oder einer beliebigen [mit CDI verbundenen Datenquelle]({{site.baseurl}}/cdi_segment_extensions/), das die gesamte Zielgruppe bei einer manuellen Aktualisierung neu berechnet. Am besten geeignet, wenn Sie einen vollständigen, aktuellen Überblick über Ihre Zielgruppe benötigen.

Tabelle mit verschiedenen Erfahrungen bei der Erstellung von Segment-Erweiterungen, aus denen Sie auswählen können.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%"}

Wenn Sie eine Erfahrung auswählen, die SQL verwendet, finden Sie weitere Informationen unter [SQL Segment-Erweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). Wenn Sie **Einfache Erweiterung** auswählen, fahren Sie mit Schritt 2 fort.

#### SQL-Kreditverbrauch

Die folgenden Typen von Segment-Erweiterungen verbrauchen SQL-Guthaben:

- SQL Segment-Erweiterungen (sowohl inkrementelle als auch vollständige Aktualisierung)
- Katalog-Segmente
- CDI Segmente 
    - Credits werden innerhalb Ihres eigenen Data Warehouse verbraucht

### Schritt 2: Benennen Sie Ihre Segmenterweiterung

Benennen Sie Ihre Segmenterweiterung, indem Sie die Art der Nutzer:innen beschreiben, nach denen Sie filtern möchten. Dadurch wird sichergestellt, dass diese Erweiterung bei der Anwendung als Filter in Ihrem Segment leicht und genau entdeckt werden kann.

![Segment-Erweiterung mit dem Namen "Online Shoppers Extension - 90 Tage".]({% image_buster /assets/img/segment/segment_extension2.png %})

### Schritt 3: Wählen Sie Ihre Kriterien

Wählen Sie zwischen den Kriterien Kauf, Nachrichteninteraktion oder benutzerdefiniertes Ereignis für die Zielgruppenansprache. Nachdem Sie die gewünschten Kriterien für den Event-Typ ausgewählt haben, wählen Sie aus, welchen gekauften Artikel, welche Nachrichten-Interaktion oder welches angepasste Event Sie für Ihre Nutzerliste als Targeting verwenden möchten. Wählen Sie dann aus, wie oft (mehr, weniger oder gleich) die:der Nutzer:in das Event abgeschlossen haben muss, und den Zeitraum - speziell für Segmenterweiterungen können Sie bis zu den letzten 730 Tagen (2 Jahre) zurückgehen.

Die Segmentierung auf der Grundlage von Event-Daten aus mehr als 730 Tagen kann mit anderen Filtern unter **Segmente** vorgenommen werden. Bei der Auswahl Ihres Zeitraums können Sie einen relativen Datumsbereich angeben, um die letzten X Tage auszuwählen, ein Startdatum, ein Enddatum oder einen genauen Datumsbereich (Datum A bis Datum B).

![Segmentierungskriterien für Nutzer:innen, die im Zeitraum vom 1\. März 2025 bis zum 31\. März 2025 mehr als 2 Mal ein angepasstes Event durchgeführt haben.]({% image_buster /assets/img/segment/segment_extension1.png %})

#### Segmentierung der Eigenschaften von Ereignissen

Um die Targeting-Präzision zu erhöhen, wählen Sie das Kontrollkästchen **Eigenschaften-Filter hinzufügen** aus. Auf diese Weise können Sie nach den spezifischen Eigenschaften Ihres Kaufs oder Ihres benutzerdefinierten Ereignisses suchen. Wir unterstützen die Segmentierung von Event-Eigenschaften auf der Basis von String-, numerischen, booleschen und zeitlichen Objekten.

Bei String-Eigenschaften können Sie mehrere Werte auf einmal eingeben. In dem folgenden Beispiel sucht dieser Filter nach Benutzern mit einem der folgenden Status: Gold, Silber oder Bronze.

![Segmentierung anhand der Eigenschaften von Strings.]({% image_buster /assets/img/segment/property5.png %})

![Segmentierung auf der Grundlage numerischer Eigenschaften.]({% image_buster /assets/img/segment/property2.png %})

![Segmentierung auf der Grundlage boolescher Eigenschaften.]({% image_buster /assets/img/segment/property3.png %})

![Segmentierung auf der Grundlage von Datumsobjekten.]({% image_buster /assets/img/segment/property4.png %})

Wir unterstützen auch die Segmentierung auf der Grundlage [verschachtelter Event-Eigenschaften]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

![Segmentierung auf der Grundlage verschachtelter Event-Eigenschaften.]({% image_buster /assets/img/segment/nested_segment_extensions.png %})

Segmenterweiterungen beruhen auf der langfristigen Speicherung von Event-Eigenschaften und haben kein Limit für die Speicherung von zeitgestempelten Eigenschaften. Sie können auf die Event-Eigenschaften zurückblicken, die in den letzten zwei Jahren getrackt wurden. Die Verwendung von Ereigniseigenschaften innerhalb von Segment Extensions hat keinen Einfluss auf die Verwendung von Datenpunkten.

{% alert note %}
Sie benötigen keine Segment-Erweiterungen, um Event-Eigenschaften oder verschachtelte angepasste Attribute in Ihrem Segment zu verwenden. Segment-Erweiterungen erweitern lediglich das historische Fenster, das zur Erstellung eines Standard Segments verwendet wird. Sie können ein [Realtime-Standardsegment]({{site.baseurl}}/user_guide/engagement_tools/segments/) erstellen, das Event-Eigenschaften der letzten 30 Tage oder verschachtelte angepasste Attribute verwendet. Ebenso können Sie Ihre Nachrichten so [planen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/), dass sie auf der Grundlage einer Event-Eigenschaft in Realtime triggern - eine Segment-Erweiterung ist nicht erforderlich.
{% endalert %}

### Schritt 4: Einstellungen für die Aktualisierung festlegen (optional)

{% multi_lang_include segments.md section='Refresh settings' %}

### Schritt 5: Speichern Sie Ihre Segmenterweiterung

Nachdem Sie **Speichern** ausgewählt haben, beginnt die Verarbeitung Ihrer Segment-Erweiterung. Wie lange es dauert, Ihre Segment-Erweiterung zu erstellen, hängt davon ab, wie viele Nutzer:innen Sie haben, wie viele angepasste Events oder Kauf-Events Sie erfassen und wie viele Tage Sie im Verlauf zurückblicken wollen.

Während Ihre Segment-Erweiterung verarbeitet wird, sehen Sie eine kleine Animation neben dem Namen der Segment-Erweiterung und das Wort "Verarbeitung" in der Spalte **"Zuletzt verarbeitet"** in der Liste Segment-Erweiterungen. Beachten Sie, dass Sie eine Segment-Erweiterung nicht bearbeiten können, während sie in Bearbeitung ist.

!["Segment-Erweiterungen" Seite mit zwei aktiven Erweiterungen.]({% image_buster /assets/img/segment/segment_extension5.png %})

Wenn eine Segment-Erweiterung verarbeitet wird, verwendet Braze für die Segmentierung der Zielgruppe weiterhin den Versionsverlauf des Standard-Segments aus der Zeit vor Beginn der Verarbeitung. Die Verarbeitung findet bei jedem Speichern oder Aktualisieren statt und beinhaltet die Abfrage und Aktualisierung von Nutzerprofilen - mit anderen Worten: Die Mitgliedschaft in Ihrem Standard Segment wird nicht sofort aktualisiert. Das bedeutet, dass wir nicht garantieren können, dass der Nutzer:innen in die Segment-Erweiterung aufgenommen wird, sobald die Aktualisierung abgeschlossen ist, es sei denn, die Aktion des Nutzers wird ausgeführt, bevor die Verarbeitung der Aktualisierung beginnt. Umgekehrt werden Nutzer:innen, die vor der Aktualisierung in der Segment-Erweiterung waren und die Kriterien nicht mehr erfüllen, weiterhin Ihrem tauben Segment zugeordnet, bis der Aktualisierungsprozess abgeschlossen ist und die Aktualisierungen angewendet werden.

### Schritt 6: Verwenden Sie Ihre Erweiterung in einem Segment

Nachdem Sie eine Segment-Erweiterung erstellt haben, können Sie diese als Filter verwenden, wenn Sie ein Segment erstellen oder eine Zielgruppe für eine Kampagne oder ein Canvas definieren. Beginnen Sie mit der Auswahl von **Braze Segment Extension** aus der Filterliste unter dem Abschnitt **Benutzerattribute**.

!["Filter"-Abschnitt mit einem Filter-Dropdown, das "Braze Segment-Erweiterungen" anzeigt.]({% image_buster /assets/img/segment/segment_extension7.png %})

Wählen Sie in der Filterliste Braze Segment-Erweiterung die Segment-Erweiterung aus, die Sie in dieses Segment ein- oder ausschließen möchten.

![Ein "Braze Segment-Erweiterungen"-Filter, der ein Segment "1 E-Mail-Klick in den letzten 56 Tagen" enthält.]({% image_buster /assets/img/segment/segment_extension6.png %})

Um die Kriterien für die Segment-Erweiterung anzuzeigen, wählen Sie **Erweiterungsdetails anzeigen**, um die Details in einem neuen Fenster anzuzeigen.

![Erweiterung für "1 E-Mail-Klick in den letzten 56 Tagen".]({% image_buster /assets/img/segment/segment_extension8.png %}){: style="max-width:70%;"}

Jetzt können Sie wie gewohnt mit der [Erstellung Ihres Segments]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) fortfahren.

## Häufig gestellte Fragen

### Kann ich eine Segment-Erweiterung erstellen, die mehrere angepasste Events verwendet?

Ja Sie können mehrere Ereignisse hinzufügen oder mehrere Snowflake-Tabellen referenzieren, wenn Sie [SQL Segment-Erweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) verwenden. 

Wenn Sie die **Einfache Erweiterung** Segment-Erweiterungen verwenden, können Sie ein angepasstes Event, ein Kauf-Event oder eine Kanal-Interaktion auswählen. Sie können jedoch mehrere Segment-Erweiterungen mit einem UND oder ODER kombinieren, wenn Sie das Standard-Segment erstellen.

### Kann ich Segment-Erweiterungen archivieren, wenn sie in einer aktiven Kampagne vorhanden sind?

Nein. Bevor Sie eine Segment-Erweiterung archivieren können, müssen Sie sie aus allen aktiven Messaging-Nachrichten entfernen.

### Kann ich Arrays in Segment-Erweiterungen verwenden?

Ja Um Arrays zu verwenden, hängen Sie eckige Klammern (`[]`) an den Namen Ihrer Eigenschaft an. Wenn Ihre Eigenschaft `location_code` ist, würden Sie `location_code[]` eingeben. 

Braze verwendet `[]`, um Arrays zu durchlaufen und zu prüfen, ob ein Artikel im durchlaufenen Array mit der Eigenschaft des Ereignisses übereinstimmt. Sie könnten zum Beispiel eine Segment-Erweiterung von Nutzer:innen erstellen, die mit mindestens einem Wert einer Eigenschaft des Arrays übereinstimmen.

### Wie berechnet Braze den Zeitraum für eine relative Zeitspanne von "letzte __ Tage"?

Wenn Segment-Erweiterungen den relativen Zeitraum ("letzte X Tage") berechnen, wird die Startzeit auf Mitternacht UTC gesetzt. Zum Beispiel wird für eine Segment-Erweiterung, die am 2024-09-16 21:00 UTC aktualisiert wird und 10 Tage angibt, die Startzeit auf 2024-09-06 00:00 UTC gesetzt, nicht auf 2024-09-06 21:00 UTC. 

Sie können jedoch die Zeitzonen angeben, indem Sie SQL-Segmente verwenden, um Nutzer:innen zu identifizieren, die das angepasste Event vor 10 Tagen auf der Basis von Mitternacht in Unternehmenszeit durchgeführt haben, oder Nutzer:innen, die das Event vor 10 Tagen auf der Basis der aktuellen Zeit durchgeführt haben.

