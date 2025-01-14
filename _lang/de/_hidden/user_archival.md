---
nav_title: Benutzer Archivierung
article_title: Benutzer Archivierung
permalink: /user_archival/
page_order: 0
page_type: reference
description: "Dieser Referenzartikel behandelt Definitionen für die Benutzerarchivierung, die Spam-Blockierung und die Anpassung Ihrer Benutzerarchivierungsrichtlinie."

---
# Benutzerarchivierung

> Jede Woche am Sonntag um 5:30 Uhr EST führt Braze einen Prozess durch, um inaktive Benutzer und ruhende Benutzer aus den Braze-Diensten zu entfernen. Beachten Sie, dass Braze die Benutzer nur dann archiviert, wenn die Anzahl der Benutzer im Arbeitsbereich die Schwelle von 250.000 erreicht. 

Dieser Prozess soll Braze dabei helfen, genaue Statistiken über die für Kampagnen erreichbaren Zielgruppen zu erstellen. Sie dient auch der Einhaltung von zwei Schlüsselkonzepten der [DSGVO][1]:

1. Der Grundsatz der Speicherbegrenzung - verarbeitete und gespeicherte personenbezogene Daten sollten nicht länger als nötig aufbewahrt werden
2. Einen legitimen Geschäftszweck für die Verarbeitung personenbezogener Daten haben.

Das heißt, personenbezogene Daten, die verarbeitet und gespeichert werden, sollten nicht länger als nötig aufbewahrt werden, und personenbezogene Daten sollten nur für legitime Geschäftszwecke verarbeitet werden. Bei archivierten Nutzern wird auch der Abmeldestatus gelöscht, um die GDPR zu erfüllen.

{% alert note %} Kunden haben die volle Kontrolle darüber, ob ein Benutzer inaktiv oder inaktiv ist. Braze Canvas bietet die Möglichkeit, dies automatisch zu tun, so dass Sie diese Funktion für einige oder alle Ihrer inaktiven oder ruhenden Benutzer effektiv ausschalten können. {% endalert %}

## Definitionen für die Benutzerarchivierung

### Aktive Benutzer

Braze definiert einen "aktiven Benutzer" für einen bestimmten Zeitraum als jeden Benutzer, der eine Sitzung in einer mobilen App oder Website aufgezeichnet hat, aktualisiert wurde, eine Nachricht erhalten hat oder mit einer Nachricht interagiert hat.

Wenn Sie Benutzer-IDs zur Identifizierung von Benutzern festlegen, wird ein neuer Benutzer, der sich anmeldet, als separater aktiver Benutzer gezählt. Benutzer, die über die API aktualisiert werden, werden in dem Zeitraum, in dem sie aktualisiert werden, ebenfalls als aktive Benutzer gezählt.

{% alert important %}
Sowohl inaktive Benutzer als auch ruhende Benutzer werden archiviert, es sei denn, der Benutzer ist aus den unten aufgeführten Gründen von der Archivierung ausgeschlossen.
{% endalert %}

### Inaktive Benutzer

"Inaktive Benutzer" sind Benutzer, die nicht erreichbar sind und wahrscheinlich abgewandert sind. Inaktive Benutzer sind diejenigen, die alle diese Kriterien erfüllen:

- Ich kann keine E-Mails empfangen. Sie haben z.B. keine E-Mail-Adresse oder sie sind von allen E-Mail-Listen abgemeldet.
- Sie können keine SMS empfangen. Sie haben z.B. keine gültige Telefonnummer oder sie sind aus allen SMS-Abonnementgruppen abgemeldet.
- Kann keine Push-Nachrichten empfangen. Sie haben zum Beispiel die App deinstalliert oder die Push-Berechtigungen deaktiviert.
- Sie können keine WhatsApp-Nachricht empfangen. Sie haben zum Beispiel keine gültige Telefonnummer oder sind von allen WhatsApp-Abonnementgruppen abgemeldet.
- Ich habe seit mehr als sechs Monaten keine mobile App mehr benutzt oder eine Website an einem Arbeitsplatz besucht.
- Ich habe seit mehr als sechs Monaten keine Nachrichten mehr von einem Arbeitsbereich erhalten.
- Wurde seit mehr als sechs Monaten nicht mehr aktualisiert.

In diesem Fall können diese Nutzer nicht angeschrieben werden und sind nicht mit Ihrer Marke verbunden. Diese Benutzer haben sich tatsächlich abgewandt.

