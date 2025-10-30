{% if include.section == "Differing audience size" %}

Die Größe der Zielpopulation, die in einer Kampagne oder einem Canvas angezeigt wird, kann sich von der [Größe der erreichbaren Zielgruppe für ein Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size#segment-membership-calculation) unterscheiden, selbst wenn Sie dieses Segment ohne zusätzliche Filter direkt in Ihre Kampagne oder Ihr Canvas einfügen.
Dafür kann es mehrere Gründe geben:

- Wenn eine globale Kontrollgruppe für eine Kampagne oder ein Canvas gilt, werden Nutzer:innen in dieser globalen Kontrollgruppe bei der Zählung der erreichbaren Nutzer:innen ausgeschlossen.
- Die Zielpopulation einer Kampagne oder eines Canvas schließt Nutzer:innen aus, die nicht über die verschiedenen Nachrichten-Kanäle kontaktiert werden können; das Verhalten unterscheidet sich von Kanal zu Kanal. So schließt die erreichbare Zielgruppe für eine Kampagne oder ein Canvas beispielsweise Nutzer:innen aus, die abgemeldet, als Spam markiert (bei E-Mails) oder als "soft bounced" (bei E-Mails) markiert sind. Das Segment selbst schließt jedoch nur Opt-outs aus, wenn es die geschätzte Anzahl der per E-Mail erreichbaren Nutzer:innen anzeigt. 
- Braze sendet SMS-Nachrichten nur an Nutzer:innen der ausgewählten Abo-Gruppe. Daher schließt die SMS Zielpopulation für eine Kampagne oder ein Canvas auch alle Nutzer:innen aus, die nicht zu Ihrer ausgewählten Abo-Gruppe gehören.

{% endif %}

{% if include.section == "Refresh settings" %}

Wenn Sie Ihre Erweiterung nicht regelmäßig aktualisieren müssen, können Sie sie auch ohne Aktualisierungseinstellungen speichern. Braze generiert Ihre Segmenterweiterung dann standardmäßig auf der Grundlage Ihrer aktuellen Benutzerzugehörigkeit. Verwenden Sie das Standardverhalten, wenn Sie die Zielgruppe nur einmal generieren und sie dann mit einer einmaligen Kampagne ansprechen möchten.

Die Verarbeitung Ihres Segments beginnt immer nach dem ersten Speichern. Jedes Mal, wenn Ihr Segment aktualisiert wird, führt Braze das Segment erneut aus und aktualisiert die Segmentmitgliedschaft, um die Benutzer in Ihrem Segment zum Zeitpunkt der Aktualisierung wiederzugeben. So können Ihre wiederkehrenden Kampagnen die relevantesten Nutzer erreichen.

#### Einrichten einer wiederkehrenden Aktualisierung

Um einen wiederkehrenden Zeitplan einzurichten, indem Sie Aktualisierungseinstellungen festlegen, wählen Sie **Enablement der Aktualisierung**. Die Option zur Festlegung von Aktualisierungseinstellungen ist für alle Arten von Segment-Erweiterungen verfügbar, einschließlich SQL-Segmente, CDI-Segment-Erweiterungen und einfache formularbasierte Segment-Erweiterungen.

{% alert important %}
Um Ihre Datenverwaltung zu optimieren, werden die Aktualisierungseinstellungen für nicht verwendete Segment-Erweiterungen automatisch deaktiviert. Segment-Erweiterungen werden als ungenutzt betrachtet, wenn sie sind:

- Nicht in aktiven oder inaktiven (Entwurf, gestoppt, archiviert) Kampagnen, Canvase oder Segmenten verwendet; oder
- Keine Änderungen in den letzten 7 Tagen

Braze benachrichtigt den Firmenkontakt und den Ersteller der Erweiterung, wenn diese Einstellung deaktiviert ist. Die Option, die Erweiterungen täglich zu regenerieren, kann jederzeit wieder aktiviert werden.
{% endalert %}

#### Auswählen Ihrer Aktualisierungseinstellungen

![Aktualisierungsintervall Einstellungen mit einer wöchentlichen Aktualisierungsfrequenz, einer Startzeit von 10 Uhr und dem ausgewählten Montag als Tag.]({% image_buster /assets/img/segment/segment_interval_settings.png %}){: style="max-width:50%;"}

Im Panel **Aktualisierungsintervall-Einstellungen** können Sie die Häufigkeit auswählen, mit der diese Segment-Erweiterung aktualisiert wird: stündlich, täglich, wöchentlich oder monatlich. Sie müssen auch die genaue Uhrzeit (die in der Zeitzone Ihres Unternehmens liegt) für die Aktualisierung auswählen, z. B:

- Wenn Sie eine E-Mail-Kampagne haben, die jeden Montag um 11 Uhr Unternehmenszeit versendet wird, und Sie sicherstellen möchten, dass Ihr Segment kurz vor dem Versand aktualisiert wird, sollten Sie einen Aktualisierungszeitplan wählen, der wöchentlich montags um 10 Uhr gilt.
- Wenn Sie möchten, dass Ihr Segment jeden Tag aktualisiert wird, wählen Sie die tägliche Aktualisierungshäufigkeit und dann die Tageszeit für die Aktualisierung aus.

{% alert note %}
Die Möglichkeit, einen stündlichen Zeitplan für die Aktualisierung festzulegen, ist für formularbasierte Segmenterweiterungen nicht verfügbar (Sie können jedoch tägliche, wöchentliche oder monatliche Zeitpläne festlegen).
{% endalert %}

#### Kreditverbrauch und zusätzliche Kosten

Da bei Aktualisierungen die Abfrage Ihres Segments erneut ausgeführt wird, verbraucht jede Aktualisierung für SQL-Segmente SQL-Segmentguthaben, und jede Aktualisierung für CDI Segment-Erweiterungen verursacht Kosten innerhalb Ihrer Drittanbieter-Daten im Data Warehouse.

{% alert note %}
Segmente können aufgrund von Datenverarbeitungszeiten bis zu 60 Minuten für die Aktualisierung benötigen. Segmente, die gerade aktualisiert werden, haben in Ihrer Liste Segmenterweiterungen den Status "In Bearbeitung". Dies hat einige Auswirkungen:

- Um die Verarbeitung Ihres Segments vor einer bestimmten Zeit abzuschließen, wählen Sie eine Aktualisierungszeit, die 60 Minuten früher liegt. 
- Für eine bestimmte Segmenterweiterung kann jeweils nur eine Aktualisierung erfolgen. Wenn es einen Konflikt gibt, bei dem eine neue Anfrage zur Aktualisierung gestartet wird, während die Verarbeitung einer bestehenden Aktualisierung bereits begonnen hat, bricht Braze die neue Anfrage zur Aktualisierung ab und setzt die laufende Verarbeitung fort.
{% endalert %}

#### Kriterien zur automatischen Deaktivierung veralteter Erweiterungen

Geplante Aktualisierungen werden automatisch deaktiviert, sobald eine Segment-Erweiterung veraltet ist. Eine Segment-Erweiterung ist veraltet, wenn sie die folgenden Kriterien erfüllt:

- Nicht in aktiven Kampagnen oder Canvasen verwendet
- Wird in keinem Segment verwendet, das sich in einer aktiven Kampagne oder einem Canvas befindet
- Wird in keinem Segment verwendet, in dem [Analytics Tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) aktiviert ist.
- Wurde seit über sieben Tagen nicht mehr geändert
- Wurde seit mehr als sieben Tagen nicht zu einer Kampagne, einem Canvas (einschließlich Entwürfen) oder einer Segmentierung hinzugefügt.

Wenn die geplante Aktualisierung für eine Segment-Erweiterung deaktiviert ist, erhält diese Erweiterung eine entsprechende Benachrichtigung.

![Eine Benachrichtigung, die besagt, dass "Geplante Aktualisierungen für diese Erweiterung ausgeschaltet wurden, da sie in keinen aktiven Kampagnen, Canvase oder Segmenten verwendet wird. Die Segment-Erweiterung wurde am 23\. Februar 2025 um 12:00 Uhr deaktiviert."]({% image_buster /assets/img/segment/segment_extension_disabled.png %})

Wenn Sie bereit sind, eine veraltete Segment-Erweiterung zu verwenden, überprüfen Sie die Aktualisierungseinstellungen, wählen Sie den Zeitplan für die Aktualisierung aus, der zu Ihrem Anwendungsfall passt, und speichern Sie dann alle Änderungen.

{% endif %}