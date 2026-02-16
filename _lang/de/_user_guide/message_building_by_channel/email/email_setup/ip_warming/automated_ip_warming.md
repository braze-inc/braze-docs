---
nav_title: Automatisiertes IP-Warming
article_title: Automatisiertes IP-Warming
page_order: 1
page_type: reference
description: "Dieser referenzierte Artikel behandelt die Automatisierung des IP-Warmings und die Überwachung Ihres IP-Warmings."
channel: email
---

# Automatisiertes IP-Warming

> Nutzen Sie das automatisierte IP-Warming, um das E-Mail-Volumen von einer neuen IP-Adresse aus allmählich zu erhöhen und so eine Absender-Reputation bei Posteingangsanbietern aufzubauen.

{% include early_access_beta_alert.md feature='Automated IP warming' %}

## Funktionsweise

Mit der Automatisierung des IP-Warming können Sie Ihr tägliches Sendevolumen allmählich erhöhen, so dass die Posteingangsprovider Ihre Sendemuster lernen und ihnen vertrauen können. Wenn Sie eine Domain zu Ihrem Workspace hinzufügen, können Sie die Kachel **Automatisiertes IP-Warming** im Abschnitt **Weitermachen, wo Sie aufgehört haben** auf Ihrem Home Dashboard auswählen, und diese Kachel bleibt dort für 60 Tage.

Braze sendet zuerst an die Abonnent:innen mit dem größten Engagement, so dass das tägliche Volumen in einem Tempo wachsen kann, das den besten Praktiken entspricht. Dann verfolgt Braze die Signale für Engagement und Zustellbarkeit. Wenn Braze irgendwelche Probleme feststellt, passt das System Ihren Zeitplan automatisch an.

{% alert note %}
Sie können nur ein IP-Warming durchführen.
{% endalert %}

## Voraussetzungen

Um die Automatisierung des IP-Warming durchzuführen, benötigen Sie Folgendes:

- Überprüfte Subdomain und aktive IP-Adressen
- Berechtigungen zum Anzeigen und Starten eines IP-Warmups
    - "Nutzungsdaten anzeigen", um den Bereich IP-Warming anzuzeigen
    - "E-Mail-Vorlagen anzeigen", um die E-Mail-Vorlagen für IP-Warming anzuzeigen und auszuwählen
    - "E-Mail-Einstellungen verwalten", um das IP-Warm-up zu starten
- "Zugangskampagnen" 
- "Kampagnen genehmigen und ablehnen", wenn der Genehmigungs-Workflow für Kampagnen aktiviert ist 
    - Braze genehmigt automatisch die Kampagnen, die durch automatisiertes IP-Warming in Ihrem Namen erstellt werden.

## Einrichten eines automatisierten IP-Warming-Plans

### Schritt 1: Einen Zeitplan festlegen

1. Wählen Sie im Abschnitt **Sendeinformationen** die **Absenderadresse** aus, für die Sie IP-Adressen erwärmen möchten.
2. Geben Sie das aktuelle tägliche Sendevolumen und das Targeting-Sendevolumen ein.
3. Wählen Sie das Startdatum für das automatisierte IP-Warming aus. Dieses Datum muss mindestens einen Tag nach dem Start des Plans liegen.
4. Geben Sie die Sendezeit ein. Dadurch werden die Nachrichten in der Zeitzone des Unternehmens gesendet.
5. Wählen Sie **Weiter: Segmente** um die Einrichtung fortzusetzen.

