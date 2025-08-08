---
nav_title: Knak
article_title: Knak
alias: /partners/knak/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Knak, einer Plattform zur Erstellung von Kampagnen, die es Ihnen erlaubt, vollständig responsive E-Mails in Minuten oder Stunden statt in Tagen oder Wochen zu erstellen und diese als gebrauchsfertige Braze Templates zu exportieren."
page_type: partner
search_tag: Knak

---

# Knak

> [Knak](https://knak.com/) ist die erste Plattform zur Erstellung von Kampagnen, die von Marketing Teams in Unternehmen selbst genutzt werden kann. Mit der Drag-and-Drop-Plattform kann jeder in wenigen Minuten ohne Programmieraufwand oder externe Hilfe ansehnliche markenspezifishce E-Mails und Landing Pages erstellen.

_Diese Integration wird von Knak gepflegt._

## Über die Integration

Die Integration von Braze und Knak erlaubt es Ihnen, vollständig responsive E-Mails in wenigen Minuten oder Stunden statt in Tagen oder Wochen zu erstellen und sie als gebrauchsfertige Braze Templates zu exportieren. Knak wurde für Marketer entwickelt, die ihre E-Mail-Erstellung für Kampagnen, die in Braze verwaltet werden, verbessern möchten, ohne externe Agenturen zu beauftragen oder manuell zu programmieren. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Knak-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Knak-Konto. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit vollständigen **Templates-Berechtigungen**. <br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Knak wurde für Marketer entwickelt, die ihre E-Mail-Erstellung verbessern möchten, ohne Code oder externe Hilfe zu benötigen. Es ist ideal für alle, die:
- Sie verwenden derzeit einfache Templates für E-Mails und möchten diese verbessern
- Verlassen Sie sich auf externe Agenturen oder Entwickler:in, um E-Mails für Braze zu erstellen
- Sie möchten die kreative Kontrolle über die Erstellung von Assets zurückgewinnen und deutlich schneller auf den Markt kommen

## Integration

### Schritt 1: Konfigurieren Sie Ihre Integration

Navigieren Sie in Knak zu **Integrationen > Plattformen > + Neue Integration hinzufügen**.

![Button Integration hinzufügen]({% image_buster /assets/img/knak/integration-setup-step-2-add-new-integration.png %})

Wählen Sie als nächstes die **Braze-Plattform** aus und geben Sie den Braze API-Schlüssel und den REST-Endpunkt an. Klicken Sie auf **Neue Integration erstellen**, um Ihre Integration abzuschließen. 

![Neue Integration erstellen]({% image_buster /assets/img/knak/integration-setup-step-4-add-api-key.png %})

### Schritt 2: Synchronisieren Sie Ihre Knak Templates

Suchen Sie in Knak nach einer E-Mail, die Sie mit Braze synchronisieren möchten, wählen Sie **Veröffentlichen** und dann **Synchronisieren**.

![Knak Integration 1]({% image_buster /assets/img/knak/integration-post-step-1-sync.png %})

Überprüfen Sie dann den Namen der E-Mail und klicken Sie auf **Synchronisieren**.

![Knak Integration 2]({% image_buster /assets/img/knak/integration-post-step-2-asset-name.png %})

## Verwendung der Integration

Sie finden Ihre hochgeladenen Knak E-Mails in Braze unter **Engagement > Templates und Medien.** Sie werden schön, markengerecht und vollständig responsiv sein. Die einzige Grenze ist Ihre eigene Kreativität!


