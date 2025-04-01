---
nav_title: Nutzerarchivierung
article_title: Nutzerarchivierung
permalink: /user_archival/
page_order: 0
page_type: reference
description: "Dieser referenzierte Artikel behandelt die Definitionen der Nutzerarchivierung, die Spam-Blockierung und wie Sie Ihre Richtlinie zur Nutzer:innen-Archivierung anpassen können."

---
# Nutzerarchivierung

> Jede Woche am Sonntag um 5:30 Uhr EST führt Braze einen Prozess durch, um inaktive und inaktive Nutzer:innen aus den Serviceleistungen; Diensten zu entfernen. Beachten Sie, dass Braze die Nutzerarchivierung erst startet, wenn die Nutzeranzahl im Workspace höher als 250.000 ist. 

Dieses Verfahren soll Braze dabei helfen, genaue Statistiken über die für Kampagnen erreichbaren Zielgruppen zu erstellen. Sie dient auch der Einhaltung von zwei Schlüsselkonzepten der [DSGVO][1]:

1. Der Grundsatz der Speicherbegrenzung – verarbeitete und gespeicherte personenbezogene Daten sollten nicht länger aufbewahrt werden als notwendig
2. Es gibt einen legitimen Geschäftszweck für die Verarbeitung personenbezogener Daten.

Das heißt, personenbezogene Daten, die verarbeitet und gespeichert werden, sollten nicht länger als nötig aufbewahrt und nur für legitime Geschäftszwecke verarbeitet werden. Bei archivierten Nutzerkonten wird auch der Abmeldestatus gemäß DSGVO gelöscht.

{% alert note %} Kunden haben die volle Kontrolle darüber, ob ein Nutzer:innen inaktiv oder inaktiv ist. Braze-Canvas kann das automatisch tun, sodass Sie diese Funktion für einzelne oder alle inaktiven oder ruhenden Nutzerkonten abschalten können. {% endalert %}

## Nutzerarchivierung – Definitionen

### Aktive Nutzer:innen

Für Braze sind "aktive Nutzerkonten" solche, die in einem bestimmten Zeitraum eine Sitzung in einer mobilen App oder Website aufgezeichnet, ein Update oder eine Nachricht erhalten oder mit einer Nachricht interagiert haben.

Wenn Sie Bezeichner zur Identifizierung von Nutzern:innen festlegen, werden diese bei der Anmeldung eines neuen Nutzers als separate aktive Nutzer:innen gezählt. Nutzerkonten, die über die API aktualisiert werden, werden im Zeitraum ihrer Aktualisierung ebenfalls als aktiv gezählt.

{% alert important %}
Sowohl inaktive Nutzer:innen als auch inaktive Nutzer:innen werden archiviert, es sei denn, der Nutzer:innen ist aus den unten aufgeführten Gründen von der Archivierung ausgeschlossen.
{% endalert %}

### Inaktive Nutzerkonten

"Inaktive Nutzer:innen" sind Nutzer:innen, die nicht erreichbar sind und wahrscheinlich abgewandert sind. Inaktive Nutzer:innen sind diejenigen, die alle diese Kriterien erfüllen:

- Ich kann keine E-Mails empfangen. Sie haben z.B. keine E-Mail-Adresse oder sie haben sich von allen E-Mail-Listen abgemeldet.
- Sie können keine SMS empfangen. Sie haben z.B. keine gültige Telefonnummer oder sie sind von allen Abo-Gruppen für SMS abgemeldet.
- Kann keinen Push empfangen. Sie haben zum Beispiel die App deinstalliert oder die Push-Berechtigungen deaktiviert.
- Ich kann keine WhatsApp Nachricht empfangen. Sie haben zum Beispiel keine gültige Telefonnummer oder sind von allen Abo-Gruppen von WhatsApp abgemeldet.
- Sie können keine LINE Nachricht empfangen. Sie haben zum Beispiel keine LINE ID oder sind von allen LINE Abo-Gruppen abgemeldet.
- Seit über sechs Monaten keine mobile App benutzt oder Workspace-Website besucht
- Seit über sechs Monaten keine Workspace-Nachrichten mehr erhalten.
- Wurde seit mehr als sechs Monaten nicht mehr aktualisiert.

In diesem Fall können diese Nutzer:innen nicht durch Messaging erreicht werden und zeigen kein Engagement für Ihre Marke. Diese Nutzer:innen haben sich tatsächlich abgewandert.

