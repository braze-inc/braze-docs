---
nav_title: Fehlersuche
article_title: Segmente zur Fehlerbehebung
page_order: 12
page_type: reference
tool: 
  - Segments
description: "Dieser Referenzartikel behandelt die Schritte zur Fehlerbehebung und die Überlegungen, die Sie bei der Verwendung von Segmenten beachten müssen."
---

# Segmente zur Fehlerbehebung

## Fehler

### Zielgruppe zu komplex zum Starten

Dieser seltene Fehler tritt auf, wenn Ihre Zielgruppe zu viele Regex-Werte, zu lange Regex-Werte, zu detaillierte Filter (wie "ist eine von 30.000 Postleitzahlen") oder zu viele Filter enthält. Dazu gehören alle Filter in einer Kampagne oder Canvas-Zielgruppe, unabhängig davon, ob sich die Filter innerhalb der referenzierten Segmente befinden oder als Filter im Schritt **Targeting** hinzugefügt wurden.

Wenn Sie einer Kampagne oder einem Canvas Segmente hinzufügen, werden diese Filter in Braze in Abfragen übersetzt (die Anzahl der Zeichen dieser Abfragen entspricht nicht 1:1 der Anzahl der Zeichen, die ein Nutzer:innen des Dashboards sieht). Wenn Braze eine Kampagne oder ein Canvas versendet, führen wir eine Abfrage durch, die alle Filter der Zielgruppen kombiniert. Wir wenden einen Schwellenwert an, der die Anzahl der Zeichen in der resultierenden Suchanfrage für eine Zielgruppe begrenzt. Für eine bestimmte Kampagne oder ein bestimmtes Canvas summieren wir die Anzahl der Zeichen über alle referenzierten Segmente, einschließlich aller zusätzlichen Filter. Für ein bestimmtes Segment summieren wir die Anzahl der Zeichen über alle Filter und Filterwerte hinweg.

Auf Ihrem Dashboard wird eine Fehlermeldung angezeigt, wenn eine Kampagne, ein Canvas oder ein Segment den Schwellenwert überschreitet und nicht gestartet werden kann. Wenn Sie diese Fehlermeldung erhalten, vereinfachen Sie Ihr Targeting, bevor Sie erneut starten, einschließlich:

- Wenn Ihre Zielgruppe mehrere Segmente referenziert, stellen Sie sicher, dass die Segmente keine Redundanzen aufweisen, z. B. dieselben Filter in mehreren Segmenten.
- Stellen Sie sicher, dass Sie in den Filtern für Segmente nicht auf veraltete Daten verweisen. Ein veralteter Filter könnte zum Beispiel nach Nutzer:innen suchen, die einen bestimmten Canvas-Schritt in der letzten Woche nicht erhalten haben, obwohl der Canvas schon seit Monaten eingestellt ist.
- Segmente, bei denen es sich lediglich um Listen von Nutzer:innen IDs oder E-Mails handelt (für die häufig ein Regex-Filter verwendet wird), können in einen [CSV-Import]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) umgewandelt und in einen einzigen CSV-Filter vereinfacht werden.
- Wenn Sie über CDI verfügen, können Sie möglicherweise ein CDI-Segment erstellen, das die Gruppe direkt aus Ihrem Data Warehouse bezieht.

Sie können [sich]({{site.baseurl}}/braze_support/) auch [an den Support wenden]({{site.baseurl}}/braze_support/), wenn Sie weitere Hilfe bei der Filteroptimierung benötigen.

{% alert note %}
Wir haben im April 2025 begonnen, die Anzahl der Zeichen zu begrenzen. Für Kampagnen und Canvase, die vor April 2025 gestartet wurden, gilt der Bestandsschutz, d.h. sie können das Limit weiterhin überschreiten, während neu erstellte Kampagnen und Canvase das Limit nicht überschreiten können. Wenn Sie eine alte Kampagne oder ein Canvas bearbeiten oder klonen, können Sie die Kampagne erst **dann** einführen, wenn die Zielgruppe so aktualisiert wurde, dass sie unter dem Grenzwert liegt.
{% endalert %}

### X aktive oder gestoppte Kampagnen oder Canvase überschreiten den Schwellenwert für die Komplexität der Zielgruppe

