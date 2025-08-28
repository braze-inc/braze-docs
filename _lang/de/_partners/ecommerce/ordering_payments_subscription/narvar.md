---
nav_title: Narvar
article_title: Narvar
description: "Erfahren Sie, wie Sie Narvar in Braze integrieren können."
alias: /partners/narvar/
page_type: partner
search_tag: Partner
---

# Narvar

> Narvar ist eine Plattform für die Zeit nach dem Kauf, die die Loyalität der Kund:in durch Tracking, Updates für die Zustellung und Retourenmanagement stärkt. Die Integration von Braze und Narvar ermöglicht es Marken, die Benachrichtigungsereignisse von Narvar zu nutzen, um Nachrichten direkt von Braze zu triggern und die Kund:innen mit zeitnahen Updates auf dem Laufenden zu halten.

## Voraussetzungen

| Anforderung           | Beschreibung                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------|
| Narvar Konto        | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Narvar-Konto.                           |
| Braze REST API-Schlüssel    | Ein REST API-Schlüssel von Braze mit der Berechtigung `messages.send`. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden.                                            |
| Braze REST Endpunkt   | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), die von der URL für Ihre Braze-Instanz abhängt.         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Unterstützte Funktionen

|Typ|Unterstützte Funktionen|
|-------|----------|
| Benachrichtigungen | \- Zustellung Vorwegnahme der Lieferung<br>\- Träger-Verzögerung<br>\- Zugestellt Standard |
| Kanäle | Push-Benachrichtigungen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Wenn Sie an weiteren Benachrichtigungsarten oder Kanälen interessiert sind, wenden Sie sich bitte an Ihren Braze und Narvar CSM.
{% endalert %}

## Details zur Integration

Für jedes Benachrichtigungsereignis initiiert Narvar eine Anfrage an den Braze [`/messaging/send`]({{site.baseurl}}/api/endpoints/messaging) Endpunkt, um eine Push Nachricht an jeden Verbraucher:in zuzustellen, der sein Opt-in gegeben hat.

Narvar ist für die Konfiguration der Push-Benachrichtigungen für jede Nachricht verantwortlich. Derzeit verfügt Narvar nicht über eine integrierte Schnittstelle für Push-Benachrichtigungen. Das Team von Narvar wird daher mit Ihrem Team zusammenarbeiten, um die Anforderungen an die Nutzdaten zu ermitteln und zu definieren. Diese Payloads können im gleichen Maße angepasst werden wie die, die über Ihr eigenes System gesendet werden, einschließlich der Unterstützung für variable Platzhalter für Inhalte, wie z.B. Bestelldaten und Verbraucher:in.

## Erste Schritte mit der Braze-Narvar Integration

1. **Kontaktieren Sie Ihren Narvar CSM**, um Ihr Interesse an der Integration zu bekunden.
2. **Bestimmen Sie Braze-Umgebungen** für Staging und Produktion.
3. **Generieren Sie API-Schlüssel** in Braze für die Verwendung durch Narvar.
4. **Erzeugen Sie Kampagnenschlüssel** nach Bedarf in Braze.
5. **Stellen Sie Narvar API- und Kampagnen-Schlüssel bereit** – über einen sicheren, einmaligen Link.
6. **Teilen Sie die Details der Push-Benachrichtigung**, um die Einrichtung abzuschließen.