### Ruhende Nutzerkonten

"Inaktive:r Nutzer:in" sind Nutzer:innen, die in den letzten zwölf Monaten nicht aktiv waren und:

- Seit über zwölf Monaten keine mobile App benutzt oder Workspace-Website besucht
- Seit über zwölf Monaten keine Workspace-Nachrichten mehr erhalten.
- Wurde seit mehr als 12 Monaten nicht mehr aktualisiert.

## Globale Kontrollgruppe Nutzer:innen

Nutzerkonten aus der globalen Kontrollgruppe auch dann nicht archiviert, wenn sie inaktiv oder ruhend sind. 

### Behandlungstichprobe

Nutzer:innen der Behandlungsstichprobe in einem Bericht der globalen Kontrollgruppe sind von der Archivierung ausgeschlossen.

## Testnutzer:innen

Testnutzer werden auch dann nicht archiviert, wenn sie inaktiv oder ruhend sind.

## Spam-Blockierung

Braze blockiert Nutzerkonten mit mehr als fünf Mio. Sitzungen ("Dummy-Konten") und nimmt ihre SDK-Ereignisse nicht mehr auf, da sie in der Regel das Ergebnis einer fehlerhaften Integration sind. Wenn Sie feststellen, dass dies bei einem rechtmäßigen Nutzer:innen passiert ist, reichen Sie ein Ticket beim Braze [Support]({{site.baseurl}}/braze_support/) ein.

Um Dummy-Konten in Ihrem Dashboard zu finden, führen Sie die folgenden Schritte durch:

1. Erstellen Sie ein [Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).
2. Wählen Sie den Filter `Session Count` aus und setzen Sie ihn auf `more than 5,000,000`.
3. Exportieren Sie das Segment über CSV.

Falls erforderlich, können Sie die Nutzer:innen über den [Endpunkt`/users/delete` ]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) löschen.

[1]: {{site.baseurl}}/dp-technical-assistance/#the-right-to-erasure
[2]: {% image_buster /assets/img_archive/user_archival_policy1.png %}
[3]: {% image_buster /assets/img_archive/user_archival_policy2.png %}
[4]: {% image_buster /assets/img_archive/user_archival_policy3.png %}

## Archivierungsrichtlinie anpassen

Braze bietet Features zur Datenorchestrierung, mit denen Sie Ihre Richtlinie für die Nutzerarchivierung ändern können. Erstellen Sie eine Richtlinie zur Nutzerarchivierung, die Ihnen das Beste aus beiden Welten bietet - mit der Komponente Canvas [User Update]({{site.baseurl}}/user_update/).

So können Sie:

- Halten Sie sich an die DSGVO und bewährte Datenschutzpraktiken, indem Sie Nutzer:innen-Profile löschen, die nicht mehr von Nutzen sind.
- Bewahren Sie alle Nutzerprofile auf, für die Sie einen legitimen geschäftlichen Grund haben.

### Schritte

1. Targeting von Nutzer:innen, die den Archivierungskriterien Ihrer Marke entsprechen und die Sie behalten möchten. Sie könnten zum Beispiel Nutzer:innen behalten, die:
    - Sie haben zuletzt vor mehr als 23 Wochen eine Nachricht erhalten oder haben noch nie eine Nachricht erhalten<br>UND<br>
    - Ihre App zuletzt vor mehr als 23 Wochen genutzt haben oder keine Sitzungen in Ihrer App hatten<br><br>
      ![Targeting Nutzer:innen, die zuletzt vor mehr als 23 Wochen eine Nachricht erhalten haben, noch nie eine Nachricht aus einer Kampagne oder einem Canvas-Schritt erhalten haben, diese Apps zuletzt vor mehr als 23 Wochen verwendet haben und diese Apps genau null Mal verwendet haben.][2]<br><br>
2. Die Neuqualifizierung bei etwas unter sechs Monaten ansetzen<br><br>
      ![Entry-Kontrollen mit aktivierter Neuqualifizierung nach 23 Wochen.][3]<br><br>
3. Konfigurieren Sie den Schritt Nutzeraktualisierung, um jedem Profil ein Ereignis hinzuzufügen.<br><br>
      ![Aufnahme des Ereignisses "do_not_archive" in das Nutzerprofil.][4]
{% details Beispielobjekt „Nutzeraktualisierung“ %}

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
