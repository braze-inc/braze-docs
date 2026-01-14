---
nav_title: DataGrail
article_title: DataGrail
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und DataGrail, einer Plattform zur Verwaltung des Datenschutzes, die es Ihnen erlaubt, Verbraucher:in-Daten zu erkennen, die in Braze gesammelt und gespeichert wurden, um DSRs schnell zu verarbeiten."
alias: /partners/datagrail/
page_type: partner
search_tag: Partner

---

# DataGrail

> [DataGrail](https://www.datagrail.io/), eine Plattform zur Verwaltung des Datenschutzes, hilft, das Vertrauen der Verbraucher:in zu stärken und riskante Geschäfte zu vermeiden. Mit kontinuierlicher Systemerkennung und automatisierter Erfüllung von Anfragen an die betroffenen Personen (DSR) unterstützt DataGrail Datenschutzprogramme, die die Einhaltung der sich entwickelnden Datenschutzgesetze und -vorschriften wie DSGVO, CCPA und CPRA unterstützen. 

_Diese Integration wird von DataGrail gepflegt._

## Über die Integration

Die Integration von Braze und DataGrail ermöglicht es Ihnen, die in Braze erfassten und gespeicherten Daten der Verbraucher:in zu erkennen, um DSRs (Zugriffs-, Lösch- und Nichtverkaufsanfragen) schnell zu bearbeiten. Braze wird mit einer automatisierten Abbildung der Daten in Ihrem Unternehmen zu einer genauen Blaupause des Verbleibs der Verbraucher:in hinzugefügt - es sind keine Umfragen oder Tabellenkalkulationen mehr erforderlich, um einen Datenschutzrahmen aufrechtzuerhalten oder ein Protokoll der Verarbeitungstätigkeiten (RoPA) zu erstellen. 

## Voraussetzungen

| Anforderungen | Beschreibung |
|---|---|
| DataGrail-Konto | Ein DataGrail-Konto, um die Vorteile dieser Partnerschaft zu nutzen.<br>Wenden Sie sich an Ihren Administrator oder mailen Sie an support@datagrail.io, wenn Sie Probleme oder Fragen zur Integration haben. |
| Braze API-Schlüssel | Ein Braze REST API-Schlüssel mit den Berechtigungen `events.list`, `users.export.ids`, `users.delete`, und `users.track`.<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-Instanz | Ihre Braze-Instanz erhalten Sie von Ihrem Braze Onboarding Manager oder auf der [Übersichtsseite über die APIs]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Melden Sie sich beim DataGrail-Portal an und wählen Sie auf der Integrationsseite für Braze **"Verbinden"** aus. Geben Sie als nächstes Ihre Instanz und den Braze API-Schlüssel ein und wählen Sie **Braze verbinden**.

Wenn es weitere Braze-Konten zu integrieren gibt:
1. Wählen Sie auf der Integrationsseite für Braze **Verbindung bearbeiten** aus.
2. Wählen Sie aus der Dropdown-Liste **+Neue Verbindung hinzufügen**.
3. Geben Sie unter **Verbindungsname** einen neuen Namen ein, um dieses separate Konto zu identifizieren (z.B. Braze Training Account).
4. Geben Sie eine separate Braze-Instanz und einen API-Schlüssel für dieses neue Konto ein.
5. Wählen Sie **Verbinden**.

Mailen Sie DataGrail an support@datagrail.io, wenn Sie Probleme oder Fragen zu Ihrer Integration haben.