### Ruhende Benutzer

"Ruhende Nutzer" sind Nutzer, die in den letzten zwölf Monaten nicht aktiv waren und:

- Ich habe seit mehr als 12 Monaten keine mobile App mehr benutzt oder eine Website an einem Arbeitsplatz besucht.
- Ich habe seit mehr als 12 Monaten keine Nachrichten mehr von einem Arbeitsbereich erhalten.
- Wurde seit mehr als 12 Monaten nicht mehr aktualisiert.

## Benutzer der Global Control Group

Benutzer in der globalen Kontrollgruppe werden niemals archiviert, selbst wenn sie der Definition von inaktiven oder ruhenden Benutzern entsprechen. 

### Behandlung Stichprobengruppe

Benutzer der Behandlungsstichprobengruppe sind von der Archivierung innerhalb eines globalen Kontrollgruppenberichts ausgeschlossen.

## Test Benutzer

Testbenutzer werden niemals archiviert, auch wenn sie der Definition von inaktiven oder ruhenden Benutzern entsprechen.

## Spam-Blockierung

Braze blockiert einzelne Benutzer mit mehr als 5 Millionen Sitzungen ("Dummy-Benutzer") und nimmt ihre SDK-Ereignisse nicht mehr auf, da sie in der Regel das Ergebnis einer falschen Integration sind. Wenn Sie feststellen, dass dies bei einem rechtmäßigen Benutzer passiert ist, reichen Sie ein Ticket beim [Braze-Support]({{site.baseurl}}/braze_support/) ein.

Um die Dummy-Benutzer Ihres Dashboards zu finden, führen Sie die folgenden Schritte aus:

1. Erstellen Sie ein [Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).
2. Wählen Sie den Filter `Session Count` und setzen Sie ihn auf `more than 5,000,000`.
3. Exportieren Sie das Segment über CSV.

Falls erforderlich, können Sie die Benutzer über den [Endpunkt`/users/delete` ]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) löschen.

[1]: {{site.baseurl}}/dp-technical-assistance/#the-right-to-erasure
[2]: {% image_buster /assets/img_archive/user_archival_policy1.png %}
[3]: {% image_buster /assets/img_archive/user_archival_policy2.png %}
[4]: {% image_buster /assets/img_archive/user_archival_policy3.png %}

## Anpassen Ihrer Benutzerarchivierungsrichtlinie

Braze bietet Funktionen zur Datenorchestrierung, mit denen Sie die Archivierungsrichtlinien Ihrer Benutzer anpassen können. Erstellen Sie mit der Komponente Canvas [User Update]({{site.baseurl}}/user_update/) eine Benutzerarchivierungsrichtlinie, die Ihnen das Beste aus beiden Welten bietet.

Dies ermöglicht Ihnen:

- Halten Sie sich an die GDPR und bewährte Datenschutzpraktiken, indem Sie Benutzerprofile löschen, die nicht mehr nützlich sind.
- Behalten Sie alle Benutzerprofile, für die Sie einen legitimen geschäftlichen Bedarf haben.

### Steps

1. Wählen Sie Benutzer aus, die die Archivierungskriterien erfüllen und die Sie behalten möchten.<br><br>
      ![Zielnutzer, die zuletzt vor mehr als 23 Wochen eine Nachricht erhalten haben, noch nie eine Nachricht von einer Kampagne oder einem Canvas-Schritt erhalten haben, diese Apps zuletzt vor mehr als 23 Wochen verwendet haben und diese Apps genau null Mal verwendet haben.][2]<br><br>
2. Legen Sie fest, dass die Wiederwählbarkeit etwas weniger als 6 Monate beträgt.<br><br>
      ![Eingangskontrollen mit eingeschalteter Wiedererstattungsfähigkeit und einem Wiedererstattungsfenster von 23 Wochen.][3]<br><br>
3. Konfigurieren Sie den Schritt Benutzeraktualisierung, um jedem Profil ein Ereignis hinzuzufügen.<br><br>
      ![Schritt der Benutzeraktualisierung, der das Ereignis "do_not_archive" zum Profil des Benutzers hinzufügt.][4]
{% details Beispiel für ein User Update Objekt %}

{% raw %}
```json
{
    "events": [
        {
            "name": "do_not_archive",
            "time": "{{ 'now' | time_zone: 'UTC' | date: '%Y-%m-%dT%H:%M:%SZ' }}"
        }
    ]
}
```
{% endraw %}

{% enddetails %}
