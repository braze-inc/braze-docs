---
nav_title: Anpassungen Übersicht
article_title: Anpassungen Übersicht
page_order: 10
description: "Dieser Referenzartikel behandelt die wesentlichen Konzepte zur Anpassung und Erweiterung der Messaging-Kanäle des SDK."
hidden: true
layout: redirect
redirect_to: /docs/developer_guide/getting_started/
---

# Anpassungsübersicht

> Fast alles bei Braze ist vollständig anpassbar! Die Artikel in diesem Anpassungsleitfaden beschreiben, wie Sie Ihr Braze-Erlebnis durch eine Mischung aus Konfiguration und Anpassung optimieren können. Während dieses Prozesses sollten Marketing- und Entwicklerteams eng zusammenarbeiten, um genau abzustimmen, wie die Messaging-Kanäle von Braze angepasst werden sollen.

{% alert note %}
Das Braze SDK ist ein leistungsfähiges Toolkit, das auf hohem Niveau zwei wichtige Funktionen bietet: Es hilft beim Sammeln und Synchronisieren von Benutzerdaten über verschiedene Plattformen hinweg in einem konsolidierten Benutzerprofil und verwaltet außerdem Nachrichtenkanäle wie In-App-Nachrichten, Push-Benachrichtigungen und Content Cards. Bei den Artikeln im Anpassungsleitfaden wird davon ausgegangen, dass Sie den [Prozess der SDK-Implementierung]({{site.baseurl}}/developer_guide/home) bereits durchlaufen haben.
{% endalert %}

Alle Komponenten von Braze sind barrierefrei, anpassungsfähig und individuell gestaltbar. Daher empfehlen wir Ihnen, mit den Standardkomponenten von `BrazeUI` zu beginnen und diese an Ihre Marke und Ihren Anwendungsfall anpassen. Bei Braze gliedern wir die Anpassung in drei verschiedene Ansätze, basierend auf dem verbundenen Aufwand und dem Grad der Flexibilität. Diese Ansätze werden als "Crawl", "Walk" und "Run" bezeichnet.

- **Crawl:** Nutzen Sie die grundlegenden Stil-Optionen für eine schnelle, mühelose Implementierung.
- **Walk:** Ergänzen Sie die Standard-Templates durch ein paar angepasste Stile, um sie besser auf Ihre Marke abzustimmen.
- **Run:** Passen Sie jeden Teil Ihrer Nachrichten an – vom Stil über das Verhalten bis hin zu den kanalübergreifenden Verbindungen.

<style>
table {
  width: 60%;
}
table td {
    word-break: break-word;
}
</style>

{% tabs %}
{% tab Crawl %}

