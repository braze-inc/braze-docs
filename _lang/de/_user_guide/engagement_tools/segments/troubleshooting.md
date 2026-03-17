---
nav_title: Fehlersuche
article_title: Fehlerbehebung bei Segmenten
page_order: 12
page_type: reference
tool: 
  - Segments
description: "Dieser Referenzartikel behandelt die Schritte zur Fehlerbehebung und die Überlegungen, die Sie bei der Verwendung von Segmenten beachten müssen."
---

# Fehlerbehebung bei Segmenten

## Fehler

### Zielgruppe zu komplex zum Starten

Dieser seltene Fehler tritt auf, wenn Ihre Zielgruppe zu viele Regex-Ausdrücke, übermäßig lange Regex-Ausdrücke, übermäßig detaillierte Filter (z. B. „ist eine von 30.000 Postleitzahlen“) oder zu viele Filter enthält. Dies umfasst alle Filter in einer Kampagne oder einer Canvas-Zielgruppe, unabhängig davon, ob sich die Filter innerhalb der referenzierten Segmente befinden oder als Filter im Schritt **„Zielgruppe“** hinzugefügt wurden.

![Fehler für eine Zielgruppe, die die Komplexitätsschwelle erreicht.]({% image_buster /assets/img/segment/target_audience_too_complex_error.png %})

Wenn Sie Segmentfilter zu einer Kampagne oder einem Canvas hinzufügen, werden diese Filter in Braze in Abfragen umgewandelt (die Zeichenanzahl dieser Abfragen entspricht nicht 1:1 der Zeichenanzahl, die ein Dashboard-Nutzer:in sieht). Wenn Braze eine Kampagne oder Canvas versendet, führen wir eine Abfrage durch, die alle Filter der Zielgruppe kombiniert. Wir wenden einen Schwellenwert an, der die Anzahl der Zeichen in der resultierenden Abfrage für eine Zielgruppe begrenzt. Für eine bestimmte Kampagne oder ein bestimmtes Canvas addieren wir die Zeichenanzahl aller referenzierten Segmente, einschließlich aller zusätzlichen Filter. Für ein bestimmtes Segment summieren wir die Zeichenanzahl über alle Filter und Filterwerte hinweg.

Ihr Dashboard zeigt eine Fehlermeldung an, wenn eine Kampagne, ein Canvas oder ein Segment den Schwellenwert überschreitet und nicht gestartet werden kann. Sollten Sie diese Fehlermeldung erhalten, empfehlen wir Ihnen, Ihre Zielgruppe vor dem erneuten Start zu vereinfachen, einschließlich:

- Wenn Ihre Zielgruppen mehrere Segmente referenzieren, stellen Sie bitte sicher, dass die Segmente keine Redundanzen aufweisen, wie beispielsweise identische Filter, die in mehreren Segmenten vorkommen.
- Bitte stellen Sie sicher, dass Sie in Segmentfiltern nicht auf veraltete Daten verweisen. Beispielsweise könnte ein veralteter Filter nach Nutzer:innen suchen, die in der vergangenen Woche einen bestimmten Canvas-Schritt nicht erhalten haben, obwohl Canvas bereits seit Monaten nicht mehr verwendet wird.
- Segmente, die lediglich Listen von Benutzer-IDs oder E-Mail-Adressen enthalten (die häufig einen Regex-Filter verwenden), können in einen [CSV-Import]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) konvertiert und zu einem einzigen CSV-Filter vereinfacht werden.
- Wenn Sie über CDI verfügen, können Sie möglicherweise ein CDI-Segment erstellen, das die Gruppe direkt aus Ihrem Data Warehouse abruft.

Für weitere Unterstützung bei der Filteroptimierung können Sie [sich]({{site.baseurl}}/braze_support/) auch [an den Support wenden]({{site.baseurl}}/braze_support/).

{% alert note %}
Im April 2025 haben wir damit begonnen, die Zeichenanzahl zu begrenzen. Kampagnen und Canvases, die vor April 2025 gestartet wurden, unterliegen einer Bestandsschutzregelung, was bedeutet, dass sie weiterhin die Grenze überschreiten dürfen, während neu erstellte Kampagnen und Canvases die Grenze nicht überschreiten dürfen. Wenn Sie eine bestehende Kampagne oder ein bestehendes Canvas bearbeiten oder klonen, **können** Sie diese **erst** starten, wenn die Zielgruppe so aktualisiert wurde, dass sie unter dem Limit liegt.
{% endalert %}

