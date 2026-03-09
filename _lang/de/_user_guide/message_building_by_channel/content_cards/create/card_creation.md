---
nav_title: Kartenerstellung
article_title: Kartenerstellung
alias: /card_creation/
description: "Dieser Artikel beschreibt die Unterschiede zwischen der Erstellung von Content Cards beim Kampagnenstart oder beim Eintritt in den Canvas-Schritt und beim ersten Eindruck."
page_order: 0
tool: Campaigns
channel:
  - content cards
---

# Kartenerstellung

> Wenn Sie angeben, wann die Karte erstellt werden soll, können festlegen, wann Braze bei neuen Content-Card-Kampagnen und Canvas-Schritten Zielgruppeneignung und Personalisierung ermittelt.

## Voraussetzungen

Um dieses Feature nutzen zu können, müssen Sie mindestens auf die folgenden SDK-Versionen upgraden:

{% sdk_min_versions swift:5.2.0 android:23.0.0 web:4.2.0 %}

Nach dem SDK-Upgrade muss auch ein Upgrade der Nutzer-App durchgeführt werden. Sie können Ihre Kampagne oder Ihre Canvas-Zielgruppe so filtern, dass nur [Nutzer mit diesen Mindestversionen der App angesprochen werden]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).

## Übersicht

{% tabs %}
{% tab Campaign %}

Sie können wählen, wann Braze eine Karte im Schritt **Zustellung** erstellt, wenn Sie eine neue [Content Card Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/) mit geplanter Zustellung erstellen.

![Abschnitt „Content-Card Controls“ beim Bearbeiten der Zustellung einer geplanten Content-Card.]({% image_buster /assets/img_archive/card_creation.png %})

Die folgenden Optionen sind verfügbar:

