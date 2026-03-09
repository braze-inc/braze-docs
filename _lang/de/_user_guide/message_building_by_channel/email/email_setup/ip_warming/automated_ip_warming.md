---
nav_title: Automatisiertes IP-Warming
article_title: Automatisiertes IP-Warming
page_order: 1
page_type: reference
description: "Dieser Referenzartikel behandelt die Automatisierung des IP-Warmings und die Überwachung Ihres IP-Warmings."
channel: email
---

# Automatisiertes IP-Warming

> Nutzen Sie automatisiertes IP-Warming, um das E-Mail-Volumen von einer neuen IP-Adresse schrittweise zu erhöhen und so die Absender-Reputation bei den Posteingangsanbietern aufzubauen.

{% multi_lang_include early_access_beta_alert.md feature='Automated IP warming' %}

## Funktionsweise

Sie können automatisiertes IP-Warming einsetzen, um Ihr tägliches Versandvolumen schrittweise zu erhöhen, sodass Posteingänge Ihre Versandmuster kennenlernen und ihnen vertrauen können. Wenn Sie Ihrem Workspace eine Domain hinzufügen, können Sie die Kachel **„Automatisches IP-Warming“** im Abschnitt **„Weitermachen, wo Sie aufgehört haben**“ Ihres Start-Dashboards auswählen. Diese Kachel bleibt 60 Tage lang dort angezeigt.

Braze sendet Ihre Nachrichten zuerst an Ihre engagiertesten Abonnent:innen, wodurch das tägliche Volumen in einem Tempo wachsen kann, das den bewährten Verfahren entspricht. Anschließend verfolgt Braze das Engagement und die Signale zur Zustellbarkeit. Sollte Braze Probleme feststellen, passt das System Ihren Zeitplan automatisch an.

{% alert note %}
Es ist nur eine IP-Warming-Maßnahme durchführbar.
{% endalert %}

## Voraussetzungen

Um automatisiertes IP-Warming durchzuführen, benötigen Sie Folgendes:

- Überprüfte Subdomains und aktive IP-Adressen
- Berechtigungen zum Anzeigen und Starten eines IP-Warmups
    - Bitte klicken Sie auf „Nutzungsdaten anzeigen“, um den Abschnitt zum IP-Warming anzuzeigen.
    - „E-Mail-Templates anzeigen“, um die E-Mail-Templates für das IP-Warming anzuzeigen und auszuwählen.
    - Bitte klicken Sie auf „E-Mail-Einstellungen verwalten”, um das IP-Warmup zu starten.
- Zugangskampagnen 
- „Kampagnen genehmigen und ablehnen“, wenn der Genehmigungsworkflow für Kampagnen aktiviert ist 
    - Braze genehmigt automatisch die Kampagnen, die aus der Automatisierung des IP-Warming in Ihrem Namen erstellt wurden.

## Erstellen Sie einen automatisierten IP-Warming-Plan.

### Schritt 1: Einen Zeitplan festlegen

1. Wählen Sie im Abschnitt **„Informationen senden**“ die Option **„Von-Adresse** für IP-Adressen aufwärmen“ aus.
2. Bitte geben Sie das aktuelle tägliche Versandvolumen und das angestrebte Versandvolumen ein.
3. Bitte wählen Sie das Startdatum für das automatische IP-Warming aus. Dieses Datum muss mindestens einen Tag nach dem Start des Plans liegen.
4. Bitte geben Sie die Sendezeit ein. Dies bewirkt, dass die Nachrichten in der Zeitzone des Unternehmens versendet werden.
5. Wählen Sie **Weiter: Segmente, **um die Einrichtung fortzusetzen.