![Beispiel Zeitplan Details.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### Schritt 2: Segmente auswählen und ranken

1. Als nächstes wählen Sie die Segmente für das Targeting aus. Während des IP-Warmings beginnt Braze mit dem Versand an Ihre Nutzer:innen mit dem höchsten Engagement und erhöht im Laufe der Zeit schrittweise das Sendevolumen und fügt nach und nach Segmente mit weniger Engagement hinzu. 
2. Ziehen Sie dann die Segmente per Drag-and-Drop, um sie von hohem zu niedrigem Engagement zu ordnen. Zu einem hohen Engagement gehören Empfänger:innen, die Ihre E-Mails regelmäßig öffnen und anklicken. Zu den Empfängern mit geringem Engagement gehören Empfänger:in, die sich nicht auf Ihre E-Mails einlassen oder sich schon sehr lange nicht mehr mit Ihren E-Mails beschäftigt haben.
3. Wählen Sie **Weiter: Nachrichten**, um die Einrichtung fortzusetzen.

![Zwei Segmente wurden für das Targeting für die Automatisierung des IP-Warming ausgewählt.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### Schritt 3: Wählen Sie die zu versendenden Nachrichten aus

1. Wählen Sie **E-Mail Templates auswählen**.
2. Wählen Sie die E-Mail Templates für die zu versendenden Nachrichten. Der Inhalt, den Sie während des IP-Warmings versenden, sollte Öffnungen und Klicks fördern. Wir empfehlen, Inhalte zu wählen, die in der Vergangenheit gut angekommen sind. So können Sie zum Beispiel Werbeangebote nutzen, um sofortiges Engagement und Käufe zu fördern.
3. Wählen Sie **Templates auswählen**. Braze berechnet die Anzahl der benötigten Templates, bevor Sie starten können. Wir empfehlen Ihnen, mehr Templates als das erforderliche Minimum zur Verfügung zu stellen, damit das System bei Problemen mit der Zustellbarkeit ohne Unterbrechung reagieren kann.
4. Nachdem Sie die gewünschte Anzahl von Templates hinzugefügt haben, wählen Sie **Weiter: Zusammenfassung**.

{% alert important %}
Änderungen an Kampagnen, die mit dem IP-Warming-Tool erstellt wurden (z.B. Änderung des Zeitplans, des Segments oder des Volumens), werden nicht auf der Seite IP-Warming **Zusammenfassung** angezeigt.
{% endalert %}

### Schritt 4: Überprüfung und Einführung

Überprüfen Sie die Details Ihres IP-Warming-Plans. Wählen Sie dann **Starten**.

## Während des aktiven IP-Warmings

IP-Warming-Kampagnen werden 1 bis 2 Tage im Voraus erstellt, es sei denn, Sie starten eine IP-Warming-Kampagne am nächsten Tag. Diese Kampagnen werden automatisch in folgendem Format benannt: `IP Warming Day [X] - [Date] - [Template Name]`.

Wenn das Targeting-Ziel für den täglichen Versand erreicht ist, stoppt das System den Versand für diesen Tag, um Ihren Ruf zu schützen. 

Das System überwacht Ihre Gesundheit auf der Grundlage der folgenden Industrie-Benchmarks: 

- Die Zustellungsrate sinkt auf weniger als oder gleich 90%.
- Öffnungsrate weniger als 10%
- Bounces größer als 5%
- Spam-Beschwerdequote größer als 0,1%

Wenn die Statistiken unter unseren Benchmarks liegen, hält das System das Volumen am nächsten Tag zurück, anstatt es zu erhöhen, um das Risiko für Ihre Absender-Reputation zu minimieren.

## Stoppen Sie einen IP-Aufwärmplan

Braze erlaubt es Ihnen, das IP-Warming und die Erstellung zukünftiger Kampagnen zu stoppen, aber wenn eine Kampagne bereits aktiv oder für die nächsten 24 bis 48 Stunden geplant ist, müssen Sie die spezifische Kampagne möglicherweise manuell stoppen. Das Stoppen eines IP-Warming-Plans stoppt auch alle damit verbundenen Kampagnen.

Wenn die Aufwärmphase jedoch gestoppt wird, kann sie nicht wieder aufgenommen werden. Stattdessen müssen Sie einen neuen Plan aufstellen, um dort weiterzumachen, wo Sie aufgehört haben:

- Herunterladen der bestehenden Daten für Ihren gestoppten Plan, um sie für Ihre Unterlagen aufzubewahren, denn sobald Sie ein neues IP-Warmup starten, wird der vorherige Tracker entfernt.
- Update des **aktuellen täglichen Sendevolumens** auf das neueste Volumen
- Hinzufügen eines Filters zu einem Segment, wenn Sie planen, dasselbe Segment aus dem letzten IP Warmup zu verwenden, indem Sie Nutzer:innen ausschließen, die bereits frühere Kampagnen erhalten haben

## Wenn ein IP-Aufwärmvorgang abgeschlossen ist

Das IP-Warming wird als abgeschlossen markiert, wenn der letzte Tag des IP-Warming um Mitternacht in der Zeitzone Ihres Unternehmens endet. Wenn zum Beispiel die letzte Kampagne des IP-Warming-Plans um 20 Uhr gesendet wird, wird der Plan nach vier Stunden als erledigt markiert.

Der Tracker bleibt nach Ablauf des Plans noch 90 Tage lang auf der Homepage. Nach 90 Tagen wird der Tracker entfernt. Das Herunterladen der Daten umfasst diese Standard Metriken für E-Mails:

- _Gesendet_	
- _Zugestellt_	
- _Absprünge_	
- _Spam-Berichte_	
- _Öffnungen gesamt_	
- _Eindeutige Öffnungen_	
- _Angeklickt_	
- _Abgemeldet_

Wenn ein Tag mehrere Kampagnen enthält, die zur Erfüllung der Volumenanforderungen verwendet werden, werden diese in der Tagesansicht aggregiert.

![IP-Warming-Tracker mit Sendevolumen für die Woche vom 16\. Januar.]({% image_buster /assets/img/automated_ip_warming_example.png %})