![Beispiel einer Finanz-App, die Karten mit Bildunterschriften und nur Bildinhalt zeigt]({% image_buster/assets/img_archive/cc_pyrite_crawl.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Beim Crawl-Ansatz haben die Marketer die Anpassung in der Hand. Zwar ist im Vorfeld ein gewisser Entwicklungsaufwand erforderlich, um die Nachrichtenkanäle von Braze in Ihre App oder Website zu integrieren, aber mit diesem Ansatz können Sie schneller mit der Arbeit beginnen. 

Marketer bestimmen über das Dashboard den Inhalt, die Zielgruppe und den Zeitpunkt der Nachrichten. Die Stil-Optionen sind jedoch begrenzt. Dieser Ansatz eignet sich am besten für Teams mit begrenzten Entwicklerressourcen oder für Teams, die schnell einfache Inhalte teilen möchten. 

<table>
<thead>
  <tr>
    <th>Anpassung</th>
    <th>Beschreibung</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>Aufwand</b></td>
    <td>Niedrig</td>
  </tr>
    <tr>
    <td><b>Entwicklungsarbeit</b></td>
    <td>0-1 Stunden</td>
  </tr>
  <tr>
    <td><b>Kartenstil</b></td>
    <td>Verwenden Sie die Standardvorlagen von Braze.</td>
  </tr>
  <tr>
    <td><b>Verhalten</b></td>
    <td>Wählen Sie aus den Standardverhaltensoptionen.</td>
  </tr>
  <tr>
    <td><b>Analytics-Tracking</b></td>
    <td>Die Analysen werden in Braze erfasst.</td>
  </tr>
  <tr>
    <td><b>Schlüssel-Wert-Paare</b></td>
    <td>Optional, ermöglicht zusätzliche UI/UX-Anpassungen.</td>
  </tr>
</tbody>
</table>

{% endtab %}
{% tab Walk %}

![Beispiel für eine Finanz-App mit Inhaltskarten und Anpassungen]({% image_buster/assets/img_archive/cc_pyrite_walk.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Der Walk-Ansatz ist ein hybrider Ansatz für die Implementierung, bei dem sowohl Marketing- als auch Entwicklerteams zusammenarbeiten, um das Branding Ihrer App oder Website anzupassen. 

Während der Implementierung schreiben die die Entwickler einen angepassten Code, um das Aussehen eines Messaging-Kanals an Ihre Marke anzupassen. Dazu gehört das Ändern von Schriftart, Schriftgröße, abgerundeten Ecken und Farben. Bei diesem Ansatz werden immer noch die Standardoptionen verwendet und nur ein programmatischer Template-Stil ergänzt.

Marketer behalten weiterhin die Kontrolle über die Zielgruppe, den Inhalt, das On-Click-Verhalten und die Dauer im Braze-Dashboard.

<table>
<thead>
  <tr>
    <th>Anpassung</th>
    <th>Beschreibung</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>Aufwand</b></td>
    <td>Niedrig</td>
  </tr>
    <tr>
    <td><b>Entwicklungsarbeit</b></td>
    <td>0-4 Stunden</td>
  </tr>
  <tr>
    <td><b>UI</b></td>
    <td>Verwenden Sie Braze-Vorlagen oder Ihre eigenen, von Entwicklern erstellten Vorlagen.</td>
  </tr>
  <tr>
    <td><b>Verhalten</b></td>
    <td>Wählen Sie aus den Standardverhaltensoptionen.</td>
  </tr>
  <tr>
    <td><b>Analytics-Tracking</b></td>
    <td>Die Standard-Analysen werden in Braze erfasst.</td>
  </tr>
  <tr>
    <td><b>Schlüssel-Wert-Paare</b></td>
    <td>Optional, ermöglicht zusätzliche UI/UX-Anpassungen.</td>
  </tr>
</tbody>
</table>

{% endtab %}
{% tab Run %}

![Beispiel einer Finanz-App mit benutzerdefinierten Inhaltskarten und E-Mail-Erfassung]({% image_buster/assets/img_archive/cc_pyrite_run.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Beim Run-Ansatz übernehmen die Entwickler die Führung und haben die volle Kontrolle über das Nutzererlebnis. Der benutzerdefinierte Code bestimmt, wie die Nachrichten aussehen, wie sie sich verhalten und wie sie mit anderen Nachrichtenkanälen interagieren (z. B. Auslösen einer Content Card auf der Grundlage einer Push-Benachrichtigung).

Wenn Sie völlig neue, angepasste Inhalte erstellen (z. B. neue Arten von Content-Cards oder In-App-Nachrichten mit maßgeschneiderter UI), erfolgt das [Analytics-Tracking]({{site.baseurl}}/developer_guide/analytics/) nicht automatisch durch das Braze SDK. Analytics müssen programmatisch verarbeitet werden, damit Marketer weiterhin Zugriff auf Metriken wie Impressionen, Klicks und Ausblendungen im Braze-Dashboard haben. Rufen Sie Analytics-Methoden des Braze SDK auf, damit das SDK diese Daten an Braze zurückgeben kann. Für jeden Messaging-Kanal gibt es einen Analyse-Artikel mit hilfreichen Informationen.

<table>
<thead>
  <tr>
    <th>Anpassung</th>
    <th>Beschreibung</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>Aufwand</b></td>
    <td>Hängt vom Anwendungsfall ab.</td>
  </tr>
    <tr>
    <td><b>Entwicklungsarbeit</b></td>
    <td>Geringer Aufwand: 1-4 Stunden<br>Mittlerer Aufwand: 4-8 Stunden<br>Hoher Aufwand: Mehr als 8 Stunden</td>
  </tr>
  <tr>
    <td><b>UI</b></td>
    <td>Angepasst</td>
  </tr>
  <tr>
    <td><b>Verhalten</b></td>
    <td>Angepasst</td>
  </tr>
  <tr>
    <td><b>Analytics-Tracking</b></td>
    <td>Angepasst</td>
  </tr>
  <tr>
    <td><b>Schlüssel-Wert-Paare</b></td>
    <td>Erforderlich</td>
  </tr>
</tbody>
</table>
{% endtab %}
{% endtabs %}

{% alert tip %}
Wenn Entwickler und Implementierer angepasste Inhalte für Braze erstellen, besteht die Möglichkeit für eine funktionsübergreifende Zusammenarbeit mit Marketern. Wenn Sie zum Beispiel eine neue Benutzeroberfläche oder eine neue Funktionalität für eine bestimmte Komponente entwickeln, sollten Sie Ihr Team auf den Erfolg vorbereiten, indem Sie das neue Verhalten und die Integration mit Ihrem Backend dokumentieren.
{% endalert %}