---
nav_title: DataGrail
article_title: DataGrail
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und DataGrail, einer Plattform zur Verwaltung des Datenschutzes, die es Ihnen ermöglicht, in Braze erfasste und gespeicherte Verbraucherdaten zu erkennen, um DSRs schnell zu verarbeiten."
alias: /partners/datagrail/
page_type: partner
search_tag: Partner

---

# DataGrail

> [DataGrail](https://www.datagrail.io/), eine Plattform zur Verwaltung des Datenschutzes, hilft, das Vertrauen der Verbraucher zu stärken und riskante Geschäfte zu vermeiden. Mit kontinuierlicher Systemerkennung und automatischer Erfüllung von Datenschutzanfragen (DSR) unterstützt DataGrail Datenschutzprogramme, die die Einhaltung der sich entwickelnden Datenschutzgesetze und -vorschriften wie GDPR, CCPA und CPRA unterstützen. 

Die Integration von Braze und DataGrail ermöglicht es Ihnen, die in Braze gesammelten und gespeicherten Verbraucherdaten zu erkennen, um DSRs (Zugriffs-, Lösch- und Nichtverkaufsanfragen) schnell zu verarbeiten. Braze wird mit automatischer Datenzuordnung zu einer genauen Blaupause des Verbleibs von Verbraucherdaten in Ihrem Unternehmen hinzugefügt - es sind keine Umfragen oder Tabellenkalkulationen mehr erforderlich, um einen Datenschutzrahmen aufrechtzuerhalten oder eine Aufzeichnung der Verarbeitungsaktivitäten (RoPA) zu erstellen. 

## Voraussetzungen

| Anforderungen | Beschreibung |
|---|---|
| DataGrail-Konto | Ein DataGrail-Konto, um die Vorteile dieser Partnerschaft zu nutzen.<br>Wenden Sie sich an Ihren Administrator oder senden Sie eine E-Mail an support@datagrail.io, wenn Sie Probleme oder Fragen zur Integration haben. |
| Braze API-Schlüssel | Ein Braze REST API-Schlüssel mit den Berechtigungen `events.list`, `users.export.ids`, `users.delete` und `users.track`.<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Hartlöt-Instanz | Ihre Braze-Instanz erhalten Sie von Ihrem Braze-Onboarding-Manager oder Sie finden sie auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Melden Sie sich beim DataGrail-Portal an und wählen Sie auf der Integrationsseite für Braze die Option **Verbinden**. Als nächstes geben Sie Ihre Instanz und den Braze-API-Schlüssel ein und wählen **Braze verbinden**.

Wenn weitere Braze-Konten zu integrieren sind:
1. Wählen Sie **Verbindung bearbeiten** auf der Integrationsseite für Braze.
2. Wählen Sie aus der Dropdown-Liste **+Neue Verbindung hinzufügen**.
3. Geben Sie unter **Verbindungsname** einen neuen Namen ein, um dieses separate Konto zu identifizieren (z.B. Braze Training Account).
4. Geben Sie eine separate Braze-Instanz und einen API-Schlüssel für dieses neue Konto ein.
5. Wählen Sie **Verbinden**.

Senden Sie eine E-Mail an DataGrail unter support@datagrail.io, wenn Sie Probleme oder Fragen zu Ihrer Integration haben.