![Beispiel für einen detaillierten Zeitplan.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### Schritt 2: Segmente auswählen und bewerten

1. Wählen Sie anschließend die Segmente aus, die Sie ansprechen möchten. Während des IP-Warming beginnt Braze mit dem Versand an Ihre am stärksten engagierten Nutzer:innen und erhöht das Versandvolumen im Laufe der Zeit schrittweise, wobei nach und nach Segmente mit geringerer Interaktion hinzugefügt werden. 
2. Anschließend können Sie die Segmente per Drag-and-Drop sortieren, um sie nach hohem bis geringem Engagement zu ordnen. Ein hohes Engagement umfasst Empfänger:innen, die Ihre E-Mails regelmäßig öffnen und Klicks darauf durchführen. Geringes Engagement umfasst Empfänger:innen, die sich unregelmäßig mit Ihren E-Mails beschäftigen oder sich seit längerer Zeit nicht mehr mit Ihren E-Mails beschäftigt haben.
3. Wählen Sie **Weiter: Nachrichten** zur Fortsetzung der Einrichtung.

![Zwei Segmente wurden ausgewählt, um sie für automatisiertes IP-Warming zu nutzen.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### Schritt 3: Bitte wählen Sie die zu versendenden Nachrichten aus.

1. **Bitte wählen** **Sie E-Mail-Templates** aus.
2. Bitte wählen Sie die E-Mail-Templates für die zu versendenden Nachrichten aus. Die Inhalte, die Sie während des IP-Warming-Prozesses versenden, sollten zur Öffnung und zum Klick anregen. Wir empfehlen, Inhalte auszuwählen, die in der Vergangenheit gut angekommen sind. Beispielsweise können Sie Aktionen nutzen, um sofortiges Engagement und Käufe zu fördern.
3. Auswählen **von Templates**. Braze berechnet die Anzahl der erforderlichen Templates, bevor Sie starten können. Wir empfehlen, mehr Templates als das erforderliche Minimum bereitzustellen, damit das System Probleme bei der Zustellbarkeit ohne Unterbrechung anpassen kann.
4. Nachdem Sie die erforderliche Anzahl an Templates hinzugefügt haben, wählen Sie **„Weiter“: Zusammenfassung**.

{% alert important %}
Änderungen an den mit dem IP-Warming-Tool erstellten Kampagnen (z. B. Änderung des Zeitplans, des Segments oder des Volumens) werden nicht auf der Übersichtsseite **für** IP-Warming angezeigt.
{% endalert %}

### Schritt 4: Überprüfung und Einführung

Bitte überprüfen Sie die Einzelheiten Ihres IP-Warming-Plans. Wählen Sie anschließend **„Starten**“.

## Während des aktiven IP-Warmings

IP-Warming-Kampagnen werden 1 bis 2 Tage im Voraus erstellt, es sei denn, Sie starten ein IP-Warming am nächsten Tag. Diese Kampagnen werden automatisch nach folgendem Format benannt: `IP Warming Day [X] - [Date] - [Template Name]`.

Sobald das angestrebte tägliche Versandziel erreicht ist, stellt das System den Versand für diesen Tag ein, um Ihre Reputation zu schützen. 

Das System überwacht Ihre Gesundheit auf Grundlage der folgenden Branchen-Benchmarks: 

- Die Zustellung sinkt auf weniger als oder gleich 90 %.
- Öffnungsrate unter 10 %
- Abspringer von mehr als 5 %
- Spam-Beschwerdequote von mehr als 0,1 %

Sollten die Statistiken unter unseren Benchmarks liegen, wird das System das Volumen am nächsten Tag zurückhalten, anstatt es zu erhöhen, um das Risiko für Ihre Absender-Reputation zu minimieren.

## IP-Warmup-Plan beenden

Mit Braze können Sie das IP-Warming und die Erstellung zukünftiger Kampagnen stoppen. Wenn jedoch eine Kampagne bereits aktiv ist oder im Zeitplan für die nächsten 24 bis 48 Stunden steht, müssen Sie die jeweilige Kampagne möglicherweise manuell stoppen. Das Beenden eines IP-Warming-Plans beendet auch alle damit verbundenen Kampagnen.

Nach dem Beenden kann die IP-Aufwärmphase jedoch nicht fortgesetzt werden. Stattdessen müssen Sie einen neuen Plan erstellen, um dort weiterzumachen, wo Sie aufgehört haben, indem Sie:

- Bitte laden Sie die vorhandenen Daten Ihres beendeten Plans herunter, um sie für Ihre Unterlagen aufzubewahren. Sobald Sie einen neuen IP-Warmup starten, wird der vorherige Tracker entfernt.
- Update des **aktuellen täglichen Versandvolumens** auf das aktuellste Volumen
- Hinzufügen eines Filters zu einem Segment, wenn Sie beabsichtigen, dasselbe Segment wie beim letzten IP-Warmup zu verwenden, indem Sie Nutzer:innen ausschließen, die bereits frühere Kampagnen erhalten haben.

## Wenn das Aufwärmen der IP abgeschlossen ist

Das IP-Warming gilt als abgeschlossen, wenn der letzte Tag des IP-Warmings um Mitternacht in der Zeitzone Ihres Unternehmens endet. Wenn beispielsweise die letzte Kampagne im Rahmen des IP-Warming-Plans um 20 Uhr versendet wird, wird der Plan nach vier Stunden als abgeschlossen markiert.

Der Tracker bleibt nach Ablauf des Plans noch 90 Tage lang auf der Startseite. Nach 90 Tagen wird der Tracker entfernt. Der Download der Daten umfasst die folgenden Standard-E-Mail-Metriken:

- _Gesendet_	
- _Zugestellt_	
- _Absprünge_	
- _Spam-Berichte_	
- _Öffnungen gesamt_	
- _Eindeutige Öffnungen_	
- _Angeklickt_	
- _Abgemeldet_

Wenn an einem Tag mehrere Kampagnen durchgeführt werden, um die Volumenanforderungen zu erfüllen, werden diese in der Tagesansicht zusammengefasst.

![IP-Warming-Tracker mit Versandvolumen für die Woche vom 16\. Januar.]({% image_buster /assets/img/automated_ip_warming_example.png %})