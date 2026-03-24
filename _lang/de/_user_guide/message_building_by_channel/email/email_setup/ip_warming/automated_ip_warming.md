---
nav_title: Automatisiertes IP-Warming
article_title: Automatisiertes IP-Warming
page_order: 1
page_type: reference
description: "Dieser Referenzartikel behandelt das automatisierte IP-Warming und wie Sie Ihr IP-Warming überwachen können."
channel: email
---

# Automatisiertes IP-Warming

> Nutzen Sie automatisiertes IP-Warming, um das E-Mail-Volumen von einer neuen IP-Adresse schrittweise zu erhöhen und so die Absender-Reputation bei Posteingangsanbietern aufzubauen.

{% multi_lang_include early_access_beta_alert.md feature='Automated IP warming' %}

## Funktionsweise

Sie können automatisiertes IP-Warming einsetzen, um Ihr tägliches Versandvolumen schrittweise zu erhöhen, sodass Posteingangsanbieter Ihre Versandmuster kennenlernen und ihnen vertrauen können. Wenn Sie Ihrem Workspace eine Domain hinzufügen, können Sie die Kachel **Automatisiertes IP-Warming** im Abschnitt **Weitermachen, wo Sie aufgehört haben** Ihres Start-Dashboards auswählen. Diese Kachel bleibt dort 60 Tage lang angezeigt.

Braze sendet zuerst an Ihre engagiertesten Abonnent:innen, wodurch das tägliche Volumen in einem Tempo wachsen kann, das den bewährten Verfahren entspricht. Anschließend verfolgt Braze Engagement- und Zustellbarkeitssignale. Sollte Braze Probleme feststellen, passt das System Ihren Zeitplan automatisch an.

{% alert note %}
Es ist nur ein IP-Warming durchführbar.
{% endalert %}

## Voraussetzungen

Um automatisiertes IP-Warming durchzuführen, benötigen Sie Folgendes:

- Verifizierte Subdomain und aktive IP-Adressen
- Berechtigungen zum Anzeigen und Starten eines IP-Warmups
    - „Nutzungsdaten anzeigen", um den Abschnitt zum IP-Warming anzuzeigen
    - „E-Mail-Templates anzeigen", um die E-Mail-Templates für das IP-Warming anzuzeigen und auszuwählen
    - „E-Mail-Einstellungen verwalten", um das IP-Warmup zu starten
- „Zugang zu Kampagnen"
- „Kampagnen genehmigen und ablehnen", wenn der Genehmigungsworkflow für Kampagnen aktiviert ist
    - Braze genehmigt automatisch die Kampagnen, die im Rahmen des automatisierten IP-Warmings in Ihrem Namen erstellt wurden.

## Einen automatisierten IP-Warming-Plan einrichten

### 1. Schritt: Einen Zeitplan festlegen

1. Wählen Sie im Abschnitt **Versandinformationen** die **Absenderadresse** aus, für die IP-Adressen aufgewärmt werden sollen.
2. Geben Sie das aktuelle tägliche Versandvolumen und das angestrebte Versandvolumen ein.
3. Wählen Sie das Startdatum für das automatisierte IP-Warming aus. Dieses Datum muss mindestens einen Tag nach dem Start des Plans liegen.
4. Geben Sie die Sendezeit ein. Die Nachrichten werden in der Zeitzone des Unternehmens versendet.
5. Wählen Sie **Weiter: Segmente**, um die Einrichtung fortzusetzen.