- **Beim Start der Kampagne:** Das bisherige Standardverhalten für Inhaltskarten. Braze ermittelt Zielgruppenzugehörigkeit und Personalisierung beim Kampagnenstart, erstellt dann die Karte und speichert sie, bis Ihre App geöffnet wird. 
- **Auf den ersten Blick (empfohlen):** Wenn der Nutzer Ihre App das nächste Mal öffnet (eine neue [Sitzung](https://www.braze.com/resources/articles/whats-an-app-session-anyway) startet), ermittelt Braze, für welche Content-Cards der Nutzer berechtigt ist, erstellt Templates für Personalisierungen wie Liquid oder Connected-Content und erstellt anschließend die Content-Card. Diese Option bietet in der Regel eine bessere Performance.

Unabhängig von der von Ihnen gewählten Option beginnt der Countdown für das Ablaufdatum der Content Card, wenn die Kampagne gestartet wird.

{% endtab %}
{% tab Canvas %}

Sie können wählen, wann Braze eine Karte auf der Registerkarte **Nachrichtenkanäle** eines [Inhaltskarten-Nachrichtenschritts]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) erstellt.

![Abschnitt „Content-Card Controls“ beim Bearbeiten der Zustellung einer geplanten Content-Card.]({% image_buster /assets/img_archive/card_creation_canvas.png %})

Die folgenden Optionen sind verfügbar:

- **Zu Beginn des Schritts:** Das bisherige Standardverhalten für Inhaltskarten. Braze ermittelt Zielgruppenzugehörigkeit und Personalisierung beim Kampagnenstart, erstellt dann die Karte und speichert sie, bis Ihre App geöffnet wird.
- **Auf den ersten Blick (empfohlen):** Braze berechnet die Zielgruppenzugehörigkeit, wenn der Canvas-Schritt gestartet wird. Wenn die Nutzer:in Ihre App das nächste Mal öffnet (eine neue [Sitzung](https://www.braze.com/resources/articles/whats-an-app-session-anyway) startet), erstellt Braze alle Personalisierungen wie Liquid oder Connected-Content und erstellt anschließend die Karte. Diese Option bietet eine verbesserte Performance bei der Zustellung von Karten und eine aktuellere Personalisierung.

Unabhängig von der ausgewählten Option beginnt der Countdown für das Ablaufdatum der Content-Card, wenn der Canvas-Schritt gestartet wird.

{% alert tip %}
Wenn bei anonymen Sitzungen zu Beginn eine Content-Card angezeigt werden soll, verwenden Sie lieber eine Kampagne als ein Canvas. Denn wenn ein anonymer Benutzer ein Canvas betritt, hat seine Sitzung bereits begonnen. Er erhält die Inhaltskarte also erst, wenn er eine neue Sitzung beginnt.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert note %}
Bei beiden Verfahren berechnet Braze nach der Kartenerstellung weder Zielgruppenzugehörigkeit noch Personalisierung neu.
{% endalert %}

### Unterschiede zwischen der Erstellung von Karten beim Start oder beim Eingang und beim ersten Eindruck {#differences}

In diesem Abschnitt werden die wichtigsten Unterschiede zwischen der Kartenerstellung beim Kampagnenstart oder beim Einstieg in den Schritt und beim ersten Eindruck beschrieben.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
.leftHeader{font-size: 12px; font-weight: bold; background-color: #f4f4f7; text-transform: uppercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">Kampagnenstart / Entry in den Canvas-Schritt</th>
    <th class="tg-0pky">Bei der ersten Impression</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">Einsatzmöglichkeiten</td>
    <td class="tg-0pky">Wenn Sie den Inhalt zu einem bestimmten Zeitpunkt (der Startzeit) als Snapshot benötigen.</td>
    <td class="tg-0pky"><ul><li>Wenn Sie neuen oder anonymen Nutzern, die nach dem Kampagnenstart der Kampagne in das Segment eintreten können, Karten anzeigen möchten (<a href="#campaign_note">nur Kampagnen*</a>).</li><li>Wenn Sie die Personalisierung verwenden und möchten, dass die neuesten Inhalte auf der Karte verfügbar sind.</li></ul></td>
  </tr>
  <tr>
    <td class="leftHeader">Zielgruppe</td>
    <td class="tg-0pky">Braze wertet die Zielgruppenzugehörigkeit aus, wenn die Kampagne gesendet wird.<br><br>Neue und anonyme Nutzer:innen werden nicht auf ihre Zielgruppenzugehörigkeit hin geprüft, wenn sie versuchen, die Karte nach dem Kampagnenversand anzusehen. Bei wiederkehrenden Kampagnen erfolgt dies im nächsten Wiederholungsintervall.</td>
    <td class="tg-0pky">Braze ermittelt die Zielgruppenzugehörigkeit, wenn Ihre App das nächste Mal geöffnet wird (Sitzungsbeginn, <a href="#campaign_note">nur Kampagnen*</a>).<br><br> Diese Einstellung hat eine größere Reichweite, da neue oder anonyme Benutzer immer auf ihre Berechtigung geprüft werden, wenn sie versuchen, die Karte einzusehen. <br><br>Darüber hinaus ist das Rate-Limiting (Begrenzung der Anzahl der Personen, die die Karte erhalten) nicht anwendbar, wenn es auf „auf den ersten Eindruck“ eingestellt ist.</td>
  </tr>
  <tr>
    <td class="leftHeader">Personalisierung</td>
    <td class="tg-0pky">Braze bewertet Liquid, Connected Content und Content-Blöcke zum Zeitpunkt des Kampagnenstarts oder wenn ein Benutzer den Canvas-Schritt betritt. Bei wiederkehrenden Kampagnen erfolgt dies im nächsten Wiederholungsintervall.</td>
    <td class="tg-0pky">Braze wertet Liquid, Connected-Content und Content-Blöcke bei der ersten Impression oder nach dem nächsten Wiederholungsintervall aus.</td>
  </tr>
  <tr>
    <td class="leftHeader">Analytics</td>
  <td class="tg-0pky"><em>„Gesendete Nachrichten“</em> bezieht sich auf die Anzahl der von Braze erstellten und zur Verfügung gestellten Karten. Dies berücksichtigt nicht, ob die Nutzer:innen die Karte angesehen haben.</td>
  <td class="tg-0pky"><em>„Gesendete Nachrichten“</em> referenziert die Anzahl der Karten, die Braze nach Beginn einer Sitzung an einen Nutzer:in sendet. Wenn eine Nutzer:in in Braze-Canvas den Schritt aufruft, ohne eine Sitzung zu starten, sendet Braze keine Karte, sodass diese Metrik möglicherweise nicht mit der Anzahl der Nutzer:innen übereinstimmt, die einen Schritt aufrufen.<br><br>Während die erreichbaren Nutzer:innen und Impressionen unverändert bleiben, ist bei der Erstellung einer Karte beim ersten Eindruck im Vergleich zum Start der Kampagne oder zum Einstieg in den Canvas-Schritt mit einem geringeren Versandvolumen (<em>gesendete Nachrichten</em>) zu rechnen.</td>
  </tr>
  <tr>
    <td class="leftHeader">Bearbeitungszeit</td>
  <td class="tg-0pky">Braze erstellt zum Zeitpunkt der Einführung Karten für jeden berechtigten Nutzer in diesem Segment. Für eine große Zielgruppe wählen Sie bitte <b>„At First Impression“</b>, damit die Karten nach dem Start schneller verfügbar sind.</td>
  <td class="tg-0pky">Braze erstellt eine Karte, wenn eine Nutzer:in zum ersten Mal versucht, sie anzuzeigen. Daher kann es beim ersten Aufruf 1–2 Sekunden dauern, bis sie angezeigt wird.</td>
  </tr>
</tbody>
</table>

<p id="campaign_note"><sup>* Dieses Szenario gilt nur für Kampagnen, da die Canvas-Zielgruppe beim Canvas-Entry und nicht auf Schrittebene ermittelt wird.</sup></p>

## Überlegungen

### Kartenerstellung nach dem Launch ändern

Braze empfiehlt, die Kartenerstellung nach dem Kampagnenstart nicht mehr zu ändern. Aufgrund der Unterschiede bei der Berechnung der gesendeten Nachrichten zwischen den beiden Arten der Kartenerstellung kann eine Änderung der Art der Kartenerstellung nach dem Start der Kampagne die Genauigkeit Ihres Sendevolumens beeinflussen.

### Mögliche Bearbeitungszeit

Für große Zielgruppen wählen Sie bitte die Option, Karten beim ersten Eindruck zu erstellen, damit die Karten nach dem Start schnell verfügbar sind. Kampagnen, die zu Beginn einer Sitzung getriggert werden, können ebenfalls von einer Umstellung auf „Erster Eindruck“ (verfügbar über geplante Zustellung) profitieren, um die Performance zu verbessern.

Wenn Karten bei der ersten Impression erstellt werden, kann es 1–2 Sekunden dauern, bis die Karten verarbeitet sind. Die Bearbeitungsdauer hängt von verschiedenen Faktoren wie der Kartengröße und der Komplexität der Template-Erstellung ab. Die Bearbeitungsdauer von Karten mit Connected-Content ist zum Beispiel mindestens so lang wie die Reaktionszeit bei Connected-Content.

### Frühere SDK-Versionen

Wenn die App eines Nutzers eine frühere SDK-Version verwendet, erhält er weiterhin die von Ihnen gesendeten Content-Cards. Allerdings dauert es länger, bis die Karten angezeigt werden, und sie werden möglicherweise erst bei der nächsten Synchronisierung der Content-Cards angezeigt.