Dieses Banner wird oben in einer Kampagne oder Canvas-Liste angezeigt, wenn aktive oder gestoppte Kampagnen oder Canvase Zielgruppen haben, die den Schwellenwert für die Komplexität der Zielgruppe überschreiten. Wählen Sie das Banner aus, um die Liste auf die Kampagnen oder Canvase zu filtern, die den Schwellenwert überschreiten, und befolgen Sie dann die Schritte zur Fehlerbehebung unter [Zielgruppe ist zu komplex zum Einführen](#target-audience-is-too-complex-to-launch).

### Filter überschreitet 10.000 Zeichen oder ist zu lang zum Speichern

Braze begrenzt die Filter für einzelne Segmente auf maximal 10.000 Zeichen. Eine Warnung wird angezeigt, wenn ein einzelner Filter 10.000 Zeichen überschreitet, unabhängig davon, ob der Filter innerhalb eines Segments oder direkt zu einer Kampagne oder einem Canvas hinzugefügt wurde. 

Dieser Fehler tritt sehr selten auf, aber wenn er auftritt, dann in der Regel bei Regex-Filtern, die eine Liste von Nutzer:innen oder E-Mail-Adressen zusammenstellen. In diesem Fall können Sie die folgenden Schritte ausführen, um die Filter in eine CSV-Datei zu konvertieren:

1. Exportieren Sie die Nutzer:innen aus dem betroffenen Segment oder dem spezifischen Regex-Filter. 
2. Bereinigen Sie die CSV-Datei nach Bedarf. Sie benötigen entweder die Braze ID oder die Appboy ID, aber Sie können alle anderen Spalten entfernen, wenn Sie sie nicht benötigen. Wir empfehlen Ihnen außerdem, Ihre Daten auf Aktualität zu prüfen (z.B. Nutzer:innen zu entfernen, die Sie nicht mehr für Ihr Targeting verwenden möchten).
3. [Importieren]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) Sie die CSV-Datei erneut, wodurch die Nutzer:innen automatisch in einem einzigen, hocheffizienten CSV-basierten Filter zusammengefasst werden.

## Benutzerverhalten

### Benutzer ist nicht mehr in einem Segment

Wenn ein Benutzer bei der Erstellung eines Segments nicht verfügbar ist, könnten sich seine Benutzerdaten, die seine Eignung für das Segment bestimmen, aufgrund seiner eigenen Aktivitäten oder anderer Kampagnen und Canvases, mit denen er zuvor interagiert hat, geändert haben. Wenn die erneute Qualifizierung aktiviert ist, werden in ihrem Nutzerprofil die neuesten Daten der erhaltenen Kampagne angezeigt.

### Informationen werden für Nutzer:innen anderer Apps angezeigt, wenn ich einen Filter für eine bestimmte App verwende

Benutzer können mehrere Apps haben. Wenn Sie also eine bestimmte App im Abschnitt **Verwendete Apps** auf der Segmentierungsseite auswählen, erhalten Sie Ergebnisse für Benutzer, die mindestens diese App haben. Der Filter liefert keine Ergebnisse für die Nutzer:innen, die ausschließlich diese App haben.

## Filterung

### Filteroptionen geändert

Ihre Filteroptionen hängen mit dem Format (Datentyp) zusammen, das Sie für Ihr angepasstes Attribut an Braze übergeben. Um den Datentyp zu überprüfen, den Braze für Ihre angepassten Attribute erkennt, navigieren Sie zu **Dateneinstellungen** > **Angepasste Attribute**.

Wenn sich Ihre Filteroptionen geändert haben, ist dies ein Hinweis darauf, dass Ihre Daten in einem anderen Format (Datentyp) an Braze übergeben werden als zuvor. Ausführliche Beschreibungen der verschiedenen Datentypen und ihrer Filteroptionen finden Sie unter [Angepasste Attribut-Datentypen]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes#custom-attribute-data-types).

Denken Sie daran, dass eine Änderung des Datentyps eines angepassten Attributs im Dashboard dazu führt, dass Daten, die in einem anderen Format an Braze gesendet werden, zurückgewiesen werden.

## Analytik und Berichterstattung

### *Gesendete Nachrichten* oder *eindeutige Empfänger* in Campaign Analytics stimmen nicht mit der Anzahl der Segmente überein 