### X aktive oder gestoppte Kampagnen oder Canvases überschreiten die Schwelle für die Komplexität der Zielgruppen.

Dieses Banner wird oben in einer Kampagne oder Canvas-Liste angezeigt, wenn aktive oder angehaltene Kampagnen oder Canvases Zielgruppen haben, die den Schwellenwert für die Zielgruppenkomplexität überschreiten. Wählen Sie das Banner aus, um die Liste auf die Kampagnen oder Canvases zu filtern, die den Schwellenwert überschreiten. Befolgen Sie anschließend die Schritte zur Fehlerbehebung unter [„Zielgruppe ist zu komplex, um gestartet zu werden](#target-audience-is-too-complex-to-launch)“.

![Fehlermeldung, die besagt, dass 4 aktive oder angehaltene Canvases den Schwellenwert für die Komplexität der Zielgruppe überschreiten.]({% image_buster /assets/img/segment/audience_complexity_threshold_banner.png %})

### Der Filter überschreitet 10.000 Bytes oder ist zu umfangreich, um gespeichert zu werden.

Braze begrenzt einzelne Segment-Filter auf maximal 10.000 Byte, was 10.000 englischen Zeichen oder 3.333 japanischen Zeichen entspricht. Eine Warnung wird angezeigt, wenn ein einzelner Filter 10.000 Byte überschreitet, unabhängig davon, ob sich der Filter innerhalb eines Segments befindet oder direkt zur Kampagne oder zu Canvas hinzugefügt wurde. 

![Fehlermeldung für einen Filter, dessen Wert 10.000 Zeichen überschreitet.]({% image_buster /assets/img/segment/filter_error.png %})

![Fehler bei einem angepassten Attribut-Filter,`menu_item`,dessen Attributwert 10.000 Zeichen überschreitet.]({% image_buster /assets/img/segment/segment_filter_error.png %})


Dieser Fehler tritt äußerst selten auf, jedoch in der Regel bei Regex-Filtern, die auf eine Liste von Benutzer-IDs oder E-Mail-Adressen abzielen. In diesem Fall können Sie die folgenden Schritte ausführen, um die Filter in eine CSV-Datei zu konvertieren:

1. Bitte exportieren Sie die Nutzer:innen aus dem betroffenen Segment oder dem spezifischen Regex-Filter. 
2. Bitte bereinigen Sie die CSV-Datei nach Bedarf. Sie benötigen entweder die Braze-ID oder die Appboy-ID, können jedoch alle anderen Spalten entfernen, wenn diese nicht erforderlich sind. Wir empfehlen Ihnen außerdem, Ihre Daten zu überprüfen, um sicherzustellen, dass sie aktuell sind (entfernen Sie beispielsweise Nutzer:innen, die Sie nicht mehr ansprechen möchten).
3. [Importieren Sie]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) die CSV-Datei erneut, wodurch die Nutzer:innen automatisch in einem einzigen, hocheffizienten CSV-basierten Filter zusammengefasst werden.

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

### Der Nutzer:in wird zwei Apps zugewiesen, obwohl er sich nur in einer App angemeldet hat.

Beim Erstellen eines Segments können Sie Zielgruppen zusammenstellen, die [bestimmte Apps verwendet]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform) haben. Eine Nutzer:in muss eine Sitzung in einer bestimmten App gehabt haben, um dieser App zugewiesen zu werden. Es gibt jedoch zwei Szenarien, in denen eine Nutzer:in einer bestimmten App zugewiesen werden kann, ohne dass sie sich in der App angemeldet hat. 

Das erste Szenario tritt ein, wenn das`app_id`Feld bei Verwendung des`/users/track`Endpunkts ausgefüllt wird – insbesondere bei Verwendung eines [Ereignis-]({{site.baseurl}}/api/objects_filters/event_object/) oder [Kauf-Objekts]({{site.baseurl}}/api/objects_filters/purchase_object/), wie in diesem Beispiel:

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

Das zweite Szenario tritt ein, wenn das`app_id`Feld bei der Verwendung des`/users/track`Endpunkts für die Migration von Push-Tickets ausgefüllt wird, wie in diesem Beispiel: 

```json
{
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
}
```