![Beispiel für Zeitplandetails.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### 2. Schritt: Segmente auswählen und priorisieren

1. Wählen Sie anschließend die Segmente aus, die Sie ansprechen möchten. Während des IP-Warmings beginnt Braze mit dem Versand an Ihre am stärksten engagierten Nutzer:innen und erhöht das Versandvolumen im Laufe der Zeit schrittweise, wobei nach und nach Segmente mit geringerem Engagement hinzugefügt werden.
2. Sortieren Sie die Segmente anschließend per Drag-and-Drop von hohem bis geringem Engagement. Hohes Engagement umfasst Empfänger:innen, die Ihre E-Mails regelmäßig öffnen und darauf klicken. Geringes Engagement umfasst Empfänger:innen, die sich unregelmäßig mit Ihren E-Mails beschäftigen oder sich seit längerer Zeit nicht mehr mit Ihren E-Mails beschäftigt haben.
3. Wählen Sie **Weiter: Nachrichten**, um die Einrichtung fortzusetzen.

![Zwei Segmente wurden für das automatisierte IP-Warming ausgewählt.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### 3. Schritt: Zu versendende Nachrichten auswählen

1. Wählen Sie **E-Mail-Templates auswählen**.
2. Wählen Sie die E-Mail-Templates für die zu versendenden Nachrichten aus. Die Inhalte, die Sie während des IP-Warmings versenden, sollten zu Öffnungen und Klicks anregen. Wir empfehlen, Inhalte auszuwählen, die in der Vergangenheit gut angekommen sind. Beispielsweise können Sie Aktionen nutzen, um sofortiges Engagement und Käufe zu fördern.
3. Wählen Sie **Templates auswählen**. Braze berechnet die Anzahl der erforderlichen Templates, bevor Sie starten können. Wir empfehlen, mehr Templates als das erforderliche Minimum bereitzustellen, damit das System bei Zustellbarkeitsproblemen Anpassungen vornehmen kann, ohne den Prozess zu unterbrechen.
4. Nachdem Sie die erforderliche Anzahl an Templates hinzugefügt haben, wählen Sie **Weiter: Zusammenfassung**.

{% alert important %}
Änderungen an den mit dem IP-Warming-Tool erstellten Kampagnen (z. B. Änderung des geplanten Datums, des Segments oder des Volumens) werden nicht auf der **Zusammenfassungsseite** des IP-Warmings angezeigt.
{% endalert %}

### 4. Schritt: Überprüfen und starten

Überprüfen Sie die Details Ihres IP-Warming-Plans. Wählen Sie anschließend **Starten**.

## Während des aktiven IP-Warmings

IP-Warming-Kampagnen werden 1 bis 2 Tage im Voraus erstellt, es sei denn, Sie starten ein IP-Warmup am nächsten Tag. Diese Kampagnen werden automatisch nach folgendem Format benannt: `IP Warming Day [X] - [Date] - [Template Name]`.

Sobald das angestrebte tägliche Versandziel erreicht ist, stellt das System den Versand für diesen Tag ein, um Ihre Reputation zu schützen.

Das System überwacht Ihren Zustand auf Grundlage der folgenden Branchen-Benchmarks:

- Zustellrate sinkt auf 90 % oder darunter
- Öffnungsrate unter 10 %
- Absprünge über 5 %
- Spam-Beschwerdequote über 0,04 %

Sollten die Statistiken unter unseren Benchmarks liegen, hält das System das Volumen am nächsten Tag konstant, anstatt es zu erhöhen, um das Risiko für Ihre Absender-Reputation zu minimieren.

## IP-Warmup-Plan beenden

Mit Braze können Sie das IP-Warming und die Erstellung zukünftiger Kampagnen stoppen. Wenn jedoch eine Kampagne bereits aktiv ist oder für die nächsten 24 bis 48 Stunden geplant ist, müssen Sie die jeweilige Kampagne möglicherweise manuell stoppen. Das Beenden eines IP-Warming-Plans beendet auch alle damit verbundenen Kampagnen.

Nach dem Beenden kann das IP-Warmup jedoch nicht fortgesetzt werden. Stattdessen müssen Sie einen neuen Plan erstellen, um dort weiterzumachen, wo Sie aufgehört haben, indem Sie:

- Die vorhandenen Daten Ihres beendeten Plans herunterladen, um sie für Ihre Unterlagen aufzubewahren, da der vorherige Tracker entfernt wird, sobald Sie ein neues IP-Warmup starten
- Das **aktuelle tägliche Versandvolumen** auf das zuletzt erreichte Volumen aktualisieren
- Einen Filter zu einem Segment hinzufügen, wenn Sie dasselbe Segment wie beim letzten IP-Warmup verwenden möchten, indem Sie Nutzer:innen ausschließen, die bereits frühere Kampagnen erhalten haben

## Wenn das IP-Warming abgeschlossen ist

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

![IP-Warming-Tracker mit Versandvolumen für die Woche vom 16. Januar.]({% image_buster /assets/img/automated_ip_warming_example.png %})