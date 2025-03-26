---
nav_title: Knak
article_title: Knak
alias: /partners/knak/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Knak, einer Plattform zur Erstellung von Kampagnen, mit der Sie vollständig responsive E-Mails in Minuten oder Stunden statt in Tagen oder Wochen erstellen und als gebrauchsfertige Braze-Vorlagen exportieren können."
page_type: partner
search_tag: Knak

---

# Knak

> [Knak][1] ist die erste Plattform zur Erstellung von Kampagnen, die für Marketingteams in Unternehmen entwickelt wurde und intern genutzt werden kann. Mit ihrer Drag-and-Drop-Plattform kann jeder in wenigen Minuten wunderschöne, markengerechte E-Mails und Landing Pages erstellen, ohne dass dafür Programmierkenntnisse oder Hilfe von außen erforderlich sind.

Die Integration von Braze und Knak ermöglicht es Ihnen, vollständig responsive E-Mails in Minuten oder Stunden statt in Tagen oder Wochen zu erstellen und sie als gebrauchsfertige Braze-Vorlagen zu exportieren. Knak wurde für Marketingexperten entwickelt, die ihre E-Mail-Erstellung für in Braze verwaltete Kampagnen verbessern möchten, ohne externe Agenturen oder manuelle Programmierung in Anspruch nehmen zu müssen. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Knak-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Knak-Konto. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit vollständigen **Vorlagenberechtigungen**. <br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][2]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Knak wurde für Marketingexperten entwickelt, die ihre E-Mail-Erstellung verbessern möchten, ohne dass sie Programmierkenntnisse oder Hilfe von außen benötigen. Es ist ideal für alle, die:
- Sie verwenden derzeit einfache Vorlagen für E-Mails und möchten ihr Angebot erweitern
- Beauftragen Sie externe Agenturen oder Entwickler mit der Erstellung von E-Mails für Braze
- Sie möchten die kreative Kontrolle über die Erstellung von Assets zurückgewinnen und deutlich schneller auf den Markt kommen

## Integration

### Schritt 1: Konfigurieren Sie Ihre Integration

Navigieren Sie in Knak zu **Integrationen > Plattformen > + Neue Integration hinzufügen**.

![Schaltfläche Integration hinzufügen][5]

Als nächstes wählen Sie die **Braze-Plattform** aus und geben den Braze-API-Schlüssel und den REST-Endpunkt an. Klicken Sie auf **Neue Integration erstellen**, um Ihre Integration abzuschließen. 

![Neue Integration erstellen][6]

### Schritt 2: Synchronisieren Sie Ihre Knak Vorlagen

Suchen Sie in Knak eine E-Mail, die Sie mit Braze synchronisieren möchten, und wählen Sie **Veröffentlichen** und dann **Synchronisieren**.

![Knak Integration 1][8]

Überprüfen Sie dann den E-Mail-Namen und klicken Sie auf **Synchronisieren**.

![Knak Integration 2][9]

## Verwendung der Integration

Sie können Ihre hochgeladenen Knak-E-Mails in Braze unter **Engagement > Vorlagen & Medien** finden. Sie werden wunderschön, markengerecht und vollständig responsiv sein. Die einzige Grenze ist Ihre eigene Kreativität!

[1]: https://knak.com/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[5]: {% image_buster /assets/img/knak/integration-setup-step-2-add-new-integration.png %}
[6]: {% image_buster /assets/img/knak/integration-setup-step-4-add-api-key.png %}
[8]: {% image_buster /assets/img/knak/integration-post-step-1-sync.png %}
[9]: {% image_buster /assets/img/knak/integration-post-step-2-asset-name.png %}