---
nav_title: Narvar
article_title: Narvar
description: "Erfahren Sie, wie Sie Narvar mit Braze integrieren können."
alias: /partners/narvar/
page_type: partner
search_tag: Partner
---

# Narvar

> Narvar ist eine Plattform für die Zeit nach dem Kauf, die die Kundenbindung durch Auftragsverfolgung, Lieferungsaktualisierungen und Retourenmanagement verbessert. Die Integration von Braze und Narvar ermöglicht es Marken, die Benachrichtigungsereignisse von Narvar zu nutzen, um Nachrichten direkt von Braze auszulösen und Kunden mit zeitnahen Updates auf dem Laufenden zu halten.

## Voraussetzungen

| Anforderung           | Beschreibung                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------|
| Narvar Konto        | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Narvar-Konto.                           |
| Braze REST API Schlüssel    | Ein Braze REST API-Schlüssel mit der Berechtigung `messages.send`. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden.                                            |
| Braze REST Endpunkt   | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), die von der URL für Ihre Braze-Instanz abhängt.         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Unterstützte Funktionen

|Typ|Unterstützte Funktionen|
|-------|----------|
| Benachrichtigungen | \- Vorfreude auf die Lieferung<br>\- Träger-Verzögerung<br>\- Geliefert Standard |
| Kanäle | Push-Benachrichtigungen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Wenn Sie an weiteren Benachrichtigungsarten oder -kanälen interessiert sind, wenden Sie sich bitte an Ihren Braze und Narvar CSM.
{% endalert %}

## Details zur Integration

Für jedes Benachrichtigungsereignis initiiert Narvar eine Anfrage an den Endpunkt von Braze [`/messaging/send`]({{site.baseurl}}/api/endpoints/messaging) eine Anfrage an den Endpunkt von Braze, um eine Push-Nachricht an jeden angemeldeten Kunden zu senden.

Narvar ist für die Konfiguration der Nutzdaten der Push-Benachrichtigung für jede Nachricht verantwortlich. Derzeit verfügt Narvar nicht über eine integrierte Design-Schnittstelle für Push-Benachrichtigungen. Das Team von Narvar wird daher mit Ihrem Team zusammenarbeiten, um die Anforderungen an die Nutzdaten zu ermitteln und zu definieren. Diese Payloads können in gleichem Maße angepasst werden wie die über Ihr eigenes System gesendeten, einschließlich der Unterstützung variabler Inhaltsplatzhalter, wie z. B. Bestelldaten und Verbraucherdetails.

## Erste Schritte mit der Braze-Narvar Integration

1. **Kontaktieren Sie Ihren Narvar CSM**, um Ihr Interesse an der Integration zu bekunden.
2. **Bestimmen Sie Braze-Umgebungen** für Staging und Produktion.
3. **Generieren Sie** in Braze **einen API-Schlüssel** für Narvar.
4. **Generieren Sie** bei Bedarf **Kampagnenschlüssel** in Braze.
5. **Stellen Sie** Narvar **die API- und Kampagnenschlüssel** über einen sicheren, einmaligen Link zur Verfügung.
6. **Teilen Sie die Details für Push-Benachrichtigungen**, um die Einrichtung abzuschließen.