Wenn die Anzahl der *gesendeten Nachrichten* oder der *eindeutigen Empfänger* in Ihrer Kampagnenanalyse nicht mit der Anzahl der Benutzer im Segmentfilter `Has received message from campaign X` übereinstimmt, kann dies zwei mögliche Gründe haben:

1. **Benutzer können seit dem Start der Kampagne archiviert, verwaist oder gelöscht worden sein.**<br><br>Nehmen wir zum Beispiel an, 1.000 Nutzer:innen erhalten eine Kampagne und Sie machen noch am selben Tag einen CSV-Export. Sie sehen 1.000 gemeldete Benutzer. Im Laufe des nächsten Monats werden 50 dieser 1.000 Nutzer:innen gelöscht (z .B. über den Endpunkt `users/delete`). Wenn Sie einen weiteren CSV-Export durchführen, sehen Sie 950 gemeldete Benutzer, während die Anzahl der *eindeutigen Empfänger* in **Campaign Analytics** immer noch 1.000 beträgt.<br><br>Mit anderen Worten: Die Metrik *Unique Recipients* ist eine inkrementelle Zählung, während der Segmenter und der CSV-Export eine Zählung der aktuell existierenden Benutzer liefert.<br><br>

2. **Die Kampagne ist wiederholbar, sodass Nutzer:innen mehrmals an der Kampagne teilnehmen können.**<br><br>Nehmen wir an, für eine E-Mail-Kampagne ist die Wiederholbarkeit auf null Minuten eingestellt (Benutzer können die Kampagne erneut betreten, solange sie die Anforderungen für das Zielgruppensegment erfüllen), und die Kampagne läuft bereits seit über einem Monat. Die Zahl der *gesendeten Nachrichten* in **Campaign Analytics** würde nicht mit der Zahl im Segment übereinstimmen, da dieses Feld Nachrichten enthalten würde, die an doppelte Benutzer gesendet wurden.<br><br>Das liegt daran, dass Braze einzigartige Benutzer als *einzigartige tägliche Empfänger* zählt, oder die Anzahl der Benutzer, die eine bestimmte Nachricht an einem Tag erhalten haben. Das bedeutet, dass erneut qualifizierte Nutzer:innen mehr als einmal als einmalige:r Empfänger:in gezählt werden, da das Fenster „eindeutig“ nur einen Tag lang geöffnet ist. Dies kann dazu führen, dass die Anzahl der *eindeutigen täglichen Empfänger* höher ist als die Anzahl der Benutzerprofile im CSV-Export. Die Benutzerprofile in der CSV-Datei sind wirklich einzigartig.

### Nutzer:innen werden zwei Apps zugewiesen, obwohl sie nur in einer App eine Sitzung angemeldet haben

Wenn Sie ein Segment zusammenstellen, können Sie Nutzer:innen ansprechen, die [bestimmte Apps verwendet]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform) haben. Ein Nutzer:in muss eine Sitzung in einer bestimmten App gehabt haben, um dieser App zugewiesen zu werden. Es gibt jedoch zwei Szenarien, in denen ein Nutzer:in einer bestimmten App zugewiesen werden kann, ohne dass er Sitzungen in dieser App angemeldet hat. 

Das erste Szenario ist, wenn das Feld `app_id` bei der Verwendung des Endpunkts `/users/track` ausgefüllt wird, insbesondere bei der Verwendung eines [Ereignisses]({{site.baseurl}}/api/objects_filters/event_object/) oder [Kauf-Objekts]({{site.baseurl}}/api/objects_filters/purchase_object/), wie in diesem Beispiel:

```json
{
    "events": [
    {
      "external_id": "john_doe123",
      "app_id": "my_web_app_id",
      "name": "Custom Event",
      "time": "2025-08-17T19:20:30+1:00"
    }
  ]
}
```

Das zweite Szenario ist, dass das Feld `app_id` ausgefüllt wird, wenn Sie den Endpunkt `/users/track` zur Migration von Push-Tickets verwenden, wie in diesem Beispiel: 

```json
"app_group_id": "{YOUR_APP_GROUP_ID}",
"attributes": [
{
      "push_token_import": false,
      "external_id": "external_id1",
      "country": "US",
      "language": "en",
      "{YOUR_CUSTOM_ATTRIBUTE}": "{YOUR_VALUE}",
      "push_tokens": [
        {"app_id": "{APP_ID_OF_OS}", "token": "{PUSH_TOKEN_STRING}"}
      ]
  }
]
```
