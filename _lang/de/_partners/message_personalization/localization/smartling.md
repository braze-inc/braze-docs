---
nav_title: Smartling
article_title: Smartling
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Smartling, einer cloudbasierten Software für die Lokalisierung. Der Braze Connector unterstützt die Übersetzung von HTML-E-Mail-Vorlagen, Content-Blöcken, Canvase und Nachrichten für Kampagnen."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling](https://www.smartling.com/) ist eine End-to-End Cloud-Übersetzungsmanagement-Software für Kunden, die die Übersetzung von Websites, Anwendungen und Kundenerlebnissen automatisieren möchten.

_Diese Integration wird von Smartling gepflegt._

## Über die Integration

Der Braze Connector unterstützt die Übersetzung von HTML-E-Mail-Vorlagen, Content-Blöcken, Canvase und Nachrichten für Kampagnen. Übersetzungen werden von Smartling angefragt, und die übersetzten Inhalte werden automatisch an Braze gesendet.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Klugscheißer-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Smartling-Konto](https://dashboard.smartling.com/). |
| Smartling Übersetzungsprojekt | Um Ihr Braze-Konto mit Smartling zu verbinden, müssen Sie sich zunächst anmelden und [ein Übersetzungsprojekt erstellen](https://help.smartling.com/hc/en-us/articles/115003074093). |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit allen Berechtigungen für Templates und Content-Blöcke. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Die Integration von Smartling Braze erlaubt Ihnen die Übersetzung von HTML-E-Mail-Vorlagen, Content-Blöcken, Canvase und Nachrichten für Kampagnen. Beachten Sie die folgenden Details, je nachdem, was Sie übersetzen möchten:

**E-Mail-Templates**
* Es werden nur HTML-Templates für E-Mails unterstützt.
* Sie müssen entscheiden, wie Ihre übersetzten E-Mails durch den Konnektor an Braze zugestellt werden sollen:
  * **Eine E-Mail für alle Sprachen:** Der Konnektor stellt alle Sprachen in der gleichen E-Mail wie die Quelle zu.
  * **Eine E-Mail pro Sprache:** Der Konnektor erstellt eine neue E-Mail für jede Sprache in Braze.

**Content-Blöcke**
* Alle Content-Blöcke werden unterstützt.
* Die Content-Blöcke enthalten sowohl die Original- als auch die übersetzte Version.
* Liquid script bestimmt die richtige Anzeigesprache anhand der Spracheinstellung des Empfängers:in.

**Kampagnen und Canvase**
* Vergewissern Sie sich, dass Sie Ihre Zielsprachen in den Einstellungen für **die Mehrsprachenunterstützung** in Braze hinzugefügt haben.
* Einzelheiten zur Konfiguration des Konnektors finden Sie in der [Dokumentation von Smartling](https://help.smartling.com/hc/en-us/articles/13248549217435).

## Integration

### Schritt 1: Richten Sie das Braze-Projekt in Smartling TMS ein

#### Braze mit Smartling verbinden

1. Erstellen Sie in [Smartling](https://dashboard.smartling.com/) einen [Braze Konnektor-Projekttyp](https://help.smartling.com/hc/en-us/articles/115003074093) in Ihrem Smartling-Konto.
  - Vergewissern Sie sich, dass alle erforderlichen Zielsprachen zum Projekt hinzugefügt wurden.
2. Wählen Sie in diesem Projekt **Einstellungen** > **Braze-Einstellungen** > **Mit Braze verbinden**.
3. Geben Sie Ihre Braze API URL und Ihren Braze API-Schlüssel ein.
4. Wählen Sie **Speichern**.

#### Vollständige Konfiguration des Braze Konnektors

Einzelheiten zur Konfiguration des Konnektors finden Sie in der [Dokumentation](https://help.smartling.com/hc/en-us/articles/13248549217435) von Smartling.

1. Wählen Sie aus, wie Sie die Automatisierung früherer Anfragen zur Übersetzung wünschen.
2. Konfigurieren Sie die Ausgangs- und Zielsprachen in der **Sprachkonfiguration**. Der Konnektor wird ihn verwenden, um Inhalte in Smartling TMS aufzunehmen und Übersetzungen an Braze zuzustellen.

![Konfiguration der Sprache des Konnektors.]({% image_buster /assets/img/smartling/smartling-braze-settings.png %})

### Schritt 2: Inhalte an Smartling senden

Sobald der Konnektor von Braze angeschlossen und eingerichtet ist, finden Sie Braze-Inhalte auf dem Tab **Braze** in Ihrem Smartling-Projekt. Lesen Sie die [Dokumentation](https://help.smartling.com/hc/en-us/articles/13248577069979) von Smartling, um mehr zu erfahren.

Smartling bietet fortschrittliche Features zum Suchen und Auswählen von Inhalten nach:

* Schlüsselwort-Suche
* Braze Content-Typ
* Braze-Tagging

![Content-Blöcke Liste.]({% image_buster /assets/img/smartling/smartling-content-blocks-list.png %})

### Schritt 3: Übersetzungen hinzufügen zu Braze

Sobald die Übersetzungen auf der Smartling-Plattform fertiggestellt sind, werden sie automatisch an Braze gesendet - eine manuelle Synchronisierung der Inhalte zwischen Smartling und Braze ist nicht erforderlich.


