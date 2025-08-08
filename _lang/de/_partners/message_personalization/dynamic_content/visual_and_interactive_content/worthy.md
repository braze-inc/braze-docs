---
nav_title: Worthy
article_title: Worthy
description: "Dieser Artikel referenziert die Partnerschaft zwischen Braze und Worthy, einer Plattform zur Personalisierung von Nachrichten, die es Ihnen erlaubt, personalisierte, reichhaltige In-App-Erlebnisse zu erstellen und diese über Braze zuzustellen."
alias: /partners/worthy/
page_type: partner
search_tag: Partner

---

# Worthy

> Die Integration von [Worthy](https://worthy.ai/) und Braze erlaubt es Ihnen, mit dem Drag-and-Drop-Editor von Worthy auf einfache Weise personalisierte, reichhaltige In-App-Erlebnisse zu erstellen und diese über Braze zuzustellen. Außerdem wird Worthy automatisch Folgendes tun:

_Diese Integration wird von Worthy gepflegt._

## Über die Integration

- Erstellen Sie einen Connected-Content Server und eine gesicherte API für Ihr Messaging.
- Gestalten Sie Ihre In-App-Nachrichten mit Analytics und Klick-Tracking, die direkt in Braze erscheinen.
- Exportieren Sie automatisch HTML über den Drag-and-Drop-Editor von Worthy zur Verwendung in **In-App-Nachricht-Kampagnen** in Braze, komplett mit den erforderlichen API-Verbindungen und dynamischen Inhalten, die Sie konfigurieren.

## Anwendungsfälle

- Angepasste Willkommenserlebnisse basierend auf der Auswahl der Nutzer:innen beim Onboarding
- In-App-Erlebnisse für besondere Ereignisse und Aktionen
- Sammeln von Kundenfeedback und Bewertungen auf der Grundlage des App-Verhaltens
- Schnelles Testen potenzieller Ideen für ein App Produkt
- Reichhaltige Mitteilungen, Nachrichten und Updates aus der Community

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| [Würdiges](https://worthy.ai/) Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Worthy-Konto. |
| Braze SDK | Sie müssen das Braze SDK in Ihrer mobilen Anwendung konfigurieren, um In-App-Nachrichten versenden zu können. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integration

### Schritt 1: Erstellen Sie personalisierte Nachrichten in Worthy

Navigieren Sie im Worthy Dashboard zu Ihrer App, wählen Sie den **Message Creator** und erstellen Sie eine personalisierte Nachricht, mit der Sie Ihre Nutzer:innen einbinden möchten.

### Schritt 2: Erstellen Sie eine Braze Kampagne

Erstellen Sie eine [In-App-Nachricht-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/) in Braze und stellen Sie den **Nachrichtentyp** auf **Custom Code** ein.

### Schritt 3: Kopieren Sie Ihre personalisierte Nachricht in Braze

Klicken Sie im Worthy message creator auf **Export** und wählen Sie **Braze**, um Ihre personalisierte Nachricht zur Verwendung in Kampagnen zu exportieren. Kopieren Sie den exportierten Inhalt in das HTML-Textfeld unter **HTML + Asset Zip** im Kampagnen-Editor von Braze.

Das war's! Sie können Ihre personalisierte Nachricht sofort testen, indem Sie den Tab **Test** im Kampagnen-Editor von Braze verwenden. 

