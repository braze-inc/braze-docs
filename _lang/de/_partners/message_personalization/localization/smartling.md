---
nav_title: Smartling
article_title: Smartling
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Smartling, einer cloudbasierten Software für die Lokalisierung. Der Braze Connector unterstützt die Übersetzung von HTML-E-Mail-Vorlagen, Content Blocks, Canvases und Kampagnen-E-Mails."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling][5] ist eine End-to-End-Cloud-Übersetzungsmanagement-Software für Kunden, die die Übersetzung von Websites, Anwendungen und Kundenerlebnissen automatisieren möchten.

Der Braze Connector unterstützt die Übersetzung von HTML-E-Mail-Vorlagen, Content Blocks, Canvases und Kampagnen-E-Mails. Die Übersetzungen werden von Smartling angefordert, und die übersetzten Inhalte werden automatisch an Braze gesendet.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Smartling-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Smartling-Konto][2]. |
| Smartling Übersetzungsprojekt | Um Ihr Braze-Konto mit Smartling zu verbinden, müssen Sie sich zunächst anmelden und [ein Übersetzungsprojekt erstellen][6]. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit allen Berechtigungen für Vorlagen und Inhaltsblöcke. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][1]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Die Smartling Braze-Integration ermöglicht Ihnen die Übersetzung von HTML-E-Mail-Vorlagen, Inhaltsblöcken, Canvases und Kampagnen-E-Mails. Beachten Sie die folgenden Details, je nachdem, was Sie übersetzen:

**E-Mail-Templates**
* Es werden nur HTML-E-Mail-Vorlagen unterstützt.
* Sie müssen entscheiden, wie Ihre übersetzten E-Mails über den Connector an Braze übermittelt werden sollen:
  * **Eine E-Mail für alle Sprachen:** Der Connector liefert alle Sprachen in der gleichen E-Mail wie die Quelle.
  * **Eine E-Mail pro Sprache:** Der Connector erstellt für jede Sprache in Braze eine neue E-Mail.

**Content-Blöcke**
* Alle Inhaltsblöcke werden unterstützt.
* Die Inhaltsblöcke enthalten sowohl die Original- als auch die übersetzte Version.
* Liquid Script bestimmt die richtige Sprache für die Anzeige anhand der Spracheinstellung des Empfängers.

**Kampagnen und Canvase**
* Vergewissern Sie sich, dass Sie Ihre Zielsprachen unter den Einstellungen für **die Mehrsprachenunterstützung** in Braze hinzugefügt haben.
* Einzelheiten zur Konfiguration der Anschlüsse finden Sie in der [Smartling-Dokumentation][3].

## Integration

### Schritt 1: Richten Sie das Braze-Projekt in Smartling TMS ein

#### Verbinden Sie Braze mit Smartling

1. Erstellen Sie in [Smartling][2] einen [Braze Connector-Projekttyp][6] in Ihrem Smartling-Konto.
  - Vergewissern Sie sich, dass alle erforderlichen Zielsprachen zum Projekt hinzugefügt wurden.
2. Wählen Sie in diesem Projekt **Einstellungen** > **Braze-Einstellungen** > **Mit Braze verbinden**.
3. Geben Sie Ihre Braze API URL und Ihren Braze API-Schlüssel ein.
4. Wählen Sie **Speichern**.

#### Vollständige Konfiguration des Lötverbinders

Einzelheiten zur Konfiguration der Anschlüsse finden Sie in der [Smartling-Dokumentation][3].

1. Wählen Sie aus, wie Sie die Automatisierung von vorherigen Übersetzungsanfragen wünschen.
2. Konfigurieren Sie die Ausgangs- und Zielsprachen in der **Sprachkonfiguration**. Der Konnektor wird ihn nutzen, um Inhalte in Smartling TMS aufzunehmen und Übersetzungen zurück an Braze zu liefern.

![Konfiguration der Sprache des Connectors.][8]

### Schritt 2: Inhalt an Smartling senden

Sobald der Braze-Anschluss angeschlossen und eingerichtet ist, finden Sie Braze-Inhalte auf der Registerkarte **Braze** in Ihrem Smartling-Projekt. Lesen Sie die [Smartling-Dokumentation][7], um mehr zu erfahren.

Smartling bietet erweiterte Funktionen zum Suchen und Auswählen von Inhalten nach:

* Schlüsselwort-Suche
* Inhaltstyp Braze
* Braze markieren

![Liste der Inhaltsblöcke.][9]

### Schritt 3: Übersetzungen hinzufügen zu Braze

Sobald die Übersetzungen auf der Smartling-Plattform fertiggestellt sind, werden sie automatisch an Braze gesendet - eine manuelle Synchronisierung der Inhalte zwischen Smartling und Braze ist nicht erforderlich.

[1]: {{site.baseurl}}/api/basics/#endpoints
[2]: https://dashboard.smartling.com/
[3]: https://help.smartling.com/hc/en-us/articles/13248549217435
[4]: https://help.smartling.com/hc/article_attachments/13347533624347
[5]: https://www.smartling.com/
[6]: https://help.smartling.com/hc/en-us/articles/115003074093
[7]: https://help.smartling.com/hc/en-us/articles/13248577069979
[8]: {% image_buster /assets/img/smartling/smartling-braze-settings.png %}
[9]: {% image_buster /assets/img/smartling/smartling-content-blocks-list.png %}