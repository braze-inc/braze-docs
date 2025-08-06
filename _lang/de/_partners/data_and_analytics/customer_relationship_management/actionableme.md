---
nav_title: actionable.me
article_title: actionable.me
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und actionable.me, einer proprietären Software und Prozessen, die es Ihnen ermöglichen, sofort das Beste aus Ihrer Braze-Investition herauszuholen."
alias: /partners/actionableme/
page_type: partner
search_tag: Partner

---

# actionable.me

> [actionable.me](https://actionable.me), das vom Team von Massive Rocket, einer Daten- und CRM-Agentur, entwickelt wurde, ist ein standardisierter und automatisierter Ansatz für die Durchführung von CRM-Programmen, der Tools und Prozesse bereitstellt, die Braze-Kunden schnell, konsistent und vorhersehbar zu einem Mehrwert verhelfen sollen. 

_Diese Integration wird von actionable.me gepflegt._

## Über die Integration

Die Integration von Braze und actionable.me erlaubt es Ihnen, einen Dienst einzurichten, um Ihre Fortschritte bei der Nutzung von Braze zu überwachen. Durch eine Kombination von Tools und Prozessen werden sie Ihre CRM Performance schnell bewerten, neue Opportunitäten identifizieren und Empfehlungen für eine bessere Performance geben.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| actionable.me Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein actionable.me Konto. |
| Braze REST API-Schlüssel | Ein REST API-Schlüssel von Braze mit den im nächsten Abschnitt aufgeführten Berechtigungen.<br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Um Braze und actionable.me zu integrieren, muss die Plattform actionable.me konfiguriert werden, und ein Braze API-Schlüssel muss in Braze erstellt und im actionable.me Dashboard konfiguriert werden.

### Schritt 1: Erstellen Sie Ihren Braze API-Schlüssel

Navigieren Sie in Braze zu **Einstellungen** > **API-Schlüssel**. Wählen Sie **Neuen API-Schlüssel erstellen** und stellen Sie sicher, dass die folgenden Berechtigungen hinzugefügt werden:

- `campaigns.list`
- `campaigns.data_series`
- `campaigns.details`
- `sends.data_series`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `events.list`
- `canvas.list`
- `canvas.data_series`
- `canvas.details`
- `canvas.data_summary`
- `kpi.mau.data_series`
- `kpi.dau.data_series`
- `kpi.new_users.data_series`
- `kpi.uninstalls.data_series`

### Schritt 2: Stellen Sie dem Team von actionable.me Informationen zur Verfügung.

Um die Integration abzuschließen, müssen Sie Ihren REST API-Schlüssel und die [URL des REST-Endpunkts]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) an Ihr actionable.me Team weitergeben. actionable.me wird dann die Verbindung herstellen und sich nach Abschluss der Einrichtung mit Ihnen in Verbindung setzen, um mit dem Austausch von Insights zu beginnen.

![Die Seite actionable.me "Plattform hinzufügen", die das Team von actionable.me konfigurieren wird.]({% image_buster /assets/img/actionableme/image2.png %})

## Fehlersuche

Kontaktieren Sie das Team von actionable.me oder Massive Rocket für weitere Unterstützung: [info@massiverocket.com](mailto:info@massiverocket.com)


